---
Description: 'Animates the mesh and advances the global animation time by a specified amount.'
ms.assetid: 'a822d92a-c301-4289-b67b-1df99808c79d'
title: 'ID3DXAnimationController::AdvanceTime method'
---

# ID3DXAnimationController::AdvanceTime method

Animates the mesh and advances the global animation time by a specified amount.

## Syntax


```C++
HRESULT AdvanceTime(
  [in] DOUBLE                         TimeDelta,
  [in] LPD3DXANIMATIONCALLBACKHANDLER pCallbackHandler
);
```



## Parameters

<dl> <dt>

*TimeDelta* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

Amount, in seconds, by which to advance the global animation time. TimeDelta value must be non-negative or zero.

</dd> <dt>

*pCallbackHandler* \[in\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONCALLBACKHANDLER**](id3dxanimationcallbackhandler.md)**

Pointer to a user-defined animation callback handler interface, [**ID3DXAnimationCallbackHandler**](id3dxanimationcallbackhandler.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




