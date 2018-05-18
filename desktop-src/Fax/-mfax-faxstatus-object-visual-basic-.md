---
Description: 'The FaxStatus object permits a fax client Visual Basic application to retrieve status information for a specific port on a connected fax server.'
ms.assetid: 'ce382d4d-aeaf-4254-9bc7-74b7d1d7f1a4'
title: FaxStatus object
---

# FaxStatus object

The **FaxStatus** object permits a fax client Visual Basic application to retrieve status information for a specific port on a connected fax server. The **FaxStatus** object has the following method and properties:

-   A method to update status information for a fax port.
-   Properties to retrieve attributes of a **FaxStatus** object, such as whether the parent [**FaxPort**](-mfax-faxport-object-visual-basic-.md) is currently sending or receiving a fax transmission. Attributes also include document and transmission data, sender and recipient names, and routing information.

The **FaxStatus** object should be created only by a [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object.

You can use the **FaxStatus** object to provide real-time status information about a parent **FaxPort** object. Some data is available at all times for an active fax port; other data is relative to sending or receiving a fax and is only available at those times.

## Members

The **FaxStatus** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxStatus** object has these methods.



| Method                                         | Description                                                                                                                                                                                     |
|:-----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Refresh**](-mfax-ifaxstatus-refresh-vb.md) | The [**Refresh**](-mfax-ifaxstatus-refresh-vb.md) method updates [FaxStatus](-mfax-faxstatus.md) object information for the associated parent [FaxPort](-mfax-faxport.md) object.<br/> |



 

### Properties

The **FaxStatus** object has these properties.



