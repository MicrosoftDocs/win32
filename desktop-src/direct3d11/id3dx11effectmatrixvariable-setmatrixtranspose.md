---
title: ID3DX11EffectMatrixVariable SetMatrixTranspose method (D3dx11effect.h)
description: Transpose and set a floating-point matrix.
ms.assetid: 228546c9-0141-4e17-bc8f-bff7201825d7
keywords:
- SetMatrixTranspose method Direct3D 11
- SetMatrixTranspose method Direct3D 11 , ID3DX11EffectMatrixVariable interface
- ID3DX11EffectMatrixVariable interface Direct3D 11 , SetMatrixTranspose method
topic_type:
- apiref
api_name:
- ID3DX11EffectMatrixVariable.SetMatrixTranspose
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectMatrixVariable::SetMatrixTranspose method

Transpose and set a floating-point matrix.

## Syntax


```C++
HRESULT SetMatrixTranspose(
   float *pData
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **float\***

A pointer to the first element of a matrix.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

Transposing a matrix will rearrange the data order from row-column order to column-row order (or vice versa).

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectMatrixVariable](id3dx11effectmatrixvariable.md)
</dt> </dl>

 

 





