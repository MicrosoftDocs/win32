---
title: IMimeSecurity2 Encode method
description: Encodes the message body.
ms.assetid: 0f3ee226-42a8-4392-8b6a-324cb857c066
keywords:
- Encode method Windows Mail (formerly Outlook Express)
- Encode method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , Encode method
topic_type:
- apiref
api_name:
- IMimeSecurity2.Encode
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeSecurity2::Encode method

Encodes the message body.

## Syntax


```C++
HRESULT Encode(
  [in] HWND  hwnd,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Specifies the handle of the parent window.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a set of security encoding flags (SEF\_\*).

<dl> <dt>

<span id="SEF_ENCRYPTWITHNOSENDERCERT"></span><span id="sef_encryptwithnosendercert"></span>**SEF\_ENCRYPTWITHNOSENDERCERT** (0x00000001)
</dt> <dt>

<span id="SEF_SENDERSCERTPROVIDED"></span><span id="sef_senderscertprovided"></span>**SEF\_SENDERSCERTPROVIDED** (0x00000002)
</dt> <dt>

<span id="SEF_NOUI"></span><span id="sef_noui"></span>**SEF\_NOUI** (0x00000004)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                           | Description                                                                   |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                  | Indicates success. <br/>                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                | Indicates that an unknown error has occurred. <br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                          | Indicates that *dwFlags* is invalid. <br/>                              |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl>                | Indicates that the body is plain text. <br/>                            |
| <dl> <dt>**MIME\_E\_SECURITY\_NOCERT**</dt> </dl>              | Indicates that no certificates were found. <br/>                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                         | Indicates that an attempt to allocate memory failed. <br/>              |
| <dl> <dt>**MIME\_E\_SECURITY\_ENCRYPTNOSENDERCERT**</dt> </dl> | Indicates that a problem with the certificate prevented encoding. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





