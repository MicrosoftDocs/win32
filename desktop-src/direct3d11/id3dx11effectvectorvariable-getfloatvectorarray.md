---
title: ID3DX11EffectVectorVariable GetFloatVectorArray method (D3dx11effect.h)
description: Get an array of four-component vectors that contain floating-point data.
ms.assetid: 30ecbd97-c16d-4ea9-b7d9-364887f42a04
keywords:
- GetFloatVectorArray method Direct3D 11
- GetFloatVectorArray method Direct3D 11 , ID3DX11EffectVectorVariable interface
- ID3DX11EffectVectorVariable interface Direct3D 11 , GetFloatVectorArray method
topic_type:
- apiref
api_name:
- ID3DX11EffectVectorVariable.GetFloatVectorArray
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVectorVariable::GetFloatVectorArray method

Get an array of four-component vectors that contain floating-point data.

## Syntax


```C++
HRESULT GetFloatVectorArray(
   float *pData,
   UINT  Offset,
   UINT  Count
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **float\***

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

[ID3DX11EffectVectorVariable](id3dx11effectvectorvariable.md)
</dt> </dl>

 

