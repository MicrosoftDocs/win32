---
title: XMINT4 structure
description: Describes an 4D integer vector.
ms.assetid: 1f21727d-fcb4-4514-b30e-d8ef0e36c256
keywords:
- XMINT4 structure HLSL
topic_type:
- apiref
api_name:
- XMINT4
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XMINT4 structure

Describes an 4D integer vector.

## Syntax


``` syntax
typedef struct _XMINT4 {
  INT x;
  INT {
    INT {
      INT w;
    }z;
  }y;
} XMINT4;
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

 

 





