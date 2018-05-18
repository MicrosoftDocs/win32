---
title: ISurfaceManager get\_IdealVideoSize method
description: The get\_IdealVideoSize method retrieves the ideal video size for the surface.
ms.assetid: 'df50fb93-0172-42c3-b8d1-94b93dfd5332'
keywords: ["get_IdealVideoSize method Windows Movie Maker and DVD Maker", "get_IdealVideoSize method Windows Movie Maker and DVD Maker , ISurfaceManager interface", "ISurfaceManager interface Windows Movie Maker and DVD Maker , get_IdealVideoSize method"]
topic_type:
- apiref
api_name:
- ISurfaceManager.get_IdealVideoSize
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ISurfaceManager::get\_IdealVideoSize method

The **get\_IdealVideoSize** method retrieves the ideal video size for the surface.

## Syntax


```C++
HRESULT get_IdealVideoSize(
  [out] VIDEO_SIZE *pSize
);
```



## Parameters

<dl> <dt>

*pSize* \[out\]
</dt> <dd>

Pointer to a [VIDEO\_SIZE](video-size.md) structure that specifies the ideal video size for the surface in this device.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

This method is used to determine non-square pixel aspect ratios when rendering to a 16:9 screen. The returned value is compared to the actual output buffer size to determine the ratio.

You can call this method to determine what size to allocate for a new surface before calling [**AllocSurfaceSize**](isurfacemanager-allocsurfacesize.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ISurfaceManager Interface**](isurfacemanager.md)
</dt> </dl>

 

 





