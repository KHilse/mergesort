// Helper function for MergeSort
// This function assumes both source arrays are sorted,
// then builds a result array by comparing the first
// elements from each and storing the lower one
const merge = (arr1, arr2) => {
    result = [];
    while (arr1.length && arr2.length) {
        (arr1[0] < arr2[0]) ? result.push(arr1.shift()) : result.push(arr2.shift())
    }
    return result.concat(arr1).concat(arr2)
}

// Sorts the input list using a recursiv
// mergesort algorithm
const MergeSort = arr => {
    if (arr.length > 1) {
        let mid = Math.floor(arr.length / 2);
        return merge(MergeSort(arr.slice(0,mid)),MergeSort(arr.slice(mid,mid.length)));
    }
    return arr;
}

//console.log(merge([2,4,6],[3,5,7,9]))

random_list = []
for (let i = 0; i < 100; i++) {
    random_list.push(Math.floor(Math.random()*100));
}
console.log(MergeSort(random_list));