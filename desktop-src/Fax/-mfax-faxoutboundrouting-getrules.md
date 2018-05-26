---
Description: The GetRules method retrieves the collection of outbound routing groups.
ms.assetid: a75724ca-76e4-47a4-93ef-523708127155
title: FaxOutboundRouting.GetRules method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRouting.GetRules method

The **GetRules** method retrieves the collection of outbound routing groups.

## Syntax


```VB
FaxOutboundRouting.GetRules() As FaxOutboundRoutingRules
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)\*\***

A [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) object.

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

[Visual Basic Example](-mfax-creating-and-managing-outbound-routing-rules.md)
</dt> <dt>

[**FaxOutboundRouting**](-mfax-faxoutboundrouting.md)
</dt> <dt>

[**IFaxOutboundRouting**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundrouting?branch=master)
</dt> </dl>

 

 




