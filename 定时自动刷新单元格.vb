Dim NextRunTime As Double

Sub StartAutoRefresh()
    ' 设置初始刷新时间为当前时间 + 1秒
    NextRunTime = Now + TimeValue("00:00:01")
    ' 开始自动刷新
    ScheduleRefresh
End Sub

Sub StopAutoRefresh()
    ' 停止自动刷新
    On Error Resume Next
    Application.OnTime NextRunTime, "ScheduleRefresh", , False
End Sub

Sub ScheduleRefresh()
    ' 设置下一次刷新的时间
    NextRunTime = Now + TimeValue("00:00:01")
    ' 调用 RefreshAllCells 以刷新所有单元格数据
    RefreshAllCells
    ' 继续下一次刷新
    Application.OnTime NextRunTime, "ScheduleRefresh"
End Sub

Sub RefreshAllCells()
    Dim ws As Worksheet
    Dim cell As Range
    Dim rng As Range
    
    ' 遍历所有工作表
    For Each ws In ThisWorkbook.Worksheets
        ' 遍历所有单元格
        For Each cell In ws.UsedRange
            ' 在这里可以编写刷新单元格数据的逻辑
            ' 这里仅示例将单元格内容设置为当前时间
            cell.Value = Now
        Next cell
    Next ws
End Sub
