---
Description: The RemoveByCountryAndArea method removes an outbound routing rule (FaxOutboundRoutingRule object) from the collection using the routing rules country/region code and area code.
ms.assetid: 2394411f-c31a-4a5b-86c8-5003007dec95
title: FaxOutboundRoutingRules.RemoveByCountryAndArea method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRules.RemoveByCountryAndArea method

The **RemoveByCountryAndArea** method removes an outbound routing rule ([**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object) from the collection using the routing rule's country/region code and area code.

## Syntax


```VB
FaxOutboundRoutingRules.RemoveByCountryAndArea( _
  ByVal lCountryCode As Long, _
  ByVal lAreaCode As Long _
) As Long
```



## Parameters

<dl> <dt>

*lCountryCode* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the country/region code of the outbound routing rule to remove from the collection. Specifying [**frrcANY\_CODE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_routing_rule_code_enum?branch=master) will remove a rule that applies to all country/region codes.

</dd> <dt>

*lAreaCode* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the area code of the outbound routing rule to remove from the collection. Specifying [**frrcANY\_CODE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_routing_rule_code_enum?branch=master) will remove a rule that applies to all area codes within the specified country/region code.

</dd> </dl>

## Remarks

You cannot set both *lCountryCode* and *lAreaCode* to [**frrcANY\_CODE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_routing_rule_code_enum?branch=master) because this is equivalent to specifying the default outbound routing rule, which cannot be removed.

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

 

 




