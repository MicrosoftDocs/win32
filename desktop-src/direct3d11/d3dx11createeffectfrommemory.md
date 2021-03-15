---
title: D3DX11CreateEffectFromMemory function (D3dx11effect.h)
description: Creates an effect from a binary effect or file.
ms.assetid: 4aa65efb-4c6b-4faf-b48f-01329bdff6cd
keywords:
- D3DX11CreateEffectFromMemory function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11CreateEffectFromMemory
api_location:
- d3dx11effect.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DX11CreateEffectFromMemory function

Creates an effect from a binary effect or file.

## Syntax


```C++
HRESULT D3DX11CreateEffectFromMemory(
   void          *pData,
   SIZE_T        DataLength,
   UINT          FXFlags,
   ID3D11Device  *pDevice,
   ID3DX11Effect **ppEffect
);
```



## Parameters

<dl> <dt>

*pData* 
</dt> <dd>

Type: **void\***

Blob of compiled effect data.

</dd> <dt>

*DataLength* 
</dt> <dd>

Type: **[**SIZE\_T**](/windows/desktop/WinProg/windows-data-types)**

Length of the data blob.

</dd> <dt>

*FXFlags* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

No effect flags exist. Set to zero.

</dd> <dt>

*pDevice* 
</dt> <dd>

Type: **[**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device)\***

Pointer to the [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) on which to create Effect resources.

</dd> <dt>

*ppEffect* 
</dt> <dd>

Type: **[**ID3DX11Effect**](id3dx11effect.md)\*\***

Address of the newly created [**ID3DX11Effect**](id3dx11effect.md) interface.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

> [!Note]  
> You must use [Effects 11 source](https://github.com/Microsoft/FX11) to build your effects-type application. For more info about using Effects 11 source, see [Differences Between Effects 10 and Effects 11](d3d11-graphics-programming-guide-effects-differences.md).

 

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx11effect.h</dt> </dl> |



## See also

<dl> <dt>

[Effects 11 Functions](d3d11-graphics-reference-effects11-functions.md)
</dt> </dl>

 

