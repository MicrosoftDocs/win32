---
Description: 'Sets an event key that changes the local time of an animation track.'
ms.assetid: 'b527e960-8ab9-42a0-bb4d-bea5aaf83424'
title: 'ID3DXAnimationController::KeyTrackPosition method'
---

# ID3DXAnimationController::KeyTrackPosition method

Sets an event key that changes the local time of an animation track.

## Syntax


```C++
D3DXEVENTHANDLE KeyTrackPosition(
  [in] UINT   Track,
  [in] DOUBLE NewPosition,
  [in] DOUBLE StartTime
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to modify.

</dd> <dt>

*NewPosition* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

New local time of the animation track.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](winprog.windows_data_types)**

Global time key. Specifies the global time when the change will take place.

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the priority blend event. **NULL** is returned if Track is invalid, or if no free event is available.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




