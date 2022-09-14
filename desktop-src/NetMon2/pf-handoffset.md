---
description: The PF\_HANDOFFSET structure defines the protocols that hand off to the parser, or the protocols that the parser hands off to.
ms.assetid: 2fda399d-a09e-47b4-bb2e-95996de9f950
title: PF_HANDOFFSET structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PF_HANDOFFSET
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PF\_HANDOFFSET structure

The **PF\_HANDOFFSET** structure defines the protocols that hand off to the parser, or the protocols that the parser hands off to.

## Syntax


```C++
typedef struct _PF_HANDOFFSET {
  DWORD           nEntries;
  PF_HANDOFFENTRY Entry[];
} PF_HANDOFFSET, *PPF_HANDOFFSET;
```



## Members

<dl> <dt>

**nEntries**
</dt> <dd>

Number of protocols.

</dd> <dt>

**Entry**
</dt> <dd>

An array of [PF\_HANDOFFENTRY](pf-handoffentry.md) structures that define each protocol.

</dd> </dl>

## Remarks

The [PF\_PARSERINFO](pf-parserinfo.md) structure uses the **PF\_HANDOFFSET** structure to list the following:

-   Which protocols hand off to the parser.
-   Which protocols the parser hands off to.

The **PF\_HANDOFFSET** structure must be allocated using **HeapAlloc**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_PARSERINFO](pf-parserinfo.md)
</dt> <dt>

[PF\_HANDOFFENTRY](pf-handoffentry.md)
</dt> </dl>

 

 




