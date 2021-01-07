---
description: Associates a group name and its handle.
ms.assetid: 76f3fe37-cf85-42ab-8f9e-3ab2c6053dcd
title: GROUPINFO structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GROUPINFO
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# GROUPINFO structure

The **GROUPINFO** structure associates a group name and its handle.

## Syntax


```C++
typedef struct {
  char   szGroupName[EXPERTGROUPNAMELENGTH+1];
  HGROUP hGroup;
} GROUPINFO, *PGROUPINFO;
```



## Members

<dl> <dt>

**szGroupName**
</dt> <dd>

Incremented value of an array in the **GROUPNAME** structure.

</dd> <dt>

**hGroup**
</dt> <dd>

Handle to a group.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




