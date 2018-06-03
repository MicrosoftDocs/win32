---
Description: Specifies tolerance values for each vertex component when comparing vertices to determine if they are similar enough to be welded together.
ms.assetid: 534903da-ff65-4629-9be9-66c9daed6ef5
title: D3DXWELDEPSILONS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DXWELDEPSILONS structure

Specifies tolerance values for each vertex component when comparing vertices to determine if they are similar enough to be welded together.

## Syntax


```C++
typedef struct _D3DXWELDEPSILONS {
  FLOAT Position;
  FLOAT BlendWeights;
  FLOAT Normal;
  FLOAT PSize;
  FLOAT Specular;
  FLOAT Diffuse;
  FLOAT Texcoord[8];
  FLOAT Tangent;
  FLOAT Binormal;
  FLOAT TessFactor;
} D3DXWELDEPSILONS, *LPD3DXWELDEPSILONS;
```



## Members

<dl> <dt>

**Position**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Position

</dd> <dt>

**BlendWeights**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Blend weight

</dd> <dt>

**Normal**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Normal

</dd> <dt>

**PSize**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Point size value

</dd> <dt>

**Specular**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Specular lighting value

</dd> <dt>

**Diffuse**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Diffuse lighting value

</dd> <dt>

**Texcoord**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Eight texture coordinates

</dd> <dt>

**Tangent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Tangent

</dd> <dt>

**Binormal**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Binormal

</dd> <dt>

**TessFactor**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Tessellation factor

</dd> </dl>

## Remarks

The LPD3DXWELDEPSILONS type is defined as a pointer to the **D3DXWELDEPSILONS** structure.


```
typedef D3DXWELDEPSILONS *LPD3DXWELDEPSILONS;
```



## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXWeldVertices**](d3dxweldvertices.md)
</dt> </dl>

 

 




