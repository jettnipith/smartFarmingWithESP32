// Function to handle GET requests
function getRecords() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  return JSON.stringify(data);
}

// Function to handle POST requests
function createRecord(title, author, isbn) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.appendRow([title, author, isbn]);
  return "Record created successfully";
}

// Function to handle PUT requests
function updateRecord(row, title, author, isbn) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var range = sheet.getRange(row, 1, 1, 3);
  range.setValues([[title, author, isbn]]);
  return "Record updated successfully";
}

// Function to handle DELETE requests
function deleteRecord(row) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.deleteRow(row);
  return "Record deleted successfully";
}
