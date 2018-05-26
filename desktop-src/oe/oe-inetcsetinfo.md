---
title: INETCSETINFO structure
description: Do not use. Holds information about a character set. A client can use an IMimeInternational object to look up an INETCSETINFO for an HCHARSET.
ms.assetid: b486fb9c-e551-4833-8c01-a7a0565dd074
keywords:
- INETCSETINFO structure Windows Mail (formerly Outlook Express)
- LPINETCSETINFO structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- INETCSETINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INETCSETINFO structure

Do not use. Holds information about a character set. A client can use an [**IMimeInternational**](oe-imimeinternational.md) object to look up an **INETCSETINFO** for an HCHARSET.

## Syntax


```C++
typedef struct tagINETCSETINFO {
  CHAR       szName[CCHMAX_CSET_NAME];
  HCHARSET   hCharset;
  CODEPAGEID cpiWindows;
  CODEPAGEID cpiInternet;
  DWORD      dwReserved1;
} INETCSETINFO, *LPINETCSETINFO;
```



## Members

<dl> <dt>

**szName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CSET\_NAME\]**

</dd> <dd>

Contains the character set name.

</dd> <dt>

**hCharset**
</dt> <dd>

Type: **HCHARSET**

</dd> <dd>

Contains the handle to this character set.

</dd> <dt>

**cpiWindows**
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

</dd> <dd>

Contains the Windows code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

**cpiInternet**
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

</dd> <dd>

Contains the Internet code page. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

**dwReserved1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





