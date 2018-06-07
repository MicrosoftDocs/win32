---
Description: Identifies the transformation matrix being set as the world transformation matrix.
ms.assetid: 2bf7ac8a-43d8-460e-a400-3b33e96441db
title: D3DTS\_WORLD macro
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

A [**D3DTRANSFORMSTATETYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtransformstatetype.htm) equivalent to [**D3DTS\_WORLDMATRIX(0)**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dts_worldmatrix.htm).

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

[**SetTransform**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settransform)
</dt> <dt>

[**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md)
</dt> </dl>

 

 




