---
description: The LABELED\_LARGEINT structure defines a label that is displayed when a specific LARGEINT property value is detected.
ms.assetid: ca565be0-96bb-4265-9422-793db0723563
title: LABELED_LARGEINT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_LARGEINT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_LARGEINT structure

The **LABELED\_LARGEINT** structure defines a label that is displayed when a specific LARGEINT property value is detected.

## Syntax


```C++
typedef struct _LABELED_LARGEINT {
  LARGE_INTEGER Value;
  LPSTR         Label;
} LABELED_LARGEINT, *LPLABELED_LARGEINT;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

LARGEINT value of the property that you want to detect.

</dd> <dt>

**Label**
</dt> <dd>

Textual description or label that is displayed when the LARGEINT value specified in the **Value** member is detected.

</dd> </dl>

## Remarks

The **lpLabeledLargeIntTable** member of the [SET](set.md) structure points to an array of **SET** structures that define one or more **Label** members of the LARGEINT value pairs. The pairs are used when you want to display a label in place of a specific LARGEINT value that is found in a protocol packet.

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

 

 




