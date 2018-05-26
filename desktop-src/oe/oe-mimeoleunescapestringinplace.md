---
title: MimeOleUnEscapeStringInPlace function
description: Do not use. Removes escape character (\\) from any backslash, quote, and parens characters in supplied zero-terminated string. Remaining characters move left in array.
ms.assetid: 32c375bf-8508-4f1c-aadd-8b74167c688d
keywords:
- MimeOleUnEscapeStringInPlace function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleUnEscapeStringInPlace
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

# MimeOleUnEscapeStringInPlace function

Do not use. Removes escape character ('\\') from any backslash, quote, and parens characters in supplied zero-terminated string. Remaining characters move left in array.

## Syntax


```C++
HRESULT MimeOleUnEscapeStringInPlace(
  _Inout_ LPSTR pszIn
);
```



## Parameters

<dl> <dt>

*pszIn* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Specifies string for operation.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that a pointer argument is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





