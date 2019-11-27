function sendRequest(){
    var ss = SpreadsheetApp.getActiveSheet();
    var range = ss.getActiveRange();
    var values = ss.getRange(range.getRow(), range.getColumn(), range.getNumRows(), range.getNumColumns()).getValues(); 
    var values2 = ss.getRange(range.getRow(), range.getColumn()+1, range.getNumRows(), range.getNumColumns()).getValues(); 
    var data =[]
    values.forEach(function(row, index){
      for (var k = 0; k<row.length; k++){
         if (row[k]!=""){
           data.push({"cell":row[k],"name":values2[index][0]})         
        }
      }    
    }) 
    var options = {
      'method' : 'post',
      'contentType': 'application/json',
      // Convert the JavaScript object to a JSON string.
      'payload' : JSON.stringify(data)
    };
    var response = UrlFetchApp.fetch('35.237.144.90/generate', options);
    
    var ui = SpreadsheetApp.getUi(); // Same variations.
    if (response = "Success"){
      var result = ui.alert(
       'REQUEST RESULT',
       'Request to server sending'+response,
        ui.ButtonSet.YES_NO);
    }else{
      var result = ui.alert(
       'REQUEST RESULT',
       'Request to server sending not success '+response,
        ui.ButtonSet.YES);    
    }
  
    
    
  }
  
  function onOpen() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet();
    var entries = [{
      name : "TTS",
      functionName : "sendRequest"
    }];
    sheet.addMenu("TTS", entries);
  };