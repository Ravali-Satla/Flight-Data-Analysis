function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.day= values[0];
    obj.group= values[1];
    obj.price= values[2];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }