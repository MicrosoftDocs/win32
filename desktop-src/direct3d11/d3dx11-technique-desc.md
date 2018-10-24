---
title: D3DX11_TECHNIQUE_DESC structure
description: Describes an effect technique.
ms.assetid: 89690a68-d7e8-4f44-9f67-c55d0a400602
keywords:
- D3DX11_TECHNIQUE_DESC structure Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11_TECHNIQUE_DESC
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DX11\_TECHNIQUE\_DESC structure

Describes an effect technique.

## Syntax


```C++
typedef struct _D3DX11_TECHNIQUE_DESC {
  LPCSTR Name;
  UINT   Passes;
  UINT   Annotations;
} D3DX11_TECHNIQUE_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Name of this technique (NULL if not anonymous).

</dd> <dt>

**Passes**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of passes contained in the technique.

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of annotations on this technique.

</dd> </dl>

## Remarks

D3DX11\_TECHNIQUE\_DESC is used with [**ID3DX11EffectTechnique::GetDesc**](id3dx11effecttechnique-getdesc.md).

## Requirements



|                   |                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

 





