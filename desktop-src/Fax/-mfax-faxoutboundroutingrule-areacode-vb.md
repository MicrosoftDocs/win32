---
Description: 'The AreaCode property specifies the area code to which the outbound routing rule applies.'
ms.assetid: '94f11d40-f03d-4ed4-8efa-1d758877ea9f'
title: 'FaxOutboundRoutingRule.AreaCode property'
---

# FaxOutboundRoutingRule.AreaCode property

The **AreaCode** property specifies the area code to which the outbound routing rule applies.

This property is read-only.

## Syntax


```VB
Property AreaCode As Long
```



## Property value

A **Long** that receives the area code to which the outbound routing rule applies.

## Remarks

If this property is equal to [**frrcANY\_CODE**](-mfax-fax-routing-rule-code-enum.md), the outbound routing rule applies to all area codes.

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

 

 




