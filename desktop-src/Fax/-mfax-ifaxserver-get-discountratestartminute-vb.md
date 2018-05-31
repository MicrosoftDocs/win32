---
Description: Sets or retrieves the DiscountRateStartMinute property for a FaxServer object. The DiscountRateStartMinute property is a number that represents the minute the discount period begins. The discount period applies only to outgoing fax transmissions.
ms.assetid: 5159eb01-d464-4cc3-8617-e785c97ff6ff
title: FaxServer.DiscountRateStartMinute property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.DiscountRateStartMinute property

Sets or retrieves the **DiscountRateStartMinute** property for a [FaxServer](-mfax-faxserver-client.md) object. The **DiscountRateStartMinute** property is a number that represents the minute the discount period begins. The discount period applies only to outgoing fax transmissions.

This property is read/write.

## Syntax


```VB
Property DiscountRateStartMinute As Integer
```



## Property value

An **Integer** that specifies or receives the minute the discount period begins. Valid values for this parameter are 0 through 59.

## Remarks

To save on transmission costs, a user can queue a fax job and request that the fax server send the transmission during the discount rate period. For more information, see [**FaxDoc.DiscountSend Property**](-mfax-ifaxdoc-get-discountsend-vb.md).

The [**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md), **DiscountRateStartMinute**, [**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md), and [**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md) properties represent local time.

If the time the discount rate period ends is less than the time the discount rate period begins, the discount rate period extends into the next day. For example, if the discount rate period begins at 9:00 P.M. and ends at 7:00 A.M., the discount rate period begins in the evening and continues until the morning of the following day.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxServer](-mfax-faxserver-client.md)
</dt> <dt>

[**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md)
</dt> <dt>

[**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md)
</dt> <dt>

[**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md)
</dt> <dt>

[**DiscountSend**](-mfax-ifaxdoc-get-discountsend-vb.md)
</dt> </dl>

 

 




