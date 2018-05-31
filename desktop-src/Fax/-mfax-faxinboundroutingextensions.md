---
Description: The FaxInboundRoutingExtensions configuration collection is used by a fax client application to manage the inbound fax routing extensions registered with the fax service. Each extension is represented by a FaxInboundRoutingExtension object.
ms.assetid: 8989c149-bbf4-46c1-b969-949d44efcf90
title: FaxInboundRoutingExtensions object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxInboundRoutingExtensions object

The **FaxInboundRoutingExtensions** configuration collection is used by a fax client application to manage the inbound fax routing extensions registered with the fax service. Each extension is represented by a [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md) object.

## Members

The **FaxInboundRoutingExtensions** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxInboundRoutingExtensions** object has these properties.



| Property                                                               | Access type          | Description                                                                                                                                                                                                                                                    |
|:-----------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxinboundroutingextensions-count-vb.md)<br/> | Read-only<br/> | The [**Count**](-mfax-faxinboundroutingextensions-count-vb.md) property represents the number of objects in the **FaxInboundRoutingExtensions** collection. This is the total number of inbound routing extensions associated with the fax server.<br/> |
| [**Item**](-mfax-faxinboundroutingextensions-item.md)<br/>      | Read-only<br/> | The [**Item**](-mfax-faxinboundroutingextensions-item.md) property returns a [**FaxInboundRoutingExtension**](-mfax-faxinboundroutingextension.md) object from the **FaxInboundRoutingExtensions** collection.<br/>                                    |



 

## Remarks

A **FaxInboundRoutingExtensions** object is accessed through a [**FaxInboundRouting**](-mfax-faxinboundrouting.md) object.

![faxinboundrouting, faxroutingextensions, and faxroutingextension objects](images/faxinboundroutingextensions.png)

To create a **FaxInboundRoutingExtensions** object in Microsoft Visual Basic, call the [**GetExtensions**](-mfax-faxinboundrouting-getextensions.md) property of the [**FaxInboundRouting**](-mfax-faxinboundrouting.md) object.

To create a **FaxInboundRoutingExtensions** object in C++, call the [**GetExtensions**](-mfax-faxinboundrouting-getextensions.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxInboundRoutingExtensions<br/>                                           |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxInboundRoutingExtensions**](-mfax-faxinboundroutingextensions-cpp.md)
</dt> </dl>

 

 




