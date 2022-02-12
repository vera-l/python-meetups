const fs = require('fs');

console.log('start');

new Promise((resolve, reject) => {
    console.log('new Promise');
    resolve();
})
.then(_ => console.log('then-1'))
.then(_ => console.log('then-2'));

setTimeout(_ => console.log('setTimeout-1'), 0);
setImmediate(_ => console.log('setImmediate-1'));

fs.open(__filename, _ => {
    console.log('fs.open');
    setImmediate(_ => console.log('setImmediate-2'));
    setTimeout(_ => console.log('setTimeout-2'), 0);
    setTimeout(_ => console.log('setTimeout-3'), 0);
    queueMicrotask(_ => {
        console.log('queueMicrotask-1')
    });
    process.nextTick(_ => console.log('nextTick-4'));
});

process.nextTick(_ => {
    console.log('nextTick-1');
    process.nextTick(_ => {
        console.log('nextTick-2');
        process.nextTick(_ => console.log('nextTick-3'));
    });
});

console.log('end');
