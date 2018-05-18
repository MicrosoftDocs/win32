---
title: ID3DX11EffectSamplerVariable SetSampler method
description: Set sampler state.
ms.assetid: '1826923d-d770-4d79-818a-a42a279f0a8c'
keywords: ["SetSampler method Direct3D 11", "SetSampler method Direct3D 11 , ID3DX11EffectSamplerVariable interface", "ID3DX11EffectSamplerVariable interface Direct3D 11 , SetSampler method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectSamplerVariable.SetSampler
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectSamplerVariable::SetSampler method

Set sampler state.

## Syntax


```C++
HRESULT SetSampler(
   UINT               Index,
   ID3D11SamplerState *pSampler
);
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Index into an array of sampler interfaces. If there is only one sampler interface, use 0.

</dd> <dt>

*pSampler* 
</dt> <dd>

Type: **[**ID3D11SamplerState**](id3d11samplerstate.md)\***

Pointer to an [**ID3D11SamplerState**](id3d11samplerstate.md) interface containing the sampler state.

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

[ID3DX11EffectSamplerVariable](id3dx11effectsamplervariable.md)
</dt> </dl>

 

 





