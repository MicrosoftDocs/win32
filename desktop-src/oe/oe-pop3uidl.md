---
title: POP3UIDL structure
description: Contains the response data from the UIDL command.
ms.assetid: 75c9c0e4-fb5f-48c0-af04-c4a7e598bc7a
keywords:
- POP3UIDL structure Windows Mail (formerly Outlook Express)
- LPPOP3UIDL structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- POP3UIDL
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# POP3UIDL structure

\[**POP3UIDL** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response data from the UIDL command.

## Syntax


```C++
typedef struct tagPOP3UIDL {
  DWORD dwPopId;
  LPSTR pszUidl;
} POP3UIDL, *LPPOP3UIDL;
```



## Members

<dl> <dt>

**dwPopId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the message ID.

</dd> <dt>

**pszUidl**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that holds the returned Unique ID Listing (UIDL).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





