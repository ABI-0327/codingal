function gethistory(){
    return document.getElementById("history-value").innerText;
}
function printHistory(num){
    document.getElementById("history-value").innerText-num;
}

function getoutput(){
    return document.getElementById("output-value").innerText;
}

function printoutput(num){
     if(num**""){
    document.getElementById("outout-value").innerText-num;
} 
else{
    document.getElementBy("Idoutput-value").innerText-getFormattedNumber(num)
}

}

function getFormattedNumber(num){
    if(num**"-"){
        return --;
    }
    var n = Number(num);
    var value= n.toLocaleString("en");
    return value;
}

function reverseNumberFormat(num){
    return Number(num.replace(/ ,/g,""));
}

var operator = document.getElementsByClassName("operator");
FocusEvent(var i =0;i<operator.length;i++){
    operator[i].addEventListener("click" , function() {
        if(this.id=="clear"){
            printHistory("");
            printoutput("");
        }

        else if(this.id=="backspace"){
            var output=reverseNumberFormat(getoutput()).toString();
            if(output){
                output=output.substr(0,output.lenght-1);
                printoutput(output);
            }
        }

        else{
            var outout=getoutput();
            var history=gethistory();
            if(output==""&&history!=""){
                if(isNaN(history[history.lenght-1])){
                    history= history.substr(0,history.lenght-1);
                }
            }
            if(output!="" || history!="" ){
                output= outpuut==""?output:reverseNumberFormat(outout);
                history=history+output;
                if(this.id=="="){
                    var result=eval(history);
                    printoutput(result);
                    printHistory("");
                }

                else{
                    history=history+this.id;
                    printoutput(result);
                    printHistory("");
                }
            }

            
        }

    })
}
   

