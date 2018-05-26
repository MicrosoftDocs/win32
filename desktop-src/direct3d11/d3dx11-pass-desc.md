---
title: D3DX11\_PASS\_DESC structure
description: Describes an effect pass, which contains pipeline state.
ms.assetid: 3695b99f-d379-403b-aa10-e3e370a6c864
keywords:
- D3DX11_PASS_DESC structure Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11_PASS_DESC
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX11\_PASS\_DESC structure

Describes an effect pass, which contains pipeline state.

## Syntax


```C++
typedef struct _D3DX11_PASS_DESC {
  LPCSTR Name;
  UINT   Annotations;
  BYTE   *pIAInputSignature;
  SIZE_T IAInputSignatureSize;
  UINT   StencilRef;
  UINT   SampleMask;
  FLOAT  BlendFactor[4];
} D3DX11_PASS_DESC;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Name of this pass (**NULL** if not anonymous).

</dd> <dt>

**Annotations**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Number of annotations on this pass.

</dd> <dt>

**pIAInputSignature**
</dt> <dd>

Type: **[**BYTE**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

</dd> <dd>

Signature from the vertex shader or geometry shader (if there is no vertex shader) or **NULL** if neither exists.

</dd> <dt>

**IAInputSignatureSize**
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

Singature size in bytes.

</dd> <dt>

**StencilRef**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

The stencil-reference value used in the depth-stencil state.

</dd> <dt>

**SampleMask**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

The sample mask for the blend state.

</dd> <dt>

**BlendFactor**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

</dd> <dd>

The per-component blend factors (RGBA) for the blend state.

</dd> </dl>

## Remarks

D3DX11\_PASS\_DESC is used with [**ID3DX11EffectPass::GetDesc**](id3dx11effectpass-getdesc.md).

## Requirements



|                   |                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

 





