<b>
  <h3>
  پروژه آموزشی جنگو 3
  </h3>
</b>

<hr>

<h2>
  در این پروژه یاد میگیرم یک وب‌سایت ساده با موضوع بلاگ طراحی کنیم و برای تسریع در توسعه پروژه از یک تمپلیت آماده رایگان از فریم‌ورک بوت استرپ استفاده می‌کنیم.
</h2>
  
<hr>

ابتدا یک محیط مجازی با دستور زیر ایجاد کنید
<br>
<div class="highlight highlight-source-shell">
  <pre>$ virtualenv .env</pre>
</div>

<br>

سپس آنرا فعال کنید

<br>

ویندوز:
<br>
<div class="highlight highlight-source-shell">
  <pre>$ .env\Scripts\activate
</pre>
</div>

<br>

لینوکس:
<br>
<div class="highlight highlight-source-shell">
  <pre>$ .env/bin/activate
</pre>
</div>

<br>

سپس پکیج‌های مورد نیاز را نصب کنید
<br>
<div class="highlight highlight-source-shell">
  <pre>$ pip install -r requirements.txt
</pre>
</div>

<br>


حال نیاز است که فایل‌های مایگریشن پروژه را ایجاد کنیم
<br>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py makemigrations
</pre>
</div>

<br>


سپس با دستور زیر جداول مایگیریشن را در دیتابیس ایجاد میکنیم
<br>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py migrate
</pre>
</div>

<br>


در آخر جهت انتقال فایل‌های استاتیک اپلیکیشن به روت پروژه، دستور زیر را بزنید
<br>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py collectstatic
</pre>
</div>

<br>

با دستور زیر پروژه را ران کنید
<br>
<div class="highlight highlight-source-shell">
  <pre>$ python manage.py runserver
</pre>
</div>

<br>

:)))  هورااا
