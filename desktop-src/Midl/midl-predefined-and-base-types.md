---
title: MIDL Predefined and Base Types
description: MIDL supports the following base and predefined types.
ms.assetid: 72da24b6-253d-4032-ba0c-58b2542701fc
keywords:
- data types MIDL , predefined and base
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Predefined and Base Types

MIDL supports the following base and predefined types.



| Data type                                  | Description                                                                                                                                                                                             | Default sign     |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [**boolean**](boolean.md)                 | 8 bits. Not compatible with [**oleautomation**](oleautomation.md) interfaces; use VARIANT\_BOOL instead.                                                                                               | Unsigned         |
| [**byte**](byte.md)                       | 8 bits.                                                                                                                                                                                                 | (not applicable) |
| [**char**](char-idl.md)                   | 8 bits.                                                                                                                                                                                                 | Unsigned         |
| [**double**](double.md)                   | 64-bit floating point number.                                                                                                                                                                           | (not applicable) |
| [**error\_status\_t**](error-status-t.md) | 32-bit unsigned integer for returning status values for error handling.                                                                                                                                 | Unsigned         |
| [**float**](float.md)                     | 32-bit floating point number.                                                                                                                                                                           | (not applicable) |
| [**handle\_t**](handle-t.md)              | Primitive handle type for binding.                                                                                                                                                                      | (not applicable) |
| [**hyper**](hyper.md)                     | 64-bit integer.                                                                                                                                                                                         | Signed           |
| [**int**](int.md)                         | 32-bit integer. On 16-bit platforms, cannot appear in remote functions without a size qualifier such as [**short**](short.md), [**small**](small.md), [**long**](long.md) or [**hyper**](hyper.md). | Signed           |
| **\_\_int8**                               | 8-bit integer. Equivalent to **small**.                                                                                                                                                                 | Signed           |
| **\_\_int16**                              | 16-bit integer. Equivalent to **short**.                                                                                                                                                                | Signed           |
| **\_\_int32**                              | 32-bit integer. Equivalent to [**long**](long.md).                                                                                                                                                     | Signed           |
| [**\_\_int3264**](--int3264.md)           | An integer that is 32-bit on 32-bit platforms, and is 64-bit on 64-bit platforms.                                                                                                                       | Signed           |
| [**\_\_int64**](--int64.md)               | 64-bit integer. Equivalent to [**hyper**](hyper.md).                                                                                                                                                   | Signed           |
| [**long**](long.md)                       | 32-bit integer.                                                                                                                                                                                         | Signed           |
| [**short**](short.md)                     | 16-bt integer.                                                                                                                                                                                          | Signed           |
| [**small**](small.md)                     | 8-bit integer.                                                                                                                                                                                          | Signed           |
| [**void**](void.md)                       | Indicates that the procedure does not return a value.                                                                                                                                                   | (not applicable) |
| **void \***                                | 32-bit pointer for context handles only.                                                                                                                                                                | (not applicable) |
| [**wchar\_t**](wchar-t.md)                | 16-bit predefined type for wide characters.                                                                                                                                                             | Unsigned         |



 

 

 




