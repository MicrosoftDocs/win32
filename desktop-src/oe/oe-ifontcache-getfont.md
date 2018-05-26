---
title: IFontCache GetFont method
description: Gets a specified system font.
ms.assetid: 02268689-ed51-4966-908c-25a258062de6
keywords:
- GetFont method Windows Mail (formerly Outlook Express)
- GetFont method Windows Mail (formerly Outlook Express) , IFontCache interface
- IFontCache interface Windows Mail (formerly Outlook Express) , GetFont method
topic_type:
- apiref
api_name:
- IFontCache.GetFont
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IFontCache::GetFont method

\[**IFontCache::GetFont** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets a specified system font.

## Syntax


```C++
HRESULT GetFont(
  [in]  FNTSYSTYPE fntType,
  [in]  HCHARSET   hCharset,
  [out] HFONT      *phFont
);
```



## Parameters

<dl> <dt>

*fntType* \[in\]
</dt> <dd>

Type: **[**FNTSYSTYPE**](oe-fntsystype.md)**

Specifies a system font type.

</dd> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies a handle to a character set.

</dd> <dt>

*phFont* \[out\]
</dt> <dd>

Type: **HFONT\***

Specifies a handle to a font.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                           |
|----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Handle to font is valid. <br/>  |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Handle to font not valid. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





