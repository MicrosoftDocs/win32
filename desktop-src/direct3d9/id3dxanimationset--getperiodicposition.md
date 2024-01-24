---
description: Returns time position in the local timeframe of an animation set.
ms.assetid: d822e1d8-f371-43a1-bbcf-2223e28a200a
title: ID3DXAnimationSet::GetPeriodicPosition method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationSet.GetPeriodicPosition
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationSet::GetPeriodicPosition method

Returns time position in the local timeframe of an animation set.

## Syntax


```C++
DOUBLE GetPeriodicPosition(
  [in] DOUBLE Position
);
```



## Parameters

<dl> <dt>

*Position* \[in\]
</dt> <dd>

Type: **[**DOUBLE**](../winprog/windows-data-types.md)**

Local time of the animation set.

</dd> </dl>

## Return value

Type: **[**DOUBLE**](../winprog/windows-data-types.md)**

Time position as measured in the timeframe of the animation set. This value will be bounded by the period of the animation set.

## Remarks

The time position returned by this method can be used as the PeriodicPosition parameter of [**ID3DXAnimationSet::GetSRT**](id3dxanimationset--getsrt.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 
