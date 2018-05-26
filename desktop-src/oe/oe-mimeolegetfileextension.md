---
title: MimeOleGetFileExtension function
description: Do not use. Gets the file name extension for the specified file.
ms.assetid: 62d651cc-2651-47db-8b8e-937e6bfeb470
keywords:
- MimeOleGetFileExtension function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetFileExtension
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

# MimeOleGetFileExtension function

Do not use. Gets the file name extension for the specified file.

## Syntax


```C++
HRESULT MimeOleGetFileExtension(
  _In_    LPCSTR pszFilePath,
  _Inout_ LPSTR  pszExt,
  _In_    ULONG  cchMax
);
```



## Parameters

<dl> <dt>

*pszFilePath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the file path.

</dd> <dt>

*pszExt* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Receives an **LPSTR** that contains the file name extension.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the largest allowable size for *pszExt*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                  |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszFilePath* or *pszExt* is **NULL** or that *cchMax* is larger than the maximum allowable size. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





