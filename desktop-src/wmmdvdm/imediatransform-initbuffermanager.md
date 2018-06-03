---
title: IMediaTransform InitBufferManager method
description: The InitBufferManager method passes a Direct3D device to your transform and enables your transform to perform any initialization it requires.
ms.assetid: 88cba8d1-cb73-4abf-aea3-4adda8cc4c8c
keywords:
- InitBufferManager method Windows Movie Maker and DVD Maker
- InitBufferManager method Windows Movie Maker and DVD Maker , IMediaTransform interface
- IMediaTransform interface Windows Movie Maker and DVD Maker , InitBufferManager method
topic_type:
- apiref
api_name:
- IMediaTransform.InitBufferManager
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaTransform::InitBufferManager method

The **InitBufferManager** method passes a Direct3D device to your transform and enables your transform to perform any initialization it requires. This method is called when the object is first instantiated, as well as whenever the device is changed by Windows Movie Maker.

## Syntax


```C++
HRESULT InitBufferManager(
  [in] IBufferManager *pManager
);
```



## Parameters

<dl> <dt>

*pManager* \[in\]
</dt> <dd>

Pointer to an **IBufferManager** interface.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

Your transform should use this method to create global objects that your transform might require or Direct3D device resources such as meshes or extra textures. Note that any handles to Direct3D objects that are stored as global members might need to be changed if Windows Movie Maker loses access to the device. Loss of device can occur if the user locks the desktop or if another application takes exclusive control of the video card, as some games do. When Windows Movie Maker gets access to a new device, it calls this method again, and the transform should reinitialize any stored Direct3D objects. When a device is lost for any reason, this method is called with a **NULL** pointer for *pManager*.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**IMediaTransform Interface**](imediatransform.md)
</dt> </dl>

 

 





