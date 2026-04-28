import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import random
import string
import smtplib
import time
from config import admin, emaill, passw, admin_email,domain,secret_key
from PIL import Image, ImageDraw, ImageFont
import random



app = Flask(__name__)
app.secret_key = f"{secret_key}"

DB_NAME = "urls.db"

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn




def is_admin():
    return session.get("is_admin") == True





def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            verified INTEGER DEFAULT 0,
            token TEXT,
            reset_token TEXT,
            reset_expires INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            url TEXT,
            clicked INTEGER DEFAULT 0,
            user_id INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            subject TEXT,
            message TEXT,
            status TEXT DEFAULT 'open',
            created_at INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS ticket_replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER,
            sender_type TEXT, -- 'user' یا 'admin'
            sender_id INTEGER,
            message TEXT,
            created_at INTEGER
        )
    """)

    conn.commit()
    conn.close()



init_db()

def make_code():
    chars = string.ascii_letters + string.digits
    while True:
        code = "".join(random.choice(chars) for _ in range(5))
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT code FROM links WHERE code=?", (code,))
        row = cur.fetchone()
        conn.close()
        if not row:
            return code



def generate_captcha():

    number = random.randint(10000, 99999)

    width = 400
    height = 200

    img = Image.new("RGB", (width, height), "purple")
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default(60)

    text = str(number)

    bbox = draw.textbbox((0, 0), text, font=font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), text, fill="white", font=font)

    img.save("static/captcha.png")

    session["captcha"] = text


def make_token():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(40))

def send_verification(email, name, token):
    verify_link = f"https://{domain}/verify/{token}"

    msg = "Content-Type: text/plain; charset=utf-8\r\n"
    msg += f"From: اسموف <{emaill}>\r\n"
    msg += f"To: {email}\r\n"
    msg += "Subject: تایید ثبت نام اسموف\r\n"
    msg += "Content-Transfer-Encoding: 8bit\r\n\r\n"
    msg += f"سلام {name}\n"
    msg += "به اسموف خوش اومدی :)\n\n"
    msg += "برای فعال‌سازی حسابت روی لینک زیر کلیک کن:\n"
    msg += verify_link

    try:
        server = smtplib.SMTP("mc.mailfa.com", 587)
        server.starttls()
        server.login(emaill, passw)
        server.sendmail(f"{emaill}", email, msg.encode("utf-8"))
        server.quit()
    except Exception as e:
        print("Email error:", e)

def send_reset_email(email, name, reset_token):
    reset_link = f"https://{domain}/reset/{reset_token}"

    msg = "Content-Type: text/plain; charset=utf-8\r\n"
    msg += f"From: اسموف <{emaill}>\r\n"
    msg += f"To: {email}\r\n"
    msg += "Subject: بازیابی رمز عبور اسموف\r\n"
    msg += "Content-Transfer-Encoding: 8bit\r\n\r\n"
    msg += f"سلام {name}\n"
    msg += "درخواست بازیابی رمز عبور برای حساب شما ثبت شده است.\n\n"
    msg += "برای تنظیم رمز عبور جدید روی لینک زیر کلیک کن:\n"
    msg += reset_link + "\n\n"
    msg += "اگر این درخواست را شما ارسال نکرده‌ای، این ایمیل را نادیده بگیر."

    try:
        server = smtplib.SMTP("mc.mailfa.com", 587)
        server.starttls()
        server.login(email, passw)
        server.sendmail(f"{emaill}", email, msg.encode("utf-8"))
        server.quit()
    except Exception as e:
        print("Reset email error:", e)

@app.route("/")
def main_home():
    return redirect("/delete")

@app.route("/smoth")
def home_page():
    return render_template(
        "index.html",
        link=None,
        logged_in=("user_id" in session),
        user_name=session.get("name")
    )

@app.route("/short_link", methods=["POST"])
def short_link():
    link = request.form.get("link")

    if not link:
        return render_template(
            "index.html",
            link=None,
            error="لطفا لینک را وارد کن",
            logged_in=("user_id" in session),
            user_name=session.get("name")
        )

    code = make_code()

    conn = get_db()
    cur = conn.cursor()

    user_id = session.get("user_id")

    cur.execute(
        "INSERT INTO links (code,url,user_id) VALUES (?,?,?)",
        (code, link, user_id)
    )
    conn.commit()
    conn.close()

    short_link_full = request.host_url + code

    return render_template(
        "index.html",
        link=short_link_full,
        error=None,
        logged_in=("user_id" in session),
        user_name=session.get("name")
    )

@app.route("/register")
def register_page():
    return render_template("register.html", error=None, success=None, old_name="", old_email="")

@app.route("/register_user", methods=["POST"])
def register_user():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not email or not password:
        return render_template(
            "register.html",
            error="لطفا همه فیلدها را کامل کن",
            success=None,
            old_name=name,
            old_email=email
        )

    token = make_token()

    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (name,email,password,token) VALUES (?,?,?,?)",
            (name, email, password, token)
        )
        conn.commit()
    except Exception:
        conn.close()
        return render_template(
            "register.html",
            error="این ایمیل قبلا ثبت شده است",
            success=None,
            old_name=name,
            old_email=email
        )

    conn.close()

    send_verification(email, name, token)

    return render_template(
        "register.html",
        error=None,
        success="لینک تایید به ایمیل شما ارسال شد",
        old_name="",
        old_email=""
    )

@app.route("/verify/<token>")
def verify(token):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE token=?", (token,))
    user = cur.fetchone()

    if not user:
        conn.close()
        return render_template(
            "login.html",
            error="لینک تایید نامعتبر است",
            success=None,
            old_email=""
        )

    cur.execute("UPDATE users SET verified=1 WHERE token=?", (token,))
    conn.commit()
    conn.close()

    return render_template(
        "login.html",
        error=None,
        success="حساب شما با موفقیت فعال شد و حالا می‌توانید وارد شوید",
        old_email=""
    )

@app.route("/login")
def login_page():
    return render_template("login.html", error=None, success=None, old_email="")

@app.route("/login_user", methods=["POST"])
def login_user():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not email or not password:
        return render_template(
            "login.html",
            error="ایمیل و رمز عبور را وارد کن",
            success=None,
            old_email=email
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id,name,verified FROM users WHERE email=? AND password=?",
        (email, password)
    )
    user = cur.fetchone()
    conn.close()

    if not user:
        return render_template(
            "login.html",
            error="ایمیل یا رمز عبور اشتباه است",
            success=None,
            old_email=email
        )

    if user[2] != 1:
        return render_template(
            "login.html",
            error="ابتدا حساب خود را از طریق لینک ارسال شده به ایمیل فعال کن",
            success=None,
            old_email=email
        )

    session["user_id"] = user[0]
    session["name"] = user[1]
    session["email"] = email


    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id,code,url,clicked FROM links WHERE user_id=? ORDER BY id DESC",
        (session["user_id"],)
    )
    links = cur.fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        name=session.get("name"),
        links=links,
        base_url=request.host_url
    )

@app.route("/create", methods=["POST"])
def create():
    if "user_id" not in session:
        return redirect("/login")

    url = request.form.get("url", "").strip()

    if not url:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT id,code,url,clicked FROM links WHERE user_id=? ORDER BY id DESC",
            (session["user_id"],)
        )
        links = cur.fetchall()
        conn.close()

        return render_template(
            "dashboard.html",
            name=session.get("name"),
            links=links,
            base_url=request.host_url,
            error="لطفا لینک را وارد کن"
        )

    code = make_code()

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO links (code,url,user_id) VALUES (?,?,?)",
        (code, url, session["user_id"])
    )
    conn.commit()
    cur.execute(
        "SELECT id,code,url,clicked FROM links WHERE user_id=? ORDER BY id DESC",
        (session["user_id"],)
    )
    links = cur.fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        name=session.get("name"),
        links=links,
        base_url=request.host_url,
        success="لینک کوتاه با موفقیت ساخته شد"
    )

@app.route("/delete/<int:link_id>")
def delete(link_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM links WHERE id=? AND user_id=?",
        (link_id, session["user_id"])
    )
    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/<code>")
def redirect_code(code):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id,url,clicked FROM links WHERE code=?", (code,))
    row = cur.fetchone()

    if not row:
        conn.close()
        return render_template("nolinks.html")

    cur.execute("UPDATE links SET clicked=? WHERE id=?", (row[2] + 1, row[0]))
    conn.commit()
    conn.close()

    return redirect(row[1])

@app.route("/delete")
def delete_process():
    conn = get_db()
    cur = conn.cursor()

    count = 450

    cur.execute("DELETE FROM links WHERE clicked >= ?", (count,))
    conn.commit()
    conn.close()
    return redirect("/captcha")

@app.route("/change_password")
def change_Password():
    return render_template("forgot_password.html")

@app.route("/reset_password", methods=["POST"])
def send_reset():
    email = request.form.get("email", "").strip()

    if not email:
        return render_template(
            "forgot_password.html",
            eror="ایمیل را وارد کن",
        )

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users WHERE email=?", (email,))
    user = cur.fetchone()
    if not user:
        conn.close()
        return render_template(
            "forgot_password.html",
            eror="این ایمیل وجود ندارد",
        )

    reset_token = make_token()
    expires_at = int(time.time()) + 3600

    cur.execute(
        "UPDATE users SET reset_token=?, reset_expires=? WHERE id=?",
        (reset_token, expires_at, user[0])
    )
    conn.commit()
    conn.close()

    send_reset_email(email, user[1], reset_token)

    return render_template(
        "forgot_password.html",
        success="لینک به ایمیل شما ارسال شد",
    )

@app.route("/reset/<token>", methods=["GET"])
def reset_password_page(token):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, reset_expires FROM users WHERE reset_token=?",
        (token,)
    )
    user = cur.fetchone()
    conn.close()

    now = int(time.time())

    if not user or not user[2] or user[2] < now:
        return render_template(
            "login.html",
            error="لینک بازیابی نامعتبر یا منقضی شده است",
            success=None,
            old_email=""
        )

    return render_template("reset_password.html", error=None, token=token)

@app.route("/reset/<token>", methods=["POST"])
def reset_password_submit(token):
    password_raw = request.form.get("password", "").strip()
    password_confirm = request.form.get("password_confirm", "").strip()

    if not password_raw or not password_confirm:
        return render_template(
            "reset_password.html",
            error="هر دو فیلد رمز عبور را پر کن",
            token=token
        )

    if password_raw != password_confirm:
        return render_template(
            "reset_password.html",
            error="رمز عبور و تکرار آن یکسان نیست",
            token=token
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, reset_expires FROM users WHERE reset_token=?",
        (token,)
    )
    user = cur.fetchone()

    now = int(time.time())

    if not user or not user[1] or user[1] < now:
        conn.close()
        return render_template(
            "login.html",
            error="لینک بازیابی نامعتبر یا منقضی شده است",
            success=None,
            old_email=""
        )

    cur.execute(
        "UPDATE users SET password=?, reset_token=NULL, reset_expires=NULL WHERE id=?",
        (password_raw, user[0])
    )
    conn.commit()
    conn.close()

    return render_template(
        "login.html",
        error=None,
        success="رمز عبور با موفقیت تغییر کرد، حالا می‌توانی وارد شوی",
        old_email=""
    )

@app.route("/delete_account")
def delete_account_home():
    return render_template("delete_account.html")

@app.route("/del_account", methods=['POST'])
def delete_home():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not email or not password:
        return render_template("delete_account.html", eror="ایمیل و رمز عبور را وارد کن")

    con = get_db()
    cur = con.cursor()

    cur.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
    user = cur.fetchone()

    if not user:
        con.close()
        return render_template("delete_account.html", eror="ایمیل یا رمز عبور اشتباه است")

    cur.execute("DELETE FROM links WHERE user_id=?", (user[0],))
    cur.execute("DELETE FROM users WHERE id=?", (user[0],))

    con.commit()
    con.close()

    session.clear()

    return render_template("login.html", success="اکانت با موفقیت حذف شد")


@app.route("/change_account_password")
def change_account_password():
    return render_template("change_account_pass.html")


@app.route("/change_pass_ac", methods=['POST'])
def change_pass_proce():
    email = request.form.get("email", "").strip()
    old_pass = request.form.get("old_pass", "").strip()
    new_pass = request.form.get("new_pass", "").strip()

    if not email or not old_pass or not new_pass:
        return render_template("change_account_pass.html", eror="تمام فیلدها را پر کنید")

    con = get_db()
    cur = con.cursor()

    cur.execute("SELECT id FROM users WHERE email=? AND password=?", (email, old_pass))
    user = cur.fetchone()

    if not user:
        con.close()
        return render_template("change_account_pass.html", eror="ایمیل یا پسورد قدیمی اشتباه است")

    cur.execute("UPDATE users SET password=? WHERE id=?", (new_pass, user[0]))
    con.commit()
    con.close()

    session.clear()
    return render_template("login.html", success="پسورد با موفقیت تغییر کرد")



@app.route("/panel")
def panel():
    return render_template("panel.html")


@app.route("/login_proc", methods=['POST'])
def login_proc():
    password = request.form.get("password")
    if password == admin:
        session["is_admin"] = True
        notif = "به پنل ادمین خوش امدی"
        return render_template("dashboard_admin.html", notif=notif)

    else:
        eror = "پسورد اشتباه هست"
        return render_template("panel.html", eror=eror)

@app.route("/add_account", methods=['POST'])
def add_account_proc():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO users (name, email, password, verified) VALUES (?,?,?,?)", (name, email, password, 1))
    con.commit()
    success = "اکانت کاربر با موفقیت ساخته شد"
    return render_template("dashboard_admin.html", success=success)




@app.route("/delete_acc_fr_admin", methods=['POST'])
def del_ac_f_ad():
    email = request.form.get("email", "").strip()

    if not email:
        return render_template("dashboard_admin.html", eror_1="ایمیل و  را وارد کن")

    con = get_db()
    cur = con.cursor()

    cur.execute("SELECT id FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if not user:
        con.close()
        return render_template("dashboard_admin.html", eror_1="ایمیل اشتباه است")

    cur.execute("DELETE FROM links WHERE user_id=?", (user[0],))
    cur.execute("DELETE FROM users WHERE id=?", (user[0],))

    con.commit()
    con.close()

    session.clear()

    return render_template("dashboard_admin.html", success_1="اکانت با موفقیت حذف شد")



@app.route("/captcha")
def captcha():
    if "user_id" in session:
        return redirect("/smoth")
    else:
        generate_captcha()
    
        return render_template("captcha.html")



@app.route("/check_captcha", methods=["POST"])
def check_captcha():

    user = request.form.get("num")

    if user == session.get("captcha"):
        return redirect("/login")

    generate_captcha()

    return render_template("captcha.html", error="کپچا اشتباه است")


@app.route("/support", methods=["GET", "POST"])
def support():
    if "user_id" not in session:
        flash("برای ارسال تیکت باید وارد حساب کاربری شوید.")
        return redirect(url_for("login_user"))

    user_id = session["user_id"]

    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not subject or not message:
            flash("عنوان و متن پیام الزامی است.")
        else:
            cursor.execute(
                """
                INSERT INTO tickets (user_id, subject, message, status, created_at)
                VALUES (?, ?, ?, 'open', ?)
                """,
                (user_id, subject, message, int(time.time()))
            )

            conn.commit()
            flash("تیکت شما با موفقیت ثبت شد.")
            return redirect(url_for("support"))

    cursor.execute(
        """
        SELECT t.id, t.subject, t.status, t.created_at,
               (SELECT message FROM ticket_replies r
                WHERE r.ticket_id = t.id
                ORDER BY r.created_at DESC
                LIMIT 1) AS last_message
        FROM tickets t
        WHERE t.user_id = ?
        ORDER BY t.created_at DESC
        """,
        (user_id,)
    )
    tickets = cursor.fetchall()
    conn.close()

    return render_template("support.html", tickets=tickets)




@app.route("/<int:ticket_id>", methods=["GET", "POST"])
def support_ticket_view(ticket_id):
    if "user_id" not in session:
        flash("برای مشاهده تیکت باید وارد شوید.")
        return redirect(url_for("login_user"))

    user_id = session["user_id"]
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets WHERE id = ? AND user_id = ?", (ticket_id, user_id))
    ticket = cursor.fetchone()
    if not ticket:
        conn.close()
        flash("تیکت یافت نشد.")
        return redirect(url_for("support"))

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if not message:
            flash("متن پیام نمی‌تواند خالی باشد.")
        else:

            if ticket["status"] == "closed":
                flash("این تیکت بسته شده است و نمی‌توانید پیام جدید ارسال کنید.")
            else:
                cursor.execute(
                    """
                    INSERT INTO ticket_replies (ticket_id, sender_type, sender_id, message, created_at)
                    VALUES (?, 'user', ?, ?, ?)
                    """,
                    (ticket_id, user_id, message, int(time.time()))
                )

                conn.commit()
                flash("پیام شما ارسال شد.")
                cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
                ticket = cursor.fetchone()

    cursor.execute(
    """
    SELECT r.*, u.name
    FROM ticket_replies r
    LEFT JOIN users u ON r.sender_id = u.id
    WHERE r.ticket_id = ?
    ORDER BY r.created_at ASC
    """,
    (ticket_id,)
)

    replies = cursor.fetchall()
    conn.close()

    return render_template("support_ticket_view.html", ticket=ticket, replies=replies)



@app.route("/te", methods=["POST"])
def create_ticket():
    if "user_id" not in session:
        return redirect("/login")

    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    if not subject or not message:
        return render_template(
            "support.html",
            logged_in=True,
            user_name=session.get("name"),
            error="لطفا عنوان و متن تیکت را کامل وارد کن",
            success=None,
            old_subject=subject,
            old_message=message,
        )

    conn = get_db()
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO tickets (user_id, subject, message, status, created_at)
        VALUES (?, ?, ?, 'open', ?)
        """,
        (session["user_id"], subject, message, int(time.time()))
    )
    conn.commit()
    conn.close()

    return render_template(
        "support.html",
            logged_in=True,
            user_name=session.get("name"),
            error=None,
            success="تیکت شما با موفقیت ثبت شد. پشتیبانی در اسرع وقت پاسخ خواهد داد.",
            old_subject="",
            old_message="",
    )


