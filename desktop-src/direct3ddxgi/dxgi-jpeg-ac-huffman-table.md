---
Description: Describes a JPEG AC huffman table.
ms.assetid: E1923FFA-E7E5-4158-9793-3E7F5A6EA7FA
title: DXGI\_JPEG\_AC\_HUFFMAN\_TABLE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DXGI\_JPEG\_AC\_HUFFMAN\_TABLE structure

Describes a JPEG AC huffman table.

## Syntax


```C++
typedef struct DXGI_JPEG_AC_HUFFMAN_TABLE {
  BYTE CodeCounts[16];
  BYTE CodeValues[162];
} DXGI_JPEG_AC_HUFFMAN_TABLE;
```



## Members

<dl> <dt>

**CodeCounts**
</dt> <dd>

The number of codes for each code length.

</dd> <dt>

**CodeValues**
</dt> <dd>

The Huffman code values, in order of increasing code length.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dxgitype.h</dt> </dl> |



## See also

<dl> <dt>

[DXGI Structures](d3d10-graphics-reference-dxgi-structures.md)
</dt> </dl>

 

 




