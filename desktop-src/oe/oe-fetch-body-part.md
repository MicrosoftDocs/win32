---
title: FETCH\_BODY\_PART structure
description: Contains a partial message body returned by the Internet Message Access Protocol (IMAP) server in a FETCH response.
ms.assetid: 1bea642d-0781-47ef-ab16-df26077ed000
keywords:
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

# FETCH\_BODY\_PART structure

\[**FETCH\_BODY\_PART** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains a partial message body returned by the Internet Message Access Protocol (IMAP) server in a FETCH response. The [**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md) or [**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md) structure contains data about the entire FETCH response when it is complete.

## Syntax


```C++
typedef struct tagFETCH_BODY_PART {
  DWORD  dwMsgSeqNum;
  LPSTR  pszBodyTag;
  DWORD  dwTotalBytes;
  DWORD  dwSizeOfData;
  DWORD  dwOffset;
  BOOL   fDone;
  LPSTR  pszData;
  LPARAM lpFetchCookie1;
  LPARAM lpFetchCookie2;
} FETCH_BODY_PART;
```



## Members

<dl> <dt>

**dwMsgSeqNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the message sequence number for the message being received. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**pszBodyTag**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the IMAP tag identifying this body section and is equivalent to "msg\_att" defined in the "Formal Syntax" section of [RFC 2060](http://www.ietf.org/rfc/rfc2060.txt) (for example, "RFC822.PEEK", or "BODY\[2.2\]&lt;0.2048&gt;"). The transport terminates the tag at the first space character, so "BODY\[HEADER.FIELDS (*string*)\]" returns as "BODY\[HEADER.FIELDS". The IMAP transport initializes this parameter to **NULL**.

</dd> <dt>

**dwTotalBytes**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the total number of bytes expected for the received body part. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**dwSizeOfData**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the number of bytes pointed to by **pszData**. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**dwOffset**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that indicates the offset of the start of the data buffer. The IMAP transport initializes this parameter to zero.

</dd> <dt>

**fDone**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether this is the last part of the message body. The IMAP transport initializes this parameter to **FALSE**.

</dd> <dt>

**pszData**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the received partial message body data. The IMAP transport initializes this parameter to **NULL**.

</dd> <dt>

**lpFetchCookie1**
</dt> <dd>

Type: **LPARAM**

</dd> <dd>

Contains an **LPARAM** that contains a user-settable value that persists throughout the FETCH response, that is, for all **FETCH\_BODY\_PART** responses (even if multiple partial message bodies are fetched) and for the final [**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md) or [**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md) structure. IMAPTransport initializes this parameter to zero.

</dd> <dt>

**lpFetchCookie2**
</dt> <dd>

Type: **LPARAM**

</dd> <dd>

Contains an **LPARAM** that contains a user-settable value that persists throughout the FETCH response, that is, for all **FETCH\_BODY\_PART** responses (even if multiple partial message bodies are fetched) and for the final [**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md) or [**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md) structure. IMAPTransport initializes this parameter to zero.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





