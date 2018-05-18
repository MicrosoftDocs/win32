---
Description: 'The code for broadcasting a fax is similar to the code for sending a fax.'
ms.assetid: '82a9e599-35d3-4fca-954f-dbc579c023f5'
title: Broadcasting a Fax
---

# Broadcasting a Fax

The code for broadcasting a fax is similar to the code for [sending a fax](-mfax-sending-a-fax.md). This code example uses the [**Submit**](-mfax-faxdocument-submit-vb.md) rather than the [**ConnectedSubmit**](-mfax-faxdocument-connectedsubmit.md) method, and therefore does not create a [**FaxServer**](-mfax-faxserver.md) object. The [**FaxDocument**](-mfax-faxdocument.md) object serves as the root object. Also, the code differs in the number of recipients and the number of job IDs returned.


```VB
    Private Sub Form_Load()
        Dim objFaxDocument As New FAXCOMEXLib.FaxDocument
        Dim collFaxRecipients As FAXCOMEXLib.FaxRecipients
        Dim JobId As Object

        'Error handling
        On Error GoTo Error_Handler

        'Set the fax body
        objFaxDocument.Body = "c:\Docs\Body.txt"

        'Name the document
        objFaxDocument.DocumentName = "My First Fax"

        'Get the recipients collection
        collFaxRecipients = objFaxDocument.Recipients

        'Add the recipients
        With collFaxRecipients
            .Add("12225550105", "H")
            .Add("12225550104", "N")
            .Add("12225550103", "G")
        End With

        'Display number of recipients
        MsgBox("Number of recipients: " & collFaxRecipients.Count)

        'Display recipient information
        Dim i As Long
        For i = 1 To collFaxRecipients.Count
            MsgBox("Recipient number " & i & ": " & _
            collFaxRecipients.Item(i).Name & ", " & _
            collFaxRecipients.Item(i).FaxNumber)
        Next

        'Load the default sender
        objFaxDocument.Sender.LoadDefaultSender()

        'Group the broadcast receipts
        objFaxDocument.GroupBroadcastReceipts = True

        'Connect to the fax server, submit the document, and get back the
        'job ID array. "" indicates the local server.
        JobId = objFaxDocument.Submit("")

        'UBound finds the size of the array
        For n = 0 To UBound(JobId)
            MsgBox("The Job ID is " & JobId(n))
        Next

        'Remove the recipients from the collection. If you do not take this step, 
        'and run this code again without closing the program, the recipients 
        'collection will retain the recipients and keep adding more recipients.
        'The count and item numbering will change as you remove the items, so 
        'just remove item (1) Count times
        Dim lCount As Long
        lCount = collFaxRecipients.Count
        For i = 1 To lCount
            collFaxRecipients.Remove(1)
        Next
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



