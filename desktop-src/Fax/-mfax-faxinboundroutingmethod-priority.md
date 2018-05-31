---
Description: The Priority property is a value associated with the order in which the fax service calls the routing method when the service receives a fax job.
ms.assetid: 23208ac4-68c8-4f62-b588-2d0a5575f87c
title: FaxInboundRoutingMethod.Priority property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxInboundRoutingMethod.Priority property

The **Priority** property is a value associated with the order in which the fax service calls the routing method when the service receives a fax job.

This property is read/write.

## Syntax


```VB
Property Priority As Long
```



## Property value

A **Long** that specifies or receives the priority of the fax routing method.

## Remarks

Valid values for this property are 1 through *n*, where 1 is the highest priority.

You should assign a unique priority value to each routing method. After you call the [**Save**](-mfax-faxinboundroutingmethod-save-vb.md) method, the fax service sorts the routing methods by priority. If two routing methods have the same priority, the fax service will choose which will have a higher priority.

If you want a particular routing method to have the lowest possible priority, specify a very large value, such as 999999, and then call the [**Save**](-mfax-faxinboundroutingmethod-save-vb.md) method.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)
</dt> <dt>

[**IFaxInboundRoutingMethod**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxinboundroutingmethod)
</dt> </dl>

 

 




