---
title: ID3DX11EffectShaderVariable GetDomainShader method
description: Get a domain shader.
ms.assetid: fd95a4f0-7df3-4098-843f-0a1e22209603
keywords:
- GetDomainShader method Direct3D 11
- GetDomainShader method Direct3D 11 , ID3DX11EffectShaderVariable interface
- ID3DX11EffectShaderVariable interface Direct3D 11 , GetDomainShader method
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable.GetDomainShader
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX11EffectShaderVariable::GetDomainShader method

Get a domain shader.

## Syntax


```C++
HRESULT GetDomainShader(
   UINT               ShaderIndex,
   ID3D11DomainShader **ppPS
);
```



## Parameters

<dl> <dt>

*ShaderIndex* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Index of the domain shader.

</dd> <dt>

*ppPS* 
</dt> <dd>

Type: **[**ID3D11DomainShader**](https://msdn.microsoft.com/en-us/library/Ff476535(v=VS.85).aspx)\*\***

Pointer to an [**ID3D11DomainShader**](https://msdn.microsoft.com/en-us/library/Ff476535(v=VS.85).aspx) pointer that will be set to the domain shader on return.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



|                    |                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectShaderVariable](id3dx11effectshadervariable.md)
</dt> </dl>

 

 





