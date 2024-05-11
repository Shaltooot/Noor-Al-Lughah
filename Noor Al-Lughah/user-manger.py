<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="login.css">
    <title> نور اللغة | انشاء حساب </title>
</head>

<body>

    <nav>
        <div class="left">
            <div class="logo">
                <img src="assests/logo.png">
            </div>
            <div class="links">
                <a href="main.html">الصفحة الرئيسية</a>
                <a href="courses.html">الدورات التعليمية</a>
                <a href="dictionary.html">القاموس</a>
            </div>
        </div>

        <div class="buttons">
            <a href="account.html"><i class='bx bx-user'></i></a>
            <a href="signup.html"><i class='bx bx-log-in'></i></a>
        </div>

    </nav>

    <div class="content">
        <div class="wrapper">z
            <h2>تغير معلوماتك</h2><br>
            <form id="account-changer-form">
                <label for="email">بريدك الاكتروني</label><br><br>
                <label for="email"></label><br><br>
                <i id="toggleEmail" class='bx bx-envelope' ></i><br><br>
                <label for="username">المستخدم</label><br><br>
                <label for="username"></label><br><br>
                <i id="toggleUser" class='bx bxs-user'></i><br><br>
                <label for="password">كلمة السر</label><br><br>
                <div class="password-container">
                    <label for="password"></label><br><br>
                    <i class="bx bxs-show" id="togglePassword"></i>
                </div><br><br>
                <button type="submit">تغير معلوماتك</button>
            </form>
            </div><br><br><br><br>
        </div>
    </div>
    <footer>
        <div class="columns">
            <div class="col">
                <h5>روابط الموقع</h5>
                <a href="main.html">الصفحة الرئيسية</a>
                <a href="courses.html">الدورات التعيمية</a>
                <a href="dictionary.html">القاموس</a>
                <a href="login.html">التسجيل الدخول</a>
                <a href="signup.html">انشاء حساب</a>
                <a href="account.html">حسابك</a>
            </div>
            <div class="col last">
                <h5>خدماتنا</h5>
                <p>نحن نقدم العديد من الميزات 
                والخدمات التي تنفع الطلاب ومفيدة 
                للمدارس</p>
                <div class="social-links">
                    <i class='bx bxl-instagram'></i>
                    <i class='bx bxl-dribbble'></i>
                    <i class='bx bxl-linkedin'></i>
                    <i class='bx bxl-twitter'></i>
                </div>
            </div>
        </div>
        <div class="copyright">
            <p> حقوق النسخ خاصة © 2024 احمد شلتوت و عائشة شلتوت</p>
        </div>
    </footer>


</body>
<script src="signup.js"></script>
</html>