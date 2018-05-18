---
Description: 'Identifies the transformation matrix being set as the world transformation matrix.'
ms.assetid: '2bf7ac8a-43d8-460e-a400-3b33e96441db'
title: 'D3DTS\_WORLD macro'
---

# D3DTS\_WORLD macro

Identifies the transformation matrix being set as the world transformation matrix.

## Syntax


```C++
D3DTRANSFORMSTATETYPE D3DTS_WORLD(void);
```



## Parameters

This macro has no parameters.

## Return value

A [**D3DTRANSFORMSTATETYPE**](direct3d9.d3dtransformstatetype) equivalent to [**D3DTS\_WORLDMATRIX(0)**](direct3d9.D3DTS_WORLDMATRIX).

## Remarks

This macro is provided to facilitate porting existing applications to Direct3D 9.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**SetTransform**](idirect3ddevice9--settransform.md)
</dt> <dt>

[**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md)
</dt> </dl>

 

 




