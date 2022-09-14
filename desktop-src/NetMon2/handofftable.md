---
description: The HANDOFFTABLE structure defines the protocols of a handoff table.
ms.assetid: '6bb7465b-c1ba-4ffe-aecf-8125993c309a'
title: HANDOFFTABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HANDOFFTABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# HANDOFFTABLE structure

The **HANDOFFTABLE** structure defines the protocols of a handoff table.

This structure is filled in by Network Monitor based on information in a user supplied .ini file provided when calling the [**CreateHandoffTable**](createhandofftable.md) function.

## Syntax


```C++
typedef struct HANDOFFTABLE {
  DWORD          hot_sig;
  DWORD          hot_NumEntries;
  LPHANDOFFENTRY hot_Entries;
} HANDOFFTABLE, *LPHANDOFFTABLE;
```



## Members

<dl> <dt>

**hot\_sig**
</dt> <dd>

Signature that identifies this table as a handoff table.

</dd> <dt>

**hot\_NumEntries**
</dt> <dd>

Number of entries that Network Monitor added to the handoff table.

</dd> <dt>

**hot\_Entries**
</dt> <dd>

Handoff table.

</dd> </dl>

## Remarks

This structure, and its associated HANDOFFENTRY structures, are filled in by Network Monitor when Network Monitor creates a handoff table.

The protocol information that is used when creating a handoff table is provided in an .ini file supplied by the application when [**CreateHandoffTable**](createhandofftable.md) is called.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[HANDOFFENTRY](handoffentry.md)
</dt> <dt>

[CreateHandoffTable](createhandofftable.md)
</dt> </dl>

 

 




