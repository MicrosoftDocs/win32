---
title: CHARSETTYPE enumeration
description: Do not use. Defines the types of character sets that are associated with a code page ID.
ms.assetid: cf8b6494-66f1-4fe5-811d-8abb7f3a3e9a
keywords:
- CHARSETTYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CHARSETTYPE enumeration

Do not use. Defines the types of character sets that are associated with a code page ID.

## Syntax


```C++
typedef enum tagCHARSETTYPE { 
  CHARSET_BODY    = 0,
  CHARSET_HEADER  = 1,
  CHARSET_WEB     = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CHARSET_BODY"></span><span id="charset_body"></span>**CHARSET\_BODY**
</dt> <dd>

Indicates the default code page character set for encoding message bodies. Corresponds to **szBodyCset**.

</dd> <dt>

<span id="CHARSET_HEADER"></span><span id="charset_header"></span>**CHARSET\_HEADER**
</dt> <dd>

Indicates the default code page character set for encoding message headers. Corresponds to **szHeaderCset**.

</dd> <dt>

<span id="CHARSET_WEB"></span><span id="charset_web"></span>**CHARSET\_WEB**
</dt> <dd>

Indicates the default code page character set for Web content. Corresponds to **szWebCset**.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





