---
title: MimeOleGetCodePageCharset function
description: Do no use. Finds a character set for the specified code page.
ms.assetid: f4963e17-1311-4944-b6ab-cb6d7610cd14
keywords:
- MimeOleGetCodePageCharset function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetCodePageCharset
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

# MimeOleGetCodePageCharset function

Do no use. Finds a character set for the specified code page.

## Syntax


```C++
HRESULT MimeOleGetCodePageCharset(
  _In_  CODEPAGEID  cpiCodePage,
  _In_  CHARSETTYPE ctCsetType,
  _Out_ LPHCHARSET  phCharset
);
```



## Parameters

<dl> <dt>

*cpiCodePage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*ctCsetType* \[in\]
</dt> <dd>

Type: **[**CHARSETTYPE**](oe-charsettype.md)**

Specifies a value from [**CHARSETTYPE**](oe-charsettype.md) that indicates the type of character set.

</dd> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | Indicates success.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | Indicates that *phCharset* is **NULL**. <br/>                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                  | Indicates that an attempt to allocate memory failed.<br/>         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                         | Indicates that there is no default character set.<br/>            |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>             | Indicates that *cpiCodePage* is invalid or cannot be found. <br/> |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>               | Indicates that no data is associated with the character set.<br/> |
| <dl> <dt>**MIME\_E\_INVALID\_CHARSET\_TYPE**</dt> </dl> | Indicates that *ctCsetType* is invalid. <br/>                     |



 

## Remarks

There are three different character set types for every code page, each type having a different purpose. [**CHARSETTYPE**](oe-charsettype.md) enumerates these character set types.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





