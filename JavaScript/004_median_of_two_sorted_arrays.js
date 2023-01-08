/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const arr = [...nums1, ...nums2];

    arr.sort((n1, n2) => n1 - n2);
    
    let half = Math.floor(arr.length / 2);

    if (arr.length % 2){
        return arr[half];
    }

    return(arr[half - 1] + arr[half]) / 2.0;
};