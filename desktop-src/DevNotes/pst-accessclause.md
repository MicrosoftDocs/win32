---
description: Contains information about the access clause for the protected storage.
ms.assetid: 59634ada-4879-4ae7-b757-dfa6a88549af
title: PST_ACCESSCLAUSE structure (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PST_ACCESSCLAUSE
api_type: 
- HeaderDef
api_location: 
- Pstore.h
---

# PST\_ACCESSCLAUSE structure

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Contains information about the access clause for the protected storage.

## Syntax


```C++
typedef struct {
  DWORD                cbSize;
  PST_ACCESSCLAUSETYPE ClauseType;
  DWORD                cbClauseData;
  BYTE                 *pbClauseData;
} PST_ACCESSCLAUSE, *PPST_ACCESSCLAUSE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

**ClauseType**
</dt> <dd>

The type of data that is pointed to by the **pbClauseData** member. For more information, see [**PStore Types**](pstore-types.md).

</dd> <dt>

**cbClauseData**
</dt> <dd>

The size of the data that is pointed to by the **pbClauseData** member.

</dd> <dt>

**pbClauseData**
</dt> <dd>

A pointer to the access clause data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



## See also

<dl> <dt>

[**PST\_ACCESSRULE**](pst-accessrule.md)
</dt> </dl>

 

 
