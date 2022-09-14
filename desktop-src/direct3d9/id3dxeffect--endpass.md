---
description: End an active pass.
ms.assetid: e20b3e0f-db9f-48e8-ab4e-761a5861f3ce
title: ID3DXEffect::EndPass method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.EndPass
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::EndPass method

End an active pass.

## Syntax


```C++
HRESULT EndPass();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

This method always returns the value S\_OK.

## Remarks

An application signals the end of rendering an active pass by calling **ID3DXEffect::EndPass**. Each **ID3DXEffect::EndPass** must be part of a matching pair of [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md) and **ID3DXEffect::EndPass** calls.

Each matching pair of [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md) and **ID3DXEffect::EndPass** calls must be located within a matching pair of [**ID3DXEffect::Begin**](id3dxeffect--begin.md) and [**ID3DXEffect::End**](id3dxeffect--end.md) calls.

If the application changes any effect state using any of the [**Effect::Setx**](id3dxeffect.md) methods inside of a [**ID3DXEffect::BeginPass**](id3dxeffect--beginpass.md)/**ID3DXEffect::EndPass** matching pair, the application must call [**ID3DXEffect::CommitChanges**](id3dxeffect--commitchanges.md) before any DrawxPrimitive call to propagate state changes to the device before rendering.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> </dl>

 

 




