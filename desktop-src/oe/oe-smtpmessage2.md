---
title: SMTPMESSAGE2 structure
description: Extends an SMTPMESSAGE structure to add Delivery Status Notification (DSN) (RFC 1891) support.
ms.assetid: 579fabcc-deff-4c50-bede-ce65d590bcf2
keywords:
- SMTPMESSAGE2 structure Windows Mail (formerly Outlook Express)
- LPSMTPMESSAGE2 structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SMTPMESSAGE2
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SMTPMESSAGE2 structure

\[**SMTPMESSAGE2** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Extends an [**SMTPMESSAGE**](oe-smtpmessage.md) structure to add Delivery Status Notification (DSN) ([RFC 1891](http://www.ietf.org/rfc/rfc1891.txt)) support.

## Syntax


```C++
typedef struct tagSMTPMESSAGE2 {
  SMTPMESSAGE smtpMsg;
  LPSTR       pszDSNENVID;
  DSNRET      dsnRet;
  DWORD       dwReserved;
  DWORD       dwReserved2;
} SMTPMESSAGE2, *LPSMTPMESSAGE2;
```



## Members

<dl> <dt>

**smtpMsg**
</dt> <dd>

Type: **[**SMTPMESSAGE**](oe-smtpmessage.md)**

</dd> <dd>

Contains the [**SMTPMESSAGE**](oe-smtpmessage.md) structure that contains the message.

</dd> <dt>

**pszDSNENVID**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the value for the envelope ID of the message so that the return message can be matched against the original message (the ENVID parameter of the MAIL command).

</dd> <dt>

**dsnRet**
</dt> <dd>

Type: **[**DSNRET**](oe-dsnret.md)**

</dd> <dd>

Contains a [**DSNRET**](oe-dsnret.md) value that indicates whether to return the full message or just the headers for a bounced message (the RET parameter of the MAIL command).

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> </dl>

## Remarks

To receive a DSN the Simple Mail Transport Protocol (SMTP) server must implement [RFC 1891](http://www.ietf.org/rfc/rfc1891.txt) and the SMTP transport must be initialized with an EHLO command.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





