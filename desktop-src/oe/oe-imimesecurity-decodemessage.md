---
title: IMimeSecurity DecodeMessage method
description: Decodes the body of the specified IMimeMessageTree object using Secure/Multipurpose Internet Mail Extensions (S/MIME).
ms.assetid: 18c9f682-9009-412c-b7a7-96f3281a976a
keywords:
- DecodeMessage method Windows Mail (formerly Outlook Express)
- DecodeMessage method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , DecodeMessage method
topic_type:
- apiref
api_name:
- IMimeSecurity.DecodeMessage
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

# IMimeSecurity::DecodeMessage method

Decodes the body of the specified [**IMimeMessageTree**](oe-imimemessagetree.md) object using Secure/Multipurpose Internet Mail Extensions (S/MIME).

## Syntax


```C++
HRESULT DecodeMessage(
  [in] IMimeMessageTree pTree,
  [in] DWORD            dwFlags
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)**

Specifies a pointer to an [**IMimeMessageTree**](oe-imimemessagetree.md) object.

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | Indicates that *pTree* is **NULL**. <br/>                  |
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



 

 





