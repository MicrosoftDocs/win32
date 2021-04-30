---
description: The HANDOFFENTRY structure defines a specific protocol entry in a HANDOFFTABLE structure.
ms.assetid: 85793326-3007-4dd9-9325-3447d6e09883
title: HANDOFFENTRY structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HANDOFFENTRY
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# HANDOFFENTRY structure

The **HANDOFFENTRY** structure defines a specific protocol entry in a **HANDOFFTABLE** structure.

This structure is filled in by Network Monitor based on information in a user supplied .ini file provided when calling the [**CreateHandoffTable**](createhandofftable.md) function. This structure should never be explicitly modified by an application.

## Syntax


```C++
typedef struct _SESSIONSTATS {
  DWORD      hoe_sig;
  DWORD      hoe_ProtIdentNumber;
  HPPROTOCOL hoe_ProtocolHandle;
  DWORD      hoe_ProtocolData;
} HANDOFFENTRY, *LPHANDOFFENTRY;
```



## Members

<dl> <dt>

**hoe\_sig**
</dt> <dd>

Signature that identifies this entry as a handoff table entry.

</dd> <dt>

**hoe\_ProtIdentNumber**
</dt> <dd>

Protocol number provided by user supplied .ini file.

</dd> <dt>

**hoe\_ProtocolHandle**
</dt> <dd>

Handle of protocol created using the protocol name provided by user supplied .ini file.

</dd> <dt>

**hoe\_ProtocolData**
</dt> <dd>

Protocol instance data provided by user supplied .ini file.

</dd> </dl>

## Remarks

This structure is filled in by Network Monitor when Network Monitor creates a handoff table.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[HANDOFFTABLE](handofftable.md)
</dt> </dl>

 

 




