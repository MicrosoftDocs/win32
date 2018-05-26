---
title: FETCH\_CMD\_RESULTS structure
description: Contains data from a FETCH response.
ms.assetid: 8147a65e-314b-4b43-b476-2d8cb8cf84c8
keywords:
- FETCH_CMD_RESULTS structure Windows Mail (formerly Outlook Express)
- FETCH_BODY_PART structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- FETCH_BODY_PART
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

# FETCH\_CMD\_RESULTS structure

\[**FETCH\_CMD\_RESULTS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains data from a FETCH response. Because FETCH responses can be unsolicited, the client should check that a data item is valid before attempting to use it.

## Syntax


```C++
typedef struct tagFETCH_CMD_RESULTS {
  DWORD         dwMsgSeqNum;
  BOOL          bMsgFlags;
  IMAP_MSGFLAGS mfMsgFlags;
  BOOL          bRFC822Size;
  DWORD         dwRFC822Size;
  BOOL          bUID;
  DWORD         dwUID;
  BOOL          bInternalDate;
  FILETIME      ftInternalDate;
  LPARAM        lpFetchCookie1;
  LPARAM        lpFetchCookie2;
} FETCH_BODY_PART;
```



## Members

<dl> <dt>

**dwMsgSeqNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the message sequence number for the fetched message.

</dd> <dt>

**bMsgFlags**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **mfMsgFlags** contains valid data.

</dd> <dt>

**mfMsgFlags**
</dt> <dd>

Type: **[**IMAP\_MSGFLAGS**](oe-imap-msgflags-constants.md)**

</dd> <dd>

Contains one or more values from the [**IMAP\_MSGFLAGS**](oe-imap-msgflags-constants.md) enumeration returned in the FLAGS data item by the FETCH response.

</dd> <dt>

**bRFC822Size**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwRFC822Size** contains valid data.

</dd> <dt>

**dwRFC822Size**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the RFC822.SIZE data item returned by the FETCH response.

</dd> <dt>

**bUID**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **dwUID** contains valid data.

</dd> <dt>

**dwUID**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the UID data item returned by the FETCH response.

</dd> <dt>

**bInternalDate**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **ftInternalDate** contains valid data.

</dd> <dt>

**ftInternalDate**
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

</dd> <dd>

Contains a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure that contains the INTERNALDATE data item returned by the FETCH response.

</dd> <dt>

**lpFetchCookie1**
</dt> <dd>

Type: **LPARAM**

</dd> <dd>

Contains an **LPARAM** that contains a user-settable value. IMAPTransport initializes this parameter to zero.

</dd> <dt>

**lpFetchCookie2**
</dt> <dd>

Type: **LPARAM**

</dd> <dd>

Contains an **LPARAM** that contains a user-settable value. IMAPTransport initializes this parameter to zero.

</dd> </dl>

## Remarks

This structure is returned after the entire FETCH response is received.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





