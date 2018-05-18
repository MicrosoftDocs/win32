---
Description: 'D3DXSHADER\_CONSTANTINFO structure'
ms.assetid: '0c42cea7-559e-4475-b66a-e932a9cb42de'
title: 'D3DXSHADER\_CONSTANTINFO structure'
---

# D3DXSHADER\_CONSTANTINFO structure

## Syntax


```C++
typedef struct D3DXSHADER_CONSTANTINFO {
  DWORD Name;
  WORD  RegisterSet;
  WORD  RegisterIndex;
  WORD  RegisterCount;
  WORD  Reserved;
  DWORD TypeInfo;
  DWORD DefaultValue;
} D3DXSHADER_CONSTANTINFO, *LPD3DXSHADER_CONSTANTINFO;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Offset from the beginning of this structure, in bytes, to the string that contains the constant information.

</dd> <dt>

**RegisterSet**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

Register set. See [**D3DXREGISTER\_SET**](direct3d9.d3dxregister_set).

</dd> <dt>

**RegisterIndex**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

The register index.

</dd> <dt>

**RegisterCount**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

Number of registers.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

Reserved.

</dd> <dt>

**TypeInfo**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Offset from the beginning of this structure, in bytes, to the string that contains the [**D3DXSHADER\_TYPEINFO**](d3dxshader-typeinfo.md) information.

</dd> <dt>

**DefaultValue**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Offset from the beginning of this structure, in bytes, to the string that contains the default value.

</dd> </dl>

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




