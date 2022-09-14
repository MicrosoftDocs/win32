---
title: Large Integers
description: The large integer functions and structures originally provided support for 64-bit values on 32-bit Windows.
ms.assetid: db4ffbd5-d9e4-4c95-83cc-6f0691c080d2
keywords:
- large integers
ms.topic: article
ms.date: 05/31/2018
---

# Large Integers

The large integer functions and structures originally provided support for 64-bit values on 32-bit Windows. Now, your C compiler may support 64-bit integers natively. For example, Microsoft Visual C++ supports the [**\_\_int64**](/windows/desktop/Midl/--int64) sized integer type. For more information, see the documentation included with your C compiler.

For information on 64-bit integers on 64-bit Windows, see [The New Data Types](/windows/desktop/WinProg64/the-new-data-types).

## Large Integer Operations

Applications can multiply signed or unsigned 32-bit integers, generating 64-bit results, by using the [**Int32x32To64**](/windows/desktop/api/Winnt/nf-winnt-int32x32to64) and [**UInt32x32To64**](/windows/desktop/api/Winnt/nf-winnt-uint32x32to64) functions. Applications can shift bits in 64-bit values to the left or right by using the [**Int64ShllMod32**](/windows/desktop/api/Winnt/nf-winnt-int64shllmod32), [**Int64ShraMod32**](/windows/desktop/api/Winnt/nf-winnt-int64shramod32), and [**Int64ShrlMod32**](/windows/desktop/api/Winnt/nf-winnt-int64shrlmod32) functions. These functions provide logical and arithmetic shifting.

Applications can also multiply and divide 32-bit values in a single operation by using the [**MulDiv**](/windows/desktop/api/Winbase/nf-winbase-muldiv) function. Although the result of the operation is a 32-bit value, the function stores the intermediate result as a 64-bit value, so that information is not lost when large 32-bit values are multiplied and divided.

## Large Integer Reference

-   [Large Integer Functions](large-integer-functions.md)
-   [Large Integer Structures](large-integer-structures.md)

 

 