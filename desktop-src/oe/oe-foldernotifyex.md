---
title: FOLDERNOTIFYEX structure
description: FOLDERNOTIFYEX structure
ms.assetid: 'eb04c683-90ac-4df7-9a6e-e1c7fdc065da'
keywords: ["FOLDERNOTIFYEX structure Windows Mail (formerly Outlook Express)", "LPFOLDERNOTIFYEX structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- FOLDERNOTIFYEX
api_location:
- Msoeapi.h
api_type:
- HeaderDef
---

# FOLDERNOTIFYEX structure

\[**FOLDERNOTIFYEX** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
typedef struct tagFOLDERNOTIFYEX {
  FOLDERNOTIFYTYPE type;
  STOREFOLDERID    idFolderOld;
  STOREFOLDERID    idFolderNew;
} FOLDERNOTIFYEX, *LPFOLDERNOTIFYEX;
```



## Members

<dl> <dt>

**type**
</dt> <dd>

Type: **[**FOLDERNOTIFYTYPE**](oe-foldernotifytype.md)**

</dd> <dd></dd> <dt>

**idFolderOld**
</dt> <dd>

Type: **STOREFOLDERID**

</dd> <dd></dd> <dt>

**idFolderNew**
</dt> <dd>

Type: **STOREFOLDERID**

</dd> <dd></dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





