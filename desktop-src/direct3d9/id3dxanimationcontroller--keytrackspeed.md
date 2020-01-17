---
Description: Sets an event key that changes the rate of play of an animation track.
ms.assetid: 217d3a2d-0fb7-4995-86ec-7a4e8420e338
title: ID3DXAnimationController::KeyTrackSpeed method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.KeyTrackSpeed
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::KeyTrackSpeed method

Sets an event key that changes the rate of play of an animation track.

## Syntax


```C++
D3DXEVENTHANDLE KeyTrackSpeed(
  [in] UINT                Track,
  [in] FLOAT               NewSpeed,
  [in] DOUBLE              StartTime,
  [in] DOUBLE              Duration,
  [in] D3DXTRANSITION_TYPE Transition
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Identifier of the track to modify.

</dd> <dt>

*NewSpeed* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

New speed of the animation track.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Global time key. Specifies the global time when the change will take place.

</dd> <dt>

*Duration* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

Transition time, which specifies how long the smooth transition will take to complete.

</dd> <dt>

*Transition* \[in\]
</dt> <dd>

Type: **[**D3DXTRANSITION\_TYPE**](https://msdn.microsoft.com/library/Bb205475(v=VS.85).aspx)**

Specifies the transition type used for transitioning between speeds. See [**D3DXTRANSITION\_TYPE**](https://msdn.microsoft.com/library/Bb205475(v=VS.85).aspx).

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the priority blend event. **NULL** is returned if one or more of the input parameters is invalid, or no free event is available.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




