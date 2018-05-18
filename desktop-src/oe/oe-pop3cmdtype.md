---
title: POP3CMDTYPE enumeration
description: Indicates the type of messages to which a command is applied.
ms.assetid: '962b7385-d0a8-4ce3-995f-7470cec45739'
keywords: ["POP3CMDTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# POP3CMDTYPE enumeration

\[**POP3CMDTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the type of messages to which a command is applied.

## Syntax


```C++
typedef enum tagPOP3CMDTYPE { 
  POP3_NONE           = 0,
  POP3CMD_GET_POPID,
  POP3CMD_GET_MARKED,
  POP3CMD_GET_ALL
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="POP3_NONE"></span><span id="pop3_none"></span>**POP3\_NONE**
</dt> <dd>

Indicates no command type.

</dd> <dt>

<span id="POP3CMD_GET_POPID"></span><span id="pop3cmd_get_popid"></span>**POP3CMD\_GET\_POPID**
</dt> <dd>

Indicates that the command applies to a single specified message.

</dd> <dt>

<span id="POP3CMD_GET_MARKED"></span><span id="pop3cmd_get_marked"></span>**POP3CMD\_GET\_MARKED**
</dt> <dd>

Indicates that the command applies to all messages marked for that command.

</dd> <dt>

<span id="POP3CMD_GET_ALL"></span><span id="pop3cmd_get_all"></span>**POP3CMD\_GET\_ALL**
</dt> <dd>

Indicates that the command applies to all messages.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





