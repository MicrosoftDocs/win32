---
Description: The UseDevice property is a Boolean value that indicates whether the outbound routing rule points to a single fax device.
ms.assetid: 932a1e3a-a673-4998-b209-a28348a6df88
title: FaxOutboundRoutingRule.UseDevice property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRule.UseDevice property

The **UseDevice** property is a Boolean value that indicates whether the outbound routing rule points to a single fax device.

This property is read/write.

## Syntax


```VB
Property UseDevice As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the outbound routing rule points to a single fax device. When this property is set to **True**, the rule points to a single device. When this property is set to **False**, the rule points to a group of devices.

## Remarks

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

 

 




