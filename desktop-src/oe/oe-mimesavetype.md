---
title: MIMESAVETYPE enumeration
description: Do not use. Indicates how an object should be persisted.
ms.assetid: f21fdcdb-2d1a-44da-92be-9d5d66c3e9c3
keywords:
- MIMESAVETYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MIMESAVETYPE enumeration

Do not use. Indicates how an object should be persisted.

## Syntax


```C++
typedef enum tagMIMESAVETYPE { 
  SAVE_RFC822   = 0,
  SAVE_RFC1521  = 1
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SAVE_RFC822"></span><span id="save_rfc822"></span>**SAVE\_RFC822**
</dt> <dd>

Indicates that the object should be saved in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) format.

</dd> <dt>

<span id="SAVE_RFC1521"></span><span id="save_rfc1521"></span>**SAVE\_RFC1521**
</dt> <dd>

Indicates that the object should be saved in [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) (MIME) format.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





