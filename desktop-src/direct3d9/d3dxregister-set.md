---
description: Data type of the register.
ms.assetid: b54530d3-4267-4b41-9a16-59d400ef3e18
title: D3DXREGISTER_SET enumeration (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXREGISTER_SET
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXREGISTER\_SET enumeration

Data type of the register.

## Syntax


```C++
typedef enum _D3DXREGISTER_SET { 
  D3DXRS_BOOL,
  D3DXRS_INT4,
  D3DXRS_FLOAT4,
  D3DXRS_SAMPLER,
  D3DXRS_FORCE_DWORD  = 0x7fffffff
} D3DXREGISTER_SET, *LPD3DXREGISTER_SET;
```



## Constants

<dl> <dt>

<span id="D3DXRS_BOOL"></span><span id="d3dxrs_bool"></span>**D3DXRS\_BOOL**
</dt> <dd>

Boolean value.

</dd> <dt>

<span id="D3DXRS_INT4"></span><span id="d3dxrs_int4"></span>**D3DXRS\_INT4**
</dt> <dd>

4D integer number.

</dd> <dt>

<span id="D3DXRS_FLOAT4"></span><span id="d3dxrs_float4"></span>**D3DXRS\_FLOAT4**
</dt> <dd>

4D floating-point number.

</dd> <dt>

<span id="D3DXRS_SAMPLER"></span><span id="d3dxrs_sampler"></span>**D3DXRS\_SAMPLER**
</dt> <dd>

The register contains 4D sampler data.

</dd> <dt>

<span id="D3DXRS_FORCE_DWORD"></span><span id="d3dxrs_force_dword"></span>**D3DXRS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[**D3DXSHADER\_CONSTANTINFO**](d3dxshader-constantinfo.md)
</dt> <dt>

[**D3DXCONSTANT\_DESC**](d3dxconstant-desc.md)
</dt> </dl>

 

 




