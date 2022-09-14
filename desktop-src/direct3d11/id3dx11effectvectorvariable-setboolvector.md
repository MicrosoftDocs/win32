---
title: ID3DX11EffectVectorVariable SetBoolVector method (D3dx11effect.h)
description: Set a four-component vector that contains boolean data.
ms.assetid: 2138eeb9-6aa0-43f5-852c-1ab9c8117a88
keywords:
- SetBoolVector method Direct3D 11
- SetBoolVector method Direct3D 11 , ID3DX11EffectVectorVariable interface
- ID3DX11EffectVectorVariable interface Direct3D 11 , SetBoolVector method
topic_type:
- apiref
api_name:
- ID3DX11EffectVectorVariable.SetBoolVector
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVectorVariable::SetBoolVector method

Set a four-component vector that contains boolean data.

## Syntax


```C++
HRESULT SetBoolVector(
   BOOL *pData
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **[**BOOL**](/windows/desktop/WinProg/windows-data-types)\***

A pointer to the first component.

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

 

