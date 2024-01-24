---
title: ID3DX11EffectVariable AsScalar method (D3dx11effect.h)
description: Get a scalar variable.
ms.assetid: 5cc02fb3-351a-4309-9145-1ed7d759a650
keywords:
- AsScalar method Direct3D 11
- AsScalar method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , AsScalar method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.AsScalar
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::AsScalar method

Get a scalar variable.

## Syntax


```C++
ID3DX11EffectScalarVariable* AsScalar();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**ID3DX11EffectScalarVariable**](id3dx11effectscalarvariable.md)\***

A pointer to a scalar variable. See [**ID3DX11EffectScalarVariable**](id3dx11effectscalarvariable.md).

## Remarks

AsScalar returns a version of the effect variable that has been specialized to a scalar variable. Similar to a cast, this specialization will return an invalid object if the effect variable does not contain scalar data.

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

 

 





