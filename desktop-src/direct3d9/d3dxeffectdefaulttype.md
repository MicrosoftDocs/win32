---
description: Effect data types. The data is contained in the pValue member of D3DXEFFECTDEFAULT.
ms.assetid: d698ad6e-2ce2-48d6-90be-49bc08f172a9
title: D3DXEFFECTDEFAULTTYPE enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXEFFECTDEFAULTTYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXEFFECTDEFAULTTYPE enumeration

Effect data types. The data is contained in the pValue member of [**D3DXEFFECTDEFAULT**](d3dxeffectdefault.md).

## Syntax


```C++
typedef enum D3DXEFFECTDEFAULTTYPE { 
  D3DXEDT_STRING      = 1,
  D3DXEDT_FLOATS      = 2,
  D3DXEDT_DWORD       = 3,
  D3DXEDT_FORCEDWORD  = 0x7fffffff
} D3DXEFFECTDEFAULTTYPE, *LPD3DXEFFECTDEFAULTTYPE;
```



## Constants

<dl> <dt>

<span id="D3DXEDT_STRING"></span><span id="d3dxedt_string"></span>**D3DXEDT\_STRING**
</dt> <dd>

The data type is a NULL-terminated ASCII text string.

</dd> <dt>

<span id="D3DXEDT_FLOATS"></span><span id="d3dxedt_floats"></span>**D3DXEDT\_FLOATS**
</dt> <dd>

The data type is an array of type float. The number of float types in the array is specified by NumBytes in [**D3DXEFFECTDEFAULT**](d3dxeffectdefault.md).

</dd> <dt>

<span id="D3DXEDT_DWORD"></span><span id="d3dxedt_dword"></span>**D3DXEDT\_DWORD**
</dt> <dd>

The data type is a DWORD.

</dd> <dt>

<span id="D3DXEDT_FORCEDWORD"></span><span id="d3dxedt_forcedword"></span>**D3DXEDT\_FORCEDWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




