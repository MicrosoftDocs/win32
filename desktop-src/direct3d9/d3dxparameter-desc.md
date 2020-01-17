---
Description: Describes a parameter used for an effect object.
ms.assetid: 60d19b52-67ef-4903-bbde-922a8fac1ad8
title: D3DXPARAMETER_DESC structure (D3dx9effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPARAMETER_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9effect.h
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

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Name of the parameter.

</dd> <dt>

**Semantic**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Semantic meaning, also called the usage.

</dd> <dt>

**Class**
</dt> <dd>

Type: **[**D3DXPARAMETER\_CLASS**](https://msdn.microsoft.com/library/Bb205378(v=VS.85).aspx)**

</dd> <dd>

Parameter class. Set this to one of the values in [**D3DXPARAMETER\_CLASS**](https://msdn.microsoft.com/library/Bb205378(v=VS.85).aspx).

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXPARAMETER\_TYPE**](https://msdn.microsoft.com/library/Bb205380(v=VS.85).aspx)**

</dd> <dd>

Parameter type. Set this to one of the values in [**D3DXPARAMETER\_TYPE**](https://msdn.microsoft.com/library/Bb205380(v=VS.85).aspx).

</dd> <dt>

**Rows**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of rows in the array.

</dd> <dt>

**Columns**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of columns in the array.

</dd> <dt>

**Elements**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of elements in the array.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of annotations.

</dd> <dt>

**StructMembers**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of structure members.

</dd> <dt>

**Flags**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Parameter attributes. See [Effect Constants](dx9-graphics-reference-effects-constants.md).

</dd> <dt>

**Bytes**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

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

 

 