@app.route("/admin/tickets")
def admin_tickets():
    if not is_admin():
        return "Access denied", 403

    status_filter = request.args.get("status", "all") 

    conn = get_db()
    c = conn.cursor()

    if status_filter == "open":
        c.execute("""
            SELECT t.id, t.subject, t.status, t.created_at, u.name, u.email
            FROM tickets t
            LEFT JOIN users u ON t.user_id = u.id
            WHERE t.status = 'open'
            ORDER BY t.created_at DESC
        """)
    elif status_filter == "closed":
        c.execute("""
            SELECT t.id, t.subject, t.status, t.created_at, u.name, u.email
            FROM tickets t
            LEFT JOIN users u ON t.user_id = u.id
            WHERE t.status = 'closed'
            ORDER BY t.created_at DESC
        """)
    else:
        c.execute("""
            SELECT t.id, t.subject, t.status, t.created_at, u.name, u.email
            FROM tickets t
            LEFT JOIN users u ON t.user_id = u.id
            ORDER BY t.created_at DESC
        """)

    tickets = c.fetchall()
    conn.close()


    return render_template(
        "admin_tickets.html",
        tickets=tickets,
        status_filter=status_filter
    )



@app.route("/admin/tickets/<int:ticket_id>")
def admin_ticket_view(ticket_id):
    if not is_admin():
        return "Access denied", 403

    conn = get_db()
    c = conn.cursor()

    c.execute("""
        SELECT t.id, t.subject, t.message, t.status, t.created_at, u.name, u.email
        FROM tickets t
        LEFT JOIN users u ON t.user_id = u.id
        WHERE t.id = ?
    """, (ticket_id,))
    ticket = c.fetchone()

    if not ticket:
        conn.close()
        return "Ticket not found", 404


    c.execute("""
        SELECT sender_type, message, created_at
        FROM ticket_replies
        WHERE ticket_id = ?
        ORDER BY created_at ASC
    """, (ticket_id,))
    replies = c.fetchall()
    conn.close()

    return render_template(
        "admin_ticket_view.html",
        ticket=ticket,
        replies=replies
    )


