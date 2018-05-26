---
Description: The Item property returns a FaxOutboundRoutingRule object from the FaxOutboundRoutingRules collection using the routing rules index.
ms.assetid: da4c8ac9-7497-46f7-8575-c4598bb9364b
title: FaxOutboundRoutingRules.Item property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRules.Item property

The **Item** property returns a [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object from the [**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md) collection using the routing rule's index.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal lIndex As Long _
) As FaxOutboundRoutingRule
```



## Property value

A [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object.

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

[**FaxOutboundRoutingRules**](-mfax-faxoutboundroutingrules.md)
</dt> <dt>

[**IFaxOutboundRoutingRules**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundroutingrules?branch=master)
</dt> </dl>

 

 




