---
title: min macro (Minwindef.h)
description: The min macro compares two values and returns the smaller one. The data type can be any numeric data type, signed or unsigned. The data type of the arguments and the return value is the same.
ms.assetid: c7d5094c-6f26-4799-95c8-804a8b48d39e
keywords:
- min macro Windows Multimedia
topic_type:
- apiref
api_name:
- min
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# min macro

The **min** macro compares two values and returns the smaller one. The data type can be any numeric data type, signed or unsigned. The data type of the arguments and the return value is the same.

## Syntax


```C++
 min(
    value1,
    value2
);
```



## Parameters

<dl> <dt>

*value1* 
</dt> <dd>

Specifies the first of two values.

</dd> <dt>

*value2* 
</dt> <dd>

Specifies the second of two values.

</dd> </dl>

## Return value

The return value is the smaller of the two specified values.

## Remarks

The **min** macro is defined as follows:


```C++
#define min(a, b)  (((a) < (b)) ? (a) : (b)) 
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Minwindef.h</dt> </dl> |



 

 





