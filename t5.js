
var op = ['+','-','*','/'];
var str = "";
function calc(i1,i2,i3,i4,i5,i6,i7,i8){
    var str = "1"+i1+"2"+i2+"3"+i3+"4"+i4+"5"+i5+"6"+i6+"7"+i7+"8"+i8+"9";
    var t = eval(str);
    if(re == 497){
        console.log(str);
    }
    return t;
}
for(var i1 =0; i1 <4;i1++){
    const op1 = op[i1];
    for(var i2 =0; i2 <4;i2++){
        const op2 = op[i2];
        for (let i3 = 0; i3 <4; i3++) {
            const op3 = op[i3];
            for (let i4 = 0; i4 <4; i4++) {
                const op4 = op[i4];
                for (let i5 = 0; i5 <4; i5++) {
                    const i5 = op[i5];
                    for (let i6 = 0; i6 <4; i6++) {
                        const op6 = op[i6];
                        for (let i7 = 0; i7 <4; i7++) {
                            const op7 = op[i7];
                            for (let i8 = 0; i8 <4; i8++) {
                                const op8 = op[i8];
                                var re = calc(op1,op2,op3,op4,op5,op6,op7,op8);
                                if(re == 497){
                                    console.log("done!");
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }
        
    }
}