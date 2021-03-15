---
title: ID3DX11EffectPass ComputeStateBlockMask method (D3dx11effect.h)
description: Generate a mask for allowing/preventing state changes.
ms.assetid: 584be931-0e22-43e6-b852-f0d2ab050bdd
keywords:
- ComputeStateBlockMask method Direct3D 11
- ComputeStateBlockMask method Direct3D 11 , ID3DX11EffectPass interface
- ID3DX11EffectPass interface Direct3D 11 , ComputeStateBlockMask method
topic_type:
- apiref
api_name:
- ID3DX11EffectPass.ComputeStateBlockMask
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectPass::ComputeStateBlockMask method

Generate a mask for allowing/preventing state changes.

## Syntax


```C++
HRESULT ComputeStateBlockMask(
   D3DX11_STATE_BLOCK_MASK *pStateBlockMask
);
```



## Parameters

<dl> <dt>

*pStateBlockMask* 
</dt> <dd>

Type: **[**D3DX11\_STATE\_BLOCK\_MASK**](d3dx11-state-block-mask.md)\***

A pointer to a state-block mask (see [**D3DX11\_STATE\_BLOCK\_MASK**](d3dx11-state-block-mask.md)).

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

 

 





