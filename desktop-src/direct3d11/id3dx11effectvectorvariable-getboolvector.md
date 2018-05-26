---
title: ID3DX11EffectVectorVariable GetBoolVector method
description: Get a four-component vector that contains boolean data.
ms.assetid: ecaf5705-d13b-4d61-9766-d2ff183af789
keywords:
- GetBoolVector method Direct3D 11
- GetBoolVector method Direct3D 11 , ID3DX11EffectVectorVariable interface
- ID3DX11EffectVectorVariable interface Direct3D 11 , GetBoolVector method
topic_type:
- apiref
api_name:
- ID3DX11EffectVectorVariable.GetBoolVector
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

# ID3DX11EffectVectorVariable::GetBoolVector method

Get a four-component vector that contains boolean data.

## Syntax


```C++
HRESULT GetBoolVector(
   BOOL *pData
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

A pointer to the first component.

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

[ID3DX11EffectVectorVariable](id3dx11effectvectorvariable.md)
</dt> </dl>

 

 





