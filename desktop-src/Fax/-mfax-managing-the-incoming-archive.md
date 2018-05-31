---
Description: The following Microsoft Visual Basic code example demonstrates how to retrieve information about the incoming archive and faxes in the archive, and how to delete a fax from the archive.
ms.assetid: 1e66b30d-e74f-4c73-b005-acd2d0fd8893
title: Managing the Incoming Archive
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing the Incoming Archive

> [!Note]  
> For Windows Vista, refer to the example in [Managing Queues and Archives](-mfax-managing-queues-and-archives.md).

 

The following Microsoft Visual Basic code example demonstrates how to retrieve information about the incoming archive and faxes in the archive, and how to delete a fax from the archive.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxIncomingArchive As FAXCOMEXLib.FaxIncomingArchive
        Dim objFaxIncomingMessage As FAXCOMEXLib.FaxIncomingMessage

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the incoming archive
        objFaxIncomingArchive = objFaxServer.Folders.IncomingArchive

        'Refresh the object and retrieve/display some of its properties
        objFaxIncomingArchive.Refresh()
        MsgBox("High quota water mark: " & objFaxIncomingArchive.HighQuotaWaterMark & _
        vbCrLf & "Low quota water mark:  " & objFaxIncomingArchive.LowQuotaWaterMark & _
        vbCrLf & "Archive folder: " & objFaxIncomingArchive.ArchiveFolder & _
        vbCrLf & "Age limit: " & objFaxIncomingArchive.AgeLimit & _
        vbCrLf & "Size high: " & objFaxIncomingArchive.SizeHigh & _
        vbCrLf & "Size low: " & objFaxIncomingArchive.SizeLow & _
        vbCrLf & "Is size quota warning on: " & objFaxIncomingArchive.SizeQuotaWarning & _
        vbCrLf & "Is archive used: " & objFaxIncomingArchive.UseArchive)

        'Set the age limit to 4 days
        objFaxIncomingArchive.AgeLimit = 4

        'Save the changes
        objFaxIncomingArchive.Save()

        'Get a message by ID
        Dim MessageID As String
        Dim Answer As String
        Dim FileName As String

        Answer = InputBox("Retrieve a message by its ID (Y/N)?")
        If Answer = "Y" Then

            MessageID = InputBox("Provide the message ID")

            'Get the job
            objFaxIncomingMessage = objFaxIncomingArchive.GetMessage(MessageID)

            'Display information about the retrieved job
            MsgBox("Caller ID: " & objFaxIncomingMessage.CallerId & _
            vbCrLf & "CSID: " & objFaxIncomingMessage.CSID & _
            vbCrLf & "Device name: " & objFaxIncomingMessage.DeviceName & _
            vbCrLf & "Message ID: " & objFaxIncomingMessage.Id & _
            vbCrLf & "Number of pages: " & objFaxIncomingMessage.Pages & _
            vbCrLf & "Number of retries: " & objFaxIncomingMessage.Retries & _
            vbCrLf & "Routing information: " & objFaxIncomingMessage.RoutingInformation & _
            vbCrLf & "Size: " & objFaxIncomingMessage.Size & " bytes" & _
            vbCrLf & "Transmission start: " & objFaxIncomingMessage.TransmissionStart & _
            vbCrLf & "Transmission end: " & objFaxIncomingMessage.TransmissionEnd & _
            vbCrLf & "TSID: " & objFaxIncomingMessage.TSID)

            'Allow user to delete the message
            Answer = InputBox("Delete this message from the archive?")
            If Answer = "Y" Then objFaxIncomingMessage.Delete()

        End If
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



