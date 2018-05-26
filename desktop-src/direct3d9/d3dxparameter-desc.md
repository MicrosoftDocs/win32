---
Description: Describes a parameter used for an effect object.
ms.assetid: 60d19b52-67ef-4903-bbde-922a8fac1ad8
title: D3DXPARAMETER\_DESC structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXPARAMETER\_DESC structure

Describes a parameter used for an effect object.

## Syntax


```C++
typedef struct D3DXPARAMETER_DESC {
  LPCSTR              Name;
  LPCSTR              Semantic;
  D3DXPARAMETER_CLASS Class;
  D3DXPARAMETER_TYPE  Type;
  UINT                Rows;
  UINT                Columns;
  UINT                Elements;
  UINT                Annotations;
  UINT                StructMembers;
  DWORD               Flags;
  UINT                Bytes;
} D3DXPARAMETER_DESC, *LPD3DXPARAMETER_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

</dd> <dd>

Name of the parameter.

</dd> <dt>

**Semantic**
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

</dd> <dd>

Semantic meaning, also called the usage.

</dd> <dt>

**Class**
</dt> <dd>

Type: **[**D3DXPARAMETER\_CLASS**](direct3d9.d3dxparameter_class)**

</dd> <dd>

Parameter class. Set this to one of the values in [**D3DXPARAMETER\_CLASS**](direct3d9.d3dxparameter_class).

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXPARAMETER\_TYPE**](direct3d9.d3dxparameter_type)**

</dd> <dd>

Parameter type. Set this to one of the values in [**D3DXPARAMETER\_TYPE**](direct3d9.d3dxparameter_type).

</dd> <dt>

**Rows**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of rows in the array.

</dd> <dt>

**Columns**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of columns in the array.

</dd> <dt>

**Elements**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of elements in the array.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of annotations.

</dd> <dt>

**StructMembers**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

Number of structure members.

</dd> <dt>

**Flags**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Parameter attributes. See [Effect Constants](dx9-graphics-reference-effects-constants.md).

</dd> <dt>

**Bytes**
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

</dd> <dd>

The size of the parameter, in bytes.

</dd> </dl>

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 




