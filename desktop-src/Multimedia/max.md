---
title: max macro (Minwindef.h)
description: The max macro compares two values and returns the larger one. The data type can be any numeric data type, signed or unsigned. The data type of the arguments and the return value is the same.
ms.assetid: 224d2ef7-6764-49c0-9782-51bfadbfb77f
keywords:
- max macro Windows Multimedia
topic_type:
- apiref
api_name:
- max
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# max macro

The **max** macro compares two values and returns the larger one. The data type can be any numeric data type, signed or unsigned. The data type of the arguments and the return value is the same.

## Syntax


```C++
 max(
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

The return value is the greater of the two specified values.

## Remarks

The **max** macro is defined as follows:


```C++
#define max(a, b)  (((a) > (b)) ? (a) : (b)) 
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Minwindef.h</dt> </dl> |



 

 





