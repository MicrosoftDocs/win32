---
title: ID3DX11EffectShaderVariable GetPatchConstantSignatureElementDesc method
description: Get a patch constant signature description.
ms.assetid: 72a86cf6-ace2-4306-ac5c-37d888c087f7
keywords:
- GetPatchConstantSignatureElementDesc method Direct3D 11
- GetPatchConstantSignatureElementDesc method Direct3D 11 , ID3DX11EffectShaderVariable interface
- ID3DX11EffectShaderVariable interface Direct3D 11 , GetPatchConstantSignatureElementDesc method
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderVariable.GetPatchConstantSignatureElementDesc
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

# ID3DX11EffectShaderVariable::GetPatchConstantSignatureElementDesc method

Get a patch constant signature description.

## Syntax


```C++
HRESULT GetPatchConstantSignatureElementDesc(
   UINT                           ShaderIndex,
   UINT                           Element,
   D3D11_SIGNATURE_PARAMETER_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*ShaderIndex* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A zero-based shader index.

</dd> <dt>

*Element* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A zero-based element index.

</dd> <dt>

*pDesc* 
</dt> <dd>

Type: **[**D3D11\_SIGNATURE\_PARAMETER\_DESC**](/windows/win32/D3D11Shader/ns-d3d11shader-_d3d11_signature_parameter_desc?branch=master)\***

A pointer to a parameter description (see [**D3D11\_SIGNATURE\_PARAMETER\_DESC**](/windows/win32/D3D11Shader/ns-d3d11shader-_d3d11_signature_parameter_desc?branch=master)).

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

 

 





