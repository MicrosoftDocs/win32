---
Description: 'The FaxRoutingMethod object permits a fax client Microsoft Visual Basic application to access fax routing configuration information for a fax port on a connected fax server.'
ms.assetid: '4ae5aa09-2961-4823-8c39-0b0a5b0bdc81'
title: FaxRoutingMethod object
---

# FaxRoutingMethod object

The **FaxRoutingMethod** object permits a fax client Microsoft Visual Basic application to access fax routing configuration information for a fax port on a connected fax server. Use this object to enable or disable a fax routing method on a specific fax port, and to retrieve and set the properties of **FaxRoutingMethod** objects. There is one **FaxRoutingMethod** object for each routing method associated with the port.

The **FaxRoutingMethod** object has the following properties:

-   Properties to retrieve, enable, or disable a fax routing method for a specific [**FaxPort object**](-mfax-faxport-object-visual-basic-.md). (Fax routing methods are defined by fax routing extension DLLs.)
-   Properties to retrieve attributes of a **FaxRoutingMethod** object, such as the name of the DLL that exports the routing method. Attributes also include the GUID and function name that uniquely identify the routing method, and the routing method's user-friendly name.

A routing method is an action that is performed each time a fax is received on a port. If fax reception is not enabled on a port, the fax service disregards the routing methods associated with the port. When the service receives a fax, it executes only those routing methods that have been enabled for a device.

## Members

The **FaxRoutingMethod** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxRoutingMethod** object has these properties.



| Property                                                                         | Access type           | Description                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeviceId**](-mfax-ifaxroutingmethod-get-deviceid-vb.md)<br/>           | Read-only<br/>  | The [**DeviceId**](-mfax-ifaxroutingmethod-get-deviceid-vb.md) property is a number representing the line identifier for the fax port. <br/>                                                                                                |
| [**DeviceName**](-mfax-ifaxroutingmethod-get-devicename-vb.md)<br/>       | Read-only<br/>  | The [**DeviceName**](-mfax-ifaxroutingmethod-get-devicename-vb.md) property is a null-terminated string that contains the user-friendly display name for a fax port. <br/>                                                                  |
| [**Enable**](-mfax-ifaxroutingmethod-get-enable-vb.md)<br/>               | Read/write<br/> | The [**Enable**](-mfax-ifaxroutingmethod-get-enable-vb.md) property is a Boolean value that indicates whether a fax routing method is enabled on a particular fax port. <br/>                                                               |
| [**ExtensionName**](-mfax-ifaxroutingmethod-get-extensionname-vb.md)<br/> | Read-only<br/>  | The [**ExtensionName**](-mfax-ifaxroutingmethod-get-extensionname-vb.md) property is a null-terminated string that contains the user-friendly name for the fax routing extension DLL that implements the specified fax routing method.<br/> |
| [**FriendlyName**](-mfax-ifaxroutingmethod-get-friendlyname-vb.md)<br/>   | Read-only<br/>  | The [**FriendlyName**](-mfax-ifaxroutingmethod-get-friendlyname-vb.md) property is a null-terminated string that contains the user-friendly name for a fax routing method. <br/>                                                            |
| [**FunctionName**](-mfax-ifaxroutingmethod-get-functionname-vb.md)<br/>   | Read-only<br/>  | The [**FunctionName**](-mfax-ifaxroutingmethod-get-functionname-vb.md) property is a null-terminated string that contains the name of the function that executes a specific fax routing procedure. <br/>                                    |
| [**Guid**](-mfax-ifaxroutingmethod-get-guid-vb.md)<br/>                   | Read-only<br/>  | The [**Guid**](-mfax-ifaxroutingmethod-get-guid-vb.md) property is a null-terminated string that contains the GUID that uniquely identifies the fax routing method. <br/>                                                                   |
| [**ImageName**](-mfax-ifaxroutingmethod-get-imagename-vb.md)<br/>         | Read-only<br/>  | The [**ImageName**](-mfax-ifaxroutingmethod-get-imagename-vb.md) property is a null-terminated string that contains the executable image name of the fax routing extension DLL that implements the fax routing method.<br/>                 |
| [**RoutingData**](-mfax-ifaxroutingmethod-get-routingdata-vb.md)<br/>     | Read-only<br/>  | The [**RoutingData**](-mfax-ifaxroutingmethod-get-routingdata-vb.md) property is a null-terminated string that contains the routing string for an incoming fax transmission.<br/>                                                           |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxRoutingMethod** object's type library information in Visual Basic syntax.

### To create a FaxRoutingMethod object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the **GetRoutingMethods** method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a [**FaxRoutingMethods object**](-mfax-faxroutingmethods-object-visual-basic-.md) on the connected fax server.
3.  Retrieve the [**Count**](-mfax-ifaxroutingmethods-get-count.md) property and then the [**Item**](-mfax-ifaxroutingmethods-get-item.md) property for the [**FaxRoutingMethods**](-mfax-faxroutingmethods-object-visual-basic-.md) collection to create a **FaxRoutingMethod** object.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




