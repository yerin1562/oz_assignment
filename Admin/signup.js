//제출 이벤트를 받는다 (이벤트 핸들링)

//제출된 입력 값들을 참조한다

//입력값에 문제가 있는 경우 이를 감지한다

//가입 화영 인사를 제공한다

const themeToggleButton = document.getElementById('themeToggle');

// 버튼 클릭 이벤트 리스너 추가
themeToggleButton.addEventListener('click', () => {
    // 현재 테마를 가져오기
    const currentTheme = document.documentElement.getAttribute('data-bs-theme');

    // 테마를 토글
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-bs-theme', 'light'); // 라이트 모드로 변경
        themeToggleButton.textContent = 'Dark Mode'; // 버튼 텍스트 변경
    } else {
        document.documentElement.setAttribute('data-bs-theme', 'dark'); // 다크 모드로 변경
        themeToggleButton.textContent = 'Light Mode'; // 버튼 텍스트 변경
    }
});



const form = document.getElementById("form")

form.addEventListener("submit", function(event){
    event.preventDefault()
    
    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value

    console.log(userId, userPw1, userPw2, userName, userPhone, userGender, userEmail)
    

    if (userId.length < 6 || userId.length > 20) {
        alert("아이디는 6자 이상 20자 이하로 입력해주세요.");
        return;
    }

    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    if (userPhone.length !== 11 || !userPhone.startsWith('010')) {
        alert("전화번호는 010으로 시작하고 11자로 입력해주세요.");
        return;
    }


    alert(`${userName}님 환영합니다! 
        아이디 : ${userId}
        이름 : ${userName}
        전화번호 : ${userPhone}
        이메일 : ${userEmail}
        성별 : ${userGender}`)

    //가입이 잘 되었습니다. 환영합니다!
    window.location.href = "login.html"
    

})

