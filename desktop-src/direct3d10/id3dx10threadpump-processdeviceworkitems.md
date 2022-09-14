---
description: Set work items to the device after they have finished loading and processing.
ms.assetid: 67a9fcb2-3513-413d-ac3d-9988ef7b5a1f
title: ID3DX10ThreadPump::ProcessDeviceWorkItems method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10ThreadPump.ProcessDeviceWorkItems
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10ThreadPump::ProcessDeviceWorkItems method

Set work items to the device after they have finished loading and processing. When the thread pump has finished loading and processing a resource or shader, it will hold it in a queue until this API is called, at which point the processed items will be set to the device. This is useful for controlling the amount of processing that is spent on binding resources to the device for each frame. See remarks.

## Syntax


```C++
HRESULT ProcessDeviceWorkItems(
  [in] UINT iWorkItemCount
);
```



## Parameters

<dl> <dt>

*iWorkItemCount* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of work items to set to the device. ProcessDeviceObjectCreation will create at most iWorkItemCount objects. If there are not enough work items in the queue to process iWorkItemCount objects, ProcessDeviceObjectCreation will create as many device objects as there are items in the queue.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

As an example of how one might use this API, say you are nearing the end of one level in your game and you want to begin preloading the textures, shaders, and other resources for the next level. The thread pump will begin loading, decompressing, and processing the resources and shaders on a separate thread until they are ready to be set to the device, at which point it will leave them in a queue. One may not want to set all the resources and shaders to the device at once because this may cause a noticable temporary slow down in the game's performance. So, this API could be called once per frame so that only a small number work items would be set to the device on each frame, thereby spreading the work load of binding resources to the device over several frames and minimizing the possibility of a noticable slow down in the game's performance.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10ThreadPump](id3dx10threadpump.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
