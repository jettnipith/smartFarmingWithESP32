function doGet(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1'); // ถ้าใช้ชื่่ออื่น เปลี่ยนตรงนี้
  
  var moisture = e.parameter.moisture;
  var status   = e.parameter.status;
  var temp     = e.parameter.temp;
  var humid    = e.parameter.humid;
  
  sheet.appendRow([
    new Date(),
    moisture,
    status,
    temp,
    humid
  ]);
  
  return ContentService.createTextOutput('OK');
}
