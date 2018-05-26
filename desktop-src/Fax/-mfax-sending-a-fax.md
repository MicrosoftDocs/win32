---
Description: The following Microsoft Visual Basic code example sends a fax.
ms.assetid: 347943cc-a417-469e-a936-8da5601e752f
title: Sending a Fax
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sending a Fax

The following Microsoft Visual Basic code example sends a fax. Note that if you were to convert this Visual Basic example to Microsoft Visual Basic Scripting Edition (VBScript), you would have to use an enumeration constant instead of the value fptHigh. For more information, see [Using Enumerations in Scripts](-mfax-using-enumerations-in-scripts.md).


```VB
    Private Sub Form_Load()
        Dim objFaxDocument As New FAXCOMEXLib.FaxDocument
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objSender As FAXCOMEXLib.FaxSender
        Dim JobID As Object

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Set the fax body
        objFaxDocument.Body = "c:\Docs\Body.txt"

        'Name the document
        objFaxDocument.DocumentName = "My First Fax"

        'Set the fax priority
        objFaxDocument.Priority = FAXCOMEXLib.FAX_PRIORITY_TYPE_ENUM.fptHIGH


        'Add the recipient with the fax number 12225550100
        objFaxDocument.Recipients.Add("12225550100", "Bud")

        'Choose to attach the fax to the fax receipt
        objFaxDocument.AttachFaxToReceipt = True

        'Set the cover page type and the path to the cover page
        objFaxDocument.CoverPageType = FAXCOMEXLib.FAX_COVERPAGE_TYPE_ENUM.fcptSERVER
        objFaxDocument.CoverPage = "generic"

        'Provide the cover page note
        objFaxDocument.Note = "Here is the info you requested"

        'Provide the address for the fax receipt
        objFaxDocument.ReceiptAddress = "someone@example.com"

        'Set the receipt type to email
        objFaxDocument.ReceiptType = FAXCOMEXLib.FAX_RECEIPT_TYPE_ENUM.frtMAIL

        'Specify that the fax is to be sent at a particular time
        objFaxDocument.ScheduleType = FAXCOMEXLib.FAX_SCHEDULE_TYPE_ENUM.fstSPECIFIC_TIME
        'CDate converts the time to the Date data type
        objFaxDocument.ScheduleTime = CDate("4:35:47 PM")

        objFaxDocument.Subject = "Today's fax"

        'Set the sender properties.
        objFaxDocument.Sender.Title = "Mr."
        objFaxDocument.Sender.Name = "Bob"
        objFaxDocument.Sender.City = "Cleveland Heights"
        objFaxDocument.Sender.State = "Ohio"
        objFaxDocument.Sender.Company = "Microsoft"
        objFaxDocument.Sender.Country = "USA"
        objFaxDocument.Sender.Email = "someone@microsoft.com"
        objFaxDocument.Sender.FaxNumber = "12165555554"
        objFaxDocument.Sender.HomePhone = "12165555555"
        objFaxDocument.Sender.OfficeLocation = "Downtown"
        objFaxDocument.Sender.OfficePhone = "12165555553"
        objFaxDocument.Sender.StreetAddress = "123 Main Street"
        objFaxDocument.Sender.TSID = "Office fax machine"
        objFaxDocument.Sender.ZipCode = "44118"
        objFaxDocument.Sender.BillingCode = "23A54"
        objFaxDocument.Sender.Department = "Accts Payable"

        'Save sender information as default
        objFaxDocument.Sender.SaveDefaultSender()

        'Submit the document to the connected fax server
        'and get back the job ID.

        JobID = objFaxDocument.ConnectedSubmit(objFaxServer)

        MsgBox("The Job ID is :" & JobID(0))

        objFaxServer.Disconnect()

        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



## Remarks

> [!Note]  
> On Windows Vista, the program must have write access to the archive folder or it will generate an exception.

 

 

 



