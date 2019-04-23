function totp(q)
{
  // alert(q.value);
  var quantity=$("#quantity").val();
  
  var price=$("#price").val();
 
  total=quantity*price;
 
  $("#tprice").val(total);

}      

function getproducts(a,b)
{
	
var elements=document.getElementsByClassName("category");

 for(var i=0;i<elements.length;i++)
 {
 if((elements[i].value)!=b)
 {
  elements[i].checked="";
 }
 }
$.ajax({
              url: '/customer/finds/', 
              data:
              {
                     
                  'val':b
                    
                },

                
                success: function (data) 
                  {
                   
                    document.getElementById("contents").innerHTML=data;

                    
                } 
              }); 
}

function getentre(a,b)
{
  
var elements=document.getElementsByClassName("category");

 for(var i=0;i<elements.length;i++)
 {
 if((elements[i].value)!=b)
 {
  elements[i].checked="";
 }
 }
$.ajax({
              url: '/customer/efinds/', 
              data:
              {
                     
                  'val':b
                    
                },

                
                success: function (data) 
                  {
                   
                    document.getElementById("contents").innerHTML=data;

                    
                } 
              }); 
}
