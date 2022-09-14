---
title: ID3DX11EffectUnorderedAccessViewVariable SetUnorderedAccessView method (D3dx11effect.h)
description: Set an unordered-access-view.
ms.assetid: a147879c-c5cf-4453-b27f-8716cb33962b
keywords:
- SetUnorderedAccessView method Direct3D 11
- SetUnorderedAccessView method Direct3D 11 , ID3DX11EffectUnorderedAccessViewVariable interface
- ID3DX11EffectUnorderedAccessViewVariable interface Direct3D 11 , SetUnorderedAccessView method
topic_type:
- apiref
api_name:
- ID3DX11EffectUnorderedAccessViewVariable.SetUnorderedAccessView
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectUnorderedAccessViewVariable::SetUnorderedAccessView method

Set an unordered-access-view.

## Syntax


```C++
HRESULT SetUnorderedAccessView(
   ID3D11UnorderedAccessView *pResource
);
```



## Parameters

<dl> <dt>

*pResource* 
</dt> <dd>

Type: **[**ID3D11UnorderedAccessView**](/windows/desktop/api/D3D11/nn-d3d11-id3d11unorderedaccessview)\***

Pointer to an [**ID3D11UnorderedAccessView**](/windows/desktop/api/D3D11/nn-d3d11-id3d11unorderedaccessview).

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

[ID3DX11EffectUnorderedAccessViewVariable](id3dx11effectunorderedaccessviewvariable.md)
</dt> </dl>

 

 





