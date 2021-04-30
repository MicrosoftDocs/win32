---
description: The LABELED\_BYTE structure defines a labeled BIT pair. The Label of the labeled BIT pair is displayed when a specific byte property value is detected.
ms.assetid: 6dc6a773-da75-4ffe-878f-b30ceef2acb1
title: LABELED_BYTE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_BYTE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_BYTE structure

The **LABELED\_BYTE** structure defines a labeled BIT pair. The **Label** of the labeled BIT pair is displayed when a specific byte property value is detected.

## Syntax


```C++
typedef struct _LABELED_BYTE {
  BYTE  Value;
  LPSTR Label;
} LABELED_BYTE, *LPLABELED_BYTE;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

BYTE value of the property that you want to detect.

</dd> <dt>

**Label**
</dt> <dd>

Textual description or label that is displayed when the value specified in the **Value** member is detected.

</dd> </dl>

## Remarks

The **lpLabeledByteTable** member of the [SET](set.md) structure points to an array of **SET** structures that define one or more **Label** members of the BYTE value pairs. These pairs are used when you want to display a label in place of a specific BYTE value that is found in the protocol packet.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[SET](set.md)
</dt> </dl>

 

 




