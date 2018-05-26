---
Description: Specifies the address to which the delivery report is sent.
ms.assetid: 854413f9-74dc-4e93-b019-61ac5bf71be8
title: FaxOutgoingMessage.ReceiptAddress property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingMessage.ReceiptAddress property

Specifies the address to which the delivery report is sent.

> [!Note]  
> This property is supported only on Windows Vista and later.

 

This property is read-only.

## Syntax


```VB
Property ReceiptAddress As String
```



## Property value

Pointer to a string specifying the address to which the delivery report is sent.

## Remarks

The type of address will vary according to the value of the [**ReceiptType**](-mfax-faxoutgoingmessage-receipttype-vb.md) property as indicated in this table.



| Value of [**ReceiptType**](-mfax-faxoutgoingmessage-receipttype-vb.md) property | Type of address                                                        |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| frtMAIL                                                                          | An SMTP email address                                                  |
| frtMSGBOX                                                                        | The computer name on which the delivery report message box will appear |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage2**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingmessage2?branch=master)
</dt> </dl>

 

 




