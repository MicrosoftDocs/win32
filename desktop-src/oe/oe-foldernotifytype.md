---
title: FOLDERNOTIFYTYPE enumeration
description: Defined as part of IStoreNamespace.
ms.assetid: 'ff3565cd-2a0a-43bc-a935-4c2521d1ebe1'
keywords: ["FOLDERNOTIFYTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Msoeapi.h
api_type:
- HeaderDef
---

# FOLDERNOTIFYTYPE enumeration

\[**FOLDERNOTIFYTYPE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Defined as part of [**IStoreNamespace**](oe-istorenamespace.md).

## Syntax


```C++
typedef enum tagFOLDERNOTIFYTYPE { 
  NEW_FOLDER            = 1,
  DELETE_FOLDER         = 1,
  RENAME_FOLDER         = 2,
  MOVE_FOLDER           = 3,
  UNREAD_CHANGE         = 4,
  IMAPFLAG_CHANGE       = 5,
  UPDATEFLAG_CHANGE     = 6,
  FOLDER_PROPS_CHANGED  = 7
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="NEW_FOLDER"></span><span id="new_folder"></span>**NEW\_FOLDER**
</dt> <dd></dd> <dt>

<span id="DELETE_FOLDER"></span><span id="delete_folder"></span>**DELETE\_FOLDER**
</dt> <dd></dd> <dt>

<span id="RENAME_FOLDER"></span><span id="rename_folder"></span>**RENAME\_FOLDER**
</dt> <dd></dd> <dt>

<span id="MOVE_FOLDER"></span><span id="move_folder"></span>**MOVE\_FOLDER**
</dt> <dd></dd> <dt>

<span id="UNREAD_CHANGE"></span><span id="unread_change"></span>**UNREAD\_CHANGE**
</dt> <dd></dd> <dt>

<span id="IMAPFLAG_CHANGE"></span><span id="imapflag_change"></span>**IMAPFLAG\_CHANGE**
</dt> <dd></dd> <dt>

<span id="UPDATEFLAG_CHANGE"></span><span id="updateflag_change"></span>**UPDATEFLAG\_CHANGE**
</dt> <dd></dd> <dt>

<span id="FOLDER_PROPS_CHANGED"></span><span id="folder_props_changed"></span>**FOLDER\_PROPS\_CHANGED**
</dt> <dd></dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





