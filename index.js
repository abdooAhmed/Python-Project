const { spawn } = require('child_process');
const {fetch} = require{'n'}
const child = spawn('python',['gpu.py','img/abdo1.jpg','img/abdo2.jpg']);
child.stdout.on('data',(data)=>{
    console.log(`stfout:${data.values()}`);
});

console.log(fetch("https://api.randomuser.me/?nat=US&results=1"));
