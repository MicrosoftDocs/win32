---
title: ID3DX11EffectVectorVariable interface (D3dx11effect.h)
description: A vector-variable interface accesses a four-component vector.
ms.assetid: 191d373b-0562-4d7b-ac3f-cd24abf259bc
keywords:
- ID3DX11EffectVectorVariable interface Direct3D 11
- ID3DX11EffectVectorVariable interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11EffectVectorVariable
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVectorVariable interface

A vector-variable interface accesses a four-component vector.

## Members

The **ID3DX11EffectVectorVariable** interface inherits from [**ID3DX11EffectVariable**](id3dx11effectvariable.md). **ID3DX11EffectVectorVariable** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11EffectVectorVariable** interface has these methods.



| Method                                                                         | Description                                                                         |
|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**GetBoolVector**](id3dx11effectvectorvariable-getboolvector.md)             | Get a four-component vector that contains boolean data.<br/>                  |
| [**GetBoolVectorArray**](id3dx11effectvectorvariable-getboolvectorarray.md)   | Get an array of four-component vectors that contain boolean data.<br/>        |
| [**GetFloatVector**](id3dx11effectvectorvariable-getfloatvector.md)           | Get a four-component vector that contains floating-point data.<br/>           |
| [**GetFloatVectorArray**](id3dx11effectvectorvariable-getfloatvectorarray.md) | Get an array of four-component vectors that contain floating-point data.<br/> |
| [**GetIntVector**](id3dx11effectvectorvariable-getintvector.md)               | Get a four-component vector that contains integer data.<br/>                  |
| [**GetIntVectorArray**](id3dx11effectvectorvariable-getintvectorarray.md)     | Get an array of four-component vectors that contain integer data.<br/>        |
| [**SetBoolVector**](id3dx11effectvectorvariable-setboolvector.md)             | Set a four-component vector that contains boolean data.<br/>                  |
| [**SetBoolVectorArray**](id3dx11effectvectorvariable-setboolvectorarray.md)   | Set an array of four-component vectors that contain boolean data.<br/>        |
| [**SetFloatVector**](id3dx11effectvectorvariable-setfloatvector.md)           | Set a four-component vector that contains floating-point data.<br/>           |
| [**SetFloatVectorArray**](id3dx11effectvectorvariable-setfloatvectorarray.md) | Set an array of four-component vectors that contain floating-point data.<br/> |
| [**SetIntVector**](id3dx11effectvectorvariable-setintvector.md)               | Set a four-component vector that contains integer data.<br/>                  |
| [**SetIntVectorArray**](id3dx11effectvectorvariable-setintvectorarray.md)     | Set an array of four-component vectors that contain integer data.<br/>        |



 

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

 

 





