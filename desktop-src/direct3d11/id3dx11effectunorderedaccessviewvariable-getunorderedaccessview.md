---
title: ID3DX11EffectUnorderedAccessViewVariable GetUnorderedAccessView method
description: Get an unordered-access-view.
ms.assetid: '46f61c4f-b3ee-4058-99b9-a43ca6944fb2'
keywords: ["GetUnorderedAccessView method Direct3D 11", "GetUnorderedAccessView method Direct3D 11 , ID3DX11EffectUnorderedAccessViewVariable interface", "ID3DX11EffectUnorderedAccessViewVariable interface Direct3D 11 , GetUnorderedAccessView method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectUnorderedAccessViewVariable.GetUnorderedAccessView
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectUnorderedAccessViewVariable::GetUnorderedAccessView method

Get an unordered-access-view.

## Syntax


```C++
HRESULT GetUnorderedAccessView(
   ID3D11UnorderedAccessView **ppResource
);
```



## Parameters

<dl> <dt>

*ppResource* 
</dt> <dd>

Type: **[**ID3D11UnorderedAccessView**](id3d11unorderedaccessview.md)\*\***

Pointer to an [**ID3D11UnorderedAccessView**](id3d11unorderedaccessview.md) pointer that will be set on return.

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

[ID3DX11EffectUnorderedAccessViewVariable](id3dx11effectunorderedaccessviewvariable.md)
</dt> </dl>

 

 





