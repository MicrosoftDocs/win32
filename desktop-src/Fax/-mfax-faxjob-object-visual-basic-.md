---
Description: The FaxJob object permits a fax client Microsoft Visual Basic application to access the job status for incoming and outgoing fax transmissions, and to pause, resume, cancel or restart a fax job.
ms.assetid: c6e95bae-c1f8-4636-9847-7c66187cfc8d
title: FaxJob object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJob object

The **FaxJob** object permits a fax client Microsoft Visual Basic application to access the job status for incoming and outgoing fax transmissions, and to pause, resume, cancel or restart a fax job. You can also use the object to retrieve information about fax jobs. Information includes, among other items, the fax number to which the fax server will send the transmission, job attributes, and recipient and sender information. There is one **FaxJob** object for each queued job associated with the server.

The **FaxJob** object has the following methods and properties:

-   A method to modify the job queue status of a fax job.
-   A method to refresh **FaxJob** object information.
-   Properties to retrieve individual attributes associated with a **FaxJob** object.

## Members

The **FaxJob** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxJob** object has these methods.



| Method                                          | Description                                                                                                                                         |
|:------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-ifaxjob-refresh-vb.md)     | The [**Refresh**](-mfax-ifaxjob-refresh-vb.md) method updates [FaxJob](-mfax-faxjob.md) object information for the associated fax job.<br/> |
| [**SetStatus**](-mfax-ifaxjob-setstatus-vb.md) | Call the [**SetStatus**](-mfax-ifaxjob-setstatus-vb.md) method to pause, resume, cancel, or restart a specified fax job.<br/>                |



 

### Properties

The **FaxJob** object has these properties.



| Property                                                               | Access type          | Description                                                                                                                                                                                                                                                            |
|:-----------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BillingCode**](-mfax-ifaxjob-get-billingcode-vb.md)<br/>     | Read-only<br/> | The [**BillingCode**](-mfax-ifaxjob-get-billingcode-vb.md) property is a null-terminated string that contains an optional billing code that applies to the fax job.<br/>                                                                                        |
| [**DeviceStatus**](-mfax-ifaxjob-get-devicestatus-vb.md)<br/>   | Read-only<br/> | The [**DeviceStatus**](-mfax-ifaxjob-get-devicestatus-vb.md) property is a null-terminated string that describes the status of the port associated with the fax job.<br/>                                                                                       |
| [**DiscountSend**](-mfax-ifaxjob-get-discountsend-vb.md)<br/>   | Read-only<br/> | The [**DiscountSend**](-mfax-ifaxjob-get-discountsend-vb.md) property is a Boolean value that indicates whether the fax server will transmit the fax job during the discount rate period. The discount period applies only to outgoing fax transmissions. <br/> |
| [**DisplayName**](-mfax-ifaxjob-get-displayname-vb.md)<br/>     | Read-only<br/> | The [**DisplayName**](-mfax-ifaxjob-get-displayname-vb.md) property is a null-terminated string that contains the user-friendly name to associate with the fax job. <br/>                                                                                       |
| [**FaxNumber**](-mfax-ifaxjob-get-faxnumber-vb.md)<br/>         | Read-only<br/> | The [**FaxNumber**](-mfax-ifaxjob-get-faxnumber-vb.md) property is a null-terminated string that contains the fax number to which the fax server will transmit the fax job. The **FaxNumber** property applies only to outgoing fax transmissions.<br/>         |
| [**JobId**](-mfax-ifaxjob-get-jobid-vb.md)<br/>                 | Read-only<br/> | The [**JobId**](-mfax-ifaxjob-get-jobid-vb.md) property is a number that uniquely identifies the specified fax job.<br/>                                                                                                                                        |
| [**PageCount**](-mfax-ifaxjob-get-pagecount-vb.md)<br/>         | Read-only<br/> | The [**PageCount**](-mfax-ifaxjob-get-pagecount-vb.md) property is a number that represents the total number of pages in a fax transmission. The **PageCount** property applies only to outgoing fax transmissions.<br/>                                        |
| [**QueueStatus**](-mfax-ifaxjob-get-queuestatus-vb.md)<br/>     | Read-only<br/> | The [**QueueStatus**](-mfax-ifaxjob-get-queuestatus-vb.md) property is a null-terminated string that describes the job queue status of the fax job.<br/>                                                                                                        |
| [**RecipientName**](-mfax-ifaxjob-get-recipientname-vb.md)<br/> | Read-only<br/> | The [**RecipientName**](-mfax-ifaxjob-get-recipientname-vb.md) property is a null-terminated string that contains the name of the recipient of the fax job.<br/>                                                                                                |
| [**SenderCompany**](-mfax-ifaxjob-get-sendercompany-vb.md)<br/> | Read-only<br/> | The [**SenderCompany**](-mfax-ifaxjob-get-sendercompany-vb.md) property is a null-terminated string that contains the company name for the sender of the fax job. The **SenderCompany** property applies only to outgoing fax transmissions. <br/>              |
| [**SenderDept**](-mfax-ifaxjob-get-senderdept-vb.md)<br/>       | Read-only<br/> | The [**SenderDept**](-mfax-ifaxjob-get-senderdept-vb.md) property is a null-terminated string that contains the department identifier for the sender of the fax job. The **SenderDept** property applies only to outgoing fax transmissions.<br/>               |
| [**SenderName**](-mfax-ifaxjob-get-sendername-vb.md)<br/>       | Read-only<br/> | The [**SenderName**](-mfax-ifaxjob-get-sendername-vb.md) property is a null-terminated string that contains the name of the sender who initiated the fax job. The **SenderName** property applies only to outgoing fax transmissions.<br/>                      |
| [**Tsid**](-mfax-ifaxjob-get-tsid-vb.md)<br/>                   | Read-only<br/> | The [**Tsid**](-mfax-ifaxjob-get-tsid-vb.md) property is a null-terminated string that contains the TSID) associated with the fax job.<br/>                                                                                                                     |
| [**Type**](-mfax-ifaxjob-get-type-vb.md)<br/>                   | Read-only<br/> | The [**Type**](-mfax-ifaxjob-get-type-vb.md) property is a number that describes the type of fax job represented by the object. <br/>                                                                                                                           |
| [**UserName**](-mfax-ifaxjob-get-username-vb.md)<br/>           | Read-only<br/> | The [**UserName**](-mfax-ifaxjob-get-username-vb.md) property is a null-terminated string that contains the name of the user who submitted the fax job to the job queue. The **UserName** property applies only to outgoing fax transmissions. <br/>            |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxJob** object's type library information in Visual Basic syntax.

### To create a FaxJob object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the [**GetJobs**](-mfax-ifaxserver-getjobs-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a [**FaxJobs object**](-mfax-faxjobs-object-visual-basic-.md) on the connected fax server.
3.  Retrieve the [**Count**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxjobs-get_count?branch=master) property and then the [**Item**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxjobs-get_item?branch=master) property for the [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md) collection to create a **FaxJob** object.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




