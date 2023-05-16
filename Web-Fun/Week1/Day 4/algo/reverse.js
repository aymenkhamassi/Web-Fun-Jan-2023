function reverse(arr){
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
reverse(["a","b","c","d","e"]);