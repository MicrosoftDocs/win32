---
title: HTTPMAILPROPTYPE enumeration
description: HTTPMail root property types.
ms.assetid: '44ba4f01-5519-44d6-a61e-17dbc5089bd1'
keywords: ["HTTPMAILPROPTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# HTTPMAILPROPTYPE enumeration

\[**HTTPMAILPROPTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

HTTPMail root property types.

## Syntax


```C++
typedef enum tagHTTPMAILPROPTYPE { 
  HTTPMAIL_PROP_INVALID             = 0,
  HTTPMAIL_PROP_ADBAR               = 1,
  HTTPMAIL_PROP_CONTACTS            = 2,
  HTTPMAIL_PROP_INBOX               = 3,
  HTTPMAIL_PROP_OUTBOX              = 4,
  HTTPMAIL_PROP_SENDMSG             = 5,
  HTTPMAIL_PROP_SENTITEMS           = 6,
  HTTPMAIL_PROP_DELETEDITEMS        = 7,
  HTTPMAIL_PROP_DRAFTS              = 8,
  HTTPMAIL_PROP_MSGFOLDERROOT       = 9,
  HTTPMAIL_PROP_SIG                 = 10,
  HTTPMAIL_PROP_MAXPOLLINGINTERVAL  = 11,
  HTTPMAIL_PROP_LAST                = 12
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="HTTPMAIL_PROP_INVALID"></span><span id="httpmail_prop_invalid"></span>**HTTPMAIL\_PROP\_INVALID**
</dt> <dd>

Indicates an invalid property.

</dd> <dt>

<span id="HTTPMAIL_PROP_ADBAR"></span><span id="httpmail_prop_adbar"></span>**HTTPMAIL\_PROP\_ADBAR**
</dt> <dd>

The URL in the address bar.

</dd> <dt>

<span id="HTTPMAIL_PROP_CONTACTS"></span><span id="httpmail_prop_contacts"></span>**HTTPMAIL\_PROP\_CONTACTS**
</dt> <dd>

The URL of the Contacts folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_INBOX"></span><span id="httpmail_prop_inbox"></span>**HTTPMAIL\_PROP\_INBOX**
</dt> <dd>

The URL of the Inbox folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_OUTBOX"></span><span id="httpmail_prop_outbox"></span>**HTTPMAIL\_PROP\_OUTBOX**
</dt> <dd>

The URL of the Outbox folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_SENDMSG"></span><span id="httpmail_prop_sendmsg"></span>**HTTPMAIL\_PROP\_SENDMSG**
</dt> <dd>

The URI to which to submit outgoing mail.

</dd> <dt>

<span id="HTTPMAIL_PROP_SENTITEMS"></span><span id="httpmail_prop_sentitems"></span>**HTTPMAIL\_PROP\_SENTITEMS**
</dt> <dd>

The URL of the Sent Items folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_DELETEDITEMS"></span><span id="httpmail_prop_deleteditems"></span>**HTTPMAIL\_PROP\_DELETEDITEMS**
</dt> <dd>

The URL of the Deleted Items folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_DRAFTS"></span><span id="httpmail_prop_drafts"></span>**HTTPMAIL\_PROP\_DRAFTS**
</dt> <dd>

The URL of the Drafts folder.

</dd> <dt>

<span id="HTTPMAIL_PROP_MSGFOLDERROOT"></span><span id="httpmail_prop_msgfolderroot"></span>**HTTPMAIL\_PROP\_MSGFOLDERROOT**
</dt> <dd>

The URL of the mailbox folder root.

</dd> <dt>

<span id="HTTPMAIL_PROP_SIG"></span><span id="httpmail_prop_sig"></span>**HTTPMAIL\_PROP\_SIG**
</dt> <dd>

The URL of the folder where signature files are kept.

</dd> <dt>

<span id="HTTPMAIL_PROP_MAXPOLLINGINTERVAL"></span><span id="httpmail_prop_maxpollinginterval"></span>**HTTPMAIL\_PROP\_MAXPOLLINGINTERVAL**
</dt> <dd>

The maximum length of time between background polls for new mail.

> [!Note]  
> Use [**GetPropertyDw**](oe-ihttpmailtransport-getpropertydw.md) to retrieve the value of this property.

 

</dd> <dt>

<span id="HTTPMAIL_PROP_LAST"></span><span id="httpmail_prop_last"></span>**HTTPMAIL\_PROP\_LAST**
</dt> <dd>

Indicates the end of the enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





