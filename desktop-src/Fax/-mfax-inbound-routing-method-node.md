---
Description: The inbound routing method node represents an inbound fax routing method.
ms.assetid: a70fc9a3-ade9-49c7-8328-57a4bba41797
title: Inbound Routing Method Node
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inbound Routing Method Node

The inbound routing method node represents an inbound fax routing method. A fax routing method is an action that is performed each time a fax is received on a port. For more information, see [About Fax Routing Methods](-mfax-about-fax-routing-methods.md).

Inbound routing method nodes are typically associated with a fax device, but can be associated with a fax routing method that is listed in the [routing methods](-mfax-mmc-snap-in-node-types.md) catalog.

The administrative Microsoft Management Console (MMC) snap-in for the fax service supplies:

-   A UI to enable and disable a fax routing method on a specific device.
-   A property sheet that contains a page of global information that applies to fax routing methods.

Third-party vendors can add an MMC property sheet extension that provides additional property pages for configuring the individual fax routing methods that the third-party vendor exports.

The fax service MMC snap-in provides the extension with a device ID that the extension can use to determine the device with which the inbound routing method node is associated. If the device ID equals zero, the context in which this routing method node appears is the global routing methods catalog list. Its context is not the list of routing methods associated with a device.

Note that the inbound routing method node can appear in either the result pane of the **Inbound Routing Methods** namespace node or in the result pane of the **Inbound Routing\\Methods** node. In the first case, the inbound routing method node represents a fax routing method that is associated with a specific device. In the second case, the node represents a fax routing method that is listed in the global routing methods catalog. An MMC extension snap-in that extends the inbound routing method node must distinguish between the two situations.

If your extension snap-in configures a fax routing method from within an inbound routing method node in the global routing methods catalog, configuration changes must apply to all fax devices. If your snap-in configures a fax routing method from within the inbound routing method node of a specific device, configuration changes must apply only to the specific device.

## When to Extend This Node

Extend this node to allow an administrator to configure the behavior of a fax routing method exposed by your fax routing method extension.

> [!Note]  
> Use the [**FaxExtSetData**](-mfax-faxextsetdata.md) function to set configuration data for a specific device and GUID.

 

## Node-Type GUID

{220D2CB0-85A9-4a43-B6E8-9D66B44F1AF5}

## IDataObject Content

Use the following custom clipboard formats to retrieve information related to the fax device node.



| Clipboard format                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CF\_MSFAXSRV\_ROUTEEXT\_NAME        | **Data format:** A null-terminated Unicode character string that contains the internal name of the fax routing extension DLL that supplies the fax routing method. This is the same string provided during registration by the *ExtensionName* parameter to the [**FaxRegisterRoutingExtension**](-mfax-faxregisterroutingextension.md) function.<br/> **Remarks:** The maximum length of the extension name string, including the terminating null character, is FAXSRV\_MAX\_ROUTEEXT\_NAME\_LEN + 1 characters.<br/>                                                                                                                                                                                                                                                               |
| CF\_MSFAXSRV\_ROUTING\_METHOD\_GUID | **Data format:** A null-terminated Unicode character string that contains a string representation of the GUID for the fax routing method. The string has the same format as the string returned by the Microsoft Win32 function [StringFromGUID2](http://msdn.microsoft.com/en-us/library/ms683893.aspx). An example of the string is {c200e360-38c5-11ce-ae62-08002b2b79ef}.<br/> **Remarks:** The maximum length of the GUID string, including the terminating null character, is FAXSRV\_MAX\_GUID\_LEN characters.<br/>                                                                                                                                                                                                                                                            |
| CF\_MSFAXSRV\_DEVICE\_ID            | **Data format:** A **DWORD** value that contains the device ID of the device with which the fax routing method is associated.<br/> **Remarks:** This value is the device ID generated by the fax service. This is not the device ID generated by a Telephony Application Programming Interface (TAPI) telephony service provider (TSP). You can use this device ID when you call the [Fax Extension Configuration API callback functions](-mfax-fax-extension-configuration-reference.md) if you specify the value DEV\_ID\_SRC\_FAX in the *DevIdSrc* parameter.<br/> If the device ID is equal to zero, it indicates that the inbound routing method node appears in the global routing methods catalog, and that the node is not associated with a specific fax device.<br/> |
| CF\_MSFAXSRV\_SERVER\_NAME          | **Data format:** A **DWORD** value that contains the name of the fax server with which the fax routing method is associated. The server name is not preceded by "\\\\".<br/> **Remarks:** The maximum length of the server name string, including the terminating null character, is FAXSRV\_MAX\_SERVER\_NAME characters.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

 

 




