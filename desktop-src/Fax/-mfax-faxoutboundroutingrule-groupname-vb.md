---
Description: The GroupName property specifies the group name if the outbound routing rule points to a group of fax devices.
ms.assetid: 2326cea7-3f33-4557-9ced-7ca2277f9216
title: FaxOutboundRoutingRule.GroupName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutboundRoutingRule.GroupName property

The **GroupName** property specifies the group name if the outbound routing rule points to a group of fax devices.

This property is read/write.

## Syntax


```VB
Property GroupName As String
```



## Property value

A **String** that specifies or receives the group name for the group of fax devices associated with a particular outbound routing rule.

## Remarks

This property is valid only if the [**UseDevice**](-mfax-faxoutboundroutingrule-usedevice-vb.md) property is equal to **False**.

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 




