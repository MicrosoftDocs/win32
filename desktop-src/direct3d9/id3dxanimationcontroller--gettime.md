---
description: Gets the global animation time.
ms.assetid: a46e2a57-a76a-4d79-a3b6-30b242321ed2
title: ID3DXAnimationController::GetTime method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.GetTime
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::GetTime method

Gets the global animation time.

## Syntax


```C++
DOUBLE GetTime();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**DOUBLE**](../winprog/windows-data-types.md)**

Returns the global animation time.

## Remarks

Animations are designed using a local animation time and mixed into global time with [**AdvanceTime**](id3dxanimationcontroller--advancetime.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 
