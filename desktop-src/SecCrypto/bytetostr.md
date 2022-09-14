---
description: The ByteToStr function converts an array of BYTE values to a hexadecimal character string.
ms.assetid: b1320e0f-fb67-4ed8-af3c-8ca7f0145468
title: ByteToStr
ms.topic: article
ms.date: 05/31/2018
---

# ByteToStr

The **ByteToStr** function converts an array of **BYTE** values to a hexadecimal character string.


```C++
#include <windows.h>

void ByteToStr(
     DWORD cb, 
     void* pv, 
     LPSTR sz)
//--------------------------------------------------------------------
// Parameters passed are:
//    pv is the array of BYTES to be converted.
//    cb is the number of BYTEs in the array.
//    sz is a pointer to the string to be returned.

{
//--------------------------------------------------------------------
//  Declare and initialize local variables.

BYTE* pb = (BYTE*) pv; // local pointer to a BYTE in the BYTE array
DWORD i;               // local loop counter
int b;                 // local variable

//--------------------------------------------------------------------
//  Begin processing loop.

for (i = 0; i<cb; i++)
{
   b = (*pb & 0xF0) >> 4;
   *sz++ = (b <= 9) ? b + '0' : (b - 10) + 'A';
   b = *pb & 0x0F;
   *sz++ = (b <= 9) ? b + '0' : (b - 10) + 'A';
   pb++;
}
*sz++ = 0;
}
```



 

 



