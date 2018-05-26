---
Description: The FaxPorts object represents a collection of FaxPort objects.
ms.assetid: 74ccb74e-7eb9-4617-ae0b-01f6f2095801
title: FaxPorts object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxPorts object

The **FaxPorts** object represents a collection of [**FaxPort objects**](-mfax-faxport-object-visual-basic-.md). The **FaxPorts** object permits a fax client Microsoft Visual Basic application to enumerate the fax ports associated with a connected fax server, and to create **FaxPort** objects for those ports. There is one **FaxPort** object for each port associated with the server.

The **FaxPorts** object has the following properties:

-   A property to enumerate the number of ports associated with a connected fax server.
-   A property to create a [**FaxPort object**](-mfax-faxport-object-visual-basic-.md) for a specified fax port.

## Members

The **FaxPorts** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxPorts** object has these properties.



| Property                                                 | Access type          | Description                                                                                                                                                                                                                                          |
|:---------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-ifaxports-get-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-ifaxjobs-get-count-vb.md) property returns the number of fax ports attached to the connected fax server.<br/>                                                                                                           |
| [**Item**](-mfax-ifaxports-get-item-vb.md)<br/>   | Read-only<br/> | The [**Item**](-mfax-ifaxports-get-item-vb.md) method creates a [FaxPort](-mfax-faxport.md) object for a specified fax port. The object allows enumeration of port configuration information for a specific connection to a fax server.<br/> |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxPorts** object's type library information in Visual Basic syntax.

### To create a FaxPorts object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the [**GetPorts**](-mfax-ifaxserver-getports-vb.md) method of the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object to create a **FaxPorts** object on the connected fax server.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




