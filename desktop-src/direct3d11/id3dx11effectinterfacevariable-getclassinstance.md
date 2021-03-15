---
title: ID3DX11EffectInterfaceVariable GetClassInstance method (D3dx11effect.h)
description: Get a class instance.
ms.assetid: a965f4e7-1761-45f1-a72e-7ad0ed1ad671
keywords:
- GetClassInstance method Direct3D 11
- GetClassInstance method Direct3D 11 , ID3DX11EffectInterfaceVariable interface
- ID3DX11EffectInterfaceVariable interface Direct3D 11 , GetClassInstance method
topic_type:
- apiref
api_name:
- ID3DX11EffectInterfaceVariable.GetClassInstance
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectInterfaceVariable::GetClassInstance method

Get a class instance.

## Syntax


```C++
HRESULT GetClassInstance(
   ID3DX11EffectClassInstanceVariable **ppEffectClassInstance
);
```



## Parameters

<dl> <dt>

*ppEffectClassInstance* 
</dt> <dd>

Type: **[**ID3DX11EffectClassInstanceVariable**](id3dx11effectclassinstancevariable.md)\*\***

Pointer to an [**ID3DX11EffectClassInstanceVariable**](id3dx11effectclassinstancevariable.md) pointer that will be set to the class instance.

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

[ID3DX11EffectInterfaceVariable](id3dx11effectinterfacevariable.md)
</dt> </dl>

 

 





