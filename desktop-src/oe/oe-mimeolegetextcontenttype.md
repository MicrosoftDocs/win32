---
title: MimeOleGetExtContentType function
description: Do not use. Returns the Content-Type of the specified file name extension.
ms.assetid: 'f3bf66d9-c111-4884-a0ea-0356963ac8ea'
keywords: ["MimeOleGetExtContentType function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleGetExtContentType
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleGetExtContentType function

Do not use. Returns the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of the specified file name extension.

## Syntax


```C++
HRESULT MimeOleGetExtContentType(
  _In_  LPCSTR pszExtension,
  _Out_ LPSTR  *ppszContentType
);
```



## Parameters

<dl> <dt>

*pszExtension* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the file name extension. The file name extension must begin with a period (".").

</dd> <dt>

*ppszContentType* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp). Note: *ppszContentType* must point to a valid **LPSTR** before this function is called and user is responsible for freeing what this parameter points to.

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**MimeOleGetExtContentTypeW**](oe-mimeolegetextcontenttypew.md)
</dt> </dl>

 

 





