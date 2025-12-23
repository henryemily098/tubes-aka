/**
 * 
 * @param {[]} matrix 
 * @param {number} n 
 */
function iterative(matrix, n) {
    let left = 0, right = 0;
    for (let i = 0; i < n; i++) {
        let k = i, total = 1;
        for (let j = 0; j < n; j++) {
            if(k >= n) k = 0;
            total *= matrix[j][k];
            k++;
        }
        left += total;
    }
    for (let i = 0; i < n; i++) {
        let k = i, total = 1;
        for (let j = 0; j < n; j++) {
            if(k < 0) k = n-1;
            total *= matrix[j][k];
            k--;
        }
        right += total;
    }
    return left - right;
}

function innerRecursive(matrix, n, column = 0, row = 0, step) {
    if(column === n) return 1;
    else {
        if(step === 1) {
            if(row === n-1) return matrix[column][row] * innerRecursive(matrix, n, column+1, 0, 1);
            else return matrix[column][row] * innerRecursive(matrix, n, column+1, row+1, 1);
        }
        else if(step === -1) {
            if(row === 0) return matrix[column][row] * innerRecursive(matrix, n, column+1, n-1, -1);
            else return matrix[column][row] * innerRecursive(matrix, n, column+1, row-1, -1);
        }
    }
}

/**
 * 
 * @param {[]} matrix 
 * @param {number} n 
 */
function recursive(matrix, n, row, step = null) {
    if(step != null) {
        if(row === n-1) return innerRecursive(matrix, n, 0, row, step);
        else return innerRecursive(matrix, n, 0, row, step) + recursive(matrix, n, row+1, step); 
    }
    else return recursive(matrix, n, 0, 1) - recursive(matrix, n, 0, -1);
}

// let matrix = [
//     [
//         1, 2, 3
//     ],
//     [
//         20, 7, 6
//     ],
//     [
//         21, 10, 11
//     ]
// ];

// console.log(recursive(matrix, matrix.length));
// console.log(iterative(matrix, matrix.length));

/**
 * 
 * (0 0) (0 1) (0 2) 
 * (1 0) (1 1) (1 2)
 * (2 0) (2 1) (2 2)
 * 
 */
