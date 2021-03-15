---
description: Describes a function used by an effect.
ms.assetid: 5d9deb82-7fe5-4408-8a6a-b34ecd97e8ba
title: D3DXFUNCTION_DESC structure (D3dx9effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFUNCTION_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9effect.h
---

# D3DXFUNCTION\_DESC structure

Describes a function used by an effect.

## Syntax


```C++
typedef struct D3DXFUNCTION_DESC {
  LPCSTR Name;
  UINT   Annotations;
} D3DXFUNCTION_DESC, *LPD3DXFUNCTION_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

</dd> <dd>

Function name.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Unused. This member will always be set to zero by [**GetFunctionDesc**](id3dxbaseeffect--getfunctiondesc.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 
