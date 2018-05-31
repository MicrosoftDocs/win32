---
Description: The UsedRoutingMethods property is an array of strings that contains the GUIDs associated with the routing methods that the device uses, where each GUID represents an inbound routing method (FaxInboundRoutingMethod).
ms.assetid: 8813ea70-2fc6-40d2-8c2f-c9c060b32424
title: FaxDevice.UsedRoutingMethods property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.UsedRoutingMethods property

The **UsedRoutingMethods** property is an array of strings that contains the GUIDs associated with the routing methods that the device uses, where each GUID represents an inbound routing method ([**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)).

This property is read-only.

## Syntax


```VB
Property UsedRoutingMethods As Variant
```



## Property value

A **Variant** that receives an array of GUIDs.

## Remarks

To add a routing method to or remove a routing method from the array of routing method GUIDs, call the [**UseRoutingMethod**](-mfax-faxdevice-useroutingmethod-vb.md) method.

To read this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-fax-device-collection.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> <dt>

[**UseRoutingMethod**](-mfax-faxdevice-useroutingmethod-vb.md)
</dt> </dl>

 

 




