---
title: Storing a 64-bit Value
description: To store a 64-bit pointer value, use ULONG\_PTR. A ULONG\_PTR value is 32 bits when compiled with a 32-bit compiler and 64 bits when compiled with a 64-bit compiler.
ms.assetid: '0712e084-cf5e-470a-8f5d-0db2ef638f42'
keywords: ["storing 64-bit values 64-bit Windows Programming"]
---

# Storing a 64-bit Value

To store a 64-bit pointer value, use **ULONG\_PTR**. A **ULONG\_PTR** value is 32 bits when compiled with a 32-bit compiler and 64 bits when compiled with a 64-bit compiler.

The following examples use real-world code that has been ported to 64-bit Windows. Commentary on the steps to make the code 64-bit compatible is included.

## Example 1: Getting an Address

The following code illustrates a portable way to get an address.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Using ULONG (a 32-bit-only method)</td>
<td><pre class="syntax" data-space="preserve"><code>ULONG getAnAddress( )
Int *somePointer
Return( (ULONG) somePointer );</code></pre></td>
</tr>
<tr class="even">
<td>Using ULONG_PTR (the portable method)</td>
<td><pre class="syntax" data-space="preserve"><code>ULONG_PTR getAnAddress( )
Int *somePointer
Return( (ULONG_PTR) somePointer );</code></pre></td>
</tr>
</tbody>
</table>



 

## Example 2: Calculating an Address

The following code illustrates a portable way to calculate an address.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Using ULONG (a 32-bit-only method)</td>
<td><pre class="syntax" data-space="preserve"><code>Int *somePointer;
Int *someOtherPointer;
somePointer = (int *)( (ULONG)someOtherPointer + 0x20 );</code></pre></td>
</tr>
<tr class="even">
<td>Using ULONG_PTR (the portable method)</td>
<td><pre class="syntax" data-space="preserve"><code>Int *somePointer;
Int *someOtherPointer;
somePointer = (int *)( (ULONG_PTR)someOtherPointer + 0x20 );</code></pre></td>
</tr>
</tbody>
</table>



 

 

 




