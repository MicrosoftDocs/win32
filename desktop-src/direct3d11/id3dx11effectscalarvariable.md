---
title: ID3DX11EffectScalarVariable interface (D3dx11effect.h)
description: An effect-scalar-variable interface accesses scalar values.
ms.assetid: 52e3b856-aa1b-4ed2-b140-7ae96ec1c94b
keywords:
- ID3DX11EffectScalarVariable interface Direct3D 11
- ID3DX11EffectScalarVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectScalarVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectScalarVariable interface

An effect-scalar-variable interface accesses scalar values.

## Members

The **ID3DX11EffectScalarVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectScalarVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectScalarVariable** interface has these methods.



| Method                                                             | Description                                          |
|:-------------------------------------------------------------------|:-----------------------------------------------------|
| [**GetBool**](id3dx11effectscalarvariable-getbool.md)             | Get a boolean variable.<br/>                   |
| [**GetBoolArray**](id3dx11effectscalarvariable-getboolarray.md)   | Get an array of boolean variables.<br/>        |
| [**GetFloat**](id3dx11effectscalarvariable-getfloat.md)           | Get a floating-point variable.<br/>            |
| [**GetFloatArray**](id3dx11effectscalarvariable-getfloatarray.md) | Get an array of floating-point variables.<br/> |
| [**GetInt**](id3dx11effectscalarvariable-getint.md)               | Get an integer variable.<br/>                  |
| [**GetIntArray**](id3dx11effectscalarvariable-getintarray.md)     | Get an array of integer variables.<br/>        |
| [**SetBool**](id3dx11effectscalarvariable-setbool.md)             | Set a boolean variable.<br/>                   |
| [**SetBoolArray**](id3dx11effectscalarvariable-setboolarray.md)   | Set an array of boolean variables.<br/>        |
| [**SetFloat**](id3dx11effectscalarvariable-setfloat.md)           | Set a floating-point variable.<br/>            |
| [**SetFloatArray**](id3dx11effectscalarvariable-setfloatarray.md) | Set an array of floating-point variables.<br/> |
| [**SetInt**](id3dx11effectscalarvariable-setint.md)               | Set an integer variable.<br/>                  |
| [**SetIntArray**](id3dx11effectscalarvariable-setintarray.md)     | Set an array of integer variables.<br/>        |



 

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

[**ID3DX11EffectVariable**](id3dx11effectvariable.md)
</dt> <dt>

[Effects 11 Interfaces](d3d11-graphics-reference-effects11-interfaces.md)
</dt> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

 





