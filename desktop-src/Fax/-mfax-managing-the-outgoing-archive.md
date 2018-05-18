---
Description: 'The following Microsoft Visual Basic code example demonstrates how to retrieve information about the outgoing archive and how to open a fax from the archive using the fax ID.'
ms.assetid: '68f6c0f2-ea06-401c-9021-c50940f8cd7a'
title: Managing the Outgoing Archive
---

# Managing the Outgoing Archive

> [!Note]  
> For Windows Vista, refer to the example in [Managing Queues and Archives](-mfax-managing-queues-and-archives.md).

 

The following Microsoft Visual Basic code example demonstrates how to retrieve information about the outgoing archive and how to open a fax from the archive using the fax ID.

> [!Note]  
> You should check the type of file the user wants to open. Do not allow a user to open a file unless you know its source and are certain that its contents are safe.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxOutgoingArchive As FAXCOMEXLib.FaxOutgoingArchive

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the outgoing archive object
        objFaxOutgoingArchive = objFaxServer.Folders.OutgoingArchive

        'Display the outgoing archive properties
        MsgBox("AgeLimit: " & objFaxOutgoingArchive.AgeLimit & _
        vbCrLf & "Archive folder: " & objFaxOutgoingArchive.ArchiveFolder & _
        vbCrLf & "High quota water mark: " & objFaxOutgoingArchive.HighQuotaWaterMark & _
        vbCrLf & "Low quota water mark: " & objFaxOutgoingArchive.LowQuotaWaterMark & _
        vbCrLf & "Size high: " & objFaxOutgoingArchive.SizeHigh & _
        vbCrLf & "Size low: " & objFaxOutgoingArchive.SizeLow & _
        vbCrLf & "Size quota warning: " & objFaxOutgoingArchive.SizeQuotaWarning & _
        vbCrLf & "Is archive used?: " & objFaxOutgoingArchive.UseArchive)

        'Allow user to change age limit
        Dim Answer As String
        Answer = InputBox("Change age limit? (Y/N)")
        If Answer = "Y" Then
            Dim NewAgeLimit As Long
            NewAgeLimit = InputBox("Provide age limit in days")
            objFaxOutgoingArchive.AgeLimit = NewAgeLimit
            objFaxOutgoingArchive.Save()
        End If

        'Allow user to retrieve a message by its ID
        Dim MessageAnswer As String
        MessageAnswer = InputBox("Retrieve a message by its ID for display? (Y/N)")
        If MessageAnswer = "Y" Then
            Dim ID As String
            Dim FileName As String
            ID = InputBox("Provide the message ID")
            FileName = InputBox("Provide path and name of file for TIFF copy, e.g. c:\MyFax.tiff")
            objFaxOutgoingArchive.GetMessage(ID).CopyTiff(FileName)

            'Open the tiff file
            Dim A As Object
            A = CreateObject("wscript.shell")
            A.run(FileName)
        End If
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



The following Visual Basic code example demonstrates how to retrieve information about faxes that have already been sent.


```VB
    Private Sub GetOutgoingArchiveMessages()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim vMessages As FAXCOMEXLib.FaxOutgoingMessageIterator

        objFaxServer.Connect("") ' Add server name ' 
        vMessages = objFaxServer.Folders.OutgoingArchive.GetMessages
        If Not vMessages.AtEOF Then
            With vMessages
                vMessages.MoveFirst()

                Do While Not vMessages.AtEOF

                    ' Here get all the properties of the message ' 
                    ' vMessages.Message.DocumentName 
                    ' vMessages.Message.Id 
                    ' vMessages.Message.TransmissionEnd 
                    ' vMessages.Message.TransmissionEnd 
                    ' vMessages.Message.Delete 

                    vMessages.MoveNext()
                Loop

            End With

        End If

    End Sub
```



 

 



