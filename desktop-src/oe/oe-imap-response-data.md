---
title: IMAP\_RESPONSE\_DATA structure
description: Contains the results of an Internet Message Access Protocol (IMAP) response that is dependent on an IMAP\_RESPONSE\_TYPE value.
ms.assetid: '639aecb9-a2f2-447e-b347-9aab0d354306'
keywords: ["IMAP_RESPONSE_DATA structure Windows Mail (formerly Outlook Express)", "IMAPADDR structure Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- IMAPADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IMAP\_RESPONSE\_DATA structure

\[**IMAP\_RESPONSE\_DATA** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the results of an Internet Message Access Protocol (IMAP) response that is dependent on an [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) value.

## Syntax


```C++
typedef struct tagIMAP_RESPONSE_DATA {
  MBOX_MSGCOUNT          *pmcMsgCount;
  DWORD                  dwDeletedMsgSeqNum;
  FETCH_BODY_PART        *pFetchBodyPart;
  FETCH_CMD_RESULTS      *pFetchResults;
  IMAP_MSGFLAGS          imfImapMessageFlags;
  DWORD                  dwUIDValidity;
  BOOL                   bReadWrite;
  IRangeList             *prlSearchResults;
  IMAP_LISTLSUB_RESPONSE illrdMailboxListing;
  IMAP_STATUS_RESPONSE   *pisrStatusResponse;
  APPEND_PROGRESS        *papAppendProgress;
  FETCH_CMD_RESULTS_EX   *pFetchResultsEx;
} IMAPADDR;
```



## Members

<dl> <dt>

**pmcMsgCount**
</dt> <dd>

Type: **[**MBOX\_MSGCOUNT**](oe-mbox-msgcount.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtMAILBOX\_UPDATE**. Contains a pointer to the [**MBOX\_MSGCOUNT**](oe-mbox-msgcount.md) structure that contains the response information from an EXISTS, RECENT, or UNSEEN server response.

</dd> <dt>

**dwDeletedMsgSeqNum**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtDELETED\_MSG**. Contains a **DWORD** that contains the message sequence number of the deleted message returned in an EXPUNGE response.

</dd> <dt>

**pFetchBodyPart**
</dt> <dd>

Type: **[**FETCH\_BODY\_PART**](oe-fetch-body-part.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtFETCH\_BODY**. Contains a pointer to the [**FETCH\_BODY\_PART**](oe-fetch-body-part.md) structure that contains a partial message body returned in a FETCH response.

</dd> <dt>

**pFetchResults**
</dt> <dd>

Type: **[**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtUPDATE\_MSG**. Contains a pointer to the [**FETCH\_CMD\_RESULTS**](oe-fetch-cmd-results.md) structure that contains the FETCH response data.

</dd> <dt>

**imfImapMessageFlags**
</dt> <dd>

Type: **[**IMAP\_MSGFLAGS**](oe-imap-msgflags-constants.md)**

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtAPPLICABLE\_FLAGS** or **irtPERMANENT\_FLAGS**. Contains one or more values from the [**IMAP\_MSGFLAGS**](oe-imap-msgflags-constants.md) enumeration that indicate the list of flags returned by the server in a FLAGS response or PERMANENTFLAGS response code.

</dd> <dt>

**dwUIDValidity**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtUIDVALIDITY**. Contains a **DWORD** that contains the unique identifier validity value for the mailbox returned by the server in a UIDVALIDITY response.

</dd> <dt>

**bReadWrite**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtREADWRITE\_STATUS**. Contains a **BOOL** that indicates whether the mailbox is read/write when **TRUE** (a READ-WRITE response code) or read-only when **FALSE** (a READ-ONLY response code).

</dd> <dt>

**prlSearchResults**
</dt> <dd>

Type: **[**IRangeList**](oe-irangelist.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtSEARCH**. Contains a pointer to the [**IRangeList**](oe-irangelist.md) object that contains the message sequence number returned by the server in a SEARCH response.

</dd> <dt>

**illrdMailboxListing**
</dt> <dd>

Type: **[**IMAP\_LISTLSUB\_RESPONSE**](oe-imap-listlsub-response.md)**

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtMAILBOX\_LISTING**. Contains an [**IMAP\_LISTLSUB\_RESPONSE**](oe-imap-listlsub-response.md) structure that contains the data returned by the server in a LIST or LSUB response.

</dd> <dt>

**pisrStatusResponse**
</dt> <dd>

Type: **[**IMAP\_STATUS\_RESPONSE**](oe-imap-status-response.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtMAILBOX\_STATUS**. Contains a pointer to the [**IMAP\_STATUS\_RESPONSE**](oe-imap-status-response.md) structure that contains the data returned by the server in a STATUS response.

</dd> <dt>

**papAppendProgress**
</dt> <dd>

Type: **[**APPEND\_PROGRESS**](oe-append-progress.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtAPPEND\_PROGRESS**. Contains a pointer to the [**APPEND\_PROGRESS**](oe-append-progress.md) structure that reports on the progress of the uploaded data.

</dd> <dt>

**pFetchResultsEx**
</dt> <dd>

Type: **[**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md)\***

</dd> <dd>

Occupies the structure when [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) is **irtUPDATE\_MSG\_EX**. Contains a pointer to the [**FETCH\_CMD\_RESULTS\_EX**](oe-fetch-cmd-results-ex.md) structure that contains the extended FETCH response data.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





