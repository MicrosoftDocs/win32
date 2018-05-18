---
Description: 'The following Microsoft Visual Basic code example demonstrates how to retrieve a fax from the outgoing archive using the outgoing fax iterator. It also displays the fax''s properties and provides an option for deleting the fax.'
ms.assetid: '072eb2cc-7fd9-4f8e-8583-44384357e708'
title: Opening a Fax from the Outgoing Archive
---

# Opening a Fax from the Outgoing Archive

The following Microsoft Visual Basic code example demonstrates how to retrieve a fax from the outgoing archive using the outgoing fax iterator. It also displays the fax's properties and provides an option for deleting the fax.

> [!Note]  
> You should check the type of file the user wants to open. Do not allow a user to open a file unless you know its source and are certain that its contents are safe.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxOutgoingMessageIterator As FAXCOMEXLib.FaxOutgoingMessageIterator
        Dim objFaxOutgoingMessage As FAXCOMEXLib.FaxOutgoingMessage
        Dim Prefetch As String
        Dim Answer As String
        Dim FileName As String

        Dim A As Object

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the iterator and Set the prefetch buffer size
        Prefetch = InputBox("How many messages should be prefetched?")

        'Refresh the archive
        objFaxServer.Folders.OutgoingArchive.Refresh()

        objFaxOutgoingMessageIterator = objFaxServer.Folders.OutgoingArchive.GetMessages(Prefetch)

        'Set the iterator cursor to the first message in the buffer
        objFaxOutgoingMessageIterator.MoveFirst()

        For i = 1 To Prefetch
            If i > 1 Then
                Answer = InputBox("View next message (Y/N)?")
                If Answer <> "Y" Then
                    Exit Sub
                End If
            End If


            'Check for end of file
            If objFaxOutgoingMessageIterator.AtEOF = True Then
                MsgBox("End of File Reached")
                Exit Sub
            End If

            'Get the message
            objFaxOutgoingMessage = objFaxOutgoingMessageIterator.Message
            FileName = InputBox("Provide path and name of file for TIFF copy, e.g. c:\MyFax.tiff")
            objFaxOutgoingMessage.CopyTiff(FileName)

            'Open the tiff file
            A = CreateObject("wscript.shell")
            A.run(FileName)

            'Display message properties
            MsgBox("Message information" & _
            vbCrLf & "CSID: " & objFaxOutgoingMessage.CSID & _
            vbCrLf & "Device name: " & objFaxOutgoingMessage.DeviceName & _
            vbCrLf & "Document name: " & objFaxOutgoingMessage.DocumentName & _
            vbCrLf & "Message ID: " & objFaxOutgoingMessage.ID & _
            vbCrLf & "Original scheduled time: " & objFaxOutgoingMessage.OriginalScheduledTime & _
            vbCrLf & "Pages: " & objFaxOutgoingMessage.Pages & _
            vbCrLf & "Priority: " & objFaxOutgoingMessage.Priority & _
            vbCrLf & "Recipient fax number: " & objFaxOutgoingMessage.Recipient.FaxNumber & _
            vbCrLf & "Retries: " & objFaxOutgoingMessage.Retries & _
            vbCrLf & "Sender name: " & objFaxOutgoingMessage.Sender.Name & _
            vbCrLf & "Size: " & objFaxOutgoingMessage.Size & _
            vbCrLf & "Subject: " & objFaxOutgoingMessage.Subject & _
            vbCrLf & "Submission ID: " & objFaxOutgoingMessage.SubmissionId & _
            vbCrLf & "Submission time: " & objFaxOutgoingMessage.SubmissionTime & _
            vbCrLf & "Transmission end time: " & objFaxOutgoingMessage.TransmissionEnd & _
            vbCrLf & "Transmission start time: " & objFaxOutgoingMessage.TransmissionStart & _
            vbCrLf & "TSID: " & objFaxOutgoingMessage.TSID)

            'Option to delete the fax
            Dim DelAnswer As String
            DelAnswer = InputBox("Delete this fax from the archive (Y/N)?")
            If DelAnswer <> "Y" Then objFaxOutgoingMessage.Delete()

            'Set the iterator cursor to the next message
            objFaxOutgoingMessageIterator.MoveNext()


        Next
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



