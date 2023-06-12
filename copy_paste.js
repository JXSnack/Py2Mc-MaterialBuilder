// copy + paste this into the console with the javadocs
// then get all the meterials with they "replace with nothing" and paste them into materials.txt
// then replace all "replace with nothing" with nothing
// run main.py
// see generated code in output.py
// copy + paste the generated code into the materials.py in Py2Mc

var cusid_ele = document.getElementsByClassName('col-last');
for (var i = 0; i < cusid_ele.length; ++i) {
    var item = cusid_ele[i];
    item.innerHTML="replace with nothing"
}