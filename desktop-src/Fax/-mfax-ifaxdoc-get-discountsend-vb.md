---
Description: Sets or retrieves the DiscountSend property for a FaxDoc object. The DiscountSend property is a Boolean value that indicates whether the fax server transmits faxes during the discount period.
ms.assetid: f7a084fe-abab-44ed-9198-df75cd196ed8
title: FaxDoc.DiscountSend property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDoc.DiscountSend property

Sets or retrieves the **DiscountSend** property for a [FaxDoc](-mfax-faxdoc.md) object. The **DiscountSend** property is a Boolean value that indicates whether the fax server transmits faxes during the discount period.

This property is read/write.

## Syntax


```VB
Property DiscountSend As Boolean
```



## Property value

A **Boolean** that specifies or receives a value that indicates whether the fax server sends documents during the transmission discount period.

## Remarks

To determine the period during which the discount rate applies, you can call the following [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver) methods: [**DiscountRateStartMinute**](-mfax-ifaxserver-get-discountratestartminute-vb.md), [**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md), [**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md), and [**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxDoc**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxdoc)
</dt> <dt>

[**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md)
</dt> <dt>

[**DiscountRateStartMinute**](-mfax-ifaxserver-get-discountratestartminute-vb.md)
</dt> <dt>

[**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md)
</dt> <dt>

[**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md)
</dt> </dl>

 

 




