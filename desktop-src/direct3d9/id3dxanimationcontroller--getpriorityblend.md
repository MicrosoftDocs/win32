---
Description: Gets the current priority blending weight used by the animation controller.
ms.assetid: ceaf611e-e85b-4958-b8ac-7e60b98b1aad
title: ID3DXAnimationControllerGetPriorityBlend method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetPriorityBlend method

Gets the current priority blending weight used by the animation controller.

## Syntax


```C++
FLOAT GetPriorityBlend();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

Returns the current priority blending weight.

## Remarks

The priority blending weight is used to blend high and low priority tracks together.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> <dt>

[**SetPriorityBlend**](id3dxanimationcontroller--setpriorityblend.md)
</dt> </dl>

 

 




