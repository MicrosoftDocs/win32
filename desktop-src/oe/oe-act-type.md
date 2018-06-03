---
title: ACT\_TYPE enumeration
description: ACT\_TYPE is no longer available for use as of Windows Vista.
ms.assetid: ecc3880a-25b2-444d-bc89-376ec355787b
keywords:
- ACT_TYPE enumeration Windows Mail (formerly Outlook Express)
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

# ACT\_TYPE enumeration

\[**ACT\_TYPE** is no longer available for use as of Windows Vista.\]

Specifies action types.

## Syntax


```C++
typedef enum tagACT_TYPE { 
  ACT_TYPE_NULL          = 0,
  ACT_TYPE_COPY          = 1,
  ACT_TYPE_FWD           = 2,
  ACT_TYPE_NOTIFYMSG     = 3,
  ACT_TYPE_NOTIFYSND     = 4,
  ACT_TYPE_REPLY         = 5,
  ACT_TYPE_MOVE          = 6,
  ACT_TYPE_DELETE        = 7,
  ACT_TYPE_DELETESERVER  = 8,
  ACT_TYPE_DONTDOWNLOAD  = 9,
  ACT_TYPE_HIGHLIGHT     = 10,
  ACT_TYPE_FLAG          = 11,
  ACT_TYPE_STOP          = 12,
  ACT_TYPE_READ          = 13,
  ACT_TYPE_MARKDOWNLOAD  = 14,
  ACT_TYPE_SHOW          = 15,
  ACT_TYPE_JUNKMAIL      = 16,
  ACT_TYPE_WATCH         = 17,
  ACT_TYPE_MAX           = 18
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="ACT_TYPE_NULL"></span><span id="act_type_null"></span>**ACT\_TYPE\_NULL**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_COPY"></span><span id="act_type_copy"></span>**ACT\_TYPE\_COPY**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_FWD"></span><span id="act_type_fwd"></span>**ACT\_TYPE\_FWD**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_NOTIFYMSG"></span><span id="act_type_notifymsg"></span>**ACT\_TYPE\_NOTIFYMSG**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_NOTIFYSND"></span><span id="act_type_notifysnd"></span>**ACT\_TYPE\_NOTIFYSND**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_REPLY"></span><span id="act_type_reply"></span>**ACT\_TYPE\_REPLY**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_MOVE"></span><span id="act_type_move"></span>**ACT\_TYPE\_MOVE**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_DELETE"></span><span id="act_type_delete"></span>**ACT\_TYPE\_DELETE**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_DELETESERVER"></span><span id="act_type_deleteserver"></span>**ACT\_TYPE\_DELETESERVER**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_DONTDOWNLOAD"></span><span id="act_type_dontdownload"></span>**ACT\_TYPE\_DONTDOWNLOAD**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_HIGHLIGHT"></span><span id="act_type_highlight"></span>**ACT\_TYPE\_HIGHLIGHT**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_FLAG"></span><span id="act_type_flag"></span>**ACT\_TYPE\_FLAG**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_STOP"></span><span id="act_type_stop"></span>**ACT\_TYPE\_STOP**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_READ"></span><span id="act_type_read"></span>**ACT\_TYPE\_READ**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_MARKDOWNLOAD"></span><span id="act_type_markdownload"></span>**ACT\_TYPE\_MARKDOWNLOAD**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_SHOW"></span><span id="act_type_show"></span>**ACT\_TYPE\_SHOW**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_JUNKMAIL"></span><span id="act_type_junkmail"></span>**ACT\_TYPE\_JUNKMAIL**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_WATCH"></span><span id="act_type_watch"></span>**ACT\_TYPE\_WATCH**
</dt> <dd></dd> <dt>

<span id="ACT_TYPE_MAX"></span><span id="act_type_max"></span>**ACT\_TYPE\_MAX**
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



 

 





