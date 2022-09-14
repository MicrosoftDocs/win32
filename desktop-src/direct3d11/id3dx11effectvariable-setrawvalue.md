---
title: ID3DX11EffectVariable SetRawValue method (D3dx11effect.h)
description: Set data.
ms.assetid: c5d53aa6-6cd8-4a93-9851-2a93bc6a728a
keywords:
- SetRawValue method Direct3D 11
- SetRawValue method Direct3D 11 , ID3DX11EffectVariable interface
- ID3DX11EffectVariable interface Direct3D 11 , SetRawValue method
topic_type:
- apiref
api_name:
- ID3DX11EffectVariable.SetRawValue
api_location:
- N/A
- N/A.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11EffectVariable::SetRawValue method

Set data.

## Syntax


```C++
HRESULT SetRawValue(
   void *pData,
   UINT Offset,
   UINT Count
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **void\***

A pointer to the variable.

</dd> <dt>

*Offset* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The offset (in bytes) from the beginning of the pointer to the data.

</dd> <dt>

*Count* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of bytes to set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns one of the following [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

This method does no conversion or type checking; it is therefore a very quick way to access array items.

> [!Note]  
> The DirectX SDK does not supply any compiled binaries for effects. You must use Effects 11 source to build your effects-type application. For more information about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx11effect.h</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>N/A (An Effects 11 library is available online as shared source.)</dt> </dl> |



## See also

<dl> <dt>

[ID3DX11EffectVariable](id3dx11effectvariable.md)
</dt> </dl>

 

