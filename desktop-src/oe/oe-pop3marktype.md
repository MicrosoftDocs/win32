---
title: POP3MARKTYPE enumeration
description: Indicates the command to use on a message during a Post Office Protocol version 3 (POP3) transaction.
ms.assetid: 'a636b7a8-8274-4569-b048-72ae6173affd'
keywords: ["POP3MARKTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# POP3MARKTYPE enumeration

\[**POP3MARKTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the command to use on a message during a Post Office Protocol version 3 (POP3) transaction.

## Syntax


```C++
typedef enum tagPOP3MARKTYPE { 
  POP3_MARK_FOR_TOP   = 0x00000001,
  POP3_MARK_FOR_RETR  = 0x00000002,
  POP3_MARK_FOR_DELE  = 0x00000004,
  POP3_MARK_FOR_UIDL  = 0x00000008,
  POP3_MARK_FOR_LIST  = 0x00000010
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="POP3_MARK_FOR_TOP"></span><span id="pop3_mark_for_top"></span>**POP3\_MARK\_FOR\_TOP**
</dt> <dd>

Indicates that the message is marked to use the TOP command during the transaction.

</dd> <dt>

<span id="POP3_MARK_FOR_RETR"></span><span id="pop3_mark_for_retr"></span>**POP3\_MARK\_FOR\_RETR**
</dt> <dd>

Indicates that the message is marked to use the RETR command during the transaction.

</dd> <dt>

<span id="POP3_MARK_FOR_DELE"></span><span id="pop3_mark_for_dele"></span>**POP3\_MARK\_FOR\_DELE**
</dt> <dd>

Indicates that the message is marked to use the DELE command during the transaction.

</dd> <dt>

<span id="POP3_MARK_FOR_UIDL"></span><span id="pop3_mark_for_uidl"></span>**POP3\_MARK\_FOR\_UIDL**
</dt> <dd>

Indicates that the message is marked to use the UIDL command during the transaction.

</dd> <dt>

<span id="POP3_MARK_FOR_LIST"></span><span id="pop3_mark_for_list"></span>**POP3\_MARK\_FOR\_LIST**
</dt> <dd>

Indicates that the message is marked to use the LIST command during the transaction.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





