---
title: SMTPRESPONSE structure
description: Contains information about a Simple Mail Transport Protocol (SMTP) response.
ms.assetid: 9a106233-dd5d-4f52-8c8b-28dfefe2a9c8
keywords:
- SMTPRESPONSE structure Windows Mail (formerly Outlook Express)
- LPSMTPRESPONSE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SMTPRESPONSE
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

# SMTPRESPONSE structure

\[**SMTPRESPONSE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains information about a Simple Mail Transport Protocol (SMTP) response.

## Syntax


```C++
typedef struct tagSMTPRESPONSE {
  SMTPCOMMAND    command;
  BOOL           fDone;
  IXPRESULT      rIxpResult;
  ISMTPTransport *pTransport;
  SMTPSTREAM     rStreamInfo;
} SMTPRESPONSE, *LPSMTPRESPONSE;
```



## Members

<dl> <dt>

**command**
</dt> <dd>

Type: **[**SMTPCOMMAND**](oe-smtpcommand.md)**

</dd> <dd>

Contains the [**SMTPCOMMAND**](oe-smtpcommand.md) for which the response was generated.

</dd> <dt>

**fDone**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the command finished. The client should wait until this member is True before issuing another SMTP command through the [**ISMTPTransport**](oe-ismtptransport.md) object.

</dd> <dt>

**rIxpResult**
</dt> <dd>

Type: **[**IXPRESULT**](oe-ixpresult.md)**

</dd> <dd>

Contains an [**IXPRESULT**](oe-ixpresult.md) structure that contains the information about the server response. If **rIxpResult**.**hrResult** specifies a FAILED result, the structure contains other information.

</dd> <dt>

**pTransport**
</dt> <dd>

Type: **[**ISMTPTransport**](oe-ismtptransport.md)\***

</dd> <dd>

Contains a pointer to the [**ISMTPTransport**](oe-ismtptransport.md) object that generated the [**OnResponse**](oe-ismtpcallback-onresponse.md) call.

</dd> <dt>

**rStreamInfo**
</dt> <dd>

Type: **[**SMTPSTREAM**](oe-smtpstream.md)**

</dd> <dd>

Contains the [**SMTPSTREAM**](oe-smtpstream.md) structure that contains information about the message stream. This structure occupies the union when **command** is equal to [**SMTP\_SEND\_STREAM**](oe-smtpcommand.md).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





