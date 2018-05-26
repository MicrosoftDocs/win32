---
Description: Returns the number of animation sets currently registered in the animation controller.
ms.assetid: 1aacc84d-5025-4601-9a6c-84b3d9b06012
title: ID3DXAnimationControllerGetNumAnimationSets method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetNumAnimationSets method

Returns the number of animation sets currently registered in the animation controller.

## Syntax


```C++
UINT GetNumAnimationSets();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](winprog.windows_data_types)**

Number of animation sets.

## Remarks

The controller contains any number of animations sets and tracks. Animation sets can be registered with [**RegisterAnimationOutput**](id3dxanimationcontroller--registeranimationoutput.md). An animation controller created by a call to [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) will automatically register loaded animation sets.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




