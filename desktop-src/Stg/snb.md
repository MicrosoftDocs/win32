---
title: SNB (Objidl.h)
description: A string name block (SNB) is a pointer to an array of pointers to strings, that ends in a NULL pointer.
ms.assetid: '8428a820-3d8a-41e0-9955-d355440e2ebc'
keywords:
- SNB
ms.topic: article
ms.date: 05/31/2018
---

# SNB

A string name block (**SNB**) is a pointer to an array of pointers to strings, that ends in a **NULL** pointer. String name blocks are used by the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface and by function calls that open storage objects. The strings point to contained storage objects or streams that are to be excluded in the open calls.


```C++
typedef OLESTR** SNB;
```



<dl> <dt>

**SNB**
</dt> <dd>

\[wire\_marshal(wireSNB)\]

</dd> </dl>

## Remarks

The **SNB** should be created by allocating a contiguous block of memory in which the pointers to strings are followed by a **NULL** pointer, which is then followed by the actual strings.

The marshaling of an **SNB** is based on the assumption that the **SNB** that was passed in was created in this way. Although it could be stored in other ways, the **SNB** created in this manner has the advantage of requiring only one allocation operation and one freeing of memory for all the strings.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Objidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Objidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage)
</dt> </dl>

 

 





