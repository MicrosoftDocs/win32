---
title: ID3DX11EffectVariable AsMatrix method (D3dx11effect.h)
description: Get a matrix variable.
ms.assetid: 5d2baf65-ab0d-44df-bc6f-6ffae16cbb01
keywords:
- AsMatrix method Direct3D 11
- AsMatrix method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsMatrix method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsMatrix
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsMatrix method

Get a matrix variable.

## Syntax


```C++
ID3DX11EffectMatrixVariable* AsMatrix();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectMatrixVariable**](id3dx11effectmatrixvariable.md)\***

A pointer to a matrix variable. See [**ID3DX11EffectMatrixVariable**](id3dx11effectmatrixvariable.md).

## Remarks

AsMatrix returns a version of the effect variable that has been specialized to a matrix variable. Similar to a cast, this specialization will return an invalid object if the effect variable does not contain matrix data.

Applications can test the returned object for validity by calling [**IsValid**](id3dx11effectvariable-isvalid.md).

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

 





