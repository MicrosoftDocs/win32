---
Description: Identifies subsequent transformation matrices that can be used to blend vertices by using the corresponding matrix and a blending (beta) weight value specified in the vertex format.
ms.assetid: cab444c2-b245-4d1a-a90c-745c92a2ea89
title: D3DTS\_WORLDn
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DTS\_WORLDn

Identifies subsequent transformation matrices that can be used to blend vertices by using the corresponding matrix and a blending (beta) weight value specified in the vertex format.

``` syntax
#define D3DTS_WORLDn 
#define D3DTS_WORLD1 D3DTS_WORLDMATRIX(1)
#define D3DTS_WORLD2 D3DTS_WORLDMATRIX(2)
#define D3DTS_WORLD3 D3DTS_WORLDMATRIX(3)
```

## Remarks

These macros are provided to facilitate porting existing applications to Direct3D 9.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Macros](dx9-graphics-reference-d3d-macros.md)
</dt> <dt>

[**SetTransform**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-settransform?branch=master)
</dt> <dt>

[**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md)
</dt> </dl>

 

 




