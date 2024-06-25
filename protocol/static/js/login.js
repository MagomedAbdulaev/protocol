const company_active = document.querySelector('.form__login .company--active');
const company_container = document.querySelector('.form__login .company--container');
const arrow_icon = document.querySelector('.form__login .login__company .arrow--icon');
const login_submit = document.querySelector('.form__login .login--submit');
let company_container_key = true;

company_active.addEventListener('click', ()=>{
    if(company_container_key){
        arrow_icon.classList.add('arrow--icon_active');
        company_container.classList.add('company--container_active');
        company_container_key = false;
    }
    else{
        arrow_icon.classList.remove('arrow--icon_active');
        company_container.classList.remove('company--container_active');
        company_container_key = true;
    }

})

company_container.addEventListener('click', (event) => {
    if(event.target.classList.contains('company__item') || event.target.classList.contains('company__value')){
        const company_active_value = company_active.querySelector('.company__value');
        const company_active_input = company_active.querySelector('.input--hidden');
        company_active_value.innerHTML = event.target.textContent.trim();
        company_active_input.value = event.target.textContent.trim();
        company_container.classList.remove('company--container_active');
        arrow_icon.classList.remove('arrow--icon_active');
        company_container_key = true;
    }
})