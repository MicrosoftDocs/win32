---
Description: 'Describes a JPEG DC huffman table.'
ms.assetid: '9D6C18C3-F75C-41E0-9EFA-E882E89DE713'
title: 'DXGI\_JPEG\_DC\_HUFFMAN\_TABLE structure'
---

# DXGI\_JPEG\_DC\_HUFFMAN\_TABLE structure

Describes a JPEG DC huffman table.

## Syntax


```C++
typedef struct DXGI_JPEG_DC_HUFFMAN_TABLE {
  BYTE CodeCounts[12];
  BYTE CodeValues[12];
} DXGI_JPEG_DC_HUFFMAN_TABLE;
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

 

 




