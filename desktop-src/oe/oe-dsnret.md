---
title: DSNRET enumeration
description: Controls what is returned with a Delivery Status Notification (DSN).
ms.assetid: a7ddb9d1-4e6e-4924-9f7d-693c804ad5b7
keywords:
- DSNRET enumeration Windows Mail (formerly Outlook Express)
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

# DSNRET enumeration

\[**DSNRET** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Controls what is returned with a Delivery Status Notification (DSN).

## Syntax


```C++
typedef enum tagDSNRET { 
  DSNRET_DEFAULT  = 0,
  DSNRET_HDRS     = 1,
  DSNRET_FULL     = 2
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="DSNRET_DEFAULT"></span><span id="dsnret_default"></span>**DSNRET\_DEFAULT**
</dt> <dd>

Indicates that the transport should be the default value established by the SMTP server.

</dd> <dt>

<span id="DSNRET_HDRS"></span><span id="dsnret_hdrs"></span>**DSNRET\_HDRS**
</dt> <dd>

Indicates that only the headers should be returned for a message that has failed to reach its destination.

</dd> <dt>

<span id="DSNRET_FULL"></span><span id="dsnret_full"></span>**DSNRET\_FULL**
</dt> <dd>

Indicates that the full message (header and body) should be returned for a message that has failed to reach its destination.

</dd> </dl>

## Remarks

The value is passed to the RET parameter of the MAIL command.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





