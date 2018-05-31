---
Description: A null-terminated string containing the address to which a delivery report will be sent, indicating success or failure.
ms.assetid: 7bafee3b-27d8-4007-94b7-6cb5264c1450
title: FaxOutgoingJob.ReceiptAddress property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.ReceiptAddress property

A null-terminated string containing the address to which a delivery report will be sent, indicating success or failure.

This property is read-only.

## Syntax


```VB
Property ReceiptAddress As String
```



## Property value

A **String** that receives an address to which the delivery report will be sent.

## Remarks

The type of address will vary according to the value of the [**ReceiptType**](-mfax-faxoutgoingjob-receipttype-vb.md) property as indicated in this table.



| Value of [**ReceiptType**](-mfax-faxoutgoingjob-receipttype-vb.md) property | Type of address                                                        |
|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| frtMAIL                                                                      | An SMTP email address                                                  |
| frtMSGBOX                                                                    | The computer name on which the delivery report message box will appear |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob2**](-mfax-faxoutgoingjob2-cpp.md)
</dt> </dl>

 

 




