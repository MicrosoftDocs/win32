---
Description: 'The following Microsoft Visual Basic code example demonstrates how to register for fax events.'
ms.assetid: '3a9f42fa-383a-4072-92a6-b59f7940ab04'
title: Registering for Fax Events
---

# Registering for Fax Events

The following Microsoft Visual Basic code example demonstrates how to register for fax events. The code registers for notification when the fax server is shut down and when a fax job is added to the outgoing queue. For more information about fax events, see [Registering for Event Notifications](-mfax-registering-for-event-notifications.md).


```VB
    Dim WithEvents g_objFaxServer As FAXCOMEXLib.FaxServer
    Dim pJobStatus As FAXCOMEXLib.FaxJobStatus

    Private Sub Form_Load()

        'Error handling
        On Error GoTo Error_Handler

        'Initialize the FaxServer object
        g_objFaxServer = New FAXCOMEXLib.FaxServer

        'Connect to the local fax server
        g_objFaxServer.Connect("")

        'Now register for the desired events
        g_objFaxServer.ListenToServerEvents( _
            FAXCOMEXLib.FAX_SERVER_EVENTS_TYPE_ENUM.fsetFXSSVC_ENDED + _
            FAXCOMEXLib.FAX_SERVER_EVENTS_TYPE_ENUM.fsetOUT_QUEUE)

        'From now on, if the fax service has stopped, the function 
        'g_objFaxServer_OnServerShutDown() will be called, if a message is 
        'added to the outgoing queue, g_objFaxServer_OnOutgoingJobAdded() will 
        'be called, and if there is a change in the status of an outgoing job, 
        'g_objFaxServer_OnOutgoingJobChanged() will be called
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)
    End Sub

    Private Sub g_objFaxServer_OnOutgoingJobAdded(ByVal pFaxServer As FAXCOMEXLib.IFaxServer, _
            ByVal bstrJobId As String)

        MsgBox("New job added to queue")

    End Sub

    Private Sub g_objFaxServer_OnOutgoingJobChanged(ByVal pFaxServer As FAXCOMEXLib.IFaxServer, _
            ByVal bstrJobId As String, ByVal pJobStatus As FAXCOMEXLib.IFaxJobStatus)
        'This event receives the FaxJobStatus object

        'Since this event is likely to result in errors, such as trying to 
        'report the transmission end time before the transmission has ended, 
        'this subroutine includes error handling

        'Error handling
        On Error GoTo Error_Handler


        'Display the FaxJobStatus object's properties when the event is called
        MsgBox(pJobStatus.AvailableOperations & _
        vbCrLf & "Caller ID: " & pJobStatus.CallerId & _
        vbCrLf & "CSID: " & pJobStatus.CSID & _
        vbCrLf & "Current page: " & pJobStatus.CurrentPage & _
        vbCrLf & "Device ID: " & pJobStatus.DeviceId & _
        vbCrLf & "Extended status: " & pJobStatus.ExtendedStatus & _
        vbCrLf & "Extended status code: " & pJobStatus.ExtendedStatusCode & _
        vbCrLf & "Job type: " & pJobStatus.JobType & _
        vbCrLf & "Pages: " & pJobStatus.Pages & _
        vbCrLf & "Retries: " & pJobStatus.Retries & _
        vbCrLf & "Routing information: " & pJobStatus.RoutingInformation & _
        vbCrLf & "Scheduled time: " & pJobStatus.ScheduledTime & _
        vbCrLf & "Size: " & pJobStatus.Size & _
        vbCrLf & "Status: " & pJobStatus.Status & _
        vbCrLf & "Transmission start: " & pJobStatus.TransmissionStart & _
        vbCrLf & "TSID: " & pJobStatus.TSID)

        'Display the transmission end time separately, as this will cause an error
        'while the transmission is still in progress
        MsgBox("Transmission end: " & pJobStatus.TransmissionEnd)

        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)
    End Sub

    Private Sub g_objFaxServer_OnServerShutDown(ByVal pFaxServer As FAXCOMEXLib.IFaxServer)

        MsgBox("The local fax server has been shut down")

    End Sub
```



 

 



