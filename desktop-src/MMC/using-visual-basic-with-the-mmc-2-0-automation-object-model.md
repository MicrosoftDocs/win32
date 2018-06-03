---
title: Using Visual Basic with the MMC 2.0 Automation Object Model
description: The following Visual Basic example code is for a simple application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e449e111-59ee-4524-a64b-133acb6bea1c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Visual Basic with the MMC 2.0 Automation Object Model

The following Visual Basic example code is for a simple application that uses the MMC 2.0 automation object model to programmatically start the MMC application, load a snap-in, set text on the status bar, and leave the user in control of the MMC console.

This example program requires that the Visual Basic project reference Microsoft Management Console 2.0.

## Example Code


```VB
' This Visual Basic project contains a reference to
' Microsoft Management Console 2.0. You can
' set the reference using VB's Project+Reference menu.
Private Sub Command1_Click()
    
    ' Provide minimal error handling.
    On Error GoTo ErrorHandler
    
    ' MMC 2.0 automation object variables.
    Dim objApp As MMC20.Application
    Dim objDoc As MMC20.Document
    Dim objSnapIns As MMC20.SnapIns
    Dim objSnapIn As MMC20.SnapIn
    Dim objView As MMC20.View
    
    ' Start the MMC application.
    Set objApp = New MMC20.Application
    
    ' Display the MMC application.
    objApp.Show
        
    ' Use the Application object to
    ' get the Document object.
    Set objDoc = objApp.Document
    
    ' Use the Document object to get
    ' the SnapIns object.
    Set objSnapIns = objDoc.SnapIns
    
    ' Use the SnapIns object to add a snap-in.
    ' This example adds the Folder snap-in by name.
    Dim strSnapName As String
    strSnapName = "Folder"
    Set objSnapIn = objSnapIns.Add(strSnapName)
    
    ' Use the Document object to get
    ' the View object.
    Set objView = objDoc.ActiveView
    
    ' Use the View object to set text on the status bar.
    Dim strText As String
    strText = "This is the left pane|middle pane|right pane"
    objView.StatusBarText = strText
        
    ' Leave the MMC application in user control.
    ' If this code is omitted, then the MMC application
    ' started by this example would be terminated when
    ' this example ends.
    objApp.UserControl = 1

    ' Done processing, so the objects can be freed.
    Set objView = Nothing
    Set objSnapIn = Nothing
    Set objSnapIns = Nothing
    Set objDoc = Nothing
    Set objApp = Nothing
    
    MsgBox ("Finished processing")
    
    Exit Sub
    
ErrorHandler:
    ' An error was encountered. Display the error
    ' description and number.
    MsgBox Err.Description & " " & Err.Number

End Sub
```



 

 




