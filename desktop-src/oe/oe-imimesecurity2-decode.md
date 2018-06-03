---
title: IMimeSecurity2 Decode method
description: Decodes the message body.
ms.assetid: 8a96f13e-aacc-457c-a310-86d3141bc254
keywords:
- Decode method Windows Mail (formerly Outlook Express)
- Decode method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , Decode method
topic_type:
- apiref
api_name:
- IMimeSecurity2.Decode
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

# IMimeSecurity2::Decode method

Decodes the message body.

## Syntax


```C++
HRESULT Decode(
  [in] HWND                  hwnd,
  [in] DWORD                 dwFlags,
  [in] IMimeSecurityCallback *pCallback
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
</dt> </dl> </dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**IMimeSecurityCallback**](oe-imimesecuritycallback.md)\***

Specifies a pointer to the [**IMimeSecurityCallback**](oe-imimesecuritycallback.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                            | Description                                                      |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Indicates success. <br/>                                   |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl> | Indicates that the message could not be decoded. <br/>     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | Indicates that *dwFlags* is invalid. <br/>                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





