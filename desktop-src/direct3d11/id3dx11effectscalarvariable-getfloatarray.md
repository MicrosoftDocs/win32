---
title: ID3DX11EffectScalarVariable GetFloatArray method
description: Get an array of floating-point variables.
ms.assetid: e5e0dbee-47f5-46ed-89a0-01782345498f
keywords:
- GetFloatArray method Direct3D 11
- GetFloatArray method Direct3D 11 , ID3DX11EffectScalarVariable interface
- ID3DX11EffectScalarVariable interface Direct3D 11 , GetFloatArray method
topic_type:
- apiref
api_name:
- ID3DX11EffectScalarVariable.GetFloatArray
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

# ID3DX11EffectScalarVariable::GetFloatArray method

Get an array of floating-point variables.

## Syntax


```C++
HRESULT GetFloatArray(
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

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Must be set to 0; this is reserved for future use.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of array elements to set.

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

 

 





