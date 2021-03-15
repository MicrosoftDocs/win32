---
description: Gets the period of the animation set.
ms.assetid: 0bb19ec1-c918-44b6-83b0-4fdbb4e1a485
title: ID3DXAnimationSet::GetPeriod method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationSet.GetPeriod
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationSet::GetPeriod method

Gets the period of the animation set.

## Syntax


```C++
DOUBLE GetPeriod();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**DOUBLE**](../winprog/windows-data-types.md)**

Period of the animation set.

## Remarks

The period is the range of time that the animation key frames are valid. For looping animations, this is the period of the loop. The time units that the key frames are specified in (for example, seconds) is determined by the application.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationSet](id3dxanimationset.md)
</dt> </dl>

 

 
