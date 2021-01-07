---
description: Represents information about call targets for Control Flow Guard (CFG).
ms.assetid: 8DEF907F-3F23-4122-95CE-F413FC7FD96B
title: CFG_CALL_TARGET_INFO structure (Ntmmapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CFG_CALL_TARGET_INFO
api_type: 
- HeaderDef
api_location: 
- ntmmapi.h
---

# CFG\_CALL\_TARGET\_INFO structure

Represents information about call targets for Control Flow Guard (CFG).

## Syntax


```C++
typedef struct _CFG_CALL_TARGET_INFO {
  ULONG_PTR Offset;
  ULONG_PTR Flags;
} CFG_CALL_TARGET_INFO, *PCFG_CALL_TARGET_INFO;
```



## Members

<dl> <dt>

**Offset**
</dt> <dd>

Offset relative to a provided (start) virtual address. This offset should be 16 byte aligned.

</dd> <dt>

**Flags**
</dt> <dd>

Flags describing the operation to be performed on the address. If **CFG\_CALL\_TARGET\_VALID** is set, then the address will be marked valid for CFG. Otherwise, it will be marked an invalid call target.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Ntmmapi.h</dt> </dl> |



 

 




