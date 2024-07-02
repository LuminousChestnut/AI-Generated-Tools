Sub UpdateCellFromExternalFile()
    Dim sourceWorkbook As Workbook
    Dim sourceWorksheet As Worksheet
    Dim targetWorkbook As Workbook
    Dim targetWorksheet As Worksheet
    Dim sourceFilePath As String
    Dim sourceCell As Range
    Dim targetCell As Range
    
    ' 设置源文件路径（其他Excel文档）
    sourceFilePath = "C:\Path\To\SourceFile.xlsx"
    
    ' 打开源工作簿和工作表
    Set sourceWorkbook = Workbooks.Open(sourceFilePath)
    Set sourceWorksheet = sourceWorkbook.Sheets("Sheet1") ' 修改为实际的工作表名称
    
    ' 设置目标工作簿和工作表（当前工作簿）
    Set targetWorkbook = ThisWorkbook
    Set targetWorksheet = targetWorkbook.Sheets("Sheet1") ' 修改为实际的工作表名称
    
    ' 源文件中的单元格
    Set sourceCell = sourceWorksheet.Range("A1") ' 修改为实际的单元格位置
    
    ' 目标文件中要更新的单元格
    Set targetCell = targetWorksheet.Range("B1") ' 修改为实际的单元格位置
    
    ' 从源文件复制数据到目标文件
    targetCell.Value = sourceCell.Value
    
    ' 关闭源工作簿并保存更改
    sourceWorkbook.Close SaveChanges:=False
    
    MsgBox "数据已成功更新到目标单元格！"
End Sub
