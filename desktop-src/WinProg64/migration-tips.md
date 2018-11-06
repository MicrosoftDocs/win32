---
title: Migration Tips
description: It is important to consider address calculations and pointer arithmetic when porting your code to 64-bit Windows.
ms.assetid: ae562a85-d6ea-4595-b54c-0a28e6532cf5
keywords:
- 64-bit Windows programming guide 64-bit Windows Programming , migration tips
- migration tips 64-bit Windows Programming
- compatibility 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Migration Tips

The two primary areas of concern when examining your code for 64-bit compatibility are as follows:

-   Address calculations
-   Pointer arithmetic

For many reasons, developers have stored addresses as a **ULONG** value. After all, on 32-bit Windows, an address, a pointer, and a **ULONG** value are all 32 bits long. However, on 64-bit Windows, an address and a **ULONG** are not the same length. While a **ULONG** remains a 32-bit value, all pointers are now 64-bit values.

## In this Section

-   [General Porting Guidelines](general-porting-guidelines.md)
-   [Storing a 64-bit Value](storing-a-64-bit-value.md)
-   [Common Compiler Errors](common-compiler-errors.md)
-   [Additional Considerations](additional-considerations.md)

 

 




