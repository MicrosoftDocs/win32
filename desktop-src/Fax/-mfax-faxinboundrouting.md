---
Description: The FaxInboundRouting configuration object is used by a fax client application to access the inbound routing extensions registered with the fax service, represented by FaxInboundRoutingExtensions objects, and the routing methods the extensions expose, represented by FaxInboundRoutingMethods objects.
ms.assetid: 4cf71225-fcd8-4d2f-b8b3-acbb32708f3b
title: FaxInboundRouting object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRouting object

The **FaxInboundRouting** configuration object is used by a fax client application to access the inbound routing extensions registered with the fax service, represented by [**FaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions.md) objects, and the routing methods the extensions expose, represented by [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md) objects.

## Members

The **FaxInboundRouting** object has these types of members:

-   [Methods](#methods)

### Methods

The **FaxInboundRouting** object has these methods.



| Method                                                         | Description                                                                                                                                                                                                                                 |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetExtensions**](-mfax-faxinboundrouting-getextensions.md) | The [**GetExtensions**](-mfax-faxinboundrouting-getextensions.md) method retrieves the collection of inbound routing extensions registered with the fax service.<br/>                                                                |
| [**GetMethods**](-mfax-faxinboundrouting-getmethods.md)       | The [**GetMethods**](-mfax-faxinboundrouting-getmethods.md) method retrieves the ordered collection of all the inbound routing methods exposed by all the inbound routing extensions currently registered with the fax service.<br/> |



 

## Remarks

A **FaxInboundRouting** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object.

![faxserver, faxinboundrouting, and subordinate objects to faxinboundrouting](images/faxinboundrouting.png)

To create a **FaxInboundRouting** object in Microsoft Visual Basic, call the [**InboundRouting**](-mfax-faxserver-inboundrouting.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

To create a **FaxInboundRouting** object in C++, call the [**InboundRouting**](-mfax-faxserver-inboundrouting.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxInboundRouting<br/>                                                     |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxInboundRouting**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxinboundrouting?branch=master)
</dt> </dl>

 

 