| Property                                                                  | Access type          | Description                                                                                                                                                                                                                                                                                                                                                              |
|:--------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Address**](-mfax-ifaxstatus-get-address-vb.md)<br/>             | Read-only<br/> | Retrieves the [**Address**](-mfax-ifaxstatus-get-address-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Address** property is a null-terminated string that contains the destination of a fax job.<br/>                                                                                   |
| [**CallerId**](-mfax-ifaxstatus-get-callerid-vb.md)<br/>           | Read-only<br/> | Retrieves the [**CallerId**](-mfax-ifaxstatus-get-callerid-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **CallerId** property is a string that identifies the calling device that sent an inbound fax job.<br/>                                                                           |
| [**Csid**](-mfax-ifaxstatus-get-csid-vb.md)<br/>                   | Read-only<br/> | Retrieves the [**Csid**](-mfax-ifaxstatus-get-csid-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Csid** property is a string that contains CSID information, typically the fax number of the receiving device.<br/>                                                                      |
| [**CurrentPage**](-mfax-ifaxstatus-get-currentpage-vb.md)<br/>     | Read-only<br/> | Retrieves the [**CurrentPage**](-mfax-ifaxstatus-get-currentpage-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **CurrentPage** property is a number that identifies the current page of an active outbound fax job on a specific port.<br/>                                                |
| [**Description**](-mfax-ifaxstatus-get-description-vb.md)<br/>     | Read-only<br/> | Retrieves the [**Description**](-mfax-ifaxstatus-get-description-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Description** property is a null-terminated string that describes the current status of the specified port.<br/>                                                          |
| [**DeviceId**](-mfax-ifaxstatus-get-deviceid-vb.md)<br/>           | Read-only<br/> | Retrieves the [**DeviceId**](-mfax-ifaxstatus-get-deviceid-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DeviceId** property is a number representing the permanent line identifier for the fax port.<br/>                                                                               |
| [**DeviceName**](-mfax-ifaxstatus-get-devicename-vb.md)<br/>       | Read-only<br/> | Retrieves the [**DeviceName**](-mfax-ifaxstatus-get-devicename-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DeviceName** property is a null-terminated string that contains the user-friendly display name for the fax port.<br/>                                                       |
| [**DocumentName**](-mfax-ifaxstatus-get-documentname-vb.md)<br/>   | Read-only<br/> | Retrieves the [**DocumentName**](-mfax-ifaxstatus-get-documentname-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DocumentName** property is a null-terminated string that contains the user-friendly name associated with an active fax document.<br/>                                   |
| [**DocumentSize**](-mfax-ifaxstatus-get-documentsize-vb.md)<br/>   | Read-only<br/> | Retrieves the [**DocumentSize**](-mfax-ifaxstatus-get-documentsize-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **DocumentSize** property is the size of the fax document associated with the active outbound job on a specific port.<br/>                                                |
| [**ElapsedTime**](-mfax-ifaxstatus-get-elapsedtime-vb.md)<br/>     | Read-only<br/> | Retrieves the [**ElapsedTime**](-mfax-ifaxstatus-get-elapsedtime-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **ElapsedTime** property is a number that represents the elapsed time for an active fax job.<br/>                                                                           |
| [**PageCount**](-mfax-ifaxstatus-get-pagecount-vb.md)<br/>         | Read-only<br/> | Retrieves the [**PageCount**](-mfax-ifaxstatus-get-pagecount-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **PageCount** property represents the total number of pages in an outbound fax transmission.<br/>                                                                               |
| [**Receive**](-mfax-ifaxstatus-get-receive-vb.md)<br/>             | Read-only<br/> | Retrieves the [**Receive**](-mfax-ifaxstatus-get-receive-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Receive** property is a Boolean value that indicates whether a specified fax port is currently receiving a fax.<br/>                                                              |
| [**RecipientName**](-mfax-ifaxstatus-get-recipientname-vb.md)<br/> | Read-only<br/> | Retrieves the [**RecipientName**](-mfax-ifaxstatus-get-recipientname-vb.md) property for a [FaxStatus](-mfax-faxstatus.md) object. The **RecipientName** property is a null-terminated string that contains the name of the recipient of an inbound fax transmission.<br/>                                                                                       |
| [**RoutingString**](-mfax-ifaxstatus-get-routingstring-vb.md)<br/> | Read-only<br/> | Retrieves the [**RoutingString**](-mfax-ifaxstatus-get-routingstring-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **RoutingString** property is a null-terminated string that contains routing information for inbound fax transmissions that is specific to a fax service provider.<br/> |
| [**Send**](-mfax-ifaxstatus-get-send-vb.md)<br/>                   | Read-only<br/> | Retrieves the [**Send**](-mfax-ifaxstatus-get-send-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Send** property is a Boolean value that indicates whether a specified fax port is currently sending a fax. <br/>                                                                        |
| [**SenderName**](-mfax-ifaxstatus-get-sendername-vb.md)<br/>       | Read-only<br/> | Retrieves the [**SenderName**](-mfax-ifaxstatus-get-sendername-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **SenderName** property is a null-terminated string that contains the name of the user who sent the fax transmission.<br/>                                                    |
| [**StartTime**](-mfax-ifaxstatus-get-starttime-vb.md)<br/>         | Read-only<br/> | Retrieves the [**StartTime**](-mfax-ifaxstatus-get-starttime-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **StartTime** property is a number that represents the starting time for an active fax job.<br/>                                                                                |
| [**SubmittedTime**](-mfax-ifaxstatus-get-submittedtime-vb.md)<br/> | Read-only<br/> | Retrieves the [**SubmittedTime**](-mfax-ifaxstatus-get-submittedtime-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **SubmittedTime** property is a number that represents the time the user submitted the active fax job.<br/>                                                             |
| [**Tsid**](-mfax-ifaxstatus-get-tsid-vb.md)<br/>                   | Read-only<br/> | Retrieves the [**Tsid**](-mfax-ifaxstatus-get-tsid-vb.md) property for the [FaxStatus](-mfax-faxstatus.md) object of a parent [FaxPort](-mfax-faxport.md) object. The **Tsid** property is a null-terminated string that contains the TSID associated with the fax port.<br/>                                                                                   |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxStatus** object's type library information in Visual Basic syntax.

### To create a FaxStatus object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object.
2.  Call the [**GetPorts**](-mfax-ifaxserver-getports-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a [**FaxPorts**](-mfax-faxports-object-visual-basic-.md) object for the connected fax server.
3.  Retrieve the [**Count**](-mfax-ifaxports-get-count.md) property and then the [**Item**](-mfax-ifaxports-get-item.md) property for the [**FaxPorts**](-mfax-faxports-object-visual-basic-.md) collection to create a [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object.
4.  Call the [**GetStatus**](-mfax-ifaxport-getstatus-vb.md) method of the [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object to create a **FaxStatus** object.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




