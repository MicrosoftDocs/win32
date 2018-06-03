---
title: IMAP\_RESPONSE\_TYPE enumeration
description: Identifies the types of server responses. The IMAP\_RESPONSE\_DATA structure is populated based on a value from this enumeration.
ms.assetid: 1f8eb369-6a0e-4314-bb03-fa52fb886be5
keywords:
- IMAP_RESPONSE_TYPE enumeration Windows Mail (formerly Outlook Express)
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

# IMAP\_RESPONSE\_TYPE enumeration

\[**IMAP\_RESPONSE\_TYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Identifies the types of server responses. The [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md) structure is populated based on a value from this enumeration.

## Syntax


```C++
typedef enum tagIMAP_RESPONSE_TYPE { 
  irtERROR_NOTIFICATION  = 0,
  irtCOMMAND_COMPLETION  = 1,
  irtSERVER_ALERT        = 2,
  irtPARSE_ERROR         = 3,
  irtMAILBOX_UPDATE      = 4,
  irtDELETED_MSG         = 5,
  irtFETCH_BODY          = 6,
  irtUPDATE_MSG          = 7,
  irtAPPLICABLE_FLAGS    = 8,
  irtPERMANENT_FLAGS     = 9,
  irtUIDVALIDITY         = 10,
  irtREADWRITE_STATUS    = 11,
  irtTRYCREATE           = 12,
  irtSEARCH              = 13,
  irtMAILBOX_LISTING     = 14,
  irtMAILBOX_STATUS      = 15,
  irtAPPEND_PROGRESS     = 16,
  irtUPDATE_MSG_EX       = 17
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="irtERROR_NOTIFICATION"></span><span id="irterror_notification"></span><span id="IRTERROR_NOTIFICATION"></span>**irtERROR\_NOTIFICATION**
</dt> <dd>

Indicates an error has been encountered while parsing the server response.

</dd> <dt>

<span id="irtCOMMAND_COMPLETION"></span><span id="irtcommand_completion"></span><span id="IRTCOMMAND_COMPLETION"></span>**irtCOMMAND\_COMPLETION**
</dt> <dd>

Indicates the IMAP command has completed. If the command failed, [**IMAP\_RESPONSE**](oe-imap-response.md).**lpszResponseText** contains the failure message.

</dd> <dt>

<span id="irtSERVER_ALERT"></span><span id="irtserver_alert"></span><span id="IRTSERVER_ALERT"></span>**irtSERVER\_ALERT**
</dt> <dd>

Indicates that the server has returned an ALERT response code. [**IMAP\_RESPONSE**](oe-imap-response.md).**lpszResponseText** contains the text of the alert.

</dd> <dt>

<span id="irtPARSE_ERROR"></span><span id="irtparse_error"></span><span id="IRTPARSE_ERROR"></span>**irtPARSE\_ERROR**
</dt> <dd>

Indicates that the server has returned a PARSE response code. [**IMAP\_RESPONSE**](oe-imap-response.md).**lpszResponseText** contains the text of the parsing error.

</dd> <dt>

<span id="irtMAILBOX_UPDATE"></span><span id="irtmailbox_update"></span><span id="IRTMAILBOX_UPDATE"></span>**irtMAILBOX\_UPDATE**
</dt> <dd>

Indicates that the server has returned an EXISTS, RECENT, or UNSEEN response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**pmcMsgCount** contains the response data.

</dd> <dt>

<span id="irtDELETED_MSG"></span><span id="irtdeleted_msg"></span><span id="IRTDELETED_MSG"></span>**irtDELETED\_MSG**
</dt> <dd>

Indicates that the server has returned an EXPUNGE response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**dwDeletedMsgSeqNum** contains the response data.

</dd> <dt>

<span id="irtFETCH_BODY"></span><span id="irtfetch_body"></span><span id="IRTFETCH_BODY"></span>**irtFETCH\_BODY**
</dt> <dd>

Indicates that the server has returned a partial message body in a FETCH response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**pFetchBodyPart** contains the response data.

</dd> <dt>

<span id="irtUPDATE_MSG"></span><span id="irtupdate_msg"></span><span id="IRTUPDATE_MSG"></span>**irtUPDATE\_MSG**
</dt> <dd>

Indicates that the server has returned a FETCH response and **IMAP\_FETCHEX\_DISABLE** is the current value of the persisted IMAPTransport extended fetch flag. The client can change the flag value with the [**EnableFetchEx**](oe-iimaptransport2-enablefetchex.md) method. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**pFetchResults** contains the response data.

</dd> <dt>

<span id="irtAPPLICABLE_FLAGS"></span><span id="irtapplicable_flags"></span><span id="IRTAPPLICABLE_FLAGS"></span>**irtAPPLICABLE\_FLAGS**
</dt> <dd>

Indicates that the server has returned a FLAGS response with a list of flags that apply to the current mailbox. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**imfImapMessageFlags** contains the response data.

</dd> <dt>

<span id="irtPERMANENT_FLAGS"></span><span id="irtpermanent_flags"></span><span id="IRTPERMANENT_FLAGS"></span>**irtPERMANENT\_FLAGS**
</dt> <dd>

Indicates that the server has returned a PERMANENTFLAGS response code with a list of flags that can be permanently changed by the client. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**imfImapMessageFlags** contains the response data.

</dd> <dt>

<span id="irtUIDVALIDITY"></span><span id="irtuidvalidity"></span><span id="IRTUIDVALIDITY"></span>**irtUIDVALIDITY**
</dt> <dd>

Indicates that the server has returned a UIDVALIDITY response code. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**dwUIDValidity** contains the response data.

</dd> <dt>

<span id="irtREADWRITE_STATUS"></span><span id="irtreadwrite_status"></span><span id="IRTREADWRITE_STATUS"></span>**irtREADWRITE\_STATUS**
</dt> <dd>

Indicates that the server has returned either a READ-WRITE or READ-ONLY response code. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**bReadWrite** indicates which response code the server returned.

</dd> <dt>

<span id="irtTRYCREATE"></span><span id="irttrycreate"></span><span id="IRTTRYCREATE"></span>**irtTRYCREATE**
</dt> <dd>

Indicates that the server has returned a TRYCREATE response code. [**IMAP\_RESPONSE**](oe-imap-response.md).**lpszResponseText** contains the text of the response code.

</dd> <dt>

<span id="irtSEARCH"></span><span id="irtsearch"></span><span id="IRTSEARCH"></span>**irtSEARCH**
</dt> <dd>

Indicates that the server has returned a SEARCH response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**prlSearchResults** indicates the returned message sequence numbers.

</dd> <dt>

<span id="irtMAILBOX_LISTING"></span><span id="irtmailbox_listing"></span><span id="IRTMAILBOX_LISTING"></span>**irtMAILBOX\_LISTING**
</dt> <dd>

Indicates that the server has returned either a LIST or LSUB response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**illrdMailboxListing** contains the response data.

</dd> <dt>

<span id="irtMAILBOX_STATUS"></span><span id="irtmailbox_status"></span><span id="IRTMAILBOX_STATUS"></span>**irtMAILBOX\_STATUS**
</dt> <dd>

Indicates that the server has returned a STATUS response. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**pisrStatusResponse** contains the response data.

</dd> <dt>

<span id="irtAPPEND_PROGRESS"></span><span id="irtappend_progress"></span><span id="IRTAPPEND_PROGRESS"></span>**irtAPPEND\_PROGRESS**
</dt> <dd>

Indicates that the progress of an uploaded stream is available. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**papAppendProgress** contains the response data.

</dd> <dt>

<span id="irtUPDATE_MSG_EX"></span><span id="irtupdate_msg_ex"></span><span id="IRTUPDATE_MSG_EX"></span>**irtUPDATE\_MSG\_EX**
</dt> <dd>

Indicates that the server has returned a FETCH response and **IMAP\_FETCHEX\_ENABLE** is the current value of the persisted IMAPTransport extended fetch flag. The client can change the flag value with the [**EnableFetchEx**](oe-iimaptransport2-enablefetchex.md) method. [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md).**pFetchResultsEx** contains the response data.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





