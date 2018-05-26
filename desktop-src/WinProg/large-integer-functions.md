---
title: Large Integer Functions
description: The following functions are used with large integers.
ms.assetid: f34932f4-b126-4d6c-a2f0-3ad706fd5629
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Large Integer Functions

The following functions are used with large integers.

## In this section



| Function                                                                    | Description                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Int32x32To64**](/windows/win32/Winnt/nf-winnt-int32x32to64?branch=master)<br/>                             | Multiplies two signed 32-bit integers, returning a signed 64-bit integer result.<br/>                                                                                                                   |
| [**Int64ShllMod32**](/windows/win32/Winnt/nf-winnt-int64shllmod32?branch=master)<br/>                         | Performs a left logical shift operation on an unsigned 64-bit integer value. The function provides improved shifting code for left logical shifts where the shift count is in the range 0-31.<br/>      |
| [**Int64ShraMod32**](/windows/win32/Winnt/nf-winnt-int64shramod32?branch=master)<br/>                         | Performs a right arithmetic shift operation on a signed 64-bit integer value. The function provides improved shifting code for right arithmetic shifts where the shift count is in the range 0-31.<br/> |
| [**Int64ShrlMod32**](/windows/win32/Winnt/nf-winnt-int64shrlmod32?branch=master)<br/>                         | Performs a right logical shift operation on an unsigned 64-bit integer value. The function provides improved shifting code for right logical shifts where the shift count is in the range 0-31.<br/>    |
| [**MulDiv**](/windows/win32/Winbase/nf-winbase-muldiv?branch=master)<br/>                                         | Multiplies two 32-bit values and then divides the 64-bit result by a third 32-bit value.<br/>                                                                                                           |
| [**Multiply128**](/windows/win32/Winnt/nf-winnt-multiply128?branch=master)<br/>                               | Multiplies two 64-bit integers to produce a 128-bit integer.<br/>                                                                                                                                       |
| [**MultiplyExtract128**](/windows/win32/Winnt/nf-winnt-multiplyextract128?branch=master)<br/>                 | Multiplies two 64-bit integers to produce a 128-bit integer, shifts the product to the right by the specified number of bits, and returns the low 64 bits of the result.<br/>                           |
| [**MultiplyHigh**](/windows/win32/Winnt/nf-winnt-multiplyhigh?branch=master)<br/>                             | Multiplies two 64-bit integers to produce a 128-bit integer and gets the high 64 bits.<br/>                                                                                                             |
| [**PopulationCount64**](/windows/win32/Winnt/nf-winnt-populationcount64?branch=master)<br/>                   | Counts the number of one bits (population count) in a 64-bit unsigned integer.<br/>                                                                                                                     |
| [**ShiftLeft128**](/windows/win32/winnt/nf-winnt-shiftleft128?branch=master)<br/>                             | Shifts 128-bit left.<br/>                                                                                                                                                                               |
| [**ShiftRight128**](/windows/win32/winnt/nf-winnt-shiftright128?branch=master)<br/>                           | Shifts 128-bit right.<br/>                                                                                                                                                                              |
| [**UInt32x32To64**](/windows/win32/Winnt/nf-winnt-uint32x32to64?branch=master)<br/>                           | Multiplies two unsigned 32-bit integers, returning an unsigned 64-bit integer result.<br/>                                                                                                              |
| [**UnsignedMultiply128**](/windows/win32/Winnt/nf-winnt-unsignedmultiply128?branch=master)<br/>               | Multiplies two unsigned 64-bit integers to produce an unsigned 128-bit integer.<br/>                                                                                                                    |
| [**UnsignedMultiplyExtract128**](/windows/win32/Winnt/nf-winnt-unsignedmultiplyextract128?branch=master)<br/> | Multiplies two unsigned 64-bit integers to produce an unsigned 128-bit integer, shifts the product to the right by the specified number of bits, and returns the low 64 bits of the result.<br/>        |
| [**UnsignedMulitplyHigh**](/windows/win32/Winnt/nf-winnt-unsignedmultiplyhigh?branch=master)<br/>             | Multiplies two 64-bit integers to produce a 128-bit integer and gets the high unsigned 64 bits.<br/>                                                                                                    |



 

 

 





