---
title: TABLEINDEX structure
description: Do not use. This struct represents an index on a table. It can be used to sort the records in the table by any of the columns.
ms.assetid: 3bec3f89-6d1a-4471-b57e-da48c4ed6203
keywords:
- TABLEINDEX structure Windows Mail (formerly Outlook Express)
- LPTABLEINDEX structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- TABLEINDEX
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TABLEINDEX structure

Do not use. This struct represents an index on a table. It can be used to sort the records in the table by any of the columns.

## Syntax


```C++
typedef struct tagTABLEINDEX {
  BYTE       cKeys;
  INDEXFLAGS bFlags;
  INDEXKEY   rgKey[CMAX_KEYS];
} TABLEINDEX, *LPTABLEINDEX;
```



## Members

<dl> <dt>

**cKeys**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The number of valid keys in rgKey.

</dd> <dt>

**bFlags**
</dt> <dd>

Type: **INDEXFLAGS**

</dd> <dd>

The flags for this index. The only valid flag is INDEX\_DESCENDING.

</dd> <dt>

**rgKey**
</dt> <dd>

Type: **[**INDEXKEY**](oe-indexkey.md)\[CMAX\_KEYS\]**

</dd> <dd>

The array of keys that are used to build this index. Precedence is given to the keys closest to the start of the array.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





