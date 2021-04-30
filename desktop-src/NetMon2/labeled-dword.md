---
description: The LABELED\_DWORD structure defines a label that is displayed when a specific DWORD property value is detected.
ms.assetid: 1aed3226-6d69-41b0-860b-4ffb5b905f1a
title: LABELED_DWORD structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LABELED_DWORD
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# LABELED\_DWORD structure

The **LABELED\_DWORD** structure defines a label that is displayed when a specific DWORD property value is detected.

## Syntax


```C++
typedef struct _LABELED_DWORD {
  DWORD Value;
  LPSTR Label;
} LABELED_DWORD, *LPLABELED_DWORD;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

DWORD value of the property that you want to detect.

</dd> <dt>

**Label**
</dt> <dd>

Textual description or label that is displayed when the DWORD value specified in the **Value** member is detected.

</dd> </dl>

## Remarks

The **lpLabeledDwordTable** member of the [SET](set.md) structure points to an array of **SET** structures that define one or more **Label** members of the DWORD value pairs. The pairs are used when you want to display a label in place of a specific DWORD value that is found in the protocol packet.

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

 

 




