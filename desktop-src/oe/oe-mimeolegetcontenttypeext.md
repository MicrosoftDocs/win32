---
title: MimeOleGetContentTypeExt function
description: Do not use. Returns the file name extension for a supplied content type.
ms.assetid: 8d70fb50-6fc5-4a0c-8c1c-7f3447c41b06
keywords:
- MimeOleGetContentTypeExt function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetContentTypeExt
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

# MimeOleGetContentTypeExt function

Do not use. Returns the file name extension for a supplied content type.

## Syntax


```C++
HRESULT MimeOleGetContentTypeExt(
  _In_  LPCSTR pszContentType,
  _Out_ LPSTR  *ppszExtension
);
```



## Parameters

<dl> <dt>

*pszContentType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a content type.

</dd> <dt>

*ppszExtension* \[out\]
</dt> <dd>

Type: **LPSTR\***

Returns pointer to string containing extension. Note: *ppszExtension* must point to a valid **LPSTR** before this function is called and user is responsible for freeing what this parameter points to.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                              |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates pointer parameter is **NULL**.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates allocation failed.<br/>                  |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates content type not found in registry.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





