---
title: ID3DX11Effect IsOptimized method (D3dx11effect.h)
description: Test an effect to see if the reflection metadata has been removed from memory.
ms.assetid: fb0a876b-7419-45b7-97fe-8352dd97d8c5
keywords:
- IsOptimized method Direct3D 11
- IsOptimized method Direct3D 11 , ID3DX11Effect interface
- ID3DX11Effect interface Direct3D 11 , IsOptimized method
topic_type:
- apiref
api_name:
- ID3DX11Effect.IsOptimized
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11Effect::IsOptimized method

Test an effect to see if the reflection metadata has been removed from memory.

## Syntax


```C++
BOOL IsOptimized();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**BOOL**](/windows/desktop/WinProg/windows-data-types)**

**TRUE** if the effect is optimized; otherwise **FALSE**.

## Remarks

An effect uses memory space two different ways: to store the information required by the runtime to execute an effect, and to store the metadata required to reflect information back to an application using the API. You can minimize the amount of memory required by an effect by calling [**ID3DX11Effect::Optimize**](id3dx11effect-optimize.md) which removes the reflection metadata from memory. Of course, API methods to read variables will no longer work once reflection data has been removed.

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

 

