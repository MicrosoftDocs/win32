---
Description: The FaxIncomingJob object is used by a fax client application to retrieve information about an incoming fax job in a fax servers queue.
ms.assetid: ef93899d-e797-4f07-bede-0860b695b32b
title: FaxIncomingJob object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob object

The **FaxIncomingJob** object is used by a fax client application to retrieve information about an incoming fax job in a fax server's queue. The object also includes methods to cancel an incoming fax job and to copy the Tagged Image File Format Class F (TIFF Class F) file associated with an inbound fax job, to a file on the local computer.

A **FaxIncomingJob** object is accessed through a [**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object.

![faxincomingqueue, faxincomingjobs, and faxincomingjob objects](images/faxincomingjob.png)

## Members

The **FaxIncomingJob** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxIncomingJob** object has these methods.



| Method                                               | Description                                                                                                                                                                  |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](-mfax-faxincomingjob-cancel-vb.md)     | The [**Cancel**](-mfax-faxincomingjob-cancel-vb.md) method cancels the incoming fax job.<br/>                                                                         |
| [**CopyTiff**](-mfax-faxincomingjob-copytiff-vb.md) | The [**CopyTiff**](-mfax-faxincomingjob-copytiff-vb.md) method copies the TIFF Class F file associated with the inbound fax job to a file on the local computer.<br/> |
| [**Refresh**](-mfax-faxincomingjob-refresh-vb.md)   | The [**Refresh**](-mfax-faxincomingjob-refresh-vb.md) method refreshes **FaxIncomingJob** object information from the fax server.<br/>                                |



 

### Properties

The **FaxIncomingJob** object has these properties.



| Property                                                                            | Access type          | Description                                                                                                                                                                                                          |
|:------------------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AvailableOperations**](-mfax-faxincomingjob-availableoperations.md)<br/>  | Read-only<br/> | The [**AvailableOperations**](-mfax-faxincomingjob-availableoperations.md) property indicates the combination of valid operations that you can perform on the fax job, given its current status.<br/>         |
| [**CallerId**](-mfax-faxincomingjob-callerid-vb.md)<br/>                     | Read-only<br/> | The [**CallerId**](-mfax-faxincomingjob-callerid-vb.md) property is a string that identifies the calling device that sent the inbound fax job.<br/>                                                           |
| [**CSID**](-mfax-faxincomingjob-csid-vb.md)<br/>                             | Read-only<br/> | The [**CSID**](-mfax-faxincomingjob-csid-vb.md) property is a null-terminated string that contains the CSID for the job.<br/>                                                                                 |
| [**CurrentPage**](-mfax-faxincomingjob-currentpage-vb.md)<br/>               | Read-only<br/> | The [**CurrentPage**](-mfax-faxincomingjob-currentpage-vb.md) property is a number that identifies the page that the fax service is actively receiving on an inbound fax job.<br/>                            |
| [**DeviceId**](-mfax-faxincomingjob-deviceid-vb.md)<br/>                     | Read-only<br/> | The [**DeviceId**](-mfax-faxincomingjob-deviceid-vb.md) property indicates the device ID of the device receiving the inbound fax job.<br/>                                                                    |
| [**ExtendedStatus**](-mfax-faxincomingjob-extendedstatus-vb.md)<br/>         | Read-only<br/> | The [**ExtendedStatus**](-mfax-faxincomingjob-extendedstatus-vb.md) property is a null-terminated string that describes the job's extended status.<br/>                                                       |
| [**ExtendedStatusCode**](-mfax-faxincomingjob-extendedstatuscode.md)<br/>    | Read-only<br/> | The [**ExtendedStatusCode**](-mfax-faxincomingjob-extendedstatuscode.md) property specifies a code describing the job's extended status.<br/>                                                                 |
| [**Id**](-mfax-faxincomingjob-id-vb.md)<br/>                                 | Read-only<br/> | The [**Id**](-mfax-faxincomingjob-id-vb.md) property is a null-terminated string that contains a unique ID for the inbound fax job.<br/>                                                                      |
| [**JobType**](-mfax-faxincomingjob-jobtype.md)<br/>                          | Read-only<br/> | The [**JobType**](-mfax-faxincomingjob-jobtype.md) property describes the type of fax job; for example, the job can be a receive job, a send job, or a routing job.<br/>                                      |
| [**Retries**](-mfax-faxincomingjob-retries-vb.md)<br/>                       | Read-only<br/> | The [**Retries**](-mfax-faxincomingjob-retries-vb.md) property is a value that indicates the number of times the fax service attempted to route an incoming fax when the initial routing attempt failed.<br/> |
| [**RoutingInformation**](-mfax-faxincomingjob-routinginformation-vb.md)<br/> | Read-only<br/> | The [**RoutingInformation**](-mfax-faxincomingjob-routinginformation-vb.md) property is a null-terminated string that specifies routing information for the inbound fax job.<br/>                             |
| [**Size**](-mfax-faxincomingjob-size-vb.md)<br/>                             | Read-only<br/> | The [**Size**](-mfax-faxincomingjob-size-vb.md) property is a value that indicates the size of the TIFF Class F file associated with the inbound fax job.<br/>                                                |
| [**Status**](-mfax-faxincomingjob-status.md)<br/>                            | Read-only<br/> | The [**Status**](-mfax-faxincomingjob-status.md) property is a number that indicates the current status of an inbound fax job in the job queue. <br/>                                                         |
| [**TransmissionEnd**](-mfax-faxincomingjob-transmissionend-vb.md)<br/>       | Read-only<br/> | The [**TransmissionEnd**](-mfax-faxincomingjob-transmissionend-vb.md) property indicates the time at which the inbound fax job completed transmission.<br/>                                                   |
| [**TransmissionStart**](-mfax-faxincomingjob-transmissionstart-vb.md)<br/>   | Read-only<br/> | The [**TransmissionStart**](-mfax-faxincomingjob-transmissionstart-vb.md) property indicates the time that the fax inbound job began transmitting.<br/>                                                       |
| [**TSID**](-mfax-faxincomingjob-tsid-vb.md)<br/>                             | Read-only<br/> | The [**TSID**](-mfax-faxincomingjob-tsid-vb.md) property is a null-terminated string that contains the TSID associated with the fax inbound job.<br/>                                                         |



 

## Remarks

To create a **FaxIncomingJob** object in Microsoft Visual Basic, call the [**Item**](-mfax-faxincomingjobs-item.md) property of the [**FaxIncomingJobs**](-mfax-faxincomingjobs.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxIncomingJob<br/>                                                        |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**FaxIncomingJobs**](-mfax-faxincomingjobs.md)
</dt> <dt>

[**IFaxIncomingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingjob?branch=master)
</dt> </dl>

 

 




