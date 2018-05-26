---
Description: The AllowedReceipts property is a value that specifies the permitted types of delivery receipts.
ms.assetid: 27bf34d0-5002-4c2b-8552-82a78aabd015
title: FaxReceiptOptions.AllowedReceipts property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxReceiptOptions.AllowedReceipts property

The **AllowedReceipts** property is a value that specifies the permitted types of delivery receipts.

This property is read/write.

## Syntax


```VB
Property AllowedReceipts As Integer
```



## Property value

A variable of type [**FAX\_RECEIPT\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_receipt_type_enum?branch=master) that specifies or receives a value or combination of values of permitted types of delivery receipts. See the **FAX\_RECEIPT\_TYPE\_ENUM** enumeration.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxReceiptOptions**](-mfax-faxreceiptoptions.md)
</dt> <dt>

[**IFaxReceiptOptions**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxreceiptoptions?branch=master)
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 




