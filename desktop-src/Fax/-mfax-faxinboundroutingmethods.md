---
Description: The FaxInboundRoutingMethods configuration collection is used by a fax client application to manage the ordered inbound fax routing methods.
ms.assetid: 5a00a56f-f82b-4e4b-b78f-d9f7417090c8
title: FaxInboundRoutingMethods object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxInboundRoutingMethods object

The **FaxInboundRoutingMethods** configuration collection is used by a fax client application to manage the ordered inbound fax routing methods.

## Members

The **FaxInboundRoutingMethods** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxInboundRoutingMethods** object has these properties.



| Property                                                            | Access type          | Description                                                                                                                                                                                                                                           |
|:--------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxinboundroutingmethods-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxinboundroutingmethods-count-vb.md) property represents the number of objects in the **FaxInboundRoutingMethods** collection. This is the total number of inbound routing methods associated with the fax server.<br/> |
| [**Item**](-mfax-faxinboundroutingmethods-item.md)<br/>      | Read-only<br/> | The [**Item**](-mfax-faxinboundroutingmethods-item.md) property returns a [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) object from the **FaxInboundRoutingMethods** collection.<br/>                                       |



 

## Remarks

Each inbound routing method is represented by a [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) object. The order of the routing methods in the collection determines the relative order in which the methods execute when an inbound fax requires routing.

A **FaxInboundRoutingMethods** object is accessed through a [**FaxInboundRouting**](-mfax-faxinboundrouting.md) object.

![faxinboundrouting, faxinboundroutingmethods, and faxinboundroutingmethod objects](images/faxinboundroutingmethods.png)

To create a **FaxInboundRoutingMethods** object in Microsoft Visual Basic, call the [**GetMethods**](-mfax-faxinboundrouting-getmethods.md) property of the [**FaxInboundRouting**](-mfax-faxinboundrouting.md) object.

To create a **FaxInboundRoutingMethods** object in C++, call the [**GetMethods**](-mfax-faxinboundrouting-getmethods-cpp.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxInboundRoutingMethods<br/>                                              |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods-cpp.md)
</dt> </dl>

 

 




