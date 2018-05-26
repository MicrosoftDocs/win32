---
title: MimeOleQueryString function
description: Do not use. Queries a specified string for a qualified match.
ms.assetid: ce7774bb-1611-4291-ab4e-33d4b73fe069
keywords:
- MimeOleQueryString function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleQueryString
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

# MimeOleQueryString function

Do not use. Queries a specified string for a qualified match.

## Syntax


```C++
HRESULT MimeOleQueryString(
  _In_ LPCSTR  pszSearchMe,
  _In_ LPCSTR  pszCriteria,
  _In_ boolean fSubString,
  _In_ boolean fCaseSensitive
);
```



## Parameters

<dl> <dt>

*pszSearchMe* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the string to be queried.

</dd> <dt>

*pszCriteria* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the string to be compared to.

</dd> <dt>

*fSubString* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether *pszCriteria* is a sub-string of *pszSearchMe*.

</dd> <dt>

*fCaseSensitive* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether query is case sensitive.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                           |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates match found.<br/>     |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates match not found.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





