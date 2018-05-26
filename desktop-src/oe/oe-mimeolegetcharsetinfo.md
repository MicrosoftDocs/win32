---
title: MimeOleGetCharsetInfo function
description: Do not use. Gets information about the specified character set.
ms.assetid: 13849d42-609e-4ef0-845e-fe0cacdbc73d
keywords:
- MimeOleGetCharsetInfo function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetCharsetInfo
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleGetCharsetInfo function

Do not use. Gets information about the specified character set.

## Syntax


```C++
HRESULT MimeOleGetCharsetInfo(
  _In_  HCHARSET       hCharset,
  _Out_ LPINETCSETINFO pCsetInfo
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set.

</dd> <dt>

*pCsetInfo* \[out\]
</dt> <dd>

Type: **LPINETCSETINFO**

Receives a pointer to an [**INETCSETINFO**](oe-inetcsetinfo.md) structure that contains information about the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                      |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hCharset* or *pCsetInfo* is **NULL**.<br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/>      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





