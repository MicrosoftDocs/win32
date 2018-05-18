---
title: FOLDERPROPS structure
description: Do not use. Defines message folder properties.
ms.assetid: 'fc5f5efa-c43f-460e-b322-5619d131184b'
keywords: ["FOLDERPROPS structure Windows Mail (formerly Outlook Express)", "LPFOLDERPROPS structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- FOLDERPROPS
api_location:
- Msoeapi.h
api_type:
- HeaderDef
---

# FOLDERPROPS structure

Do not use. Defines message folder properties.

## Syntax


```C++
typedef struct tagFOLDERPROPS {
  DWORD         cbSize;
  STOREFOLDERID dwFolderId;
  INT           cSubFolders;
  SPECIALFOLDER sfType;
  DWORD         cUnread;
  DWORD         cMessage;
  CHAR          szName[CCHMAX_FOLDER_NAME];
} FOLDERPROPS, *LPFOLDERPROPS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size of this structure in bytes.

</dd> <dt>

**dwFolderId**
</dt> <dd>

Type: **STOREFOLDERID**

</dd> <dd>

ID of the folder these properties represent.

</dd> <dt>

**cSubFolders**
</dt> <dd>

Type: **INT**

</dd> <dd>

Count of the number of child folders underneath this folder.

</dd> <dt>

**sfType**
</dt> <dd>

Type: **[**SPECIALFOLDER**](oe-specialfolder.md)**

</dd> <dd>

Specifies the type of message folder. Corresponds to a type in the [**SPECIALFOLDER**](oe-specialfolder.md) enumeration.

</dd> <dt>

**cUnread**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The number of unread messages in this folder.

</dd> <dt>

**cMessage**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The total number of messages in this folder.

</dd> <dt>

**szName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_FOLDER\_NAME\]**

</dd> <dd>

The display name of this folder.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





