---
title: MimeOleEscapeString function
description: Do not use. Adds escape character (\\) to otherwise-invalid characters, such as backslash, quote and parens, in supplied zero-terminated string.
ms.assetid: 1cc3e6d5-5dff-4e30-a60f-c8bbac06309a
keywords:
- MimeOleEscapeString function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleEscapeString
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

# MimeOleEscapeString function

Do not use. Adds escape character ('\\') to otherwise-invalid characters, such as backslash, quote and parens, in supplied zero-terminated string.

## Syntax


```C++
HRESULT MimeOleEscapeString(
  _In_  CODEPAGEID cpiCodePage,
  _In_  LPCSTR     pszIn,
  _Out_ LPSTR      *ppszOut
);
```



## Parameters

<dl> <dt>

*cpiCodePage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies a code page. See [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pszIn* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the target string.

</dd> <dt>

*ppszOut* \[out\]
</dt> <dd>

Type: **LPSTR\***

On success, returns a pointer to the escaped string.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates *ppszOut* was allocated and set to the escaped string. <br/>    |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates *ppszOut* is **NULL** - *pszIn* did not require escaping. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





