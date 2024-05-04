document.addEventListener("DOMContentLoaded", function(){
      var el = document.querySelector(".button-bird");
      var text = document.querySelector(".button-bird__text");
          el.addEventListener('click', function() {
            el.classList.toggle('active');

            if(el.classList.contains('active')){
            	console.log('true');
            	text.innerHTML = 'DONE';
                setTimeout(yagnaraval, 3000);

                
        
                

            }else{
            	text.innerHTML = 'SEND';
            }
           
        });
    });

    function yagnaraval() {
        window.location.assign("http://localhost/projects/cn/main/dist/website/result.php")
      }