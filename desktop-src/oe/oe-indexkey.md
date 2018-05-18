---
title: INDEXKEY structure
description: Do not use. Describes a key used in an index.
ms.assetid: '93ca7a60-b21d-483e-93d6-10a542cbe560'
keywords: ["INDEXKEY structure Windows Mail (formerly Outlook Express)", "LPINDEXKEY structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- INDEXKEY
api_type:
- NA
---

# INDEXKEY structure

Do not use. Describes a key used in an index.

## Syntax


```C++
typedef struct tagINDEXKEY {
  COLUMNORDINAL iColumn;
  COMPAREFLAGS  bCompare;
  DWORD         dwReserved;
} INDEXKEY, *LPINDEXKEY;
```



## Members

<dl> <dt>

**iColumn**
</dt> <dd>

Type: **COLUMNORDINAL**

</dd> <dd>

The index of the column being compared.

</dd> <dt>

**bCompare**
</dt> <dd>

Type: **[**COMPAREFLAGS**](oe-compareflags.md)**

</dd> <dd>

The compare flags to be used. See COMPAREFLAGS for a description of these.

</dd> <dt>

**dwReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Reserved. Set this **DWORD** to 0.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Product<br/>                  | Outlook Express 6.0<br/>                       |



 

 





