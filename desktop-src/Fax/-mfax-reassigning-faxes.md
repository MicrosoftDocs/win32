---
Description: 'The following example shows how to reassign a received fax.'
ms.assetid: 'f7dffa99-c8fd-4eb1-94eb-fc8897920bfc'
title: Reassigning Faxes
---

# Reassigning Faxes

The following example shows how to reassign a received fax.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxIncomingMessageIterator As FAXCOMEXLib.FaxIncomingMessageIterator
        Dim objFaxIncomingMessage As FAXCOMEXLib.FaxIncomingMessage
        Dim Prefetch As String
        Dim Answer As String
        Dim UserName As String
        Dim A As Object
        Dim i As Integer

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the iterator and Set the prefetch buffer size
        Prefetch = InputBox("How many messages should be prefetched?")

        'Refresh the archive
        objFaxServer.CurrentAccount.Folders.IncomingArchive.Refresh()

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

            'Reassign the fax
            If objFaxIncomingMessage.WasReassigned = False Then
                MsgBox("Message is not reassigned")
                Answer = InputBox("Do you want to reassign the message (Y/N)?")
                If Answer <> "Y" Then
                    UserName = InputBox("Enter username e.g. DomainName\UserName")
                    objFaxIncomingMessage.Subject = "Reassigning Message"
                    objFaxIncomingMessage.SenderName = "Test User"
                    objFaxIncomingMessage.Recipients = UserName
                    objFaxIncomingMessage.SenderFaxNumber = "1234" 'Some Fax Number
                    'Reassign
                    objFaxIncomingMessage.ReAssign()
                End If
            End If

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



 

 



