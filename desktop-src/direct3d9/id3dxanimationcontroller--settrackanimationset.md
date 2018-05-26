---
Description: Applies the animation set to the specified track.
ms.assetid: f48bb0f1-3ccd-4db9-8a30-58c79ae0939e
title: ID3DXAnimationControllerSetTrackAnimationSet method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::SetTrackAnimationSet method

Applies the animation set to the specified track.

## Syntax


```C++
HRESULT SetTrackAnimationSet(
  [in] UINT               Track,
  [in] LPD3DXANIMATIONSET pAnimSet
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to which the animation set is applied.

</dd> <dt>

*pAnimSet* \[in\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONSET**](id3dxanimationset.md)**

Pointer to the [**ID3DXAnimationSet**](id3dxanimationset.md) animation set to be added to the track.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method sets the animation set to the specified track for mixing. The animation set for each track is blended according to the track weight and speed when [**AdvanceTime**](id3dxanimationcontroller--advancetime.md) is called.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




