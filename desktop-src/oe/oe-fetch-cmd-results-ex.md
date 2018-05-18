---
title: FETCH\_CMD\_RESULTS\_EX structure
description: Extended version of FETCH\_CMD\_RESULTS\_EX structure.
ms.assetid: '872f2c40-b6b0-443f-8872-64242b714c06'
keywords: ["FETCH_CMD_RESULTS_EX structure Windows Mail (formerly Outlook Express)", "FETCH_BODY_PART structure Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- FETCH_BODY_PART
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# FETCH\_CMD\_RESULTS\_EX structure

\[**FETCH\_CMD\_RESULTS\_EX** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Extended version of **FETCH\_CMD\_RESULTS\_EX** structure. Contains data from a FETCH response. Because FETCH responses can be unsolicited, the client should check that a data item is valid before attempting to use it.

## Syntax


```C++
typedef struct tagFETCH_CMD_RESULTS_EX {
  DWORD         dwMsgSeqNum;
  BOOL          bMsgFlags;
  IMAP_MSGFLAGS mfMsgFlags;
  BOOL          bRFC822Size;
  DWORD         dwRFC822Size;
  BOOL          bUID;
  DWORD         dwUID;
  BOOL          bInternalDate;
  FILETIME      ftInternalDate;
  LPARAM        lpFetchCookie1;
  LPARAM        lpFetchCookie2;
  BOOL          bEnvelope;
  FILETIME      ftENVDate;
  LPSTR         pszENVSubject;
  IMAPADDR      *piaENVFrom;
  IMAPADDR      *piaENVSender;
  IMAPADDR      *piaENVReplyTo;
  IMAPADDR      *piaENVTo;
  IMAPADDR      *piaENVCc;
  IMAPADDR      *piaENVBcc;
  LPSTR         pszENVInReplyTo;
  LPSTR         pszENVMessageID;
  DWORD         dwReserved1;
  DWORD         dwReserved2;
  DWORD         dwReserved3;
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

</dd> <dt>

**bEnvelope**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether **ftENVDate**, **pszENVSubject**, **piaENVFrom**, **piaENVSender**, **piaENVReplyTo**, **piaENVTo**, **piaENVCc**, **piaENVBcc**, **pszENVInReplyTo**, and **pszENVMessageID** contain valid data.

</dd> <dt>

**ftENVDate**
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

</dd> <dd>

Contains a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure that contains the date field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**pszENVSubject**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the subject field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVFrom**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the from field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVSender**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the sender field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVReplyTo**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the reply-to field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVTo**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the to field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVCc**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the cc field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**piaENVBcc**
</dt> <dd>

Type: **[**IMAPADDR**](oe-imapaddr.md)\***

</dd> <dd>

Contains a pointer to an array of [**IMAPADDR**](oe-imapaddr.md) structures that contains the bcc field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**pszENVInReplyTo**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the in-reply-to field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**pszENVMessageID**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the message-id field returned by the FETCH response in the ENVELOPE data item.

</dd> <dt>

**dwReserved1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved. Unused.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved. Unused.

</dd> <dt>

**dwReserved3**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved. Unused.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





