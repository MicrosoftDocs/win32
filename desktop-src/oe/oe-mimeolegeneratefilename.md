---
title: MimeOleGenerateFileName function
description: Do not use. On success, creates a file name.
ms.assetid: ce5c2843-de0e-4786-a813-d31ebdfaf741
keywords:
- MimeOleGenerateFileName function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGenerateFileName
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

# MimeOleGenerateFileName function

Do not use. On success, creates a file name.

## Syntax


```C++
HRESULT MimeOleGenerateFileName(
  _In_    LPCSTR pszContentType,
  _In_    LPCSTR pszSuggest,
  _In_    LPCSTR pszDefaultExt,
  _Inout_ LPSTR  *ppszFileName
);
```



## Parameters

<dl> <dt>

*pszContentType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the content type.

</dd> <dt>

*pszSuggest* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies suggested file name.

</dd> <dt>

*pszDefaultExt* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies default file name extension.

</dd> <dt>

*ppszFileName* \[in, out\]
</dt> <dd>

Type: **LPSTR\***

Specifies pointer to contain new file name.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/>    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates pointer parameter is **NULL**.<br/> |



 

## Remarks

> [!Note]  
> User responsible for freeing *ppszFileName*.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





