---
title: ID3DX11EffectScalarVariable GetFloat method
description: Get a floating-point variable.
ms.assetid: '0416db40-5e70-44e4-905f-86f49a9b58b8'
keywords: ["GetFloat method Direct3D 11", "GetFloat method Direct3D 11 , ID3DX11EffectScalarVariable interface", "ID3DX11EffectScalarVariable interface Direct3D 11 , GetFloat method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectScalarVariable.GetFloat
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectScalarVariable::GetFloat method

Get a floating-point variable.

## Syntax


```C++
HRESULT GetFloat(
   float *pValue
);
```



## Parameters

<dl> <dt>

*pValue* 
</dt> <dd>

Type: **float\***

A pointer to the variable.

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

[ID3DX11EffectScalarVariable](id3dx11effectscalarvariable.md)
</dt> </dl>

 

 





