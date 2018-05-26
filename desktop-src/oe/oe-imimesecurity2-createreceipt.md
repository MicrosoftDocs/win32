---
title: IMimeSecurity2 CreateReceipt method
description: Creates a receipt.
ms.assetid: aaa887b2-b70b-4d92-803c-379e7bd4820a
keywords:
- CreateReceipt method Windows Mail (formerly Outlook Express)
- CreateReceipt method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , CreateReceipt method
topic_type:
- apiref
api_name:
- IMimeSecurity2.CreateReceipt
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

# IMimeSecurity2::CreateReceipt method

Creates a receipt.

## Syntax


```C++
HRESULT CreateReceipt(
  [in]        DWORD          dwFlags,
  [in]        DWORD          cbFromNames,
  [in]  const BYTE           *pbFromNames,
  [in]        DWORD          cSignerCertificates,
  [in]        PCCERT_CONTEXT *rgSignerCertificates,
  [out]       IMimeMessage   **ppMimeMessageReceipt
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*cbFromNames* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of names in *pbFromNames*.

</dd> <dt>

*pbFromNames* \[in\]
</dt> <dd>

Type: **const BYTE\***

Specifies a pointer to a **BYTE** that contains the names of the receipt senders.

</dd> <dt>

*cSignerCertificates* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of certificates in *rgSignerCertificates*.

</dd> <dt>

*rgSignerCertificates* \[in\]
</dt> <dd>

Type: **PCCERT\_CONTEXT\***

Specifies the address of a pointer to a [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) that contains the certificates.

</dd> <dt>

*ppMimeMessageReceipt* \[out\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\*\***

Receives the address of a pointer to an [**IMimeMessage**](oe-imimemessage.md) object that is the receipt.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                   | Description                                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                        |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the sender of the receipt cannot be found. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





