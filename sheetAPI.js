var ss = SpreadsheetApp.openById('1mICyEsokUMQX_rj6r0ofmFkeLQ2zqangyxB4ILv47c8')
var sheet = ss.getSheetByName('ชีต1')

function doGet(e) {
  var action = e.parameter.action
if (action == 'getAllData') {
    return getAllData(e)
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
