---
title: D3DX11_EFFECT_SHADER_DESC structure (D3dx11effect.h)
description: Describes an effect shader.
ms.assetid: 4377eec6-f331-4cad-bf16-189d6296f886
keywords:
- D3DX11_EFFECT_SHADER_DESC structure Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11_EFFECT_SHADER_DESC
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX11\_EFFECT\_SHADER\_DESC structure

Describes an effect shader.

## Syntax


```C++
typedef struct _D3DX11_EFFECT_SHADER_DESC {
  const BYTE *pInputSignature;
  BOOL       IsInline;
  const BYTE *pBytecode;
  UINT       BytecodeLength;
  LPCSTR     SODecls[D3D11_SO_STREAM_COUNT];
  UINT       RasterizedStream;
  UINT       NumInputSignatureEntries;
  UINT       NumOutputSignatureEntries;
  UINT       NumPatchConstantSignatureEntries;
} D3DX11_EFFECT_SHADER_DESC;
```



## Members

<dl> <dt>

**pInputSignature**
</dt> <dd>

Type: **const [**BYTE**](/windows/desktop/WinProg/windows-data-types)\***

</dd> <dd>

Passed into CreateInputLayout. Only valid on a vertex shader or geometry shader. See [**ID3D11Device::CreateInputLayout**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createinputlayout).

</dd> <dt>

**IsInline**
</dt> <dd>

Type: **[**BOOL**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

**TRUE** is the shader is defined inline; otherwise **FALSE**.

</dd> <dt>

**pBytecode**
</dt> <dd>

Type: **const [**BYTE**](/windows/desktop/WinProg/windows-data-types)\***

</dd> <dd>

Shader bytecode.

</dd> <dt>

**BytecodeLength**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

The length of pBytecode.

</dd> <dt>

**SODecls**
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Stream out declaration string (for geometry shader with SO).

</dd> <dt>

**RasterizedStream**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Indicates which stream is rasterized. D3D11 geometry shaders can output up to four streams of data, one of which can be rasterized.

</dd> <dt>

**NumInputSignatureEntries**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Number of entries in the input signature.

</dd> <dt>

**NumOutputSignatureEntries**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Number of entries in the output signature.

</dd> <dt>

**NumPatchConstantSignatureEntries**
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Number of entries in the patch constant signature.

</dd> </dl>

## Remarks

D3DX11\_EFFECT\_SHADER\_DESC is used with [**ID3DX11EffectShaderVariable::GetShaderDesc**](id3dx11effectshadervariable-getshaderdesc.md).

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Structures](d3d11-graphics-reference-effects11-structures.md)
</dt> </dl>

 

