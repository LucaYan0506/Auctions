var submenu_left = false;
var submenu_right = false;

if (document.querySelector("[name='user-name']") != null){
    document.querySelector("[name='user-name']").addEventListener("mousedown",function(){
        var submenu = document.querySelector(".right #sub-menu");
        if (submenu_right == false){
            submenu.style.visibility = "visible";
            submenu.style.pointerEvents = "unset";
            submenu.style.opacity = "1";
            submenu.style.height = "92px";
            submenu.style.width = "130px";
            submenu_right = true;
        }
        else{
            submenu.style.visibility = "hidden";
            submenu.style.pointerEvents = "none";
            submenu.style.opacity = "0";
            submenu.style.height = "0px";
            submenu.style.width = "0px";
            submenu_right = false;
        }
    });
    document.querySelector("[name='user-name']").addEventListener("mouseenter",function(){
        var submenu = document.querySelector(".right #sub-menu");
        submenu.style.visibility = "visible";
        submenu.style.pointerEvents = "unset";
        submenu.style.opacity = "1";
        submenu.style.height = "92px";
        submenu.style.width = "130px";
    });

    document.querySelector("[name='user-name']").addEventListener("mouseleave",function(){
        var submenu = document.querySelector(".right #sub-menu");
        submenu.style.visibility = "hidden";
        submenu.style.pointerEvents = "none";
        submenu.style.opacity = "0";
        submenu.style.height = "0px";
        submenu.style.width = "0px";
    });
    document.querySelector(".right #sub-menu").addEventListener("mouseenter",function(){
        var submenu = document.querySelector(".right #sub-menu");
        submenu.style.visibility = "visible";
        submenu.style.pointerEvents = "unset";
        submenu.style.opacity = "1";
        submenu.style.height = "92px";
        submenu.style.width = "130px";
    });
    
    document.querySelector(".right #sub-menu").addEventListener("mouseleave",function(){
        var submenu = document.querySelector(".right #sub-menu");
        submenu.style.visibility = "hidden";
        submenu.style.pointerEvents = "none";
        submenu.style.opacity = "0";
        submenu.style.height = "0px";
        submenu.style.width = "0px";
    });
}

document.querySelector("[name='categories']").addEventListener("mousedown",function(){
    var submenu = document.querySelector(".left #sub-menu");
    if (submenu_left == false){
        submenu.style.visibility = "visible";
        submenu.style.pointerEvents = "unset";
        submenu.style.opacity = "1";
        submenu.style.height = "146px";
        submenu.style.width = "130px";
        submenu_left = true
    }
    else{
        submenu.style.pointerEvents = "none";
        submenu.style.opacity = "0";
        submenu.style.height = "0px";
        submenu.style.width = "0px";
        submenu_left = false;
    }
});

document.querySelector("[name='categories']").addEventListener("mouseenter",function(){
    var submenu = document.querySelector(".left #sub-menu");
    submenu.style.visibility = "visible";
    submenu.style.pointerEvents = "unset";
    submenu.style.opacity = "1";
    submenu.style.height = "146px";
    submenu.style.width = "130px";
    console.log("F")
});

document.querySelector("[name='categories']").addEventListener("mouseleave",function(){
    var submenu = document.querySelector(".left #sub-menu");
    submenu.style.visibility = "hidden";
    submenu.style.pointerEvents = "none";
    submenu.style.opacity = "0";
    submenu.style.height = "0px";
    submenu.style.width = "0px";
});

document.querySelector(".left #sub-menu").addEventListener("mouseenter",function(){
    var submenu = document.querySelector(".left #sub-menu");
    submenu.style.visibility = "visible";
    submenu.style.pointerEvents = "unset";
    submenu.style.opacity = "1";
    submenu.style.height = "146px";
    submenu.style.width = "130px";
});

document.querySelector(".left #sub-menu").addEventListener("mouseleave",function(){
    var submenu = document.querySelector(".left #sub-menu");
    submenu.style.visibility = "hidden";
    submenu.style.pointerEvents = "none";
    submenu.style.opacity = "0";
    submenu.style.height = "0px";
    submenu.style.width = "0px";
});

document.getElementById("comment-input").addEventListener("focusin",function(){
    let hr = document.querySelector("#black-hr");
    hr.style = "display:revert"
});

document.getElementById("comment-input").addEventListener("focusout",function(){
    let hr = document.querySelector("#black-hr");
    hr.style = "display:none"
});


function clear_input(){
    let comment = document.querySelector("#comment-input");
    comment.value = "";
}

function check_input(){
    input = document.getElementById("comment-input");
    btn = document.getElementById("Add-comment");

    if (input.value == "")
        btn.className = "btn disabled";
    else
        btn.className = "btn";
}

function standby() {
    document.getElementById('img').src = "../../../no_image.png"
}