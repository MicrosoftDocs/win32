---
Description: The FaxServer object is used by a fax client Microsoft Visual Basic application to manage a connection to the fax service.
ms.assetid: 8991a9b4-b4bc-4c7c-92ec-c1e7ecb6c33a
title: FaxServer object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxServer object

The [**FaxServer**](-mfax-faxstatus-object-visual-basic-.md) object is used by a fax client Microsoft Visual Basic application to manage a connection to the fax service. You can also retrieve and set the properties of **FaxServer** objects, such as settings for retransmission, branding, archiving and cover pages; discount rate periods; and the status of the fax server queue.

The [**FaxServer**](-mfax-faxstatus-object-visual-basic-.md) object has the following methods and properties:

-   Methods to initiate and terminate connections with a fax server.
-   Methods to create [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md), [**FaxPorts**](-mfax-faxports-object-visual-basic-.md), and [**FaxDoc objects**](-mfax-faxdoc-object-visual-basic-.md).
-   Properties to set and retrieve individual attributes of [**FaxServer**](-mfax-faxstatus-object-visual-basic-.md) objects.

Use the **FaxServer** object to connect to and disconnect from an active fax server. After you obtain a connection, you can call the following methods to create other objects you need.

-   The [**GetJobs**](-mfax-ifaxserver-getjobs-vb.md) method to create a [**FaxJobs object**](-mfax-faxjobs-object-visual-basic-.md). Use this object to create [**FaxJob objects**](-mfax-faxjob-object-visual-basic-.md) and enumerate the fax jobs associated with a connected fax server.
-   The [**GetPorts**](-mfax-ifaxserver-getports-vb.md) method to create a [**FaxPorts object**](-mfax-faxports-object-visual-basic-.md). Use this object to create [**FaxPort objects**](-mfax-faxport-object-visual-basic-.md) and enumerate fax port configuration information for a connection to a fax server.
-   The [**CreateDocument**](-mfax-ifaxserver-createdocument-vb.md) method to create a [**FaxDoc object**](-mfax-faxdoc-object-visual-basic-.md). Use this object to transmit a fax and to retrieve and set the properties of **FaxDoc** objects.

> [!Note]  
> A fax client application must call the [**Connect**](-mfax-ifaxserver-connect-client-vb.md) method to initiate a connection with an active fax server before accessing most other objects that begin with **Fax**. (A fax server connection is not required to access a [**FaxTiff object**](-mfax-faxtiff-object-visual-basic-.md).)

 

To create a **FaxServer** object, call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function as illustrated in the following sample:


```
Dim FaxServer as Object
Set FaxServer = CreateObject("FaxServer.FaxServer")
```



## Members

The **FaxServer** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxServer** object has these methods.



| Method                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Connect**](-mfax-ifaxserver-connect-client-vb.md)        | The [**Connect**](-mfax-ifaxserver-connect-client-vb.md) method connects a fax client application to the specified fax server. Before accessing most interfaces that begin with **IFax**, the application must call this method to initiate a connection with an active fax server. A fax server connection is not required to access an [**IFaxTiff**](-mfax-ifaxtiff.md) interface.<br/> |
| [**CreateDocument**](-mfax-ifaxserver-createdocument-vb.md) | The [**CreateDocument**](-mfax-ifaxserver-createdocument-vb.md) method creates a [FaxDoc](-mfax-faxdoc.md) object for a specified [FaxServer](-mfax-faxserver-client.md) object. The FaxDoc object allows a user to create and transmit a document to one or more fax recipients.<br/>                                                                                                    |
| [**Disconnect**](-mfax-ifaxserver-disconnect-client-vb.md)  | The [**Disconnect**](-mfax-ifaxserver-disconnect-client-vb.md) method terminates a fax client application's connection to a fax server.<br/>                                                                                                                                                                                                                                                |
| [**GetJobs**](-mfax-ifaxserver-getjobs-vb.md)               | The [**GetJobs**](-mfax-ifaxserver-getjobs-vb.md) method creates and initializes a [**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md) object for a specified [FaxServer](-mfax-faxserver-client.md) object. The [FaxJobs](-mfax-faxjobs.md) object allows enumeration of the current queued jobs for the connected fax server.<br/>                                                    |
| [**GetPorts**](-mfax-ifaxserver-getports-vb.md)             | The [**GetPorts**](-mfax-ifaxserver-getports-vb.md) method creates and initializes a [FaxPorts](-mfax-faxports.md) object for a specified [FaxServer](-mfax-faxserver-client.md) object. The FaxPorts object allows enumeration of fax port configuration information for the connected fax server.<br/>                                                                                  |



 

### Properties

The **FaxServer** object has these properties.



