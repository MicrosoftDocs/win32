---
title: ID3DX11Effect Optimize method (D3dx11effect.h)
description: Minimize the amount of memory required for an effect.
ms.assetid: fa1d0769-6746-44f6-9979-31a534646884
keywords:
- Optimize method Direct3D 11
- Optimize method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , Optimize method
topic_type:
- apiref
api_name:
- ID3DX11Effect.Optimize
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::Optimize method

Minimize the amount of memory required for an effect.

## Syntax


```C++
HRESULT Optimize();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

An effect uses memory space two different ways: to store the information required by the runtime to execute an effect, and to store the metadata required to reflect information back to an application using the API. You can minimize the amount of memory required by an effect by calling **ID3DX11Effect::Optimize** which removes the reflection metadata from memory. API methods to read variables will no longer work once reflection data has been removed.

The following methods will fail after Optimize has been called on an effect.

-   [**ID3DX11Effect::GetConstantBufferByIndex**](id3dx11effect-getconstantbufferbyindex.md)
-   [**ID3DX11Effect::GetConstantBufferByName**](id3dx11effect-getconstantbufferbyname.md)
-   [**ID3DX11Effect::GetDesc**](id3dx11effect-getdesc.md)
-   [**ID3DX11Effect::GetDevice**](id3dx11effect-getdevice.md)
-   [**ID3DX11Effect::GetTechniqueByIndex**](id3dx11effect-gettechniquebyindex.md)
-   [**ID3DX11Effect::GetTechniqueByName**](id3dx11effect-gettechniquebyname.md)
-   [**ID3DX11Effect::GetVariableByIndex**](id3dx11effect-getvariablebyindex.md)
-   [**ID3DX11Effect::GetVariableByName**](id3dx11effect-getvariablebyname.md)
-   [**ID3DX11Effect::GetVariableBySemantic**](id3dx11effect-getvariablebysemantic.md)

> [!Note]  
> References retrieved with these methods before calling **ID3DX11Effect::Optimize** are still valid after **ID3DX11Effect::Optimize** is called. This allows the application to get all the variables, techniques, and passes it will use, call Optimize, and then use the effect.

 

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11Effect](id3dx11effect.md)
</dt> </dl>

 

 





