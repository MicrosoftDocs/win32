---
Description: Describes a matrix.
ms.assetid: d6b98a32-e745-4724-b8ce-a81a3f5416f3
title: D3DMATRIX
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DMATRIX
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DMATRIX

Describes a matrix.

``` syntax
typedef struct _D3DMATRIX {
    union {
        struct {
            float        _11, _12, _13, _14;
            float        _21, _22, _23, _24;
            float        _31, _32, _33, _34;
            float        _41, _42, _43, _44;

        };
        float m[4][4];
    };
} D3DMATRIX;
```

Derived types: \*LPD3DMATRIX

## Members



| Item                                                        | Description                                                                                                                                                                                                     |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="_ij"></span><span id="_IJ"></span>\_ij<br/> | An array of floats that represent a 4x4 matrix, where i is the row number and j is the column number. For example, \_34 means the same as \[a₃₄\], the component in the third row and fourth column.<br/> |



 

## Remarks

In Direct3D, the \_34 element of a projection matrix cannot be a negative number. If your application needs to use a negative value in this location, it should scale the entire projection matrix by -1 instead.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetTransform**](https://msdn.microsoft.com/library/Bb174414(v=VS.85).aspx)
</dt> <dt>

[**MultiplyTransform**](https://msdn.microsoft.com/library/Bb174422(v=VS.85).aspx)
</dt> <dt>

[**SetTransform**](https://msdn.microsoft.com/library/Bb174463(v=VS.85).aspx)
</dt> <dt>

**SetTransform**
</dt> <dt>

[**D3DXMATRIX**](d3dxmatrix.md)
</dt> <dt>

[Transforms (Direct3D 9)](transforms.md)
</dt> </dl>

 

 




