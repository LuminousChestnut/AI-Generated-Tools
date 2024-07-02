Sub FetchWebsiteData()
    Dim url As String
    Dim http As Object
    Dim html As Object
    Dim dataElement As Object
    Dim rowNum As Integer
    
    ' 网站URL
    url = "https://example.com/data"
    
    ' 创建一个新的HTTP请求
    Set http = CreateObject("MSXML2.XMLHTTP")
    http.Open "GET", url, False
    http.send
    
    ' 解析HTML内容
    Set html = CreateObject("htmlfile")
    html.body.innerHTML = http.responseText
    
    ' 查找特定的数据元素，这里假设数据在一个特定的元素中
    Set dataElement = html.getElementById("dataElementId")
    
    ' 如果找到数据元素
    If Not dataElement Is Nothing Then
        ' 写入Excel表格中的第一列，逐行写入数据
        rowNum = 1
        Do While Len(dataElement.innerText) > 0
            Cells(rowNum, 1).Value = dataElement.innerText
            Set dataElement = dataElement.NextSibling
            rowNum = rowNum + 1
        Loop
        
        MsgBox "数据已成功获取并写入Excel表格！"
    Else
        MsgBox "未找到数据元素。"
    End If
    
    ' 清理对象
    Set http = Nothing
    Set html = Nothing
    Set dataElement = Nothing
End Sub
