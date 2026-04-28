<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>python-shortlink | کوتاه‌کننده لینک حرفه‌ای</title>
  <style>
    :root {
      --bg: #0b1020;
      --bg2: #111936;
      --card: rgba(17, 25, 54, 0.72);
      --card2: rgba(255, 255, 255, 0.04);
      --text: #e8eefc;
      --muted: #a9b4d0;
      --primary: #7c5cff;
      --primary2: #00d4ff;
      --success: #3ddc97;
      --warning: #ffcc66;
      --danger: #ff6b6b;
      --border: rgba(255,255,255,0.08);
      --shadow: 0 20px 60px rgba(0,0,0,0.35);
      --radius: 22px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Tahoma, Arial, sans-serif;
      background:
        radial-gradient(circle at top, rgba(124,92,255,0.25), transparent 35%),
        radial-gradient(circle at right, rgba(0,212,255,0.16), transparent 30%),
        linear-gradient(180deg, var(--bg) 0%, #070b16 100%);
      color: var(--text);
      min-height: 100vh;
      padding: 40px 18px;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
    }

    .hero {
      background: linear-gradient(135deg, rgba(124,92,255,0.18), rgba(0,212,255,0.12));
      border: 1px solid var(--border);
      border-radius: 30px;
      padding: 42px 28px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      backdrop-filter: blur(16px);
    }

    .hero::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.08), transparent 25%);
      pointer-events: none;
    }

    .badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 18px;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 14px;
      border-radius: 999px;
      background: rgba(255,255,255,0.06);
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 13px;
      backdrop-filter: blur(10px);
    }

    .title {
      font-size: clamp(30px, 5vw, 56px);
      line-height: 1.2;
      margin-bottom: 14px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }

    .title span {
      background: linear-gradient(90deg, var(--primary2), var(--primary));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .subtitle {
      font-size: 18px;
      color: var(--muted);
      line-height: 1.9;
      max-width: 900px;
      margin-bottom: 22px;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 22px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 14px 18px;
      border-radius: 14px;
      border: 1px solid transparent;
      text-decoration: none;
      color: white;
      font-weight: 700;
      transition: 0.25s ease;
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--primary), var(--primary2));
      box-shadow: 0 12px 30px rgba(124,92,255,0.28);
    }

    .btn-secondary {
      background: rgba(255,255,255,0.06);
      border-color: var(--border);
    }

    .btn:hover {
      transform: translateY(-2px);
      opacity: 0.96;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 18px;
      margin-top: 22px;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(14px);
    }

    .card h2 {
      font-size: 22px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .card p, .card li {
      color: var(--muted);
      line-height: 1.95;
      font-size: 15px;
    }

    .features {
      grid-column: span 7;
    }

    .config {
      grid-column: span 5;
    }

    .feature-list, .step-list {
      list-style: none;
      display: grid;
      gap: 12px;
      margin-top: 16px;
    }

    .feature-list li, .step-list li {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.06);
      padding: 14px 16px;
      border-radius: 16px;
      display: flex;
      gap: 12px;
      align-items: flex-start;
    }

    .icon {
      width: 30px;
      height: 30px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex: 0 0 30px;
      color: white;
      font-size: 16px;
      background: linear-gradient(135deg, var(--primary), var(--primary2));
    }

    .section {
      margin-top: 22px;
    }

    .code-box {
      background: #0a0f1f;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 18px;
      padding: 18px;
      overflow-x: auto;
      font-family: Consolas, monospace;
      font-size: 14px;
      color: #d7e3ff;
      line-height: 1.8;
    }

    code {
      background: rgba(255,255,255,0.08);
      padding: 2px 6px;
      border-radius: 8px;
      color: #fff;
    }

    .pill-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }

    .pill {
      background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
      border: 1px solid var(--border);
      padding: 16px;
      border-radius: 18px;
    }

    .pill strong {
      display: block;
      margin-bottom: 8px;
      color: white;
    }

    .footer {
      margin-top: 22px;
      text-align: center;
      color: var(--muted);
      font-size: 14px;
      padding: 20px 0 4px;
    }

    .highlight {
      color: #fff;
      font-weight: 700;
    }

    @media (max-width: 900px) {
      .features, .config {
        grid-column: span 12;
      }
      .hero {
        padding: 28px 20px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <section class="hero">
      <div class="badge-row">
        <div class="badge">⚡ Flask</div>
        <div class="badge">🔗 Short Link Service</div>
        <div class="badge">🛡️ User Authentication</div>
        <div class="badge">📩 Email Verification</div>
        <div class="badge">🔐 Reset Password</div>
      </div>

      <h1 class="title">
        <span>python-shortlink</span><br>
        یک کوتاه‌کننده لینک حرفه‌ای، سبک و قابل توسعه
      </h1>

      <p class="subtitle">
        این پروژه یک سرویس جذاب و کاربردی برای ساخت لینک کوتاه است که با Python و Flask پیاده‌سازی شده
        و امکاناتی مثل ثبت‌نام کاربر، ورود، تأیید ایمیل، ریست پسورد، مدیریت لینک‌ها و ساختار قابل توسعه را در اختیار شما می‌گذارد.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="https://github.com/AbolfazlNbDeV/python-shortlink">⭐ مشاهده ریپو</a>
        <a class="btn btn-secondary" href="#features">✨ قابلیت‌ها</a>
        <a class="btn btn-secondary" href="#config">⚙️ تنظیمات</a>
      </div>
    </section>

    <div class="grid">
      <section id="features" class="card features">
        <h2>🚀 قابلیت‌های اصلی</h2>
        <ul class="feature-list">
          <li><span class="icon">🔗</span><div><span class="highlight">کوتاه‌سازی لینک</span><br>تبدیل لینک‌های طولانی به لینک کوتاه، تمیز و قابل اشتراک‌گذاری.</div></li>
          <li><span class="icon">👤</span><div><span class="highlight">ثبت‌نام و ورود کاربران</span><br>سیستم کاربری برای مدیریت دسترسی‌ها و نگهداری لینک‌های هر کاربر.</div></li>
          <li><span class="icon">✅</span><div><span class="highlight">تأیید ایمیل</span><br>فعال‌سازی حساب از طریق لینک ارسالی به ایمیل کاربر.</div></li>
          <li><span class="icon">🔐</span><div><span class="highlight">بازیابی رمز عبور</span><br>ارسال لینک امن برای تنظیم رمز جدید و بازیابی حساب.</div></li>
          <li><span class="icon">📊</span><div><span class="highlight">قابلیت توسعه برای آمار</span><br>امکان افزودن شمارش کلیک و گزارش‌گیری برای لینک‌ها.</div></li>
          <li><span class="icon">🧩</span><div><span class="highlight">ساختار ساده و قابل شخصی‌سازی</span><br>مناسب برای پروژه آموزشی، دمو، یا تبدیل به سرویس واقعی.</div></li>
        </ul>

        <div class="section">
          <h2>🎯 این پروژه برای چه کسانی مناسب است؟</h2>
          <div class="pill-grid">
            <div class="pill"><strong>Developers</strong>برای یادگیری Flask و ساخت وب‌اپ‌های کاربردی</div>
            <div class="pill"><strong>Students</strong>برای پروژه دانشگاهی یا تمرین بک‌اند</div>
            <div class="pill"><strong>Freelancers</strong>برای شروع یک SaaS ساده و سبک</div>
            <div class="pill"><strong>Creators</strong>برای ساخت سرویس لینک کوتاه شخصی</div>
          </div>
        </div>
      </section>

      <aside id="config" class="card config">
        <h2>⚙️ فایل config.py</h2>
        <p>
          این فایل برای تنظیم مقادیر اصلی پروژه استفاده می‌شود.  
          برای اجرای درست برنامه، مقادیر زیر را باید با اطلاعات واقعی خودتان جایگزین کنید:
        </p>

        <div class="section code-box">
<pre>admin = "پسورد پنل بزار"
emaill = "جیمیل خود را بگزارید"
passw = "پسورد app را بگزارید"
admin_email = "admin@أدامنه خود را بگزارید مثلا test.ir"
domain = "دامنه خودتان بگزارید مثلا test.ir"</pre>
        </div>

        <div class="section">
          <ul class="step-list">
            <li><span class="icon">1</span><div><span class="highlight">admin</span><br>رمز پنل مدیریت.</div></li>
            <li><span class="icon">2</span><div><span class="highlight">emaill</span><br>آدرس ایمیل اصلی (مثلاً Gmail).</div></li>
            <li><span class="icon">3</span><div><span class="highlight">passw</span><br>رمز عبور اپلیکیشن برای ارسال ایمیل.</div></li>
            <li><span class="icon">4</span><div><span class="highlight">admin_email</span><br>ایمیل مدیر سیستم.</div></li>
            <li><span class="icon">5</span><div><span class="highlight">domain</span><br>دامنه‌ای که لینک‌ها روی آن ساخته می‌شوند.</div></li>
          </ul>
        </div>
      </aside>
    </div>

    <div class="grid">
      <section class="card" style="grid-column: span 12;">
        <h2>🛠 راه‌اندازی سریع</h2>
        <ul class="step-list">
          <li><span class="icon">①</span><div>ریپو را کلون کنید: <code>git clone https://github.com/AbolfazlNbDeV/python-shortlink.git</code></div></li>
          <li><span class="icon">②</span><div>وابستگی‌ها را نصب کنید (در صورت وجود): <code>pip install -r requirements.txt</code></div></li>
          <li><span class="icon">③</span><div>مقادیر فایل <code>config.py</code> را با اطلاعات خودتان جایگزین کنید.</div></li>
          <li><span class="icon">④</span><div>برنامه را اجرا کنید: <code>python app.py</code></div></li>
        </ul>
      </section>
    </div>

    <div class="grid">
      <section class="card" style="grid-column: span 12;">
        <h2>🔒 نکات امنیتی پیشنهادی</h2>
        <p>
          اگر این پروژه را روی اینترنت منتشر می‌کنید، بهتر است تنظیمات حساس مثل
          <code>SECRET_KEY</code>، پسوردها و تنظیمات SMTP را در فایل‌های عمومی قرار ندهید
          و از متغیرهای محیطی استفاده کنید.
        </p>
        <p style="margin-top: 10px;">
          همچنین برای نسخه نهایی می‌توانید ذخیره‌سازی پسورد را به حالت هش‌شده تغییر دهید
          تا امنیت حساب کاربران بالاتر برود.
        </p>
      </section>
    </div>

    <div class="footer">
      ساخته شده برای پروژه <span class="highlight">python-shortlink</span> — سبک، شیک، حرفه‌ای و قابل توسعه
    </div>
  </div>
</body>
</html>
