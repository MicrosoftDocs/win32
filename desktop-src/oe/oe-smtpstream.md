---
title: SMTPSTREAM structure
description: Contains information about the Simple Mail Transport Protocol (SMTP) stream.
ms.assetid: 07d67bbb-e88c-4812-80ef-167fb1c75167
keywords:
- SMTPSTREAM structure Windows Mail (formerly Outlook Express)
- LPSMTPSTREAM structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SMTPSTREAM
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

# SMTPSTREAM structure

\[**SMTPSTREAM** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains information about the Simple Mail Transport Protocol (SMTP) stream.

## Syntax


```C++
typedef struct tagSMTPSTREAM {
  DWORD cbIncrement;
  DWORD cbCurrent;
  DWORD cbTotal;
} SMTPSTREAM, *LPSMTPSTREAM;
```



## Members

<dl> <dt>

**cbIncrement**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the size in bytes of the stream sent since the last [**OnResponse**](oe-ismtpcallback-onresponse.md) call.

</dd> <dt>

**cbCurrent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the total number of bytes sent at the time of the [**OnResponse**](oe-ismtpcallback-onresponse.md) call.

</dd> <dt>

**cbTotal**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the total size in bytes of the message being streamed.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





