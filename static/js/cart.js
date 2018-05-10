// 加载页面的时候，为需要点击的地方添加函数
$(function () {
        sumprice()
        $('#test').click(function () {
            alert('111')
        })
        $('#allcheck').click(function () {
            $(".onecheck").prop('checked', false);
            if ($(this).is(':checked')) {
                $(".onecheck").prop('checked',true);
            }
            sumprice();
        })
        $('.onecheck').click(
            function () {
                sumprice()
            }
        )
        function sumprice() {
            var sumprice = 0;
            $('.onecheck').each(
                function () {
                    if ($(this).is(":checked")) {
                        console.log($(this).parent().parent().children("[class='price']"))
                        sumprice += parseFloat($(this).parent().parent().children("[class='price']").html());
                        console.log(sumprice)
                    }
                }
            )
            $('.sumprice').html('总价:'+sumprice);
        }
        $('.addgood').click(function () {
            alert('1')
        });
        $('.delBtn').click(function () {
            // $order_lists = $(this).parents('.order_lists');
            // $order_content = $order_lists.parents('.order_content');
            // $('.model_bg').fadeIn(300);
            $('.my_model').fadeIn(300);
        });
        $('.dialog-close').click(function () {
            $('.my_model').fadeOut(300);
        })
    }
)
function name(params) {
    
}
function add(id, pic, title, price){
    //获取5个文本框的值，并创建2个按钮
    var goodid=id;
    var pic=pic;
    var prduct_name=title;
    var pro_price=price;
    var pro_num=1;
    //动态创建4个TD，分别保存值，以及两个按钮
    //动态创建一个tr，并将4个td设置为一个tr的子元素
    
    var line=document.createElement('tr');
    var id_td=document.createElement('td');
    var pic_td=document.createElement('td');
    var name_td=document.createElement('td');
    var price_td=document.createElement('td');
    var num_td=document.createElement('td');
    var bt=document.createElement('td');
    var btdelete=document.createElement('button');
    var btchange=document.createElement('button');
    //为删除和修改按钮绑定事件
    btdelete.onclick=function(){
        $('main').removeChild(btdelete.parentNode.parentNode);
    }
    btchange.onclick=function(){
        console.log(btchange.parentNode.previousSibling);
        var changebox=btchange.parentNode.previousSibling;
        if (btchange.innerHTML=='修改'){
            var num=changebox.innerHTML;
            changebox.innerHTML="";
            var inputbox=document.createElement('input');
            inputbox.type='text';
            inputbox.value=num;
            inputbox.onkeypress=function(event){
                var reg=/\d*/g;						
                if((event.key).search(/\d+/g)!=-1){return true}
                return false;
            }
            changebox.appendChild(inputbox);
            btchange.innerHTML='确定';
        }else{
            var num=changebox.children[0].value;
            console.log(num);
            if(num>=0){
            changebox.innerHTML=num;
            btchange.innerHTML='修改';
            }else{
            alert('请输入大于0的数字');
            }
        }
    }
    
    btdelete.innerHTML='删除';
    btchange.innerHTML='修改';
    //添加动态元素属性
    line.className='line';
    id_td.innerHTML = goodid;
    pic_td.innerHTML = pic;
    name_td.innerHTML=prduct_name;
    price_td.innerHTML=pro_price;
    num_td.innerHTML=pro_num;
    //将tr添加到body中
    bt.appendChild(btdelete);
    bt.appendChild(btchange);
    line.appendChild(id_td);
    line.appendChild(pic_td);
    line.appendChild(name_td);
    line.appendChild(price_td);
    line.appendChild(num_td);
    line.appendChild(bt);

    $('main').appendChild(line);
}