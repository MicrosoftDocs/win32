---
Description: 'Maps indices in the range 0 through 255 to the corresponding transform states.'
ms.assetid: 'b0a1548c-de5d-4eff-baf9-4aecb5e13443'
title: 'D3DTS\_WORLDMATRIX macro'
---

# D3DTS\_WORLDMATRIX macro

Maps indices in the range 0 through 255 to the corresponding transform states.

## Syntax


```C++
D3DTRANSFORMSTATETYPE D3DTS_WORLDMATRIX(
   int index
);
```



## Parameters

<dl> <dt>

*index* 
</dt> <dd>

An index value in the range 0 through 255.

</dd> </dl>

## Return value

The [**D3DTRANSFORMSTATETYPE**](direct3d9.d3dtransformstatetype) that maps to the given *index*.

## Remarks

Transform states in the range 256 through 511 are reserved to store up to 256 matrices that can be indexed using 8-bit indices.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**SetTransform**](idirect3ddevice9--settransform.md)
</dt> </dl>

 

 




