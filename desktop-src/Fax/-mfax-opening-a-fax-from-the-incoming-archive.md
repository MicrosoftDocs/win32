---
Description: The following Microsoft Visual Basic code example demonstrates how to retrieve a fax from the incoming archive using the incoming fax iterator.
ms.assetid: bdc7cdaa-0e37-4124-a9b3-9f9eabbe329e
title: Opening a Fax from the Incoming Archive
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Opening a Fax from the Incoming Archive

The following Microsoft Visual Basic code example demonstrates how to retrieve a fax from the incoming archive using the incoming fax iterator.

> [!Note]  
> You should check the type of file the user wants to open. Do not allow a user to open a file unless you know its source and are certain that its contents are safe.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxIncomingMessageIterator As FAXCOMEXLib.FaxIncomingMessageIterator
        Dim objFaxIncomingMessage As FAXCOMEXLib.FaxIncomingMessage
        Dim Prefetch As String
        Dim Answer As String
        Dim FileName As String

        Dim i As Integer

        Dim A As Object

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the iterator and Set the prefetch buffer size
        Prefetch = InputBox("How many messages should be prefetched?")

        'Refresh the archive
        objFaxServer.Folders.IncomingArchive.Refresh()

        objFaxIncomingMessageIterator = objFaxServer.Folders.IncomingArchive.GetMessages(Prefetch)

        'Set the iterator cursor to the first message in the buffer
        objFaxIncomingMessageIterator.MoveFirst()

        For i = 1 To Prefetch
            If i > 1 Then
                Answer = InputBox("View next message (Y/N)?")
                If Answer <> "Y" Then
                    Exit Sub
                End If
            End If

            'Get the message.
            objFaxIncomingMessage = objFaxIncomingMessageIterator.Message

            'Check for end of file.
            If objFaxIncomingMessageIterator.AtEOF = True Then
                MsgBox("End of File Reached")
                Exit Sub
            End If

            FileName = InputBox("Provide path and name of file for TIFF copy, e.g. c:\MyFax.tiff")
            objFaxIncomingMessage.CopyTiff(FileName)

            'Open the tiff file  
            A = CreateObject("wscript.shell")
            A.run(FileName)

            'Set the iterator cursor to the next message
            objFaxIncomingMessageIterator.MoveNext()

        Next
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



