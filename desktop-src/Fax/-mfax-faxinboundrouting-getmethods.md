---
Description: The GetMethods method retrieves the ordered collection of all the inbound routing methods exposed by all the inbound routing extensions currently registered with the fax service.
ms.assetid: 185e9bbe-da8d-4041-af5f-7bf95bd647b9
title: FaxInboundRouting.GetMethods method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxInboundRouting.GetMethods method

The **GetMethods** method retrieves the ordered collection of all the inbound routing methods exposed by all the inbound routing extensions currently registered with the fax service.

## Syntax


```VB
FaxInboundRouting.GetMethods() As FaxInboundRoutingMethods
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md)\*\***

A [**FaxInboundRoutingMethods**](-mfax-faxinboundroutingmethods.md) object.

## Remarks

Order is based on the [**Priority**](-mfax-faxinboundroutingmethod-priority.md) property of each routing method. The priority is associated with the order in which the fax service calls the routing method when the service receives a fax job.

To use this method, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-routing-extensions-and-routing-methods.md)
</dt> <dt>

[**FaxInboundRouting**](-mfax-faxinboundrouting.md)
</dt> </dl>

 

 




