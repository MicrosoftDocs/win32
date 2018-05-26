---
Description: The Status property indicates the current status of the outbound routing rule; for example, whether the rule is valid and whether it can apply to fax jobs.
ms.assetid: 41e1552e-e7eb-4fd4-82b5-73c54e5f37bd
title: FaxOutboundRoutingRule.Status property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRule.Status property

The **Status** property indicates the current status of the outbound routing rule; for example, whether the rule is valid and whether it can apply to fax jobs.

This property is read-only.

## Syntax


```VB
Property Status As Integer
```



## Property value

Value from the [**FAX\_RULE\_STATUS\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_rule_status_enum?branch=master) enumeration that specifies the rule status.

## Remarks

To read this property, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxOutboundRoutingRule**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundroutingrule?branch=master)
</dt> </dl>

 

 




