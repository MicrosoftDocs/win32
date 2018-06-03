---
title: MimeOleCombineURL function
description: Do not use. On success, combines base and relative URL.
ms.assetid: c6b87603-dade-4b18-a9e2-15ebab15ca0c
keywords:
- MimeOleCombineURL function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCombineURL
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

# MimeOleCombineURL function

Do not use. On success, combines base and relative URL.

## Syntax


```C++
HRESULT MimeOleCombineURL(
  _In_  LPCSTR pszBase,
  _In_  ULONG  cchBase,
  _In_  LPCSTR pszURL,
  _In_  ULONG  cchURL,
  _In_  BOOL   fUnEscape,
  _Out_ LPSTR  *ppszAbsolute
);
```



## Parameters

<dl> <dt>

*pszBase* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies base URL.

</dd> <dt>

*cchBase* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies length of *pszBase*.

</dd> <dt>

*pszURL* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies relative URL.

</dd> <dt>

*cchURL* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies length of *pszURL*.

</dd> <dt>

*fUnEscape* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies how to handle illegal characters within URL. See [**MimeOleUnEscapeStringInPlace**](oe-mimeoleunescapestringinplace.md).

</dd> <dt>

*ppszAbsolute* \[out\]
</dt> <dd>

Type: **LPSTR\***

Returns pointer to combined URL. Note: **LPSTR** needs to have been valid prior to call and user is responsible for freeing what is pointed to by this parameter.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that an incoming pointer parameter is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





