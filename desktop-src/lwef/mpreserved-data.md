---
title: MPRESERVED_DATA structure (MpClient.h)
description: Reserved notification data.
ms.assetid: C92206BD-6E56-4B7D-ABB1-DC1149AE141D
keywords:
- MPRESERVED_DATA structure Legacy Windows Environment Features
- PMPRESERVED_DATA structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPRESERVED_DATA
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPRESERVED\_DATA structure

Reserved notification data.

## Syntax


```C++
typedef struct tagMPRESERVED_DATA {
  DWORD cbReservedData;
  BYTE  *pbReservedData;
} MPRESERVED_DATA, *PMPRESERVED_DATA;
```



## Members

<dl> <dt>

**cbReservedData**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Size of reserved data, in bytes.

</dd> <dt>

**pbReservedData**
</dt> <dd>

Type: **BYTE\***

</dd> <dd>

Pointer to reserved data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





