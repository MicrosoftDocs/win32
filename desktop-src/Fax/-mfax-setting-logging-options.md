---
Description: 'The following Microsoft Visual Basic code example demonstrates how to set logging options. The log path is not set in this example. If you change the path to the activity log directory, be sure to use a secured directory.'
ms.assetid: 'afee6ea0-f63d-4818-9ff0-1887638d232c'
title: Setting Logging Options
---

# Setting Logging Options

The following Microsoft Visual Basic code example demonstrates how to set logging options. The log path is not set in this example. If you change the path to the activity log directory, be sure to use a secured directory.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxActivityLogging As FAXCOMEXLib.FaxActivityLogging
        Dim objFaxLoggingOptions As FAXCOMEXLib.FaxLoggingOptions
        Dim objFaxEventLogging As FAXCOMEXLib.FaxEventLogging

        'Error handling
        On Error GoTo Error_Handler

        'Connect to fax server. Empty string defaults to local server
        objFaxServer.Connect("")

        'Create the logging options object
        objFaxLoggingOptions = objFaxServer.LoggingOptions

        'Create the activity and event logging objects
        objFaxActivityLogging = objFaxLoggingOptions.ActivityLogging
        objFaxEventLogging = objFaxLoggingOptions.EventLogging

        'Refresh the activity logging object
        objFaxActivityLogging.Refresh()
        'Set the activity logging properties
        objFaxActivityLogging.LogIncoming = True
        objFaxActivityLogging.LogOutgoing = True
        'Save the changes
        objFaxActivityLogging.Save()

        'Refresh the event logging object
        objFaxEventLogging.Refresh()
        'Set the event logging properties
        objFaxEventLogging.GeneralEventsLevel = FAXCOMEXLib.FAX_LOG_LEVEL_ENUM.fllMED
        objFaxEventLogging.InboundEventsLevel = FAXCOMEXLib.FAX_LOG_LEVEL_ENUM.fllMAX
        objFaxEventLogging.InitEventsLevel = FAXCOMEXLib.FAX_LOG_LEVEL_ENUM.fllMIN
        objFaxEventLogging.OutboundEventsLevel = FAXCOMEXLib.FAX_LOG_LEVEL_ENUM.fllNONE
        'Save the changes
        objFaxEventLogging.Save()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



