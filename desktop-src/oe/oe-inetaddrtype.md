---
title: INETADDRTYPE enumeration
description: Indicates the type of address and Delivery Status Notification (DSN) request.
ms.assetid: 'cc379a8a-6013-46ad-b2fc-6c612b988d89'
keywords: ["INETADDRTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# INETADDRTYPE enumeration

\[**INETADDRTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the type of address and Delivery Status Notification (DSN) request.

## Syntax


```C++
typedef enum tagINETADDRTYPE { 
  ADDR_TO           = 0,
  ADDR_FROM         = 1,
  ADDR_DSN_NEVER    = 16,
  ADDR_DSN_SUCCESS  = 32,
  ADDR_DSN_FAILURE  = 64,
  ADDR_DSN_DELAY    = 128
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="ADDR_TO"></span><span id="addr_to"></span>**ADDR\_TO**
</dt> <dd>

Indicates the recipient of the message (To, CC, Bcc).

</dd> <dt>

<span id="ADDR_FROM"></span><span id="addr_from"></span>**ADDR\_FROM**
</dt> <dd>

Indicates the sender of the message.

</dd> <dt>

<span id="ADDR_DSN_NEVER"></span><span id="addr_dsn_never"></span>**ADDR\_DSN\_NEVER**
</dt> <dd>

Indicates that all DSN should be suppressed.

</dd> <dt>

<span id="ADDR_DSN_SUCCESS"></span><span id="addr_dsn_success"></span>**ADDR\_DSN\_SUCCESS**
</dt> <dd>

Indicates a request for a DSN on successful delivery.

</dd> <dt>

<span id="ADDR_DSN_FAILURE"></span><span id="addr_dsn_failure"></span>**ADDR\_DSN\_FAILURE**
</dt> <dd>

Indicates a request for a DSN on delivery failure.

</dd> <dt>

<span id="ADDR_DSN_DELAY"></span><span id="addr_dsn_delay"></span>**ADDR\_DSN\_DELAY**
</dt> <dd>

Indicates a request for a DSN if delivery is delayed.

</dd> </dl>

## Remarks

The Simple Mail Transport Protocol (SMTP) protocol distinguishes only between a sender (**ADDR\_FROM**) and recipients (**ADDR\_TO**). A DSN request can made by including the additional DSN flags only if the SMTP server supports DSN ([RFC 1891](http://www.ietf.org/rfc/rfc1891.txt)) and the transport connected with an EHLO command.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





