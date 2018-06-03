---
title: IMimeSecurity DecodeBody method
description: Decodes the specified message body using Secure/Multipurpose Internet Mail Extensions (S/MIME).
ms.assetid: 84410eb4-0f01-4889-8669-f8bfe580854d
keywords:
- DecodeBody method Windows Mail (formerly Outlook Express)
- DecodeBody method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , DecodeBody method
topic_type:
- apiref
api_name:
- IMimeSecurity.DecodeBody
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

# IMimeSecurity::DecodeBody method

Decodes the specified message body using Secure/Multipurpose Internet Mail Extensions (S/MIME).

## Syntax


```C++
HRESULT DecodeBody(
  [in] IMimeMessageTree pTree,
  [in] HBODY            hDecodeRoot,
  [in] DWORD            dwFlags
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)**

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object containing the body to decode.

</dd> <dt>

*hDecodeRoot* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body to decode.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                            | Description                                                      |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | Indicates that *pTree* or *hDecodeRoot* is **NULL**. <br/> |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl> | Indicates that the body is not encoded. <br/>              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | Indicates that an attempt to allocate memory failed. <br/> |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>         | Indicates that there is a decoding error. <br/>            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





