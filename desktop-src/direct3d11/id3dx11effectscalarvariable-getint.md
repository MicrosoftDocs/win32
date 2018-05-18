---
title: ID3DX11EffectScalarVariable GetInt method
description: Get an integer variable.
ms.assetid: '82a5a7a5-17cb-4e5e-ae4e-57c0ff9757c5'
keywords: ["GetInt method Direct3D 11", "GetInt method Direct3D 11 , ID3DX11EffectScalarVariable interface", "ID3DX11EffectScalarVariable interface Direct3D 11 , GetInt method"]
topic_type:
- apiref
api_name:
- ID3DX11EffectScalarVariable.GetInt
api_location:
- N/A
- N/A.dll
api_type:
- COM
---

# ID3DX11EffectScalarVariable::GetInt method

Get an integer variable.

## Syntax


```C++
HRESULT GetInt(
   int *pValue
);
```



## Parameters

<dl> <dt>

*pValue* 
</dt> <dd>

Type: **[**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

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

 

 





