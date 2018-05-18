---
Description: 'Describes a quaternion key for use in key frame animation. A quaternion key is a quaternion value at a given time.'
ms.assetid: '8f5b74a3-f712-40ac-942c-a2189c2327c8'
title: 'D3DXKEY\_QUATERNION structure'
---

# D3DXKEY\_QUATERNION structure

Describes a quaternion key for use in key frame animation. A quaternion key is a quaternion value at a given time.

## Syntax


```C++
typedef struct D3DXKEY_QUATERNION {
  FLOAT          Time;
  D3DXQUATERNION Value;
} D3DXKEY_QUATERNION, *LPD3DXKEY_QUATERNION;
```



## Members

<dl> <dt>

**Time**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Time value.

</dd> <dt>

**Value**
</dt> <dd>

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)**

</dd> <dd>

[**D3DXQUATERNION**](d3dxquaternion.md) quaternion that supplies rotation values.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




