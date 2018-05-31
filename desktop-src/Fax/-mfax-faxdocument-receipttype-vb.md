---
Description: The ReceiptType property specifies the type of delivery receipt to deliver when the fax job reaches a final state.
ms.assetid: 7b557c22-110d-40c2-ab21-412d825deb0c
title: FaxDocument.ReceiptType property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.ReceiptType property

The **ReceiptType** property specifies the type of delivery receipt to deliver when the fax job reaches a final state.

This property is read/write.

## Syntax


```VB
Property ReceiptType As Integer
```



## Property value

A variable of type [**FAX\_RECEIPT\_TYPE\_ENUM**](-mfax-fax-receipt-type-enum.md) that specifies or receives a receipt type. For possible values, see **FAX\_RECEIPT\_TYPE\_ENUM**.

## Remarks

The fax service sends a report (a delivery receipt) to the sender of the fax when the fax completes successfully or when the fax transmission fails.

If an email receipt will be sent, an address has to be provided in the [**ReceiptAddress**](-mfax-faxdocument-receiptaddress-vb.md) property. If the receipt type is set to 0x0004, the message box will appear on the computer from which the document was sent. By default, **ReceiptType** is set to 0x0000, indicating that no receipt will be sent.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




