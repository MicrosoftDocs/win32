---
Description: Specifies tolerance values for each vertex component when comparing vertices to determine if they are similar enough to be welded together.
ms.assetid: b28a17bd-5d5b-41b3-86d9-327f5497fc94
title: D3DX10\_WELD\_EPSILONS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DX10\_WELD\_EPSILONS structure

Specifies tolerance values for each vertex component when comparing vertices to determine if they are similar enough to be welded together.

## Syntax


```C++
typedef struct D3DX10_WELD_EPSILONS {
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
} D3DX10_WELD_EPSILONS, *LPD3DX10_WELD_EPSILONS;
```



## Members

<dl> <dt>

**Position**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Position

</dd> <dt>

**BlendWeights**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Blend weight

</dd> <dt>

**Normal**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Normal

</dd> <dt>

**PSize**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Point size value

</dd> <dt>

**Specular**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Specular lighting value

</dd> <dt>

**Diffuse**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Diffuse lighting value

</dd> <dt>

**Texcoord**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Eight texture coordinates

</dd> <dt>

**Tangent**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Tangent

</dd> <dt>

**Binormal**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Binormal

</dd> <dt>

**TessFactor**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Tessellation factor

</dd> </dl>

## Remarks

The LPD3DXWeldEpsilons type is defined as a pointer to the D3DXWeldEpsilons structure.


```
typedef D3DX_WELD_EPSILONS *LPD3DX_WELD_EPSILONS;
```



## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 




