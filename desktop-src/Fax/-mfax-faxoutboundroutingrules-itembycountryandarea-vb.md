---
Description: The ItemByCountryAndArea method returns an outbound routing rule (FaxOutboundRoutingRule object) from the collection using the routing rules country/region code and area code.
ms.assetid: 9e9130b9-2176-4d99-8e67-b80fb5edb95d
title: FaxOutboundRoutingRules.ItemByCountryAndArea method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRules.ItemByCountryAndArea method

The **ItemByCountryAndArea** method returns an outbound routing rule ([**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object) from the collection using the routing rule's country/region code and area code.

## Syntax


```VB
FaxOutboundRoutingRules.ItemByCountryAndArea( _
  ByVal lCountryCode As Long, _
  ByVal lAreaCode As Long, _
  ByVal FaxOutboundRoutingRule As FaxOutboundRoutingRule _
) As Long
```



## Parameters

<dl> <dt>

*lCountryCode* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the country/region code of the outbound routing rule to retrieve. Specifying [**frrcANY\_CODE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_routing_rule_code_enum?branch=master) will return a rule for any country/region code.

</dd> <dt>

*lAreaCode* 
</dt> <dd>

Type: **Long**

A **Long** value that specifies the area code of the outbound routing rule to retrieve. Specifying [**frrcANY\_CODE**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_routing_rule_code_enum?branch=master) will return a rule for any area code within the specified country/region code.

</dd> <dt>

*FaxOutboundRoutingRule* 
</dt> <dd>

Type: **[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)\*\***

A [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) object.

</dd> </dl>

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

 

 




