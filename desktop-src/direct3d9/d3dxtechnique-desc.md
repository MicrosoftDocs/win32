---
description: Describes a technique used by an effect.
ms.assetid: 7ba2dbb3-8039-4d1c-ad9d-130d9bf3d80a
title: D3DXTECHNIQUE_DESC structure (D3dx9effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXTECHNIQUE_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9effect.h
---

# D3DXTECHNIQUE\_DESC structure

Describes a technique used by an effect.

## Syntax


```C++
typedef struct D3DXTECHNIQUE_DESC {
  LPCSTR Name;
  UINT   Passes;
  UINT   Annotations;
} D3DXTECHNIQUE_DESC, *LPD3DXTECHNIQUE_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

String that contains the technique name.

</dd> <dt>

**Passes**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of rendering passes the technique requires. See Remarks.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

The number of annotations. See [Add Information to Effect Parameters with\_Annotations](using-an-effect.md).

</dd> </dl>

## Remarks

Some video cards can render two textures in a single pass. However, if a card does not have this capability, it is often possible to render the same effect in two passes, using one texture for each pass.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 
