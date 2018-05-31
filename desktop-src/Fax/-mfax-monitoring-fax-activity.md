---
Description: The following Microsoft Visual Basic code example tells you the number of incoming, outgoing, routing, and queued messages for the fax server.
ms.assetid: cf85750a-56ac-41d5-b6c0-5444934afce7
title: Monitoring Fax Activity
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Fax Activity

The following Microsoft Visual Basic code example tells you the number of incoming, outgoing, routing, and queued messages for the fax server.


```VB
    Private Sub Form_Load()
        'Create the root object.
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxActivity As FAXCOMEXLib.FaxActivity
        'Error handling
        On Error GoTo Error_Handler

        objFaxActivity = objFaxServer.Activity
        ' Connect to the fax server. 
        ' "" defaults to the server on which the script is running.
        objFaxServer.Connect("")

        'Refresh the activity object
        objFaxActivity.Refresh()

        'Display the activity properties
        MsgBox(objFaxActivity.IncomingMessages & " Incoming Messages")
        MsgBox(objFaxActivity.OutgoingMessages & " Outgoing Messages")
        MsgBox(objFaxActivity.RoutingMessages & " Routing Messages")
        MsgBox(objFaxActivity.QueuedMessages & " Queued Messages")
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



## VBScript

The Microsoft Visual Basic Scripting Edition (VBScript) equivalent is shown here. Creation of the root object is highlighted, as the code differs from that used in Visual Basic. Note that the error handling has been modified from that used in the Visual Basic code.


```VB
Sub Activity

'Create the root object.
Set objFaxServer = CreateObject ("FaxComEx.FaxServer")
Set objFaxActivity = objFaxServer.Activity

'Error handling    
On Error Resume Next

objFaxServer.Connect ""

If Err.Number <> 0 Then
    MsgBox "Error number: " & Err.Number & ", " & Err.Description
    Exit Sub
End If

'Refresh the activity object
objFaxActivity.Refresh

If Err.Number <> 0 Then
    MsgBox "Error number: " & Err.Number & ", " & Err.Description
    Exit Sub
End If

'Display the activity properties
MsgBox objFaxActivity.IncomingMessages & " Incoming Messages"
MsgBox objFaxActivity.OutgoingMessages & " Outgoing Messages"
MsgBox objFaxActivity.RoutingMessages & " Routing Messages"
MsgBox objFaxActivity.QueuedMessages & " Queued Messages"

End Sub

Activity
```



 

 



