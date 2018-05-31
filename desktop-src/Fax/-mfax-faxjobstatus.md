---
Description: The FaxJobStatus object is used for notifications and to hold the dynamic information of the job.
ms.assetid: b4e2dc9e-6a32-4fc7-94fc-2132dedcec9e
title: FaxJobStatus object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxJobStatus object

The **FaxJobStatus** object is used for notifications and to hold the dynamic information of the job. Dynamic information is data that changes as a job progresses. This may include the current job status, the page that is currently being transmitted, and the number of attempts the fax service has made to transmit the job (retries). The fax service uses this object to notify a fax client application of job updates. For more information, see [Fax Job Status](-mfax-fax-job-status.md).

## Members

The **FaxJobStatus** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxJobStatus** object has these properties.



| Property                                                                            | Access type          | Description                                                                                                                                                                                                   |
|:------------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AvailableOperations**](-mfax-faxjobstatus-availableoperations-vb.md)<br/> | Read-only<br/> | The [**AvailableOperations**](-mfax-faxjobstatus-availableoperations-vb.md) property indicates the combination of valid operations that you can perform on the fax job, given its current status.<br/> |
| [**CallerId**](-mfax-faxjobstatus-callerid-vb.md)<br/>                       | Read-only<br/> | The [**CallerId**](-mfax-faxjobstatus-callerid-vb.md) property is a null-terminated string that identifies the calling device associated with the fax job.<br/>                                        |
| [**CSID**](-mfax-faxjobstatus-csid-vb.md)<br/>                               | Read-only<br/> | The [**CSID**](-mfax-faxjobstatus-csid-vb.md) property is a null-terminated string that contains the CSID for the job.<br/>                                                                            |
| [**CurrentPage**](-mfax-faxjobstatus-currentpage-vb.md)<br/>                 | Read-only<br/> | The [**CurrentPage**](-mfax-faxjobstatus-currentpage-vb.md) property is a number that identifies the page that the fax service is actively processing.<br/>                                            |
| [**DeviceId**](-mfax-faxjobstatus-deviceid-vb.md)<br/>                       | Read-only<br/> | The [**DeviceId**](-mfax-faxjobstatus-deviceid-vb.md) property indicates the device ID of the device associated with the fax job.<br/>                                                                 |
| [**ExtendedStatus**](-mfax-faxjobstatus-extendedstatus-vb.md)<br/>           | Read-only<br/> | The [**ExtendedStatus**](-mfax-faxjobstatus-extendedstatus-vb.md) property is a null-terminated string that describes the job's extended status.<br/>                                                  |
| [**ExtendedStatusCode**](-mfax-faxjobstatus-extendedstatuscode-vb.md)<br/>   | Read-only<br/> | The [**ExtendedStatusCode**](-mfax-faxjobstatus-extendedstatuscode-vb.md) property specifies a code describing the job's extended status.<br/>                                                         |
| [**JobType**](-mfax-faxjobstatus-jobtype-vb.md)<br/>                         | Read-only<br/> | The [**JobType**](-mfax-faxjobstatus-jobtype-vb.md) property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.<br/>                              |
| [**Pages**](-mfax-faxjobstatus-pages-vb.md)<br/>                             | Read-only<br/> | The [**Pages**](-mfax-faxjobstatus-pages-vb.md) property is a number that indicates the total number of pages received so far in the fax transmission.<br/>                                            |
| [**Retries**](-mfax-faxjobstatus-retries-vb.md)<br/>                         | Read-only<br/> | The [**Retries**](-mfax-faxjobstatus-retries-vb.md) property is a value that indicates the number of times that the fax service attempted to transmit a fax job when the initial attempt failed.<br/>  |
| [**RoutingInformation**](-mfax-faxjobstatus-routinginformation-vb.md)<br/>   | Read-only<br/> | The [**RoutingInformation**](-mfax-faxjobstatus-routinginformation-vb.md) property is a null-terminated string that specifies the routing information for the fax job.<br/>                            |
| [**ScheduledTime**](-mfax-faxjobstatus-scheduledtime-vb.md)<br/>             | Read-only<br/> | The [**ScheduledTime**](-mfax-faxjobstatus-scheduledtime-vb.md) property indicates the time that the fax job is scheduled for transmission.<br/>                                                       |
| [**Size**](-mfax-faxjobstatus-size-vb.md)<br/>                               | Read-only<br/> | The [**Size**](-mfax-faxjobstatus-size-vb.md) property is a value that indicates the number of bytes of the TIFF Class F file received so far for the fax job.<br/>                                    |
| [**Status**](-mfax-faxjobstatus-status-vb.md)<br/>                           | Read-only<br/> | The [**Status**](-mfax-faxjobstatus-status-vb.md) property is a number that indicates the current status of fax job in the job queue.<br/>                                                             |
| [**TransmissionEnd**](-mfax-faxjobstatus-transmissionend-vb.md)<br/>         | Read-only<br/> | The [**TransmissionEnd**](-mfax-faxjobstatus-transmissionend-vb.md) property indicates the time that the fax job completed transmission.<br/>                                                          |
| [**TransmissionStart**](-mfax-faxjobstatus-transmissionstart-vb.md)<br/>     | Read-only<br/> | The [**TransmissionStart**](-mfax-faxjobstatus-transmissionstart-vb.md) property indicates the time that the fax job began transmitting.<br/>                                                          |
| [**TSID**](-mfax-faxjobstatus-tsid-vb.md)<br/>                               | Read-only<br/> | The [**TSID**](-mfax-faxjobstatus-tsid-vb.md) property is a null-terminated string that contains the TSID associated with the fax job.<br/>                                                            |



 

## Remarks

You do not create the **FaxJobStatus** object. It is received as part of a notification when you implement [**FaxServerNotify.OnIncomingJobChanged**](-mfax-ifaxservernotify-onincomingjobchanged.md) or [**FaxServerNotify.OnOutgoingJobChanged**](-mfax-ifaxservernotify-onoutgoingjobchanged.md), which include a pointer to the **FaxJobStatus** object. When the event occurs and the implemented function is called, you receive this object containing the dynamic information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxJobStatus<br/>                                                          |



## See also

<dl> <dt>

[**IFaxJobStatus**](-mfax-faxjobstatus-cpp.md)
</dt> </dl>

 

 




