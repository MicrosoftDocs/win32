---
Description: The AllowedReceipts property is a value that specifies the permitted types of delivery receipts.
ms.assetid: 27bf34d0-5002-4c2b-8552-82a78aabd015
title: FaxReceiptOptions.AllowedReceipts property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxReceiptOptions.AllowedReceipts property

The **AllowedReceipts** property is a value that specifies the permitted types of delivery receipts.

This property is read/write.

## Syntax


```VB
Property AllowedReceipts As Integer
```



## Property value

A variable of type [**FAX\_RECEIPT\_TYPE\_ENUM**](-mfax-fax-receipt-type-enum.md) that specifies or receives a value or combination of values of permitted types of delivery receipts. See the **FAX\_RECEIPT\_TYPE\_ENUM** enumeration.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxReceiptOptions**](-mfax-faxreceiptoptions-cpp.md)
</dt> <dt>

[Setting Receipt Options](-mfax-setting-receipt-options.md)
</dt> </dl>

 

 




