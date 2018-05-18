---
Description: 'A description of a constant in a constant table.'
ms.assetid: 'd1970536-7195-4270-a1b9-b082ebe4f17f'
title: 'D3DXCONSTANT\_DESC structure'
---

# D3DXCONSTANT\_DESC structure

A description of a constant in a constant table.

## Syntax


```C++
typedef struct D3DXCONSTANT_DESC {
  LPCSTR              Name;
  D3DXREGISTER_SET    RegisterSet;
  UINT                RegisterIndex;
  UINT                RegisterCount;
  D3DXPARAMETER_CLASS Class;
  D3DXPARAMETER_TYPE  Type;
  UINT                Rows;
  UINT                Columns;
  UINT                Elements;
  UINT                StructMembers;
  UINT                Bytes;
  LPCVOID             DefaultValue;
} D3DXCONSTANT_DESC, *LPD3DXCONSTANT_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

</dd> <dd>

Name of the constant.

</dd> <dt>

**RegisterSet**
</dt> <dd>

Type: **[**D3DXREGISTER\_SET**](direct3d9.d3dxregister_set)**

</dd> <dd>

Constant data type. See [**D3DXREGISTER\_SET**](direct3d9.d3dxregister_set).

</dd> <dt>

**RegisterIndex**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Zero-based index of the constant in the table.

</dd> <dt>

**RegisterCount**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of registers that contain data.

</dd> <dt>

**Class**
</dt> <dd>

Type: **[**D3DXPARAMETER\_CLASS**](direct3d9.d3dxparameter_class)**

</dd> <dd>

Parameter class. See [**D3DXPARAMETER\_CLASS**](direct3d9.d3dxparameter_class).

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXPARAMETER\_TYPE**](direct3d9.d3dxparameter_type)**

</dd> <dd>

Parameter type. See [**D3DXPARAMETER\_TYPE**](direct3d9.d3dxparameter_type).

</dd> <dt>

**Rows**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of rows.

</dd> <dt>

**Columns**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of columns.

</dd> <dt>

**Elements**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of elements in the array.

</dd> <dt>

**StructMembers**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of structure member sub-parameters.

</dd> <dt>

**Bytes**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Data size in number of bytes.

</dd> <dt>

**DefaultValue**
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

</dd> <dd>

Pointer to the default value.

</dd> </dl>

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXCONSTANTTABLE\_DESC**](d3dxconstanttable-desc.md)
</dt> </dl>

 

 




