---
description: The ANDEXP structure contains an array of pattern matches used to evaluate frame data.
ms.assetid: e5f4c030-eb2b-4cc9-9032-9ad4701b6503
title: ANDEXP structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ANDEXP
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# ANDEXP structure

The **ANDEXP** structure contains an array of pattern matches used to evaluate frame data.

## Syntax


```C++
typedef struct _ANDEXP {
  DWORD        nPatternMatches;
  PATTERNMATCH PatternMatch[MAX_PATTERNS];
} ANDEXP, *LPANDEXP;
```



## Members

<dl> <dt>

**nPatternMatches**
</dt> <dd>

Number of pattern matches.

</dd> <dt>

**PatternMatch**
</dt> <dd>

Array of pattern match elements. Note that each **ANDEXP** structure can contain up to four pattern match elements. For more information about this member, see [Capture Filters](capture-filters.md).

</dd> </dl>

## Remarks

The patterns in the **PatternMatch**\[MAX\_PATTERNS\] array are joined as peers in logical OR statements in the format

(Pattern 1 \|\| Pattern 2 \|\| Pattern 3).

For more information about implementing this structure, see [Capture Filters](capture-filters.md) .

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PATTERNMATCH](patternmatch.md)
</dt> </dl>

 

 