| Property                                                                                      | Access type           | Description                                                                                                                                                                                                                                                                                                                                                    |
|:----------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ArchiveDirectory**](-mfax-ifaxserver-get-archivedirectory-vb.md)<br/>               | Read/write<br/> | The [**ArchiveDirectory**](-mfax-ifaxserver-get-archivedirectory-vb.md) method retrieves the **ArchiveDirectory** property for a [FaxServer](-mfax-faxserver-client.md) object. The **ArchiveDirectory** property is a null-terminated string that contains the location in which the fax server stores archived outbound faxes.<br/>                  |
| [**ArchiveOutboundFaxes**](-mfax-ifaxserver-get-archiveoutboundfaxes-vb.md)<br/>       | Read/write<br/> | Sets or retrieves the [**ArchiveOutboundFaxes**](-mfax-ifaxserver-get-archiveoutboundfaxes-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **ArchiveOutboundFaxes** property is a Boolean value that indicates whether the fax server archives outgoing fax transmissions. <br/>                                              |
| [**Branding**](-mfax-ifaxserver-get-branding-vb.md)<br/>                               | Read/write<br/> | Sets or retrieves the [**Branding**](-mfax-ifaxserver-get-branding-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **Branding** property is a Boolean value that indicates whether the fax server generates branding information at the top of fax transmissions.<br/>                                                        |
| [**DirtyDays**](-mfax-ifaxserver-get-dirtydays-vb.md)<br/>                             | Read/write<br/> | Sets or retrieves the [**DirtyDays**](-mfax-ifaxserver-get-dirtydays-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **DirtyDays** property is the number of days the fax server retains an unsent job in the fax job queue.<br/>                                                                                             |
| [**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md)<br/>         | Read/write<br/> | Sets or retrieves the [**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **DiscountRateEndHour** property is a number that represents the hour the discount period ends. The discount period applies only to outgoing fax transmissions.<br/>                 |
| [**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md)<br/>     | Read/write<br/> | Sets or retrieves the [**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **DiscountRateEndMinute** property is a number that represents the minute the discount period ends. The discount period applies only to outgoing fax transmissions.<br/>         |
| [**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md)<br/>     | Read/write<br/> | Sets or retrieves the [**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **DiscountRateStartHour** property is a number that represents the hour the discount period begins. The discount period applies only to outgoing fax transmissions. <br/>        |
| [**DiscountRateStartMinute**](-mfax-ifaxserver-get-discountratestartminute-vb.md)<br/> | Read/write<br/> | Sets or retrieves the [**DiscountRateStartMinute**](-mfax-ifaxserver-get-discountratestartminute-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **DiscountRateStartMinute** property is a number that represents the minute the discount period begins. The discount period applies only to outgoing fax transmissions.<br/> |
| [**PauseServerQueue**](-mfax-ifaxserver-get-pauseserverqueue-vb.md)<br/>               | Read/write<br/> | Sets or retrieves the [**PauseServerQueue**](-mfax-ifaxserver-get-pauseserverqueue-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **PauseServerQueue** property is a Boolean value that indicates whether the fax server has paused the fax job queue.<br/>                                                                  |
| [**Retries**](-mfax-ifaxserver-get-retries-vb.md)<br/>                                 | Read/write<br/> | Sets or retrieves the [**Retries**](-mfax-ifaxserver-get-retries-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **Retries** property is a value that represents the number of times the fax server attempts to retransmit an outgoing fax when the initial transmission fails.<br/>                                          |
| [**RetryDelay**](-mfax-ifaxserver-get-retrydelay-vb.md)<br/>                           | Read/write<br/> | Sets or retrieves the [**RetryDelay**](-mfax-ifaxserver-get-retrydelay-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **RetryDelay** property is a value that represents the time interval, in minutes, the fax server waits before attempting to retransmit an outbound fax job.<br/>                                       |
| [**ServerCoverpage**](-mfax-ifaxserver-get-servercoverpage-vb.md)<br/>                 | Read/write<br/> | Sets or retrieves the [**ServerCoverpage**](-mfax-ifaxserver-get-servercoverpage-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **ServerCoverpage** property is a Boolean value that indicates whether the fax server permits the use of common cover pages only. <br/>                                                      |
| [**ServerMapiProfile**](-mfax-ifaxserver-get-servermapiprofile-vb.md)<br/>             | Read/write<br/> | Sets or retrieves the [**ServerMapiProfile**](-mfax-ifaxserver-get-servermapiprofile-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **ServerMapiProfile** property is a null-terminated string that contains the MAPI user profile that the fax server uses for routing incoming fax transmissions.<br/>                     |
| [**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md)<br/>                     | Read/write<br/> | Sets or retrieves the [**UseDeviceTsid**](-mfax-ifaxserver-get-usedevicetsid-vb.md) property for a [FaxServer](-mfax-faxserver-client.md) object. The **UseDeviceTsid** property is a Boolean value that indicates whether the fax server uses the device's TSID instead of a user-specified TSID.<br/>                                                |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxServer** object's type library information in Visual Basic syntax.

 

 




