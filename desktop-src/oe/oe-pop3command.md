---
title: POP3COMMAND enumeration
description: Enumerates the Post Office Protocol version 3 (POP3) commands that have been issued to the server and the various states following an action.
ms.assetid: 3e775faa-d0bc-4a16-824d-5534e063bb03
keywords:
- POP3COMMAND enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# POP3COMMAND enumeration

\[**POP3COMMAND** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enumerates the Post Office Protocol version 3 (POP3) commands that have been issued to the server and the various states following an action.

## Syntax


```C++
typedef enum tagPOP3COMMAND { 
  POP3_NONE       = 0,
  POP3_BANNER     = 1,
  POP3_CONNECTED  = 2,
  POP3_USER       = 3,
  POP3_PASS       = 4,
  POP3_AUTH       = 5,
  POP3_UIDL       = 6,
  POP3_STAT       = 7,
  POP3_LIST       = 8,
  POP3_DELE       = 9,
  POP3_RETR       = 10,
  POP3_TOP        = 11,
  POP3_NOOP       = 12,
  POP3_QUIT       = 13,
  POP3_RSET       = 14,
  POP3_CUSTOM     = 15
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="POP3_NONE"></span><span id="pop3_none"></span>**POP3\_NONE**
</dt> <dd>

Indicates no current command.

</dd> <dt>

<span id="POP3_BANNER"></span><span id="pop3_banner"></span>**POP3\_BANNER**
</dt> <dd>

Indicates that a new server connection has been established and that the client has received the server's welcome banner. The POP3 transport is attempting to send either the AUTH or USER command to the server.

</dd> <dt>

<span id="POP3_CONNECTED"></span><span id="pop3_connected"></span>**POP3\_CONNECTED**
</dt> <dd>

Indicates that an authenticated connection has been established with the server.

</dd> <dt>

<span id="POP3_USER"></span><span id="pop3_user"></span>**POP3\_USER**
</dt> <dd>

Indicates that a USER command has been sent to the server and that, if successful, the POP3 transport is attempting to send the PASS command.

</dd> <dt>

<span id="POP3_PASS"></span><span id="pop3_pass"></span>**POP3\_PASS**
</dt> <dd>

Indicates that a PASS command has been sent to the server.

</dd> <dt>

<span id="POP3_AUTH"></span><span id="pop3_auth"></span>**POP3\_AUTH**
</dt> <dd>

Indicates that an AUTH command has been sent to the server.

</dd> <dt>

<span id="POP3_UIDL"></span><span id="pop3_uidl"></span>**POP3\_UIDL**
</dt> <dd>

Indicates that a UIDL command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_STAT"></span><span id="pop3_stat"></span>**POP3\_STAT**
</dt> <dd>

Indicates that a STAT command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_LIST"></span><span id="pop3_list"></span>**POP3\_LIST**
</dt> <dd>

Indicates that a LIST command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_DELE"></span><span id="pop3_dele"></span>**POP3\_DELE**
</dt> <dd>

Indicates that a DELE command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_RETR"></span><span id="pop3_retr"></span>**POP3\_RETR**
</dt> <dd>

Indicates that an RETR command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_TOP"></span><span id="pop3_top"></span>**POP3\_TOP**
</dt> <dd>

Indicates that a TOP command has been sent to the server and that, if successful, the POP3 transport is populating the [**POP3RESPONSE**](oe-pop3response.md) structure with response data.

</dd> <dt>

<span id="POP3_NOOP"></span><span id="pop3_noop"></span>**POP3\_NOOP**
</dt> <dd>

Indicates that an NOOP command has been sent to the server to help maintain the connection during a period of inactivity.

</dd> <dt>

<span id="POP3_QUIT"></span><span id="pop3_quit"></span>**POP3\_QUIT**
</dt> <dd>

Indicates that a QUIT command has been sent to the server and that the POP3 transport is closing the socket on the client.

</dd> <dt>

<span id="POP3_RSET"></span><span id="pop3_rset"></span>**POP3\_RSET**
</dt> <dd>

Indicates that an RSET command has been sent to the server to reset the state of the session.

</dd> <dt>

<span id="POP3_CUSTOM"></span><span id="pop3_custom"></span>**POP3\_CUSTOM**
</dt> <dd>

Indicates that a custom protocol command has been sent.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





