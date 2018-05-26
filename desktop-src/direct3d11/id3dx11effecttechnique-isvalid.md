---
title: ID3DX11EffectTechnique IsValid method
description: Test a technique to see if it contains valid syntax.
ms.assetid: 599b191b-6307-4d36-b4e4-15a1ac36c65e
keywords:
- IsValid method Direct3D 11
- IsValid method Direct3D 11 , ID3DX11EffectTechnique interface
- ID3DX11EffectTechnique interface Direct3D 11 , IsValid method
topic_type:
- apiref
api_name:
- ID3DX11EffectTechnique.IsValid
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX11EffectTechnique::IsValid method

Test a technique to see if it contains valid syntax.

## Syntax


```C++
BOOL IsValid();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

**TRUE** if the code syntax is valid; otherwise **FALSE**.

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

[ID3DX11EffectTechnique](id3dx11effecttechnique.md)
</dt> </dl>

 

 





