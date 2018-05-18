---
title: D3DX11\_EFFECT\_VARIABLE\_DESC structure
description: Describes an effect variable.
ms.assetid: '9c975ad4-b90e-4e69-b78f-4f5cc61083ff'
keywords: ["D3DX11_EFFECT_VARIABLE_DESC structure Direct3D 11"]
topic_type:
- apiref
api_name:
- D3DX11_EFFECT_VARIABLE_DESC
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
---

# D3DX11\_EFFECT\_VARIABLE\_DESC structure

Describes an effect variable.

## Syntax


```C++
typedef struct _D3DX11_EFFECT_VARIABLE_DESC {
  LPCSTR Name;
  LPCSTR Semantic;
  UINT   Flags;
  UINT   Annotations;
  UINT   BufferOffset;
  UINT   ExplicitBindPoint;
} D3DX11_EFFECT_VARIABLE_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Name of this variable, annotation, or structure member.

</dd> <dt>

**Semantic**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Semantic string of this variable or structure member (NULL for annotations or if not present).

</dd> <dt>

**Flags**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Optional flags for effect variables.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of annotations on this variable (always 0 for annotations).

</dd> <dt>

**BufferOffset**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Offset into containing cbuffer or tbuffer (always 0 for annotations or variables not in constant buffers).

</dd> <dt>

**ExplicitBindPoint**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Used if the variable has been explicitly bound using the register keyword. Check Flags for D3DX11\_EFFECT\_VARIABLE\_EXPLICIT\_BIND\_POINT.

</dd> </dl>

## Remarks

D3DX11\_EFFECT\_VARIABLE\_DESC is used with [**ID3DX11EffectVariable::GetDesc**](id3dx11effectvariable-getdesc.md).

## Requirements



|                   |                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

 





