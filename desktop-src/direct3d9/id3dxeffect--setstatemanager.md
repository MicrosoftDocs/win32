---
description: Set the effect state manager.
ms.assetid: 87409687-03f1-4593-ae58-3a8ba08e592b
title: ID3DXEffect::SetStateManager method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffect.SetStateManager
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffect::SetStateManager method

Set the effect state manager.

## Syntax


```C++
HRESULT SetStateManager(
  [in] LPD3DXEFFECTSTATEMANAGER pManager
);
```



## Parameters

<dl> <dt>

*pManager* \[in\]
</dt> <dd>

Type: **[**LPD3DXEFFECTSTATEMANAGER**](id3dxeffectstatemanager.md)**

A pointer to the state manager. See [**ID3DXEffectStateManager**](id3dxeffectstatemanager.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

The [**ID3DXEffectStateManager**](id3dxeffectstatemanager.md) is a user-implemented interface that furnishes callbacks into an application for setting device state from an effect.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> <dt>

[**ID3DXEffect::GetStateManager**](id3dxeffect--getstatemanager.md)
</dt> </dl>

 

 




