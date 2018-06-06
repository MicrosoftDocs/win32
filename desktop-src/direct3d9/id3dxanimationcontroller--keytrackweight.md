---
Description: Sets an event key that changes the weight of an animation track. The weight is used as a multiplier when combining multiple tracks together.
ms.assetid: fb2859de-9e77-49dd-be48-a50e22e2fc3a
title: ID3DXAnimationController::KeyTrackWeight method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXAnimationController::KeyTrackWeight method

Sets an event key that changes the weight of an animation track. The weight is used as a multiplier when combining multiple tracks together.

## Syntax


```C++
D3DXEVENTHANDLE KeyTrackWeight(
  [in] UINT                Track,
  [in] FLOAT               NewWeight,
  [in] DOUBLE              StartTime,
  [in] DOUBLE              Duration,
  [in] D3DXTRANSITION_TYPE Transition
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Identifier of the track to modify.

</dd> <dt>

*NewWeight* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

New weight of the track.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Global time key. Specifies the global time when the change will take place.

</dd> <dt>

*Duration* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Transition time, which specifies how long the smooth transition will take to complete.

</dd> <dt>

*Transition* \[in\]
</dt> <dd>

Type: **[**D3DXTRANSITION\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxtransition_type.htm)**

Specifies the transition type used for transitioning between weights. See [**D3DXTRANSITION\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxtransition_type.htm).

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the priority blend event. **NULL** is returned if one or more of the input parameters is invalid, or no free event is available.

## Remarks

The weight is used like a multiplier to determine how much of this track to blend together with other tracks.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




