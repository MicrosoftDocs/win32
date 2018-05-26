---
title: ORDINALLIST structure
description: Do not use. This struct stores the array of index ordinals for two records. These ordinals can be used for seeking to the record in the table.
ms.assetid: ce984417-3cbf-40ed-9c20-8d8217ad5bc0
keywords:
- ORDINALLIST structure Windows Mail (formerly Outlook Express)
- ORGINALLIST structure Windows Mail (formerly Outlook Express)
- LPORDINALLIST structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ORGINALLIST
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ORDINALLIST structure

Do not use. This struct stores the array of index ordinals for two records. These ordinals can be used for seeking to the record in the table.

## Syntax


```C++
typedef struct tagORDINALLIST {
  ROWORDINAL rgiRecord1[CMAX_INDEXES];
  ROWORDINAL rgiRecord2[CMAX_INDEXES];
} ORGINALLIST, *LPORDINALLIST;
```



## Members

<dl> <dt>

**rgiRecord1**
</dt> <dd>

Type: **ROWORDINAL\[CMAX\_INDEXES\]**

</dd> <dd>

The first set of row ordinals.

</dd> <dt>

**rgiRecord2**
</dt> <dd>

Type: **ROWORDINAL\[CMAX\_INDEXES\]**

</dd> <dd>

The second set of row ordinals.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





