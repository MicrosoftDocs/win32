---
title: ID3DX11EffectRenderTargetViewVariable SetRenderTargetArray method
description: Set an array of render-targets.
ms.assetid: 03e1c4ea-292c-439f-a647-070b9e91a044
keywords:
- SetRenderTargetArray method Direct3D 11
- SetRenderTargetArray method Direct3D 11 , ID3DX11EffectRenderTargetViewVariable interface
- ID3DX11EffectRenderTargetViewVariable interface Direct3D 11 , SetRenderTargetArray method
topic_type:
- apiref
api_name:
- ID3DX11EffectRenderTargetViewVariable.SetRenderTargetArray
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

# ID3DX11EffectRenderTargetViewVariable::SetRenderTargetArray method

Set an array of render-targets.

## Syntax


```C++
HRESULT SetRenderTargetArray(
   ID3D11RenderTargetView **ppResources,
   UINT                   Offset,
   UINT                   Count
);
```



## Parameters

<dl> <dt>

*ppResources* 
</dt> <dd>

Type: **[**ID3D11RenderTargetView**](/windows/win32/D3D11/nn-d3d11-id3d11rendertargetview?branch=master)\*\***

Set an array of render-target-view interfaces. See [**ID3D11RenderTargetView**](/windows/win32/D3D11/nn-d3d11-id3d11rendertargetview?branch=master).

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The zero-based array index to store the first interface.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of elements in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

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

[ID3DX11EffectRenderTargetViewVariable](id3dx11effectrendertargetviewvariable.md)
</dt> </dl>

 

 





