---
title: D3DX11\_EFFECT\_TYPE\_DESC structure
description: Describes an effect-variable type.
ms.assetid: 'bf2aa5b7-c68c-42bb-ae70-2fe16f8669a4'
keywords: ["D3DX11_EFFECT_TYPE_DESC structure Direct3D 11"]
topic_type:
- apiref
api_name:
- D3DX11_EFFECT_TYPE_DESC
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
---

# D3DX11\_EFFECT\_TYPE\_DESC structure

Describes an effect-variable type.

## Syntax


```C++
typedef struct _D3DX11_EFFECT_TYPE_DESC {
  LPCSTR                      TypeName;
  D3D10_SHADER_VARIABLE_CLASS Class;
  D3D10_SHADER_VARIABLE_TYPE  Type;
  UINT                        Elements;
  UINT                        Members;
  UINT                        Rows;
  UINT                        Columns;
  UINT                        PackedSize;
  UINT                        UnpackedSize;
  UINT                        Stride;
} D3DX11_EFFECT_TYPE_DESC;
```



## Members

<dl> <dt>

**TypeName**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Name of the type, for example "float4" or "MyStruct".

</dd> <dt>

**Class**
</dt> <dd>

Type: **[**D3D10\_SHADER\_VARIABLE\_CLASS**](https://msdn.microsoft.com/library/windows/desktop/bb172440)**

</dd> <dd>

The variable class (see [**D3D10\_SHADER\_VARIABLE\_CLASS**](https://msdn.microsoft.com/library/windows/desktop/bb172440)).

</dd> <dt>

**Type**
</dt> <dd>

Type: **[**D3D10\_SHADER\_VARIABLE\_TYPE**](https://msdn.microsoft.com/library/windows/desktop/bb172443)**

</dd> <dd>

The variable type (see [**D3D10\_SHADER\_VARIABLE\_TYPE**](https://msdn.microsoft.com/library/windows/desktop/bb172443)).

</dd> <dt>

**Elements**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of elements in this type (0 if not an array).

</dd> <dt>

**Members**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of members (0 if not a structure).

</dd> <dt>

**Rows**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of rows in this type (0 if not a numeric primitive).

</dd> <dt>

**Columns**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of columns in this type (0 if not a numeric primitive).

</dd> <dt>

**PackedSize**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of bytes required to represent this data type, when tightly packed.

</dd> <dt>

**UnpackedSize**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of bytes occupied by this data type, when laid out in a constant buffer.

</dd> <dt>

**Stride**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of bytes to seek between elements, when laid out in a constant buffer.

</dd> </dl>

## Remarks

D3DX11\_EFFECT\_TYPE\_DESC is used with [**ID3DX11EffectType::GetDesc**](id3dx11effecttype-getdesc.md)

## Requirements



|                   |                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

 





