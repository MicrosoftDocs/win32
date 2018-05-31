---
Description: The FaxPort object permits a fax client Microsoft Visual Basic application to access configuration information for a fax port on a connected fax server.
ms.assetid: 7888d042-7d85-4921-b233-f6e95e0c80d9
title: FaxPort object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxPort object

The **FaxPort** object permits a fax client Microsoft Visual Basic application to access configuration information for a fax port on a connected fax server. Information includes, among other items, a device identifier, the port's name and current status, and station identifiers. There is one **FaxPort** object for each port associated with the server.

The **FaxPort** object has the following methods and properties:

-   Methods to create [**FaxRoutingMethods objects**](-mfax-faxroutingmethods-object-visual-basic-.md) and [**FaxStatus objects**](-mfax-faxstatus-object-visual-basic-.md).
-   Properties to set and retrieve individual attributes associated with a **FaxPort** object.

Before attempting to change port configuration information, a fax client application can retrieve the [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property for a **FaxPort** object to ensure that the client has access to modify the specified fax port.

## Members

The **FaxPort** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FaxPort** object has these methods.



| Method                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRoutingMethods**](-mfax-ifaxport-getroutingmethods-vb.md) | The [**GetRoutingMethods**](-mfax-ifaxport-getroutingmethods-vb.md) interface method creates a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object for the parent [FaxPort](-mfax-faxport.md) object. The FaxRoutingMethods object allows enumeration of the fax routing methods associated with a fax port. Fax routing methods are defined by a fax routing extension DLL.<br/> |
| [**GetStatus**](-mfax-ifaxport-getstatus-vb.md)                 | The [**GetStatus**](-mfax-ifaxport-getstatus-vb.md) method creates a [FaxStatus](-mfax-faxstatus.md) object for the parent [FaxPort](-mfax-faxport.md) object. The FaxStatus object contains the current status of a fax port.<br/>                                                                                                                                                  |



 

### Properties

The **FaxPort** object has these properties.



| Property                                                        | Access type           | Description                                                                                                                                                                                                                                                           |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md)<br/> | Read-only<br/>  | The [**CanModify**](-mfax-ifaxport-get-canmodify-vb.md) property is a Boolean value that indicates whether the user has permission to modify configuration information for the fax port.<br/>                                                                  |
| [**Csid**](-mfax-ifaxport-get-csid-vb.md)<br/>           | Read/write<br/> | The [**Csid**](-mfax-ifaxport-get-csid-vb.md) property is a null-terminated string that contains the CSID associated with the fax port. <br/>                                                                                                                  |
| [**DeviceId**](-mfax-ifaxport-get-deviceid-vb.md)<br/>   | Read-only<br/>  | The [**DeviceId**](-mfax-ifaxport-get-deviceid-vb.md) property is a number representing the permanent line identifier for the fax port. <br/>                                                                                                                  |
| [**Name**](-mfax-ifaxport-get-name-vb.md)<br/>           | Read-only<br/>  | The [**Name**](-mfax-ifaxport-get-name-vb.md) property is a null-terminated string that contains the user-friendly display name for a fax port.<br/>                                                                                                           |
| [**Priority**](-mfax-ifaxport-get-priority-vb.md)<br/>   | Read/write<br/> | The [**Priority**](-mfax-ifaxport-get-priority-vb.md) property is a number representing the transmission priority designated for a specified fax port. Priority determines the relative order in which available fax devices send outgoing transmissions.<br/> |
| [**Receive**](-mfax-ifaxport-get-receive-vb.md)<br/>     | Read/write<br/> | The [**Receive**](-mfax-ifaxport-get-receive-vb.md) property is a Boolean value that indicates whether a specified fax port is enabled to receive faxes.<br/>                                                                                                  |
| [**Rings**](-mfax-ifaxport-get-rings-vb.md)<br/>         | Read/write<br/> | The [**Rings**](-mfax-ifaxport-get-rings-vb.md) property represents the number of rings an incoming fax call should wait before the fax port answers the call. <br/>                                                                                           |
| [**Send**](-mfax-ifaxport-get-send-vb.md)<br/>           | Read/write<br/> | The [**Send**](-mfax-ifaxport-get-send-vb.md) property is a Boolean value that indicates whether a fax port is enabled to send faxes. <br/>                                                                                                                    |
| [**Tsid**](-mfax-ifaxport-get-tsid-vb.md)<br/>           | Read/write<br/> | The [**Tsid**](-mfax-ifaxport-get-tsid-vb.md) property is a null-terminated string that contains the TSID associated with the fax port.<br/>                                                                                                                   |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxPort** object's type library information in Visual Basic syntax.

### To create a FaxPort object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the [**GetPorts**](-mfax-ifaxserver-getports-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a [**FaxPorts object**](-mfax-faxports-object-visual-basic-.md) on the connected fax server.
3.  Retrieve the [**Count**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxports-get_count) property and then the [**Item**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxports-get_item) property for the [**FaxPorts**](-mfax-faxports-object-visual-basic-.md) collection to create a **FaxPort** object.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




