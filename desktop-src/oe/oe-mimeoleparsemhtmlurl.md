---
title: MimeOleParseMhtmlUrl function
description: Do not use. On success, supplied MHTML URL is parsed into root and body.
ms.assetid: 9e4e81c7-c6ae-4a48-8d6e-280879f1903d
keywords:
- MimeOleParseMhtmlUrl function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleParseMhtmlUrl
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

# MimeOleParseMhtmlUrl function

Do not use. On success, supplied MHTML URL is parsed into root and body.

## Syntax


```C++
HRESULT MimeOleParseMhtmlUrl(
  _In_  LPSTR pszUrl,
  _Out_ LPSTR *ppszRootUrl,
  _Out_ LPSTR *ppszBodyUrl
);
```



## Parameters

<dl> <dt>

*pszUrl* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies supplied URL.

</dd> <dt>

*ppszRootUrl* \[out\]
</dt> <dd>

Type: **LPSTR\***

Returns pointer to root portion.

</dd> <dt>

*ppszBodyUrl* \[out\]
</dt> <dd>

Type: **LPSTR\***

Returns pointer to body portion.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that *pszUrl* does not start with "mhtml:". <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszUrl* is **NULL**. <br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that allocation failed. <br/>                     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





