---
title: Bitwise-Comparison Operators
description: Bitwise-Comparison Operators
ms.assetid: 9343e7f6-67fd-422f-9364-bbdeabb2fb3a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bitwise-Comparison Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Bitwise-comparison operators are also available in addition to the traditional relational operators. The **AllOf** (^a) and **SomeOf** (^s) operators allow property values to be compared against bit pattern on a bit-by-bit basis. The following table gives an example of each bitwise-comparison operator.



| Operator | Example         | Note                                                                   |
|----------|-----------------|------------------------------------------------------------------------|
| ^a       | @attrib^a 0x820 | Specifies compressed documents that have the archive bit attribute on. |
| ^s       | @attrib^s 0x20  | Specifies any documents that have the archived bit set on.             |



 

The **AllOf** and **SomeOf** operators can be used in conjunction with the relational operators when performing vector property comparisons. When using the ^a operator, every vector element on the left side must pass the comparison against every vector element on the right side. When using the ^s operator, at least one of the vector elements must match the comparison for the test to pass.

The following table illustrates what happens with the comparison of two vectors with different numbers of elements.



| Test                  | Result | Note                                                                                                                                                                               |
|-----------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (1; 2; 3)^a&gt;(1; 2) | FAILS  | (1; 2; 3)&gt;(1; 2) normally passes. However, when ^a is specified, the test fails since the first element on the left side is less than the second element on the right side.     |
| (1; 2; 3)^s&gt;(2; 1) | PASSES | (1; 2; 3)&gt;(2; 1) normally fails. However, when ^s is specified, the test passes because the third element on the left side is greater than the first element on the right side. |



 

 

 




