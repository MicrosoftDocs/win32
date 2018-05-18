---
title: POP3LIST structure
description: Contains the response data from the LIST command.
ms.assetid: 'ed54d97a-a0cf-424d-8447-94cf1a7ac981'
keywords: ["POP3LIST structure Windows Mail (formerly Outlook Express)", "LPPOP3LIST structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- POP3LIST
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# POP3LIST structure

\[**POP3LIST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response data from the LIST command.

## Syntax


```C++
typedef struct tagPOP3LIST {
  DWORD dwPopId;
  DWORD cbSize;
} POP3LIST, *LPPOP3LIST;
```



## Members

<dl> <dt>

**dwPopId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the message ID.

</dd> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that holds the size (in bytes) of the message on the server.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





