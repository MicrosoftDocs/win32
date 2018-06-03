---
title: POP3RESPONSE structure
description: Do not use. Contains information about a Post Office Protocol version 3 (POP3) response.
ms.assetid: 6d40a8a8-e0b1-45f7-8b8f-1efa0e8a272a
keywords:
- POP3RESPONSE structure Windows Mail (formerly Outlook Express)
- LPPOP3RESPONSE structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- POP3RESPONSE
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

# POP3RESPONSE structure

\[The **POP3RESPONSE** structure is available for use in Windows XP. It might be altered or unavailable in subsequent versions.\]

Do not use. Contains information about a Post Office Protocol version 3 (POP3) response.

## Syntax


```C++
typedef struct tagPOP3RESPONSE {
  POP3COMMAND    command;
  BOOL           fDone;
  IXPRESULT      rIxpResult;
  IPOP3Transport *pTransport;
  BOOL           fValidInfo;
  union {
    POP3UIDL rUidlInfo;
    POP3STAT rStatInfo;
    POP3LIST rListInfo;
    DWORD    dwPopId;
    POP3RETR rRetrInfo;
    POP3TOP  rTopInfo;
  };
} POP3RESPONSE, *LPPOP3RESPONSE;
```



## Members

<dl> <dt>

**command**
</dt> <dd>

Type: **[**POP3COMMAND**](oe-pop3command.md)**

</dd> <dd>

Contains the [**POP3COMMAND**](oe-pop3command.md) for which the response was generated.

</dd> <dt>

**fDone**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the command finished. The client should wait until this member is **TRUE** before issuing another POP3 command through the [**IPOP3Transport**](oe-ipop3transport.md) object.

</dd> <dt>

**rIxpResult**
</dt> <dd>

Type: **[**IXPRESULT**](oe-ixpresult.md)**

</dd> <dd>

Contains an [**IXPRESULT**](oe-ixpresult.md) structure that contains the information about the server response. If **rIxpResult**.**hrResult** specifies a FAILED result, the structure contains other information.

</dd> <dt>

**pTransport**
</dt> <dd>

Type: **[**IPOP3Transport**](oe-ipop3transport.md)\***

</dd> <dd>

Contains a pointer to the [**IPOP3Transport**](oe-ipop3transport.md) object that generated the [**OnResponse**](oe-ipop3callback-onresponse.md) call.

</dd> <dt>

**fValidInfo**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the data in the union is valid. This parameter has a value of **FALSE** when the received response has no data.

</dd> <dt>

**rUidlInfo**
</dt> <dd>

Type: **[**POP3UIDL**](oe-pop3uidl.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_UIDL**](oe-pop3command.md). Contains the [**POP3UIDL**](oe-pop3uidl.md) structure that holds the response data.

</dd> <dt>

**rStatInfo**
</dt> <dd>

Type: **[**POP3STAT**](oe-pop3stat.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_STAT**](oe-pop3command.md). Contains the [**POP3STAT**](oe-pop3stat.md) structure that holds the response data.

</dd> <dt>

**rListInfo**
</dt> <dd>

Type: **[**POP3LIST**](oe-pop3list.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_LIST**](oe-pop3command.md). Contains the [**POP3LIST**](oe-pop3list.md) structure that holds the response data.

</dd> <dt>

**dwPopId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_DELE**](oe-pop3command.md). Contains a **DWORD** that holds the success or error message from the DELE command.

</dd> <dt>

**rRetrInfo**
</dt> <dd>

Type: **[**POP3RETR**](oe-pop3retr.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_RETR**](oe-pop3command.md). Contains the [**POP3RETR**](oe-pop3retr.md) structure that holds the response data.

</dd> <dt>

**rTopInfo**
</dt> <dd>

Type: **[**POP3TOP**](oe-pop3top.md)**

</dd> <dd>

Occupies the union when **command** is equal to [**POP3\_TOP**](oe-pop3command.md). Contains the [**POP3TOP**](oe-pop3top.md) structure that holds the response data.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





