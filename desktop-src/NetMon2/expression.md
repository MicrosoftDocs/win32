---
description: Contains a group of ANDEXP arrays evaluated as peers.
ms.assetid: 14fa568c-9535-4415-923d-7e93ba4d2e80
title: EXPRESSION structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EXPRESSION
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# EXPRESSION structure

The **EXPRESSION** structure contains a group of **ANDEXP** arrays evaluated as peers in logical AND expressions, which have the format

(ANDEXP 1 && ANDEXP 2 && ANDEXP 3).

## Syntax


```C++
typedef struct _EXPRESSION {
  DWORD  nAndExps;
  ANDEXP AndExp[MAX_PATTERNS];
} EXPRESSION, *LPEXPRESSION;
```



## Members

<dl> <dt>

**nAndExps**
</dt> <dd>

Number of **ANDEXP** patterns.

</dd> <dt>

**AndExp**
</dt> <dd>

Array of **ANDEXP** patterns. The capture filter arranges all rows of this array as logical AND statements. Be aware that each EXPRESSION structure can contain a maximum of four **ANDEXP** patterns.

</dd> </dl>

## Remarks

For more information about implementing this structure as part of a capture filter, see [Capture Filters](capture-filters.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[ANDEXP](andexp.md)
</dt> <dt>

[CAPTUREFILTER](capturefilter.md)
</dt> </dl>

 

 




