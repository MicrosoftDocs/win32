---
Description: 'The following Microsoft Visual Basic code example demonstrates how to obtain information about faxes that are in the incoming queue, how to view a fax, and how to cancel a fax.'
ms.assetid: '88cde2d4-09ee-4fbf-8a75-35de58dd45f5'
title: Managing the Incoming Queue
---

# Managing the Incoming Queue

The following Microsoft Visual Basic code example demonstrates how to obtain information about faxes that are in the incoming queue, how to view a fax, and how to cancel a fax.

> [!Note]  
> You should check the type of file the user wants to open. Do not allow a user to open a file unless you know its source and are certain that its contents are safe.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim collFaxIncomingJobs As FAXCOMEXLib.FaxIncomingJobs
        Dim objFaxIncomingJob As FAXCOMEXLib.FaxIncomingJob

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the collection of jobs in the incoming queue
        collFaxIncomingJobs = objFaxServer.Folders.IncomingQueue.GetJobs

        'Display the number of jobs in the collection
        MsgBox("There are " & collFaxIncomingJobs.Count & " jobs in the incoming queue.")

        Dim n As Long

        'Get the job
        n = InputBox("Input the item number for which you want information.")
        objFaxIncomingJob = collFaxIncomingJobs.Item(n)

        'Refresh the job object (job is in process of being received, you
        'want current information)
        objFaxIncomingJob.Refresh()

        'Display the job properties
        MsgBox("Available operations: " & objFaxIncomingJob.AvailableOperations & _
        vbCrLf & "Caller ID: " & objFaxIncomingJob.CallerId & _
        vbCrLf & "CSID: " & objFaxIncomingJob.CSID & _
        vbCrLf & "Current page: " & objFaxIncomingJob.CurrentPage & _
        vbCrLf & "Device ID: " & objFaxIncomingJob.DeviceId & _
        vbCrLf & "Extended status: " & objFaxIncomingJob.ExtendedStatus & _
        vbCrLf & "Extended status code : " & objFaxIncomingJob.ExtendedStatusCode & _
        vbCrLf & "Job ID: " & objFaxIncomingJob.Id & _
        vbCrLf & "Job type: " & objFaxIncomingJob.JobType & _
        vbCrLf & "Retries: " & objFaxIncomingJob.Retries & _
        vbCrLf & "Routing information: " & objFaxIncomingJob.RoutingInformation & _
        vbCrLf & "Size: " & objFaxIncomingJob.Size & _
        vbCrLf & "Status: " & objFaxIncomingJob.Status & _
        vbCrLf & "Transmission start: " & objFaxIncomingJob.TransmissionStart & _
        vbCrLf & "Transmission end: " & objFaxIncomingJob.TransmissionEnd & _
        vbCrLf & "TSID: " & objFaxIncomingJob.TSID)

        'Allow user to cancel the selected fax
        Dim CancelString As String
        CancelString = InputBox("Cancel this fax (Y/N)?")
        If CancelString = "Y" Then objFaxIncomingJob.Cancel()

        'Allow user to open the selected fax
        Dim OpenString As String
        OpenString = InputBox("Open this fax (Y/N)?")
        If OpenString = "Y" Then
            Dim FileName As String
            FileName = InputBox("Provide path and name of file for TIFF copy, e.g. c:\MyFax.tiff")
            objFaxIncomingJob.CopyTiff(FileName)

            'Open the tiff file
            Dim A As Object
            A = CreateObject("wscript.shell")
            A.run(FileName)
        End If
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



