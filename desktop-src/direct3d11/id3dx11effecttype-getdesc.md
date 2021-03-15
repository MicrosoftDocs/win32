---
title: ID3DX11EffectType GetDesc method (D3dx11effect.h)
description: Get an effect-type description.
ms.assetid: 08a8a1b6-fe2d-431b-a0e4-d628f0ceb1a0
keywords:
- GetDesc method Direct3D 11
- GetDesc method Direct3D 11 , ID3DX11EffectType interface
- ID3DX11EffectType interface Direct3D 11 , GetDesc method
topic_type:
- apiref
api_name:
- ID3DX11EffectType.GetDesc
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectType::GetDesc method

Get an effect-type description.

## Syntax


```C++
HRESULT GetDesc(
   D3DX11_EFFECT_TYPE_DESC *pDesc
);
```



## Parameters

<dl> <dt>

*pDesc* 
</dt> <dd>

Type: **[**D3DX11\_EFFECT\_TYPE\_DESC**](d3dx11-effect-type-desc.md)\***

A pointer to an effect-type description. See [**D3DX11\_EFFECT\_TYPE\_DESC**](d3dx11-effect-type-desc.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

The effect-variable description contains data about the name, annotations, semantic, flags and buffer offset of the effect type.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectType](id3dx11effecttype.md)
</dt> </dl>

 

 





