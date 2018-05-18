---
title: D3D\_SHADER\_DATA structure
description: Describes shader data.
ms.assetid: '34cde0c9-e8ee-428d-86f5-87c91b95f5d8'
keywords: ["D3D_SHADER_DATA structure HLSL"]
topic_type:
- apiref
api_name:
- D3D_SHADER_DATA
api_location:
- D3Dcompiler.h
api_type:
- HeaderDef
---

# D3D\_SHADER\_DATA structure

Describes shader data.

## Syntax


```C++
typedef struct _D3D_SHADER_DATA {
  LPCVOID pBytecode;
  SIZE_T  BytecodeLength;
} D3D_SHADER_DATA;
```



## Members

<dl> <dt>

**pBytecode**
</dt> <dd>

A pointer to shader data.

</dd> <dt>

**BytecodeLength**
</dt> <dd>

Length of shader data that **pBytecode** points to.

</dd> </dl>

## Remarks

An array of **D3D\_SHADER\_DATA** structures is passed to [**D3DCompressShaders**](d3dcompressshaders.md) to compress the shader data into a more compact form.

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3Dcompiler.h</dt> </dl> |



## See also

<dl> <dt>

[Structures](dx-graphics-d3dcompiler-reference-structs.md)
</dt> </dl>

 

 





