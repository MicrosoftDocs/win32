---
title: Storing a 64-bit Value
description: To store a 64-bit pointer value, use ULONG\_PTR. A ULONG\_PTR value is 32 bits when compiled with a 32-bit compiler and 64 bits when compiled with a 64-bit compiler.
ms.assetid: 0712e084-cf5e-470a-8f5d-0db2ef638f42
keywords:
- storing 64-bit values 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Storing a 64-bit Value

To store a 64-bit pointer value, use **ULONG\_PTR**. A **ULONG\_PTR** value is 32 bits when compiled with a 32-bit compiler and 64 bits when compiled with a 64-bit compiler.

The following examples use real-world code that has been ported to 64-bit Windows. Commentary on the steps to make the code 64-bit compatible is included.

## Example 1: Getting an Address

The following code illustrates a portable way to get an address.




| 
|
| Using ULONG (a 32-bit-only method) | <pre class="syntax" data-space="preserve"><code>ULONG getAnAddress( )Int *somePointerReturn( (ULONG) somePointer );</code></pre> | 
| Using ULONG_PTR (the portable method) | <pre class="syntax" data-space="preserve"><code>ULONG_PTR getAnAddress( )Int *somePointerReturn( (ULONG_PTR) somePointer );</code></pre> | 




 

## Example 2: Calculating an Address

The following code illustrates a portable way to calculate an address.




| 
|
| Using ULONG (a 32-bit-only method) | <pre class="syntax" data-space="preserve"><code>Int *somePointer;Int *someOtherPointer;somePointer = (int *)( (ULONG)someOtherPointer + 0x20 );</code></pre> | 
| Using ULONG_PTR (the portable method) | <pre class="syntax" data-space="preserve"><code>Int *somePointer;Int *someOtherPointer;somePointer = (int *)( (ULONG_PTR)someOtherPointer + 0x20 );</code></pre> | 




 

 

 




