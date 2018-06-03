---
title: CRIT\_TYPE enumeration
description: CRIT\_TYPE is no longer available for use as of Windows Vista.
ms.assetid: 56a559de-ad64-453f-a901-f3cd884795db
keywords:
- CRIT_TYPE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Oerules.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CRIT\_TYPE enumeration

\[**CRIT\_TYPE** is no longer available for use as of Windows Vista.\]

Specifies criteria types.

## Syntax


```C++
typedef enum tagCRIT_TYPE { 
  CRIT_TYPE_NULL         = 0,
  CRIT_TYPE_NEWSGROUP    = 1,
  CRIT_TYPE_TOME         = 2,
  CRIT_TYPE_CCME         = 3,
  CRIT_TYPE_BCCME        = 4,
  CRIT_TYPE_TOADDR       = 5,
  CRIT_TYPE_CCADDR       = 6,
  CRIT_TYPE_FROMADDR     = 7,
  CRIT_TYPE_SUBJECT      = 8,
  CRIT_TYPE_BODY         = 9,
  CRIT_TYPE_TO           = 10,
  CRIT_TYPE_CC           = 11,
  CRIT_TYPE_FROM         = 12,
  CRIT_TYPE_PRIORITY     = 13,
  CRIT_TYPE_ATTACH       = 14,
  CRIT_TYPE_SIZE         = 15,
  CRIT_TYPE_DATE         = 16,
  CRIT_TYPE_HEADER       = 17,
  CRIT_TYPE_JUNK         = 18,
  CRIT_TYPE_ACCOUNT      = 19,
  CRIT_TYPE_ALL          = 20,
  CRIT_TYPE_TOORCCADDR   = 21,
  CRIT_TYPE_TOORCC       = 22,
  CRIT_TYPE_SENDER       = 23,
  CRIT_TYPE_REPLIES      = 24,
  CRIT_TYPE_DOWNLOADED   = 25,
  CRIT_TYPE_DELETED      = 26,
  CRIT_TYPE_THREADSTATE  = 27,
  CRIT_TYPE_READ         = 28,
  CRIT_TYPE_LINES        = 29,
  CRIT_TYPE_AGE          = 30,
  CRIT_TYPE_SECURE       = 31,
  CRIT_TYPE_FLAGGED      = 32,
  CRIT_TYPE_MAX          = 33
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="CRIT_TYPE_NULL"></span><span id="crit_type_null"></span>**CRIT\_TYPE\_NULL**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_NEWSGROUP"></span><span id="crit_type_newsgroup"></span>**CRIT\_TYPE\_NEWSGROUP**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_TOME"></span><span id="crit_type_tome"></span>**CRIT\_TYPE\_TOME**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_CCME"></span><span id="crit_type_ccme"></span>**CRIT\_TYPE\_CCME**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_BCCME"></span><span id="crit_type_bccme"></span>**CRIT\_TYPE\_BCCME**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_TOADDR"></span><span id="crit_type_toaddr"></span>**CRIT\_TYPE\_TOADDR**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_CCADDR"></span><span id="crit_type_ccaddr"></span>**CRIT\_TYPE\_CCADDR**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_FROMADDR"></span><span id="crit_type_fromaddr"></span>**CRIT\_TYPE\_FROMADDR**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_SUBJECT"></span><span id="crit_type_subject"></span>**CRIT\_TYPE\_SUBJECT**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_BODY"></span><span id="crit_type_body"></span>**CRIT\_TYPE\_BODY**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_TO"></span><span id="crit_type_to"></span>**CRIT\_TYPE\_TO**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_CC"></span><span id="crit_type_cc"></span>**CRIT\_TYPE\_CC**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_FROM"></span><span id="crit_type_from"></span>**CRIT\_TYPE\_FROM**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_PRIORITY"></span><span id="crit_type_priority"></span>**CRIT\_TYPE\_PRIORITY**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_ATTACH"></span><span id="crit_type_attach"></span>**CRIT\_TYPE\_ATTACH**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_SIZE"></span><span id="crit_type_size"></span>**CRIT\_TYPE\_SIZE**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_DATE"></span><span id="crit_type_date"></span>**CRIT\_TYPE\_DATE**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_HEADER"></span><span id="crit_type_header"></span>**CRIT\_TYPE\_HEADER**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_JUNK"></span><span id="crit_type_junk"></span>**CRIT\_TYPE\_JUNK**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_ACCOUNT"></span><span id="crit_type_account"></span>**CRIT\_TYPE\_ACCOUNT**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_ALL"></span><span id="crit_type_all"></span>**CRIT\_TYPE\_ALL**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_TOORCCADDR"></span><span id="crit_type_toorccaddr"></span>**CRIT\_TYPE\_TOORCCADDR**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_TOORCC"></span><span id="crit_type_toorcc"></span>**CRIT\_TYPE\_TOORCC**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_SENDER"></span><span id="crit_type_sender"></span>**CRIT\_TYPE\_SENDER**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_REPLIES"></span><span id="crit_type_replies"></span>**CRIT\_TYPE\_REPLIES**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_DOWNLOADED"></span><span id="crit_type_downloaded"></span>**CRIT\_TYPE\_DOWNLOADED**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_DELETED"></span><span id="crit_type_deleted"></span>**CRIT\_TYPE\_DELETED**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_THREADSTATE"></span><span id="crit_type_threadstate"></span>**CRIT\_TYPE\_THREADSTATE**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_READ"></span><span id="crit_type_read"></span>**CRIT\_TYPE\_READ**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_LINES"></span><span id="crit_type_lines"></span>**CRIT\_TYPE\_LINES**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_AGE"></span><span id="crit_type_age"></span>**CRIT\_TYPE\_AGE**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_SECURE"></span><span id="crit_type_secure"></span>**CRIT\_TYPE\_SECURE**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_FLAGGED"></span><span id="crit_type_flagged"></span>**CRIT\_TYPE\_FLAGGED**
</dt> <dd></dd> <dt>

<span id="CRIT_TYPE_MAX"></span><span id="crit_type_max"></span>**CRIT\_TYPE\_MAX**
</dt> <dd></dd> </dl>

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



 

 





