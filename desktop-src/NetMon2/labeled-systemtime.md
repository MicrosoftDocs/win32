---
description: The LABELED\_SYSTEMTIME structure defines a label that is displayed when a specific SYSTEMTIME property value is detected.
ms.assetid: 307b490a-af8e-4f2a-a45a-33a84fcb4d5c
title: LABELED_SYSTEMTIME structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_SYSTEMTIME
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_SYSTEMTIME structure

The **LABELED\_SYSTEMTIME** structure defines a label that is displayed when a specific SYSTEMTIME property value is detected.

## Syntax


```C++
typedef struct _LABELED_SYSTEMTIME {
  SYSTEMTIME Value;
  LPSTR      Label;
} LABELED_SYSTEMTIME, *LPLABELED_SYSTEMTIME;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

SYSTEMTIME value of a property that you want to detect.

</dd> <dt>

**Label**
</dt> <dd>

Textual description or label that is displayed when the SYSTEMTIME value specified in the **Value** member is detected.

</dd> </dl>

## Remarks

The **lpLabeledSystemTimeTable** member of the [SET](set.md) structure points to an array of **SET** structures that define one or more label value pairs. The pairs are used when you want to display a label in place of a specific LARGEINT value that is found in the protocol packet.

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

 

 




