---
description: The PF\_FOLLOWSET structure defines the protocols that may precede or follow a protocol.
ms.assetid: ef444af9-edae-4547-9548-8a682c279f08
title: PF_FOLLOWSET structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PF_FOLLOWSET
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PF\_FOLLOWSET structure

The **PF\_FOLLOWSET** structure defines the protocols that may precede or follow a protocol.

## Syntax


```C++
typedef struct _PF_FOLLOWSET {
  DWORD          nEntries;
  PF_FOLLOWENTRY Entry[];
} PF_FOLLOWSET, *PPF_FOLLOWSET;
```



## Members

<dl> <dt>

**nEntries**
</dt> <dd>

Number of protocols in the list.

</dd> <dt>

**Entry**
</dt> <dd>

Array of [PF\_FOLLOWENTRY](pf-followentry.md) structures that describe each protocol.

</dd> </dl>

## Remarks

The [PF\_PARSERINFO](pf-parserinfo.md) structure uses the **PF\_FOLLOWSET** structure to list the protocols that may precede or follow the protocol that the parser detects.

Network Monitor uses the information in the **PF\_FOLLOWSET** structure to update the follow sets of specific parsers. The **PF\_FOLLOWSET** structure must be allocated using **HeapAlloc**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_FOLLOWENTRY](pf-followentry.md)
</dt> <dt>

[PF\_PARSERINFO](pf-parserinfo.md)
</dt> </dl>

 

 




