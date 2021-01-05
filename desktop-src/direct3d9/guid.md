---
description: Defines a GUID that can be used in other templates.
ms.assetid: dbfdd307-310f-4c80-b4aa-f16a81a9a372
title: Guid (DirectX 9)
ms.topic: reference
ms.date: 05/31/2018
---

# Guid (DirectX 9)

Defines a GUID that can be used in other templates.

``` syntax
template Guid
{
    < a42790e0-7810-11cf-8f52-0040333594a3 >
    DWORD data1;
    WORD data2;
    WORD data3;
    array UCHAR data4[8];
} 
```

Where the parameters together form the binary storage format for a GUID:

-   data1 - 32-bit unsigned integer data value
-   data2 - 16-bit unsigned integer data value
-   data3 - 16-bit unsigned integer data value
-   data4 - An array of unsigned characters

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



