---
title: SMTPCOMMAND enumeration
description: Enumerates the Simple Mail Transport Protocol (SMTP) commands that have been issued to the server and the various states following an action.
ms.assetid: 45ba9535-86c8-4647-a42b-2f99b16bbb51
keywords:
- SMTPCOMMAND enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMTPCOMMAND enumeration

\[**SMTPCOMMAND** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enumerates the Simple Mail Transport Protocol (SMTP) commands that have been issued to the server and the various states following an action.

## Syntax


```C++
typedef enum tagSMTPCOMMAND { 
  SMTP_NONE          = 0,
  SMTP_BANNER        = 1,
  SMTP_CONNECTED     = 2,
  SMTP_SEND_MESSAGE  = 3,
  SMTP_AUTH          = 4,
  SMTP_EHLO          = 5,
  SMTP_HELO          = 6,
  SMTP_MAIL          = 7,
  SMTP_RCPT          = 8,
  SMTP_RSET          = 9,
  SMTP_QUIT          = 10,
  SMTP_DATA          = 11,
  SMTP_DOT           = 12,
  SMTP_SEND_STREAM   = 13,
  SMTP_CUSTOM        = 14
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SMTP_NONE"></span><span id="smtp_none"></span>**SMTP\_NONE**
</dt> <dd>

Indicates no current command.

</dd> <dt>

<span id="SMTP_BANNER"></span><span id="smtp_banner"></span>**SMTP\_BANNER**
</dt> <dd>

Indicates that a new server connection has been established and that the client has received the server's welcome banner. The SMTP transport is attempting to send either the HELO or EHLO command to the server.

</dd> <dt>

<span id="SMTP_CONNECTED"></span><span id="smtp_connected"></span>**SMTP\_CONNECTED**
</dt> <dd>

Indicates that an authenticated connection has been established with the server.

</dd> <dt>

<span id="SMTP_SEND_MESSAGE"></span><span id="smtp_send_message"></span>**SMTP\_SEND\_MESSAGE**
</dt> <dd>

Indicates that the SMTP transport has finished sending the message.

</dd> <dt>

<span id="SMTP_AUTH"></span><span id="smtp_auth"></span>**SMTP\_AUTH**
</dt> <dd>

Indicates that an AUTH command has been sent to the server.

</dd> <dt>

<span id="SMTP_EHLO"></span><span id="smtp_ehlo"></span>**SMTP\_EHLO**
</dt> <dd>

Indicates that an EHLO command has been sent to the server and that the SMTP transport is attempting to authenticate the connection.

</dd> <dt>

<span id="SMTP_HELO"></span><span id="smtp_helo"></span>**SMTP\_HELO**
</dt> <dd>

Indicates that a HELO command has been sent to the server and that the SMTP transport is attempting to authenticate the connection.

</dd> <dt>

<span id="SMTP_MAIL"></span><span id="smtp_mail"></span>**SMTP\_MAIL**
</dt> <dd>

Indicates that a MAIL FROM: command has been sent to the server and that the SMTP transport is attempting to send the message.

</dd> <dt>

<span id="SMTP_RCPT"></span><span id="smtp_rcpt"></span>**SMTP\_RCPT**
</dt> <dd>

Indicates that a RCPT TO: command has been sent to the server and that the SMTP transport is attempting to send the message to the next recipient.

</dd> <dt>

<span id="SMTP_RSET"></span><span id="smtp_rset"></span>**SMTP\_RSET**
</dt> <dd>

Indicates that a RSET command has been sent to the server. If a message was interrupted, the SMTP transport may try to resend.

</dd> <dt>

<span id="SMTP_QUIT"></span><span id="smtp_quit"></span>**SMTP\_QUIT**
</dt> <dd>

Indicates that a QUIT command has been sent to the server and that the SMTP transport is closing the socket on the client.

</dd> <dt>

<span id="SMTP_DATA"></span><span id="smtp_data"></span>**SMTP\_DATA**
</dt> <dd>

Indicates that a DATA command has been sent to the server and that the SMTP transport is attempting to send the message stream.

</dd> <dt>

<span id="SMTP_DOT"></span><span id="smtp_dot"></span>**SMTP\_DOT**
</dt> <dd>

Indicates that a DOT command has been sent to the server and that the SMTP transport is cleaning up (for example, it releases the message object) and sets the current command to **SMTP\_SEND\_MESSAGE**.

</dd> <dt>

<span id="SMTP_SEND_STREAM"></span><span id="smtp_send_stream"></span>**SMTP\_SEND\_STREAM**
</dt> <dd>

Indicates that the SMTP transport has finished sending the message stream.

</dd> <dt>

<span id="SMTP_CUSTOM"></span><span id="smtp_custom"></span>**SMTP\_CUSTOM**
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



 

 





