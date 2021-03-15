---
description: Describes an effect object.
ms.assetid: 161d3e7a-213a-4a83-a1b5-837b0aab96bf
title: D3DXEFFECT_DESC structure (D3dx9effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXEFFECT_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9effect.h
---

# D3DXEFFECT\_DESC structure

Describes an effect object.

## Syntax


```C++
typedef struct D3DXEFFECT_DESC {
  LPCSTR Creator;
  UINT   Parameters;
  UINT   Techniques;
  UINT   Functions;
} D3DXEFFECT_DESC, *LPD3DXEFFECT_DESC;
```



## Members

<dl> <dt>

**Creator**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

String that contains the name of the effect creator.

</dd> <dt>

**Parameters**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of parameters used for effect.

</dd> <dt>

**Techniques**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of techniques that can render the effect.

</dd> <dt>

**Functions**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of functions that can render the effect.

</dd> </dl>

## Remarks

An effect object can contain multiple rendering techniques and parameters for the same effect.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 
