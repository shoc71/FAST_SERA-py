const print = (inforamtion) => {console.log(`${inforamtion}`)}

print('program start')

// const add = (a, b) => a + b;

const add = (...allNumbers) => {
    // print(nums)
    let total = 0;
        allNumbers.forEach(n => total += n) 
    return print(total)
}

add(30,123, 54, 324, 7658, 2432, 234, 1065, 324)
add(1000, 234,653,5687,73,3143,416,154)
add(30,12)

print('program end')