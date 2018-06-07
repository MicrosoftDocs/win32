---
Description: Tests whether a pointer is aligned to a specified boundary. If not, this macro invokes the ASSERT macro. Ignored in retail builds.
ms.assetid: 4d9ec3a9-7107-45a3-a7aa-28d6e38fa92a
title: DbgAssertAligned macro
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DbgAssertAligned macro

Tests whether a pointer is aligned to a specified boundary. If not, this macro invokes the [**ASSERT**](assert.md) macro. Ignored in retail builds.

## Syntax


```C++
void DbgAssertAligned(
    ptr,
    alignment
);
```



## Parameters

<dl> <dt>

*ptr* 
</dt> <dd>

Pointer variable.

</dd> <dt>

*alignment* 
</dt> <dd>

Required alignment.

</dd> </dl>

## Return value

This macro does not return a value.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[Assert and Breakpoint Macros](assert-and-breakpoint-macros.md)
</dt> </dl>

 

 




