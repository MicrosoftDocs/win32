---
title: Large Integers
description: The large integer functions and structures originally provided support for 64-bit values on 32-bit Windows.
ms.assetid: 'db4ffbd5-d9e4-4c95-83cc-6f0691c080d2'
keywords: ["large integers"]
---

# Large Integers

The large integer functions and structures originally provided support for 64-bit values on 32-bit Windows. Now, your C compiler may support 64-bit integers natively. For example, Microsoft Visual C++ supports the [**\_\_int64**](https://msdn.microsoft.com/library/windows/desktop/aa367391) sized integer type. For more information, see the documentation included with your C compiler.

For information on 64-bit integers on 64-bit Windows, see [The New Data Types](https://msdn.microsoft.com/library/windows/desktop/aa384264).

## Large Integer Operations

Applications can multiply signed or unsigned 32-bit integers, generating 64-bit results, by using the [**Int32x32To64**](int32x32to64.md) and [**UInt32x32To64**](uint32x32to64.md) functions. Applications can shift bits in 64-bit values to the left or right by using the [**Int64ShllMod32**](int64shllmod32.md), [**Int64ShraMod32**](int64shramod32.md), and [**Int64ShrlMod32**](int64shrlmod32.md) functions. These functions provide logical and arithmetic shifting.

Applications can also multiply and divide 32-bit values in a single operation by using the [**MulDiv**](muldiv.md) function. Although the result of the operation is a 32-bit value, the function stores the intermediate result as a 64-bit value, so that information is not lost when large 32-bit values are multiplied and divided.

## Large Integer Reference

-   [Large Integer Functions](large-integer-functions.md)
-   [Large Integer Structures](large-integer-structures.md)

 

 




