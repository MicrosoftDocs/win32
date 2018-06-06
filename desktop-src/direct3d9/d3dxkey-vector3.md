---
Description: Describes a vector key for use in key frame animation. It specifies a vector at a given time. This is used for scale and translation keys.
ms.assetid: 7a7ba2ce-c9f3-4a04-b865-39de9070868b
title: D3DXKEY\_VECTOR3 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DXKEY\_VECTOR3 structure

Describes a vector key for use in key frame animation. It specifies a vector at a given time. This is used for scale and translation keys.

## Syntax


```C++
typedef struct D3DXKEY_VECTOR3 {
  FLOAT       Time;
  D3DXVECTOR3 Value;
} D3DXKEY_VECTOR3, *LPD3DXKEY_VECTOR3;
```



## Members

<dl> <dt>

**Time**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Key frame time stamp.

</dd> <dt>

**Value**
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)**

</dd> <dd>

[**D3DXVECTOR3**](d3dxvector3.md) 3D vector that supplies scale and/or translation values.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




