function betterThanAverage(arr) {
    var sum = 0;
    var avg = 0;
    // calculate the average
    for(var i = 0;i<arr.length;i++){
        sum = sum + arr[i];
        avg = sum/arr.length;
    }
    var count = 0
    // count how many values are greated than the average
    for(var y = 0;y<arr.length;y++){
        if(arr[y]>avg){
            count++;
        }

    }

    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4
