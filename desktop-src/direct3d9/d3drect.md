---
Description: Defines a rectangle.
ms.assetid: a8590411-fd34-4048-a41f-b4155d955573
title: D3DRECT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DRECT
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DRECT structure

Defines a rectangle.

## Syntax


```C++
typedef struct D3DRECT {
  LONG x1;
  LONG y1;
  LONG x2;
  LONG y2;
} D3DRECT;
```



## Members

<dl> <dt>

**x1**
</dt> <dd>

Type: **[**LONG**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

The x-coordinate of the upper-left corner of the rectangle.

</dd> <dt>

**y1**
</dt> <dd>

Type: **[**LONG**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

The y-coordinate of the upper-left corner of the rectangle.

</dd> <dt>

**x2**
</dt> <dd>

Type: **[**LONG**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

The x-coordinate of the lower-right corner of the rectangle.

</dd> <dt>

**y2**
</dt> <dd>

Type: **[**LONG**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

The y-coordinate of the lower-right corner of the rectangle.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**Clear**](https://msdn.microsoft.com/library/Bb174352(v=VS.85).aspx)
</dt> </dl>

 

 




