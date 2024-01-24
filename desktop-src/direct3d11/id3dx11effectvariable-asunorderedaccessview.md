---
title: ID3DX11EffectVariable AsUnorderedAccessView method (D3dx11effect.h)
description: Get an unordered-access-view variable.
ms.assetid: e8b7c104-09f7-4bfb-9980-a5603550b723
keywords:
- AsUnorderedAccessView method Direct3D 11
- AsUnorderedAccessView method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsUnorderedAccessView method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsUnorderedAccessView
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsUnorderedAccessView method

Get an unordered-access-view variable.

## Syntax


```C++
ID3DX11EffectUnorderedAccessViewVariable* AsUnorderedAccessView();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectUnorderedAccessViewVariable**](id3dx11effectunorderedaccessviewvariable.md)\***

A pointer to an unordered-access-view variable. See [**ID3DX11EffectUnorderedAccessViewVariable**](id3dx11effectunorderedaccessviewvariable.md).

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

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

 





