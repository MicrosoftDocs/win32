---
title: IMAP\_STATUS\_RESPONSE structure
description: Returns the results of a STATUS response.
ms.assetid: '82fdccc7-43fe-4649-8b68-4974b19c8a99'
keywords: ["IMAP_STATUS_RESPONSE structure Windows Mail (formerly Outlook Express)", "IMAPADDR structure Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- IMAPADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IMAP\_STATUS\_RESPONSE structure

\[**IMAP\_STATUS\_RESPONSE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the results of a STATUS response.

## Syntax


```C++
typedef struct tagIMAP_STATUS_RESPONSE {
  LPSTR pszMailboxName;
  BOOL  fMessages;
  DWORD dwMessages;
  BOOL  fRecent;
  DWORD dwRecent;
  BOOL  fUIDNext;
  DWORD dwUIDNext;
  BOOL  fUIDValidity;
  DWORD dwUIDValidity;
  BOOL  fUnseen;
  DWORD dwUnseen;
} IMAPADDR;
```



## Members

<dl> <dt>

**pszMailboxName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the mailbox name for which status is reported.

</dd> <dt>

**fMessages**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwMessages** contains valid data.

</dd> <dt>

**dwMessages**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the total number of messages in the mailbox.

</dd> <dt>

**fRecent**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwRecent** contains valid data.

</dd> <dt>

**dwRecent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the total number of messages with the "\\recent" flag set.

</dd> <dt>

**fUIDNext**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwUIDNext** contains valid data.

</dd> <dt>

**dwUIDNext**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the unique identifier (UID) to be assigned the next new message.

</dd> <dt>

**fUIDValidity**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwUIDValidity** contains valid data.

</dd> <dt>

**dwUIDValidity**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the UID validity value for the mailbox.

</dd> <dt>

**fUnseen**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwUnseen** contains valid data.

</dd> <dt>

**dwUnseen**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the total number of messages without the "\\seen" flag set.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





