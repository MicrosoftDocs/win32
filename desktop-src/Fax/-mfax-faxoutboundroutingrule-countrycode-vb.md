---
Description: The CountryCode property specifies the country/region code to which the outbound routing rule applies.
ms.assetid: e5a056d6-3fef-4111-bf49-cb301f5195c3
title: FaxOutboundRoutingRule.CountryCode property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingRule.CountryCode property

The **CountryCode** property specifies the country/region code to which the outbound routing rule applies.

This property is read-only.

## Syntax


```VB
Property CountryCode As Long
```



## Property value

A **Long** that receives the country/region code to which the outbound routing rule applies.

## Remarks

If this property is equal to [**frrcANY\_CODE**](-mfax-fax-routing-rule-code-enum.md), the outbound routing rule applies to all country/region codes.

To read this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)
</dt> <dt>

[**IFaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule-cpp.md)
</dt> </dl>

 

 




