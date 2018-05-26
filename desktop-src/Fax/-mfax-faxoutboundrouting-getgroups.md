---
Description: The GetGroups method retrieves the collection of outbound routing groups.
ms.assetid: d2f481be-502e-49d4-a290-d5a9053ca3c4
title: FaxOutboundRouting.GetGroups method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRouting.GetGroups method

The **GetGroups** method retrieves the collection of outbound routing groups.

## Syntax


```VB
FaxOutboundRouting.GetGroups() As FaxOutboundRoutingGroups
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md)\*\***

A [**FaxOutboundRoutingGroups**](-mfax-faxoutboundroutinggroups.md) object.

## Remarks

To use this method, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outbound-routing-groups.md)
</dt> <dt>

[**FaxOutboundRouting**](-mfax-faxoutboundrouting.md)
</dt> <dt>

[**IFaxOutboundRouting**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundrouting?branch=master)
</dt> </dl>

 

 




