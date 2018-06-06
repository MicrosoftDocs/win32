---
Description: Maps indices in the range 0 through 255 to the corresponding transform states.
ms.assetid: b0a1548c-de5d-4eff-baf9-4aecb5e13443
title: D3DTS\_WORLDMATRIX macro
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

The [**D3DTRANSFORMSTATETYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dtransformstatetype.htm) that maps to the given *index*.

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

[**SetTransform**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-settransform)
</dt> </dl>

 

 




