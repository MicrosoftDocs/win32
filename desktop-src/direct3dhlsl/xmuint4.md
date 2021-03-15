---
title: XMUINT4 structure
description: Describes an 4D unsigned integer vector.
ms.assetid: 289293e5-882e-479c-886e-82c802f824b5
keywords:
- XMUINT4 structure HLSL
topic_type:
- apiref
api_name:
- XMUINT4
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XMUINT4 structure

Describes an 4D unsigned integer vector.

## Syntax


``` syntax
typedef struct _XMUINT4 {
  UINT x;
  UINT {
    UINT {
      UINT w;
    }z;
  }y;
} XMUINT4;
```



## Members

<dl> <dt>

**x**
</dt> <dd>

x-component of the vector.

</dd> <dt>

**y**
</dt> <dd>

y-component of the vector.

<dl> <dt>

**z**
</dt> <dd>

z-component of the vector.

<dl> <dt>

**w**
</dt> <dd>

w-component of the vector.

</dd> </dl> </dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX\_DXGIFormatConvert.inl</dt> </dl> |



## See also

<dl> <dt>

[Structures](format-conversion-structures.md)
</dt> <dt>

[Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md)
</dt> </dl>

 

 





