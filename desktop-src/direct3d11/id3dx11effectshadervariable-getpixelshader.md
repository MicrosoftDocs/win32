---
title: ID3DX11EffectShaderVariable GetPixelShader method
description: Get a pixel shader.
ms.assetid: 4ce4b248-23b9-4135-a2b4-262e63247688
keywords:
- GetPixelShader method Direct3D 11
- GetPixelShader method Direct3D 11 , ID3DX11EffectShaderVariable interface
- ID3DX11EffectShaderVariable interface Direct3D 11 , GetPixelShader method
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable.GetPixelShader
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX11EffectShaderVariable::GetPixelShader method

Get a pixel shader.

## Syntax


```C++
HRESULT GetPixelShader(
   UINT              ShaderIndex,
   ID3D11PixelShader **ppPS
);
```



## Parameters

<dl> <dt>

*ShaderIndex* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A zero-based index.

</dd> <dt>

*ppPS* 
</dt> <dd>

Type: **[**ID3D11PixelShader**](/windows/win32/D3D11/?branch=master)\*\***

A pointer to an [**ID3D11PixelShader**](/windows/win32/D3D11/?branch=master) pointer that will be set to the pixel shader on return.

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

 

 





