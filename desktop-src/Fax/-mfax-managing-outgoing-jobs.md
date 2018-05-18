---
Description: 'The following Microsoft Visual Basic code example shows how to manage jobs in the outgoing queue.'
ms.assetid: '5fab26c3-99f6-4740-9899-3dccbd26a3ba'
title: Managing Outgoing Jobs
---

# Managing Outgoing Jobs

The following Microsoft Visual Basic code example shows how to manage jobs in the outgoing queue. Note that transmission start and end times can only be retrieved for faxes that have started or completed transmission. Individual faxes that have completed transmission will move from the outgoing queue to the outgoing archive, so you will not be able to retrieve that information through the [**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md) object. However, completed faxes that are part of a broadcast that has not completed transmission remain in the queue, and will have useful values in the [**TransmissionStart**](-mfax-faxoutgoingjob-transmissionstart-vb.md) and [**TransmissionEnd**](-mfax-faxoutgoingjob-transmissionend-vb.md) properties.

> [!Note]  
> You should check the type of file the user wants to open. Do not allow a user to open a file unless you know its source and are certain that its contents are safe.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxOutgoingQueue As FAXCOMEXLib.FaxOutgoingQueue
        Dim objFaxOutgoingJob As FAXCOMEXLib.FaxOutgoingJob

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the outgoing queue object
        objFaxOutgoingQueue = objFaxServer.Folders.OutgoingQueue

        'Refresh the queue object
        objFaxOutgoingQueue.Refresh()

        MsgBox("There are  " & objFaxOutgoingQueue.GetJobs.Count & " faxes in the outgoing queue")

        Dim n As Integer
        n = InputBox("Which fax should be displayed (item number)?")

        Dim FileName As String
        FileName = InputBox("Provide path and name of file for TIFF copy, e.g. c:\MyFax.tiff")

        'Get the job based on the item number
        objFaxOutgoingJob = objFaxOutgoingQueue.GetJobs.Item(n)

        'Or, if you request the job name from the user, you could use the following:
        'Set objFaxOutgoingJob = objFaxOutgoingQueue.GetJob("My Fax Job")

        'Copy the job to a tiff file for display
        objFaxOutgoingJob.CopyTiff(FileName)


        'Display information about the job. See the SDK documentation for the meaning
        'of numeric values
        MsgBox("Available operations: " & objFaxOutgoingJob.AvailableOperations & _
        vbCrLf & "CSID: " & objFaxOutgoingJob.CSID & _
        vbCrLf & "Current page: " & objFaxOutgoingJob.CurrentPage & _
        vbCrLf & "Device ID: " & objFaxOutgoingJob.DeviceId & _
        vbCrLf & "Document name: " & objFaxOutgoingJob.DocumentName & _
        vbCrLf & "Extended status: " & objFaxOutgoingJob.ExtendedStatus & _
        vbCrLf & "Extended status code: " & objFaxOutgoingJob.ExtendedStatusCode & _
        vbCrLf & "Broadcast receipts grouped?: " & objFaxOutgoingJob.GroupBroadcastReceipts & _
        vbCrLf & "Job ID: " & objFaxOutgoingJob.Id & _
        vbCrLf & "Original scheduled time: " & objFaxOutgoingJob.OriginalScheduledTime & _
        vbCrLf & "Pages: " & objFaxOutgoingJob.Pages & _
        vbCrLf & "Priority: " & objFaxOutgoingJob.Priority & _
        vbCrLf & "Receipt type: " & objFaxOutgoingJob.ReceiptType)

        'Open the tiff file
        Dim A As Object
        A = CreateObject("wscript.shell")
        A.run(FileName)

        'Job options
        Dim Answer As String
        Answer = InputBox("Do you want to cancel(C), Pause(P), Restart (R) or Resume (E) job " & objFaxOutgoingJob.ID & "? (n for none)")
        If Answer = "C" Then objFaxOutgoingJob.Cancel()
        If Answer = "P" Then objFaxOutgoingJob.Pause()
        If Answer = "R" Then objFaxOutgoingJob.Restart()
        If Answer = "E" Then objFaxOutgoingJob.Resume()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



