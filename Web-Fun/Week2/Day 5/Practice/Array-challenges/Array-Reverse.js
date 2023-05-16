function reverse(arr) {
    // your code here
        var start =0
        var end=arr.length-1
        var temp;
    
    
        while(start<end/2){
            temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start+=1;
            end-=1;
    
        }
       console.log (arr);
    }
    

   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
