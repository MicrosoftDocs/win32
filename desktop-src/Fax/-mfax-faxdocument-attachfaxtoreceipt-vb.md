---
Description: The AttachFaxToReceipt property indicates whether to attach a fax to the receipt.
ms.assetid: da5a2d29-4002-49ad-ba44-ec7841598581
title: FaxDocument.AttachFaxToReceipt property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.AttachFaxToReceipt property

The **AttachFaxToReceipt** property indicates whether to attach a fax to the receipt.

This property is read/write.

## Syntax


```VB
Property AttachFaxToReceipt As Boolean
```



## Property value

A **Boolean** that specifies or receives a value indicating whether to attach a fax to the receipt.

## Remarks

By default, **AttachFaxToReceipt** is set to **False**.

When a fax consisting only of a cover page is sent to multiple recipients, you cannot attach the fax to the receipt because the fax differs for each recipient. If there is a fax body, then the body can be attached to the receipt, even when there are multiple recipients.

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

[**IFaxDocument**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument)
</dt> </dl>

 

 




