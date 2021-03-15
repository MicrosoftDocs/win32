---
title: ID3DX11EffectScalarVariable GetBoolArray method (D3dx11effect.h)
description: Get an array of boolean variables.
ms.assetid: 0335417a-a0aa-4157-881d-7828ffb3f47a
keywords:
- GetBoolArray method Direct3D 11
- GetBoolArray method Direct3D 11 , ID3DX11EffectScalarVariable interface
- ID3DX11EffectScalarVariable interface Direct3D 11 , GetBoolArray method
topic_type:
- apiref
api_name:
- ID3DX11EffectScalarVariable.GetBoolArray
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectScalarVariable::GetBoolArray method

Get an array of boolean variables.

## Syntax


```C++
HRESULT GetBoolArray(
   BOOL *pData,
   UINT Offset,
   UINT Count
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **[**BOOL**](/windows/desktop/WinProg/windows-data-types)\***

A pointer to the start of the data to set.

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

Must be set to 0; this is reserved for future use.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of array elements to set.

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

[ID3DX11EffectScalarVariable](id3dx11effectscalarvariable.md)
</dt> </dl>

 

