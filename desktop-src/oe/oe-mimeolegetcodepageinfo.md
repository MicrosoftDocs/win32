---
title: MimeOleGetCodePageInfo function
description: Do not use. Returns a specified CODEPAGEINFO struct.
ms.assetid: '406ea1e5-56e9-47db-a63d-f7b8de9dea19'
keywords: ["MimeOleGetCodePageInfo function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleGetCodePageInfo
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleGetCodePageInfo function

Do not use. Returns a specified CODEPAGEINFO struct.

## Syntax


```C++
HRESULT MimeOleGetCodePageInfo(
  _In_  CODEPAGEID     cpiCodePage,
  _Out_ LPCODEPAGEINFO pCodePageInfo
);
```



## Parameters

<dl> <dt>

*cpiCodePage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies a code page. See [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pCodePageInfo* \[out\]
</dt> <dd>

Type: **LPCODEPAGEINFO**

Returns a pointer to a [**CODEPAGEINFO**](oe-codepageinfo.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                             |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pCodePageInfo* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





