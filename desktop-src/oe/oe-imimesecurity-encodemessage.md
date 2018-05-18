---
title: IMimeSecurity EncodeMessage method
description: Encodes the body of the specified IMimeMessageTree object using Secure/Multipurpose Internet Mail Extensions (S/MIME).
ms.assetid: '5ed8830f-9320-4932-ab81-f01f9be2ccc8'
keywords: ["EncodeMessage method Windows Mail (formerly Outlook Express)", "EncodeMessage method Windows Mail (formerly Outlook Express) , IMimeSecurity interface", "IMimeSecurity interface Windows Mail (formerly Outlook Express) , EncodeMessage method"]
topic_type:
- apiref
api_name:
- IMimeSecurity.EncodeMessage
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity::EncodeMessage method

Encodes the body of the specified [**IMimeMessageTree**](oe-imimemessagetree.md) object using Secure/Multipurpose Internet Mail Extensions (S/MIME).

## Syntax


```C++
HRESULT EncodeMessage(
  [in] IMimeMessageTree pTree,
  [in] DWORD            dwFlags
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

Specifies security encoding flags (SEF\_\*).

<dl> <dt>

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                          | Indicates that *pTree* is **NULL**. <br/>                                     |
| <dl> <dt>**MIME\_S\_SECURITY\_NOOP**</dt> </dl>                | Indicates that the body is not encoded. <br/>                                 |
| <dl> <dt>**MIME\_E\_SECURITY\_CLASSNOTSUPPORTED**</dt> </dl>   | Indicates that the message is an unsupported S/MIME class. <br/>              |
| <dl> <dt>**MIME\_E\_SECURITY\_NOCERT**</dt> </dl>              | Indicates that no certificates were found. <br/>                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                         | Indicates that an attempt to allocate memory failed. <br/>                    |
| <dl> <dt>**MIME\_E\_SECURITY\_ENCRYPTNOSENDERCERT**</dt> </dl> | Indicates that the body is already encoded with an unknown certificate. <br/> |



 

## Remarks

S/MIME is the version of MIME.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





