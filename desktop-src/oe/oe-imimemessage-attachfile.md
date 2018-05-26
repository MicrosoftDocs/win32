---
title: IMimeMessage AttachFile method
description: Attaches the contents of a file to the message.
ms.assetid: 6b663ace-e7a3-42a6-bf00-216f1c70c1a6
keywords:
- AttachFile method Windows Mail (formerly Outlook Express)
- AttachFile method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , AttachFile method
topic_type:
- apiref
api_name:
- IMimeMessage.AttachFile
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

# IMimeMessage::AttachFile method

Attaches the contents of a file to the message.

## Syntax


```C++
HRESULT AttachFile(
  [in]           LPCSTR  pszFilePath,
  [in, optional] IStream *pstmFile,
  [out]          LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*pszFilePath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the path and filename of the file to attach. When *pstmFile* is **NULL**, *pszFilePath* is used to indicate the file to attach. In this case, the file must exist and MimeOLE must have read access to it. Otherwise, *pszFilePath* is used only to indicate the filename of the attached file, which might not exist.

</dd> <dt>

*pstmFile* \[in, optional\]
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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszFilePath* is **NULL**.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/> |



 

## Remarks

This method creates the attachment in the multipart/mixed section of the message. If a multipart/mixed section does not exist, one is created.

Data in the object that *pszFilePath* points to must be stored in either [**IET\_BINARY**](oe-encodingtype.md) or **IET\_DECODED** type. For more information, see **ENCODINGTYPE**.

The method sets the PID\_HDR\_CNTTYPE property of the new attachment from the extension specified in *pszFilePath*.

This method sets the PID\_ATT\_FILENAME property of the new attachment and sets the PID\_HDR\_CNTDISP property to "attachment".

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





