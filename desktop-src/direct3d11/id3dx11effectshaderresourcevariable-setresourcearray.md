---
title: ID3DX11EffectShaderResourceVariable SetResourceArray method
description: Set an array of shader resources.
ms.assetid: 'b9597878-01af-42f3-9cc6-2ce1af4f08f6'
keywords: ["SetResourceArray method Direct3D 11", "SetResourceArray method Direct3D 11 , ID3DX11EffectShaderResourceVariable interface", "ID3DX11EffectShaderResourceVariable interface Direct3D 11 , SetResourceArray method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectShaderResourceVariable.SetResourceArray
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectShaderResourceVariable::SetResourceArray method

Set an array of shader resources.

## Syntax


```C++
HRESULT SetResourceArray(
   ID3D11ShaderResourceView **ppResources,
   UINT                     Offset,
   UINT                     Count
);
```



## Parameters

<dl> <dt>

*ppResources* 
</dt> <dd>

Type: **[**ID3D11ShaderResourceView**](id3d11shaderresourceview.md)\*\***

The address of an array of shader-resource-view interfaces. See [**ID3D11ShaderResourceView**](id3d11shaderresourceview.md).

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The zero-based array index to get the first interface.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of elements in the array.

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

[ID3DX11EffectShaderResourceVariable](id3dx11effectshaderresourcevariable.md)
</dt> </dl>

 

 





