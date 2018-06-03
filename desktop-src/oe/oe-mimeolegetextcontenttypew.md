---
title: MimeOleGetExtContentTypeW function
description: Do not use. Returns the Content-Type of the specified Unicode file name extension string.
ms.assetid: f8c75991-742b-4f8b-9eb8-ea8c89d1004b
keywords:
- MimeOleGetExtContentTypeW function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetExtContentTypeW
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleGetExtContentTypeW function

Do not use. Returns the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of the specified Unicode file name extension string.

## Syntax


```C++
HRESULT MimeOleGetExtContentTypeW(
  _In_  LPCWSTR pszExtension,
  _Out_ LPWSTR  *ppszContentType
);
```



## Parameters

<dl> <dt>

*pszExtension* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies an **LPCWSTR** that contains the file name extension. The file name extension must begin with a period (".").

</dd> <dt>

*ppszContentType* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that contains the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp). Note: *ppszContentType* must point to a valid **LPWSTR** before this function is called and user is responsible for freeing what this parameter points to.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                                                                     |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                                                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszExtension* or *ppszContentType* is **NULL** or that *pszExtension* does not begin with a period. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates an attempt to allocate memory failed. <br/>                                                                     |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that no proper file name extension was found. <br/>                                                             |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





