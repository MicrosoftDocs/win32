---
Description: 'Note  For Windows Vista, refer to the example in Managing Queues and Archives.  This Microsoft Visual Basic code example sets several outgoing queue properties.'
ms.assetid: '64866029-686e-451b-b7b5-33b5235ad307'
title: Setting the Outgoing Queue Properties
---

# Setting the Outgoing Queue Properties

> [!Note]  
> For Windows Vista, refer to the example in [Managing Queues and Archives](-mfax-managing-queues-and-archives.md).

 

This Microsoft Visual Basic code example sets several outgoing queue properties. The comment lines indicate which property is being set. The Microsoft Visual Basic Scripting Edition (VBScript) equivalent follows the Visual Basic code.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxOutgoingQueue As FAXCOMEXLib.FaxOutgoingQueue

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server.
        objFaxServer.Connect("")

        'Create the outgoing queue object
        objFaxOutgoingQueue = objFaxServer.Folders.OutgoingQueue

        'Set the outgoing queue properties
        'Set the age limit to 2 days
        objFaxOutgoingQueue.AgeLimit = 2
        'Allow personal cover pages
        objFaxOutgoingQueue.AllowPersonalCoverPages = True
        'Ensure that the queue is not blocked or paused
        objFaxOutgoingQueue.Blocked = False
        objFaxOutgoingQueue.Paused = False
        'Enable Branding
        objFaxOutgoingQueue.Branding = True
        'Set the discount rate start and end times
        objFaxOutgoingQueue.DiscountRateStart = Date.FromOADate(15.0)
        objFaxOutgoingQueue.DiscountRateEnd = Date.FromOADate(15.25)
        'Set the number of retries
        objFaxOutgoingQueue.Retries = 6
        'Set the retry delay to 10 minutes
        objFaxOutgoingQueue.RetryDelay = 10
        'Use the device TSID
        objFaxOutgoingQueue.UseDeviceTSID = True

        'Save the outgoing queue changes
        objFaxOutgoingQueue.Save()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



## VBScript

The VBScript equivalent is shown here. Creation of the root object is highlighted, as the code differs from that used in Visual Basic. Note that the error handling has been modified from that used in the Visual Basic code.


```VB
        Sub OutQueue()
        Dim objFaxServer As FAXCOMEXLib.FaxServer
        Dim objFaxOutgoingQueue As FAXCOMEXLib.FaxOutgoingQueue

        'Create the root object
        objFaxServer = CreateObject("FaxComEx.FaxServer")

        'Error handling
        On Error Resume Next

        'Connect to the fax server
        objFaxServer.Connect ("")

        If Err.Number <> 0 Then
            MsgBox ("Error number: " & Err.Number & ", " & Err.Description)
            Exit Sub
        End If

        'Create the outgoing queue object
        objFaxOutgoingQueue = objFaxServer.Folders.OutgoingQueue

        If Err.Number <> 0 Then
            MsgBox ("Error number: " & Err.Number & ", " & Err.Description)
            Exit Sub
        End If

        'Set the outgoing queue properties
        'Set the age limit to 2 days
        objFaxOutgoingQueue.AgeLimit = 2
        'Allow personal cover pages
        objFaxOutgoingQueue.AllowPersonalCoverPages = True
        'Ensure that the queue is not blocked or paused
        objFaxOutgoingQueue.Blocked = False
        objFaxOutgoingQueue.Paused = False
        'Enable Branding
        objFaxOutgoingQueue.Branding = True
        'Set the discount rate start and end times
        objFaxOutgoingQueue.DiscountRateStart = 15#
        objFaxOutgoingQueue.DiscountRateEnd = 15.25
        'Set the number of retries
        objFaxOutgoingQueue.Retries = 6
        'Set the retry delay to 10 minutes
        objFaxOutgoingQueue.RetryDelay = 10
        'Use the device TSID
        objFaxOutgoingQueue.UseDeviceTSID = True

        'Save the outgoing queue changes
        objFaxOutgoingQueue.Save
        
        If Err.Number <> 0 Then
            MsgBox ("Error number: " & Err.Number & ", " & Err.Description)
            Exit Sub
        End If

    End Sub 'OutQueue
```



 

 



