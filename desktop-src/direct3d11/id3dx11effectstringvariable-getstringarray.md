---
title: ID3DX11EffectStringVariable GetStringArray method (D3dx11effect.h)
description: Get an array of strings.
ms.assetid: 2cc45b2f-1851-49d2-8844-3e249c48f327
keywords:
- GetStringArray method Direct3D 11
- GetStringArray method Direct3D 11 , ID3DX11EffectStringVariable interface
- ID3DX11EffectStringVariable interface Direct3D 11 , GetStringArray method
topic_type:
- apiref
api_name:
- ID3DX11EffectStringVariable.GetStringArray
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectStringVariable::GetStringArray method

Get an array of strings.

## Syntax


```C++
HRESULT GetStringArray(
   LPCSTR *ppStrings,
   UINT   Offset,
   UINT   Count
);
```



## Parameters

<dl> <dt>

*ppStrings* 
</dt> <dd>

Type: **[**LPCSTR**](/windows/desktop/WinProg/windows-data-types)\***

A pointer to the first string in the array.

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The offset (in number of strings) between the start of the array and the first string to get.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of strings in the returned array.

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

[ID3DX11EffectStringVariable](id3dx11effectstringvariable.md)
</dt> </dl>

 

