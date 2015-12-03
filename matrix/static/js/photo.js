/**
 * Created by mazheng on 2015/12/3.
 */

function preview(){
    $('#photo').change(function(){
      var file = this.files[0];
      var r = new FileReader();
      r.readAsDataURL(file);
        $(r).load(function(){
          $('#preview').html('<img id="photo_img" class="img-circle" src="'+ this.result +'" alt="" />');
        });
    });
};