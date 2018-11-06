---
Description: A description of a constant in a constant table.
ms.assetid: d1970536-7195-4270-a1b9-b082ebe4f17f
title: D3DXCONSTANT_DESC structure
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCONSTANT_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
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

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Name of the constant.

</dd> <dt>

**RegisterSet**
</dt> <dd>

Type: **[**D3DXREGISTER\_SET**](https://msdn.microsoft.com/en-us/library/Bb205424(v=VS.85).aspx)**

</dd> <dd>

Constant data type. See [**D3DXREGISTER\_SET**](https://msdn.microsoft.com/en-us/library/Bb205424(v=VS.85).aspx).

</dd> <dt>

**RegisterIndex**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Zero-based index of the constant in the table.

</dd> <dt>

**RegisterCount**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of registers that contain data.

</dd> <dt>

**Class**
</dt> <dd>

Type: **[**D3DXPARAMETER\_CLASS**](https://msdn.microsoft.com/en-us/library/Bb205378(v=VS.85).aspx)**

</dd> <dd>

Parameter class. See [**D3DXPARAMETER\_CLASS**](https://msdn.microsoft.com/en-us/library/Bb205378(v=VS.85).aspx).

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXPARAMETER\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb205380(v=VS.85).aspx)**

</dd> <dd>

Parameter type. See [**D3DXPARAMETER\_TYPE**](https://msdn.microsoft.com/en-us/library/Bb205380(v=VS.85).aspx).

</dd> <dt>

**Rows**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of rows.

</dd> <dt>

**Columns**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of columns.

</dd> <dt>

**Elements**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of elements in the array.

</dd> <dt>

**StructMembers**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of structure member sub-parameters.

</dd> <dt>

**Bytes**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Data size in number of bytes.

</dd> <dt>

**DefaultValue**
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

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

 

 




