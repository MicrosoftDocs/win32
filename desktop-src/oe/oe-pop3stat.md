---
title: POP3STAT structure
description: Contains the response data from the STAT command.
ms.assetid: ab594e58-d571-42b1-8b18-6018f9a206a5
keywords:
- POP3STAT structure Windows Mail (formerly Outlook Express)
- LPPOP3STAT structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- POP3STAT
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

# POP3STAT structure

\[**POP3STAT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response data from the STAT command.

## Syntax


```C++
typedef struct tagPOP3STAT {
  DWORD cMessages;
  DWORD cbMessages;
} POP3STAT, *LPPOP3STAT;
```



## Members

<dl> <dt>

**cMessages**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the number of messages on the server.

</dd> <dt>

**cbMessages**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the size (in bytes) of messages on the server.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





