---
Description: The DeviceId property specifies the device ID if the outbound routing rule points to a single fax device.
ms.assetid: 0b9328d5-4213-4d10-9201-8c9035a22ccc
title: FaxOutboundRoutingRule.DeviceId property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutboundRoutingRule.DeviceId property

The **DeviceId** property specifies the device ID if the outbound routing rule points to a single fax device.

This property is read/write.

## Syntax


```VB
Property DeviceId As Long
```



## Property value

A **Long** value that receives the device ID of the single fax device associated with a particular outbound routing rule.

## Remarks

This property is valid only if the [**UseDevice**](-mfax-faxoutboundroutingrule-usedevice-vb.md) property is equal to **True**.

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

[**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md)
</dt> <dt>

[**IFaxOutboundRoutingRule**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutboundroutingrule?branch=master)
</dt> </dl>

 

 




