---
title: IMimeSecurity EncodeBody method
description: Encodes the specified message body using Secure/Multipurpose Internet Mail Extensions (S/MIME).
ms.assetid: f6cfcdd6-ea65-4173-a381-9c8a0a0531db
keywords:
- EncodeBody method Windows Mail (formerly Outlook Express)
- EncodeBody method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , EncodeBody method
topic_type:
- apiref
api_name:
- IMimeSecurity.EncodeBody
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

# IMimeSecurity::EncodeBody method

Encodes the specified message body using Secure/Multipurpose Internet Mail Extensions (S/MIME).

## Syntax


```C++
HRESULT EncodeBody(
  [in] IMimeMessageTree pTree,
  [in] HBODY            hEncodeRoot,
  [in] DWORD            dwFlags
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)**

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object that contains the body to encode.

</dd> <dt>

*hEncodeRoot* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body to encode.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a set of encode body flags (EBF\_\*) or security encoding flags (SEF\_\*). Do not overlap EBF\_\* and SEF\_\* flags.

<dl> <dt>

<span id="EBF_RECURSE"></span><span id="ebf_recurse"></span>**EBF\_RECURSE** (0x00010000)
</dt> <dt>

<span id="EBF_COMMITIFDIRTY"></span><span id="ebf_commitifdirty"></span>**EBF\_COMMITIFDIRTY** (0x00020000)
</dt> <dt>

<span id="EBF_MASK"></span><span id="ebf_mask"></span>**EBF\_MASK** (0xffff0000)
</dt> <dt>

<span id="SEF_ENCRYPTWITHNOSENDERCERT"></span><span id="sef_encryptwithnosendercert"></span>**SEF\_ENCRYPTWITHNOSENDERCERT** (0x00000001)
</dt> <dt>

<span id="SEF_SENDERSCERTPROVIDED"></span><span id="sef_senderscertprovided"></span>**SEF\_SENDERSCERTPROVIDED** (0x00000002)
</dt> <dt>

<span id="SEF_NOUI"></span><span id="sef_noui"></span>**SEF\_NOUI** (0x00000004)
</dt> <dt>

<span id="SEF_MASK"></span><span id="sef_mask"></span>**SEF\_MASK** (0x0000ffff)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                           | Description                                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                  | Indicates success. <br/>                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                | Indicates that an unknown error has occurred. <br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                          | Indicates that *pTree* or *hEncodeRoot* is **NULL**. <br/>                    |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl>                | Indicates that the body is not encoded. <br/>                                 |
| <dl> <dt>**MIME\_E\_SECURITY\_CLASSNOTSUPPORTED**</dt> </dl>   | Indicates that the message is an unsupported S/MIME class. <br/>              |
| <dl> <dt>**MIME\_E\_SECURITY\_NOCERT**</dt> </dl>              | Indicates that no certificates were found. <br/>                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                         | Indicates that an attempt to allocate memory failed. <br/>                    |
| <dl> <dt>**MIME\_E\_SECURITY\_ENCRYPTNOSENDERCERT**</dt> </dl> | Indicates that the body is already encoded with an unknown certificate. <br/> |



 

## Remarks

S/MIME is the secure version of MIME.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





