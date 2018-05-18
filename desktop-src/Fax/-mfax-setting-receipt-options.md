---
Description: 'The following Microsoft Visual Basic code example demonstrates how to set receipt options.'
ms.assetid: '4558e770-c6ae-4892-a2b3-40c59f6275fa'
title: Setting Receipt Options
---

# Setting Receipt Options

The following Microsoft Visual Basic code example demonstrates how to set receipt options.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxReceiptOptions As FAXCOMEXLib.FaxReceiptOptions

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the receipt options object
        objFaxReceiptOptions = objFaxServer.ReceiptOptions
        'Refresh the object
        objFaxReceiptOptions.Refresh()

        'Display the current object properties
        MsgBox("Allowed receipt types: " & objFaxReceiptOptions.AllowedReceipts & _
        vbCrLf & "Authentication type: " & objFaxReceiptOptions.AuthenticationType & _
        vbCrLf & "SMTP port: " & objFaxReceiptOptions.SMTPPort & _
        vbCrLf & "SMTP sender: " & objFaxReceiptOptions.SMTPSender & _
        vbCrLf & "SMTP server: " & objFaxReceiptOptions.SMTPServer & _
        vbCrLf & "Use for inbound routing: " & objFaxReceiptOptions.UseForInboundRouting)

        'Change the receipt options
        'Send a delivery report through SMTP mail
        objFaxReceiptOptions.AllowedReceipts = FAXCOMEXLib.FAX_RECEIPT_TYPE_ENUM.frtMAIL

        'Use basic authentication
        objFaxReceiptOptions.AuthenticationType = FAXCOMEXLib.FAX_SMTP_AUTHENTICATION_TYPE_ENUM.fsatBASIC

        'Set the SMTP port
        objFaxReceiptOptions.SMTPPort = 25

        'Set the SMTP sender
        objFaxReceiptOptions.SMTPSender = "someone@example.com"

        'Set the SMTP server
        objFaxReceiptOptions.SMTPServer = "My SMTP Server"

        'Set to use for inbound routing to email addresses
        objFaxReceiptOptions.UseForInboundRouting = True

        'Save the changes
        objFaxReceiptOptions.Save()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



