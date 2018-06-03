---
title: RULEINFO structure
description: RULEINFO is no longer available for use as of Windows Vista.
ms.assetid: 570cda20-dac7-49ad-a6ef-1e15b340de55
keywords:
- RULEINFO structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- RULEINFO
api_location:
- Oerules.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# RULEINFO structure

\[**RULEINFO** is no longer available for use as of Windows Vista.\]

Contains a rule.

## Syntax


```C++
typedef struct tagRULEINFO {
  RULEID  ridRule;
  IOERule *pIRule;
} RULEINFO;
```



## Members

<dl> <dt>

**ridRule**
</dt> <dd>

Type: **RULEID**

</dd> <dd>

Specifies one of the following values.



| Value                                                                                                                                                                                                                                                | Meaning                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="RULEID_JUNK"></span><span id="ruleid_junk"></span><dl> <dt>**RULEID\_JUNK**</dt> <dt>-3</dt> </dl>                                      | Indicates a Blocked Senders rule. <br/> |
| <span id="RULEID_SENDERS"></span><span id="ruleid_senders"></span><dl> <dt>**RULEID\_SENDERS**</dt> <dt>-2</dt> </dl>                             | Indicates a Mail or News rule. <br/>    |
| <span id="RULEID_VIEW_ALL"></span><span id="ruleid_view_all"></span><dl> <dt>**RULEID\_VIEW\_ALL**</dt> <dt>0xffa</dt> </dl>                      |                                               |
| <span id="RULEID_VIEW_UNREAD"></span><span id="ruleid_view_unread"></span><dl> <dt>**RULEID\_VIEW\_UNREAD**</dt> <dt>0xffb</dt> </dl>             |                                               |
| <span id="RULEID_VIEW_DOWNLOADED"></span><span id="ruleid_view_downloaded"></span><dl> <dt>**RULEID\_VIEW\_DOWNLOADED**</dt> <dt>0xffc</dt> </dl> |                                               |
| <span id="RULEID_VIEW_DELETED"></span><span id="ruleid_view_deleted"></span><dl> <dt>**RULEID\_VIEW\_DELETED**</dt> <dt>0xffd</dt> </dl>          |                                               |
| <span id="RULEID_VIEW_REPLIES"></span><span id="ruleid_view_replies"></span><dl> <dt>**RULEID\_VIEW\_REPLIES**</dt> <dt>0xffe</dt> </dl>          |                                               |
| <span id="RULEID_VIEW_IGNORED"></span><span id="ruleid_view_ignored"></span><dl> <dt>**RULEID\_VIEW\_IGNORED**</dt> <dt>0xfff</dt> </dl>          |                                               |



 

</dd> <dt>

**pIRule**
</dt> <dd>

Type: **[**IOERule**](oe-ioerule.md)\***

</dd> <dd>

Specifies a pointer to an [**IOERule**](oe-ioerule.md) interface.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Oerules.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl> |



 

 





