---
title: IMimeSecurity2 VerifyReceipt method
description: Verifies the receipt against the original message.
ms.assetid: a044dc7a-eeaf-460a-acd8-f821231df5c9
keywords:
- VerifyReceipt method Windows Mail (formerly Outlook Express)
- VerifyReceipt method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , VerifyReceipt method
topic_type:
- apiref
api_name:
- IMimeSecurity2.VerifyReceipt
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeSecurity2::VerifyReceipt method

Verifies the receipt against the original message.

## Syntax


```C++
HRESULT VerifyReceipt(
  [in] DWORD        dwFlags,
  [in] IMimeMessage *pMimeMessageReceipt
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*pMimeMessageReceipt* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Specifies a pointer to the [**IMimeMessage**](oe-imimemessage.md) object that contains the receipt.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                                      | Description                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                             | Indicates success. <br/>                                                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                           | Indicates that an unknown error has occurred. <br/>                                                                                                     |
| <dl> <dt>**MIME\_E\_SECURITY\_RECEIPT\_NOMATCHINGRECEIPTBODY**</dt> </dl> | Indicates that no matching receipt was found. <br/>                                                                                                     |
| <dl> <dt>**MIME\_E\_SECURITY\_RECEIPT\_MSGHASHMISMATCH**</dt> </dl>       | Indicates that the original message has no digest or that the hash value of the original message is different from the hash value of the receipt. <br/> |



 

## Remarks

This method assumes that the object in *pMimeMessageReceipt* has been decoded and its signature has been verified.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





