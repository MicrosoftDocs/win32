---
description: The RANGE structure defines a range of valid property values.
ms.assetid: 7bd14410-f5c1-487b-8776-405567991e5a
title: RANGE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RANGE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# RANGE structure

The **RANGE** structure defines a range of valid property values.

## Syntax


```C++
typedef struct range {
  DWORD MinValue;
  DWORD MaxValue;
} RANGE, *LPRANGE;
```



## Members

<dl> <dt>

**MinValue**
</dt> <dd>

Lowest possible value in a range.

</dd> <dt>

**MaxValue**
</dt> <dd>

Highest possible value in a range.

</dd> </dl>

## Remarks

The **RANGE** structure is used to specify a valid range of numbers for a protocol property. If the **DataQualifier** member of the **PROPERTYINFO** structure is set to **PROP\_QUAL\_RANGE**, the **lpRange** member of the [PROPERTYINFO](propertyinfo.md) structure must provide a pointer to a **RANGE** structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PROPERTYINFO](propertyinfo.md)
</dt> </dl>

 

 




