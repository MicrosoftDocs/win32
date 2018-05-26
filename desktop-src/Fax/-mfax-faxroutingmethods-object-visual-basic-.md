---
Description: The FaxRoutingMethods object represents a collection of FaxRoutingMethod objects.
ms.assetid: 2172900a-c793-4a65-ac24-72d514479880
title: FaxRoutingMethods object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxRoutingMethods object

The **FaxRoutingMethods** object represents a collection of [**FaxRoutingMethod objects**](-mfax-faxroutingmethod-object-visual-basic-.md). The **FaxRoutingMethods** object permits a fax client Microsoft Visual Basic application to enumerate the fax routing methods associated with a fax port, and to create **FaxRoutingMethod** objects for individual routing methods. There is one **FaxRoutingMethod** object for each routing method associated with the port.

The **FaxRoutingMethods** object has the following properties:

-   A property to enumerate the number of fax routing methods associated with a connected fax port.
-   A property to create a [**object**](-mfax-faxroutingmethod-object-visual-basic-.md) for a specified fax routing method.

## Members

The **FaxRoutingMethods** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxRoutingMethods** object has these properties.



| Property                                                          | Access type          | Description                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-ifaxroutingmethods-get-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-ifaxroutingmethods-get-count-vb.md) returns the number of fax routing methods associated with a [FaxPort](-mfax-faxport.md) object.<br/>                                                                                                                       |
| [**Item**](-mfax-ifaxroutingmethods-get-item-vb.md)<br/>   | Read-only<br/> | The [**Item**](-mfax-ifaxroutingmethods-get-item-vb.md) method creates a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object for a specified fax routing method. The object allows enumeration of fax routing information for a specified [FaxPort](-mfax-faxport.md) object.<br/> |



 

## Remarks

### When to Implement

You should not implement this class. The Microsoft standard implementation provides complete functionality. You can use the Visual Basic Object Browser to view the **FaxRoutingMethods** object's type library information in Visual Basic syntax.

### To create a FaxRoutingMethods object

1.  Call the Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create a [**FaxServer object**](-mfax-faxserver-object-visual-basic-.md).
2.  Call the [**GetRoutingMethods**](-mfax-ifaxport-getroutingmethods-vb.md) method of the [**FaxPort**](-mfax-faxport-object-visual-basic-.md) object to create a **FaxRoutingMethods** object on the connected fax server.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Faxcom.h</dt> </dl> |



 

 




