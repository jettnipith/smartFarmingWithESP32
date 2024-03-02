var ss = SpreadsheetApp.openById('1mICyEsokUMQX_rj6r0ofmFkeLQ2zqangyxB4ILv47c8')
var sheet = ss.getSheetByName('ชีต1')

function doGet(e) {
  var action = e.parameter.action;
  if (action == 'getAllData') {
    return getAllData(e);
  } else if (action == 'createNewData') {
    return createNewData(e);
  } else if (action == 'updateData') {
    return updateData(e);
  }
}

function getAllData(e) {
  var rows = sheet.getRange(2,1,sheet.getLastRow()-1,sheet.getLastColumn()).getValues()
  var data =[]
  for(var i=0; i<rows.length;i++){
    var row = rows[i]
    var record = {}
        record['DeviceId']=row[0]
        record['DeviceType']=row[1]
        record['DeviceName']=row[2]
        record['DeviceVal']=row[3]
        data.push(record)
  }
  var result = JSON.stringify(data)
  return ContentService.createTextOutput(result).setMimeType(ContentService.MimeType.JSON)
}

function createNewData(e) {
  var deviceId = e.parameter.deviceId;
  var deviceType = e.parameter.deviceType;
  var deviceName = e.parameter.deviceName;
  var deviceVal = e.parameter.deviceVal;
  
  // Assuming the data will be added to the next available row
  var newRow = [deviceId, deviceType, deviceName, deviceVal];
  sheet.appendRow(newRow);
  
  return ContentService.createTextOutput("Data created successfully").setMimeType(ContentService.MimeType.TEXT);
}

function updateData(e) {
  var rowToUpdate = e.parameter.row; // Assuming this is the row number to update
  var deviceId = e.parameter.deviceId;
  var deviceType = e.parameter.deviceType;
  var deviceName = e.parameter.deviceName;
  var deviceVal = e.parameter.deviceVal;

  // Update the values in the specified row
  var range = sheet.getRange(rowToUpdate, 1, 1, 4); // Assuming 4 columns
  var newValues = [deviceId, deviceType, deviceName, deviceVal];
  range.setValues([newValues]);
  
  return ContentService.createTextOutput("Data updated successfully").setMimeType(ContentService.MimeType.TEXT);
}
