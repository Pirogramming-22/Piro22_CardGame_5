//main.html에서 로그인하지 않고 start버튼 누르면 로그인하라는 메시지 나옴.
document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".login_btn_start");

    // 버튼 클릭 이벤트 처리
    button.addEventListener("click", function () {
        alert("로그인하세요!");
    });
});
