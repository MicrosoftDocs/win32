---
Description: 'Clones, or copies, an animation controller.'
ms.assetid: '9836653c-9ea5-4fbc-89ac-0b46054a12d7'
title: 'ID3DXAnimationController::CloneAnimationController method'
---

# ID3DXAnimationController::CloneAnimationController method

Clones, or copies, an animation controller.

## Syntax


```C++
HRESULT CloneAnimationController(
  [in] UINT                      MaxNumAnimationOutputs,
  [in] UINT                      MaxNumAnimationSets,
  [in] UINT                      MaxNumTracks,
  [in] UINT                      MaxNumEvents,
  [in] LPD3DXANIMATIONCONTROLLER *ppAnimController
);
```



## Parameters

<dl> <dt>

*MaxNumAnimationOutputs* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Maximum number of animation outputs the controller can support.

</dd> <dt>

*MaxNumAnimationSets* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Maximum number of animation sets the controller can support.

</dd> <dt>

*MaxNumTracks* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Maximum number of tracks the controller can support.

</dd> <dt>

*MaxNumEvents* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Maximum number of events the controller can support.

</dd> <dt>

*ppAnimController* \[in\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONCONTROLLER**](id3dxanimationcontroller.md)\***

Address of a pointer to the cloned [**ID3DXAnimationController**](id3dxanimationcontroller.md) animation controller.

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

 

 




