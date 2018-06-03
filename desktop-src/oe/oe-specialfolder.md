---
title: SPECIALFOLDER enumeration
description: Do not use. Contains constants that specify special message folders in Windows Mail (formerly Outlook Express).
ms.assetid: 6ee8132a-b600-4acf-ae2d-439b4b2bb6cb
keywords:
- SPECIALFOLDER enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Msoeapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# SPECIALFOLDER enumeration

Do not use. Contains constants that specify special message folders in Windows Mail (formerly Outlook Express).

## Syntax


```C++
typedef enum tagSPECIALFOLDER { 
  FOLDER_NOTSPECIAL  = -1,
  FOLDER_INBOX       = 1,
  FOLDER_OUTBOX      = 2,
  FOLDER_SENT        = 3,
  FOLDER_DELETED     = 4,
  FOLDER_DRAFT       = 5,
  FOLDER_MAX         = 6
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="FOLDER_NOTSPECIAL"></span><span id="folder_notspecial"></span>**FOLDER\_NOTSPECIAL**
</dt> <dd>

Specifies a folder that is not special.

</dd> <dt>

<span id="FOLDER_INBOX"></span><span id="folder_inbox"></span>**FOLDER\_INBOX**
</dt> <dd>

Specifies the folder that holds incoming messages.

</dd> <dt>

<span id="FOLDER_OUTBOX"></span><span id="folder_outbox"></span>**FOLDER\_OUTBOX**
</dt> <dd>

Specifies the folder that holds messages waiting to be sent.

</dd> <dt>

<span id="FOLDER_SENT"></span><span id="folder_sent"></span>**FOLDER\_SENT**
</dt> <dd>

Specifies the folder that holds messages that have been sent.

</dd> <dt>

<span id="FOLDER_DELETED"></span><span id="folder_deleted"></span>**FOLDER\_DELETED**
</dt> <dd>

Specifies the folder that holds deleted messages.

</dd> <dt>

<span id="FOLDER_DRAFT"></span><span id="folder_draft"></span>**FOLDER\_DRAFT**
</dt> <dd>

Specifies the folder that holds messages saved but not yet sent.

</dd> <dt>

<span id="FOLDER_MAX"></span><span id="folder_max"></span>**FOLDER\_MAX**
</dt> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





