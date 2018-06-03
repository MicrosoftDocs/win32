---
title: MBOX\_MSGCOUNT structure
description: Contains information from an EXISTS, RECENT or UNSEEN Internet Message Access Protocol (IMAP) server response.
ms.assetid: 8545fafb-223a-426b-9396-15e5f4dc36db
keywords:
- MBOX_MSGCOUNT structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MBOX_MSGCOUNT
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

# MBOX\_MSGCOUNT structure

\[**MBOX\_MSGCOUNT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains information from an EXISTS, RECENT or UNSEEN Internet Message Access Protocol (IMAP) server response.

## Syntax


```C++
typedef struct tagMBOX_MSGCOUNT {
  BOOL  bGotExistsResponse;
  DWORD dwExists;
  BOOL  bGotRecentResponse;
  DWORD dwRecent;
  BOOL  bGotUnseenResponse;
  DWORD dwUnseen;
} MBOX_MSGCOUNT;
```



## Members

<dl> <dt>

**bGotExistsResponse**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether **dwExists** contains a value. The IMAP transport initializes this parameter to **FALSE**.

</dd> <dt>

**dwExists**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the number of messages in the mailbox after the most recent command. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**bGotRecentResponse**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether **dwRecent** contains a value. The IMAP transport initializes this parameter to **FALSE**.

</dd> <dt>

**dwRecent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the number of messages that have arrived since the last server session. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**bGotUnseenResponse**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Indicates whether **dwUnseen** contains a value. The IMAP transport initializes this parameter to **FALSE**.

</dd> <dt>

**dwUnseen**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the message sequence number of the first unseen message. The IMAP transport initializes this parameter to zero.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





