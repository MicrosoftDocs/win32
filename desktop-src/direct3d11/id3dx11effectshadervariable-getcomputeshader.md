---
title: ID3DX11EffectShaderVariable GetComputeShader method
description: Get a compute shader.
ms.assetid: 16a48be1-4e73-4206-837f-615f8d624086
keywords:
- GetComputeShader method Direct3D 11
- GetComputeShader method Direct3D 11 , ID3DX11EffectShaderVariable interface
- ID3DX11EffectShaderVariable interface Direct3D 11 , GetComputeShader method
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable.GetComputeShader
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX11EffectShaderVariable::GetComputeShader method

Get a compute shader.

## Syntax


```C++
HRESULT GetComputeShader(
   UINT                ShaderIndex,
   ID3D11ComputeShader **ppPS
);
```



## Parameters

<dl> <dt>

*ShaderIndex* 
</dt> <dd>

Type: **[**UINT**](https://docs.microsoft.com/windows/desktop/WinProg/windows-data-types)**

Index of the compute shader.

</dd> <dt>

*ppPS* 
</dt> <dd>

Type: **[**ID3D11ComputeShader**](https://msdn.microsoft.com/en-us/library/Ff476363(v=VS.85).aspx)\*\***

Pointer to an [**ID3D11ComputeShader**](https://msdn.microsoft.com/en-us/library/Ff476363(v=VS.85).aspx) pointer that will be set to the compute shader on return.

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

 

 





