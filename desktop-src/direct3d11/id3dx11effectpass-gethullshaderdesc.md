---
title: ID3DX11EffectPass GetHullShaderDesc method (D3dx11effect.h)
description: Get hull-shader description.
ms.assetid: 1a683e61-da9a-4d78-8073-a6104625852b
keywords:
- GetHullShaderDesc method Direct3D 11
- GetHullShaderDesc method Direct3D 11 , ID3DX11EffectPass interface
- ID3DX11EffectPass interface Direct3D 11 , GetHullShaderDesc method
topic_type:
- apiref
api_name:
- ID3DX11EffectPass.GetHullShaderDesc
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectPass::GetHullShaderDesc method

Get hull-shader description.

## Syntax


```C++
HRESULT GetHullShaderDesc(
   D3DX11_PASS_SHADER_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* 
</dt> <dd>

Type: **[**D3DX11\_PASS\_SHADER\_DESC**](d3dx11-pass-shader-desc.md)\***

A pointer to a hull-shader description (see [**D3DX11\_PASS\_SHADER\_DESC**](d3dx11-pass-shader-desc.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectPass](id3dx11effectpass.md)
</dt> </dl>

 

 





