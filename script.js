const checkButton = document.getElementById("check-button");

checkButton.addEventListener("click", function(){
    const getPassword = document.getElementById("password-input").value;
    const strengthText = document.getElementById("strength-text");
    const bar = document.querySelector(".strength-fill");
    const checks = {
        lengths: getPassword.length >= 8,
        lowercase: /[a-z]/.test(getPassword),
        uppercase: /[A-Z]/.test(getPassword),
        number: /[0-9]/.test(getPassword)
    };
    const passed = Object.values(checks).filter(Boolean).length;
    if (passed == 4){
        strengthText.textContent = "Strong";
        bar.style.width = "100%";
    }
    else if (passed >= 2){
        strengthText.textContent = "Medium";
        bar.style.width = "50%";
    }
    else{
        strengthText.textContent = "Weak";
        bar.style.width = "0%";
    }
    const length = document.getElementById("eight-char");
    const upper = document.getElementById("upper-char");
    const lower = document.getElementById("lower-char");
    const number = document.getElementById("number-char");

    if (checks.lengths){
        length.style.color = "#1cbd57";
    }else{
        length.style.color = "#bd1c1c";
    }
    if (checks.uppercase){
        upper.style.color = "#1cbd57";
    }else{
        upper.style.color = "#bd1c1c";
    }
    if (checks.lowercase){
        lower.style.color = "#1cbd57";
    }else{
        lower.style.color = "#bd1c1c";
    }
    if (checks.number){
        number.style.color = "#1cbd57";
    }else{
        number.style.color = "#bd1c1c";
    }
}
);