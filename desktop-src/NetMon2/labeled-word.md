---
description: The LABELED\_WORD structure defines a label that is displayed when a specific WORD property value is detected.
ms.assetid: bfb1d34e-4a07-493f-8e43-508b77cce581
title: LABELED_WORD structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_WORD
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_WORD structure

The **LABELED\_WORD** structure defines a label that is displayed when a specific WORD property value is detected.

## Syntax


```C++
typedef struct _LABELED_WORD {
  WORD  Value;
  LPSTR Label;
} LABELED_WORD, *LPLABELED_WORD;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

WORD value of the property that you want to detect.

</dd> <dt>

**Label**
</dt> <dd>

Textual description or label that is displayed when the WORD value specified in the **Value** member is detected.

</dd> </dl>

## Remarks

The **lpLabeledWordTable** member of the [SET](set.md) structure points to an array of SET structures to define one or more label value pairs. These pairs are used when you want to display a label in place of a specific WORD value that is found in a protocol packet.

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

 

 




