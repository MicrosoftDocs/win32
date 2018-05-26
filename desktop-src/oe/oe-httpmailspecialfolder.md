---
title: HTTPMAILSPECIALFOLDER enumeration
description: The HTTP special folder types.
ms.assetid: 975a0315-9583-4811-9dc3-65ade73e11ee
keywords:
- HTTPMAILSPECIALFOLDER enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTTPMAILSPECIALFOLDER enumeration

\[**HTTPMAILSPECIALFOLDER** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The HTTP special folder types.

## Syntax


```C++
typedef enum tagHTTPMAILSPECIALFOLDER { 
  HTTPMAIL_SF_NONE          = 0,
  HTTPMAIL_SF_UNRECOGNIZED  = 1,
  HTTPMAIL_SF_INBOX         = 2,
  HTTPMAIL_SF_DELETEDITEMS  = 3,
  HTTPMAIL_SF_DRAFTS        = 4,
  HTTPMAIL_SF_OUTBOX        = 5,
  HTTPMAIL_SF_SENTITEMS     = 6,
  HTTPMAIL_SF_CONTACTS      = 7,
  HTTPMAIL_SF_CALENDAR      = 8,
  HTTPMAIL_SF_MSNPROMO      = 9,
  HTTPMAIL_SF_BULKMAIL      = 10,
  HTTPMAIL_SF_LAST          = 11
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="HTTPMAIL_SF_NONE"></span><span id="httpmail_sf_none"></span>**HTTPMAIL\_SF\_NONE**
</dt> <dd>

No folder.

</dd> <dt>

<span id="HTTPMAIL_SF_UNRECOGNIZED"></span><span id="httpmail_sf_unrecognized"></span>**HTTPMAIL\_SF\_UNRECOGNIZED**
</dt> <dd>

Unknown folder type.

</dd> <dt>

<span id="HTTPMAIL_SF_INBOX"></span><span id="httpmail_sf_inbox"></span>**HTTPMAIL\_SF\_INBOX**
</dt> <dd>

Represents "InboxSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_DELETEDITEMS"></span><span id="httpmail_sf_deleteditems"></span>**HTTPMAIL\_SF\_DELETEDITEMS**
</dt> <dd>

Represents "DeletedItemsSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_DRAFTS"></span><span id="httpmail_sf_drafts"></span>**HTTPMAIL\_SF\_DRAFTS**
</dt> <dd>

Represents "DraftsSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_OUTBOX"></span><span id="httpmail_sf_outbox"></span>**HTTPMAIL\_SF\_OUTBOX**
</dt> <dd>

Represents "OutboxSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_SENTITEMS"></span><span id="httpmail_sf_sentitems"></span>**HTTPMAIL\_SF\_SENTITEMS**
</dt> <dd>

Represents "SentItemsSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_CONTACTS"></span><span id="httpmail_sf_contacts"></span>**HTTPMAIL\_SF\_CONTACTS**
</dt> <dd>

Represents "ContactsSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_CALENDAR"></span><span id="httpmail_sf_calendar"></span>**HTTPMAIL\_SF\_CALENDAR**
</dt> <dd>

Represents "CalendarSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_MSNPROMO"></span><span id="httpmail_sf_msnpromo"></span>**HTTPMAIL\_SF\_MSNPROMO**
</dt> <dd>

Represents "MsnPromoSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_BULKMAIL"></span><span id="httpmail_sf_bulkmail"></span>**HTTPMAIL\_SF\_BULKMAIL**
</dt> <dd>

Represents "BulkMailSpecialFolder".

</dd> <dt>

<span id="HTTPMAIL_SF_LAST"></span><span id="httpmail_sf_last"></span>**HTTPMAIL\_SF\_LAST**
</dt> <dd>

Last member of this enumeration.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





