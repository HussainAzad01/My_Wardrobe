searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
  searchForm.classList.toggle('active');
}

let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () =>{
  loginForm.classList.toggle('active');
}

document.querySelector('#close-login-btn').onclick = () =>{
  loginForm.classList.remove('active');
}

window.onscroll = () =>{

  searchForm.classList.remove('active');

  if(window.scrollY > 80){
    document.querySelector('.header .header-2').classList.add('active');
  }else{
    document.querySelector('.header .header-2').classList.remove('active');
  }

}

//window.onload = () =>{
//
//  if(window.scrollY > 80){
//    document.querySelector('.header .header-2').classList.add('active');
//  }else{
//    document.querySelector('.header .header-2').classList.remove('active');
//  }
//
//  fadeOut();
//
//}

//function loader(){
//  document.querySelector('.loader-container').classList.add('active');
//}

//function fadeOut(){
//  setTimeout(loader, 4000);
//}

var swiper = new Swiper(".books-slider", {
  loop:true,
  centeredSlides: false,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".featured-slider", {
  spaceBetween: 10,
  loop:true,
  centeredSlides: false,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    450: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
});

var swiper = new Swiper(".arrivals-slider", {
  spaceBetween: 10,
  loop:false,
  centeredSlides: false,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 10,
  grabCursor:true,
  loop:true,
  centeredSlides: false,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

var swiper = new Swiper(".blogs-slider", {
  spaceBetween: 10,
  grabCursor:true,
  loop:true,
  centeredSlides: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});

if(localStorage.getItem('cart') == null){
var cart = {};

}
else{
cart = JSON.parse(localStorage.getItem('cart'));
document.getElementById('cart').innerHTML = Object.keys(cart).length;
update_cart(cart);
}

$('.cart').click(function(){

    var idstr = this.id.toString();
    if (cart[idstr] != undefined){
    cart[idstr] = cart[idstr] + 1;
    update_cart(cart);
    }
    else{
    cart[idstr] = 1;
    update_cart(cart);
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
});

function update_cart(cart){
    for (var item in cart){
        document.getElementById('div'+item).innerHTML = "<button id='minus"+item +"' class='btn cart minus'>-</button><span id='val"+ item +"'>  "+ cart[item] +"  </span><button id='plus" + item +"' class='btn cart plus'>+</button>";

    }
}