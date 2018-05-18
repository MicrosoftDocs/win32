---
title: ID3DX11EffectShaderVariable GetGeometryShader method
description: Get a geometry shader.
ms.assetid: '395d5c92-a941-4fbf-9bb9-b43634c1810b'
keywords: ["GetGeometryShader method Direct3D 11", "GetGeometryShader method Direct3D 11 , ID3DX11EffectShaderVariable interface", "ID3DX11EffectShaderVariable interface Direct3D 11 , GetGeometryShader method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable.GetGeometryShader
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectShaderVariable::GetGeometryShader method

Get a geometry shader.

## Syntax


```C++
HRESULT GetGeometryShader(
   UINT                 ShaderIndex,
   ID3D11GeometryShader **ppGS
);
```



## Parameters

<dl> <dt>

*ShaderIndex* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A zero-based index.

</dd> <dt>

*ppGS* 
</dt> <dd>

Type: **[**ID3D11GeometryShader**](id3d11geometryshader.md)\*\***

A pointer to an [**ID3D11GeometryShader**](id3d11geometryshader.md) pointer that will be set to the geometry shader on return.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 





