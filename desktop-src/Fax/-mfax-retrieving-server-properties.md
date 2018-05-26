---
Description: The following Microsoft Visual Basic code example retrieves several read-only properties of the fax server.
ms.assetid: 80437d99-5b9f-4faa-8f09-ed91fc622d4b
title: Retrieving Server Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Server Properties

The following Microsoft Visual Basic code example retrieves several read-only properties of the fax server.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Display server properties

        MsgBox("Server information" & vbCrLf & _
        vbCrLf & "API Version: " & objFaxServer.APIVersion & _
        vbCrLf & "Debug: " & objFaxServer.Debug & _
        vbCrLf & "Build and version: " & objFaxServer.MajorBuild & "." & _
        objFaxServer.MinorBuild & "." & objFaxServer.MajorVersion & "." & _
        objFaxServer.MinorVersion & "." & _
        vbCrLf & "Server name: " & objFaxServer.ServerName)
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



