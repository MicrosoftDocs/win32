---
title: IMimeMessageW AttachFileW method
description: Attaches the contents of a file to the message.
ms.assetid: 'c44e2816-093b-4af0-86de-2461ad1420ef'
keywords: ["AttachFileW method Windows Mail (formerly Outlook Express)", "AttachFileW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface", "IMimeMessageW interface Windows Mail (formerly Outlook Express) , AttachFileW method"]
topic_type:
- apiref
api_name:
- IMimeMessageW.AttachFileW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageW::AttachFileW method

Attaches the contents of a file to the message.

## Syntax


```C++
HRESULT AttachFileW(
  [in]  LPCWSTR pwszFilePath,
  [in]  IStream *pstmFile,
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*pwszFilePath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the path and filename of the file to attach. When *pstmFile* is **NULL**, *pwszFilePath* is used to indicate the file to attach, in which case the file must exist and MimeOLE must have read access to it. Otherwise, *pwszFilePath* is used only to indicate the filename of the attached file, which might not exist.

</dd> <dt>

*pstmFile* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object for the file to attach. MimeOLE increments the reference count for this object and does not release it until the whole message object is freed or until [**HandsOffStorage**](oe-imimemessagetree-handsoffstorage.md) is called.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pwszFilePath* is **NULL**.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





