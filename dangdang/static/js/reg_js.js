$(function () {
    // {#====定义标记变量======#}
    var f1
    var f2
    var f3
    var f4
    var f5
    // {#==========ajax请求头=========#}
    $.ajaxSetup({
        headers:{"X-CSRFToken":"{{ csrf_token }}"},
    })
    // {#=======用户名检测=============#}
    // {#-----------定义正则-----------#}
    var user=/^13(\d{9})$|^15(\d{9})$|^18(\d{9})$|^17(\d{9})$|^16(\d{9})$/
    var Email=/\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/
    var username= $('#txt_username')
    username.focus()
    username.blur(function () {
        if (username.val().match(user) || username.val().match(Email)) {
            $('#username_ok').attr('src','{% static "images/5-121204193934-50.gif" %}')
            $.ajax({
                type:'post',
                url:'{% url "log_reg:checkname" %}',
                data:'username='+username.val(),
                success:function (res) {
                    console.log(res)
                    if (res==='0'){
                        $('#J_tipUsername').html('此手机号已注册，请更换其它手机号，或使用该&nbsp;<a href="{% url 'log_reg:login' %}" name="mobile_login _link" class="more">手机号登录</a>')
                         $('#spn_username_ok').html('✘')
                         $('#spn_username_ok').css('color','red')
                    }else if (res==='1'){
                        f1=1
                        $('#J_tipUsername').html('>|用户名可用|<')
                        $('#J_tipUsername').css('color','green')
                        $('#spn_username_ok').html('✔')
                        $('#spn_username_ok').css('color','green')
                    }
                }
            })
        }else {
            $('#J_tipUsername').html('请输入合法用户名>11手机号或者合法电子邮箱')
        }
    })
    // {#============密码检测===========#}
    // {#  ----------定义正则---------  #}
    var pwd_q=/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$/
    var pwd_z= /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{6,16}$/
    var pwd_r= /^[0-9]{6,16}$|^[a-zA-Z]{6,16}$/
    var pwd_p=$('#txt_password')
    pwd_p.blur(function () {
          $('#J_tipPassword').html('')
         if (pwd_p.val().length>5) {
            if (pwd_p.val().match(pwd_r)){
                f2=1
                $('#div_1').css('background-color','red')
                $('#div_4').css('color','red')
                $('#div_2').css('background-color','grey')
                $('#div_5').css('color','grey')
                $('#div_3').css('background-color','grey')
                $('#div_6').css('color','grey')
            }
            if (pwd_p.val().match(pwd_z)){
                f2=2
                $('#div_2').css('background-color','gold')
                $('#div_5').css('color','gold')
                $('#div_3').css('background-color','grey')
                $('#div_6').css('color','grey')
            }
            if (pwd_p.val().match(pwd_q)){
                f2=2
                $('#div_3').css('background-color','green')
                $('#div_6').css('color','green')
            }
        } else {
            $('#J_tipPassword').html('请输入6-16位的合法密码！')
            $('#J_tipPassword').css('color','red')
            $('#div_1').css('background-color','grey')
            $('#div_2').css('background-color','grey')
            $('#div_3').css('background-color','grey')
            $('#div_4').css('color','grey')
            $('#div_5').css('color','grey')
            $('#div_6').css('color','grey')
        }
    })
    // {#  ------------密码一致性检测-----------  #}
    var check_pwd=$('#repassword')
    check_pwd.blur(function () {
        if (check_pwd.val()){
            if (check_pwd.val()===username.val()){
                f3=1
                $('#spn_repassword_ok').html('✔')
                $('#spn_repassword_ok').css('color','greenyellow')
                $('#J_tipSurePassword').html('密码一致')
                $('#J_tipSurePassword').css('color','greenyellow')
            }else{
                $('#spn_repassword_ok').html('✘')
                $('#spn_repassword_ok').css('color','gold')
                $('#J_tipSurePassword').html('两次密码不一致！请确认')
                $('#J_tipSurePassword').css('color','gold')
            }
        } else {
            $('#spn_repassword_ok').html('✘')
            $('#spn_repassword_ok').css('color','red')
            $('#J_tipSurePassword').html('密码为空！请重新输入')
            $('#J_tipSurePassword').css('color','red')
        }
    })
    // {#  ==============验证码检测==============  #}
    $('#txt_vcode').blur(function () {
        $('#vcode_ok').attr('src','{% static "images/5-121204193934-50.gif" %}')
        $.ajax({
            type: 'post',
            url:'{% url "log_reg:checkcapt" %}',
            data: 'cap='+  $('#txt_vcode').val(),
            success:function (res) {
                if (res==='1'){
                    f4=1
                    $('#spn_vcode_ok').html('✔')
                    $('#spn_vcode_ok').css('color','green')
                    $('#J_tipVcode').html('验证通过')
                    $('#J_tipVcode').css('color','green')
                }else if (res==='0'){
                    $('#spn_vcode_ok').html('✘')
                    $('#spn_vcode_ok').css('color','red')
                    $('#J_tipVcode').html('验证失败！')
                    $('#J_tipVcode').css('color','red')
                }
            }
        })
    })
    // {#  ============条款状态检测============  #}
    $('#chb_agreement').click(function () {
        if ( $('#chb_agreement').prop('checked')){
            f5=1
        }
    })
    // {#  ==============注册检测=============  #}
    $('#J_submitRegister').click(function () {
        if (f2===1){
            var y=confirm('密码等级过低！是否确认注册')
            if (y) {
                if (f4===1){
                    if (f5===1){
                        if (f1===1 & f3===1 & f2===2){
                            $('#register_form').submit()
                        } else {
                            alert('输入有误！请重新输入')
                        }
                    } else {
                        alert('请先仔细阅读相关条款！')
                    }
                } else {
                    alert('验证失败！请确认验证码')
                }
            }
        }else {
              if (f4===1){
                    if (f5===1){
                        if (f1===1 & f3===1 & f2===2){
                            $('#register_form').submit()
                        } else {
                            alert('输入有误！请重新输入')
                        }
                    } else {
                        alert('请先仔细阅读相关条款！')
                    }
              } else {
                    alert('验证失败！请确认验证码')
            }
        }
    })
})