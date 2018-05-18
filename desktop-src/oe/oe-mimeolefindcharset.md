---
title: MimeOleFindCharset function
description: Do not use. On success, finds handle of specified character set.
ms.assetid: '2d40b9d6-eca9-4632-931d-89ff14cfd437'
keywords: ["MimeOleFindCharset function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleFindCharset
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleFindCharset function

Do not use. On success, finds handle of specified character set.

## Syntax


```C++
HRESULT MimeOleFindCharset(
  _In_  LPCSTR     pszCharset,
  _Out_ LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*pszCharset* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **null**-terminated string containing the desired character set.

</dd> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Returns a handle to the specified character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that pointer argument is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





