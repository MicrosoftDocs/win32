---
Description: 'Get the effect state manager.'
ms.assetid: '4a09eb2a-2393-40b0-81b9-3c27998c2b77'
title: 'ID3DXEffect::GetStateManager method'
---

# ID3DXEffect::GetStateManager method

Get the effect state manager.

## Syntax


```C++
HRESULT GetStateManager(
  [out] LPD3DXEFFECTSTATEMANAGER *ppManager
);
```



## Parameters

<dl> <dt>

*ppManager* \[out\]
</dt> <dd>

Type: **[**LPD3DXEFFECTSTATEMANAGER**](id3dxeffectstatemanager.md)\***

Returns a pointer to the state manager. See [**ID3DXEffectStateManager**](id3dxeffectstatemanager.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA.

## Remarks

The [**ID3DXEffectStateManager**](id3dxeffectstatemanager.md) is a user-implemented interface that furnishes callbacks into an application for setting device state from an effect.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffect](id3dxeffect.md)
</dt> <dt>

[**ID3DXEffect::SetStateManager**](id3dxeffect--setstatemanager.md)
</dt> </dl>

 

 




