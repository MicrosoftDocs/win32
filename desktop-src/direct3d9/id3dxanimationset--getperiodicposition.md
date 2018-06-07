---
Description: Returns time position in the local timeframe of an animation set.
ms.assetid: d822e1d8-f371-43a1-bbcf-2223e28a200a
title: ID3DXAnimationSet::GetPeriodicPosition method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Local time of the animation set.

</dd> </dl>

## Return value

Type: **[**DOUBLE**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Time position as measured in the timeframe of the animation set. This value will be bounded by the period of the animation set.

## Remarks

The time position returned by this method can be used as the PeriodicPosition parameter of [**ID3DXAnimationSet::GetSRT**](id3dxanimationset--getsrt.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 