@app.route("/admin/tickets/<int:ticket_id>/reply", methods=["POST"])
def admin_ticket_reply(ticket_id):
    if not is_admin():
        return "Access denied", 403

    message = request.form.get("message", "").strip()
    if not message:
        return redirect(url_for("admin_ticket_view", ticket_id=ticket_id))

    conn = get_db()
    c = conn.cursor()

    c.execute("""
        INSERT INTO ticket_replies (ticket_id, sender_type, sender_id, message, created_at)
        VALUES (?, 'admin', ?, ?, ?)
    """, (ticket_id, session.get("user_id"), message, int(time.time())))

    conn.commit()
    conn.close()

    return redirect(url_for("admin_ticket_view", ticket_id=ticket_id))



@app.route("/admin/tickets/<int:ticket_id>/close", methods=["POST"])
def admin_ticket_close(ticket_id):
    if not is_admin():
        return "Access denied", 403

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tickets SET status='closed' WHERE id=?",
        (ticket_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin_ticket_view", ticket_id=ticket_id))




@app.route("/admin/tickets/<int:ticket_id>/open", methods=["POST"])
def admin_ticket_open(ticket_id):
    if not is_admin():
        return "Access denied", 403

    conn = get_db()
    c = conn.cursor()
    c.execute("UPDATE tickets SET status='open' WHERE id=?", (ticket_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("admin_ticket_view", ticket_id=ticket_id))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
