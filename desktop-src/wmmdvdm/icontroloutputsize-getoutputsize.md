---
title: IControlOutputSize GetOutputSize method
description: The GetOutputSize method is called by Windows Movie Maker to let the transform evaluate (and modify) the output buffer size that Windows Movie Maker intends to allocate for the next call to IMediaTransform Process.
ms.assetid: dc7ad7e4-c99b-4383-a819-6a6e2fc05162
keywords:
- GetOutputSize method Windows Movie Maker and DVD Maker
- GetOutputSize method Windows Movie Maker and DVD Maker , IControlOutputSize interface
- IControlOutputSize interface Windows Movie Maker and DVD Maker , GetOutputSize method
topic_type:
- apiref
api_name:
- IControlOutputSize.GetOutputSize
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

# IControlOutputSize::GetOutputSize method

The **GetOutputSize** method is called by Windows Movie Maker to let the transform evaluate (and modify) the output buffer size that Windows Movie Maker intends to allocate for the next call to [**IMediaTransform::Process**](imediatransform-process.md). Windows Movie Maker calls this method before each call to **IMediaTransform::Process**.

## Syntax


```C++
HRESULT GetOutputSize(
  [in]  PIPELINE_TIME timeGet,
  [in]  PIPELINE_TIME timeDuration,
  [in]  VIDEO_SIZE    *rgSizeIn,
  [in]  int           nSizeCount,
  [out] VIDEO_SIZE    *pOutSize
);
```



## Parameters

<dl> <dt>

*timeGet* \[in\]
</dt> <dd>

The frame time when the next **IMediaTransform::Process** call will be made, on the absolute timeline (where 0 is the start of the video).

</dd> <dt>

*timeDuration* \[in\]
</dt> <dd>

The duration of the whole transform.

</dd> <dt>

*rgSizeIn* \[in\]
</dt> <dd>

An array of [VIDEO\_SIZE](video-size.md) structures that describe the input buffers that Windows Movie Maker will send to its next call to **IMediaTransform::Process**. One structure will be sent for each input buffer. The number of structures is specified by *nSizeCount*.

</dd> <dt>

*nSizeCount* \[in\]
</dt> <dd>

The number of elements allocated by Windows Movie Maker in *rgSizeIn*.

</dd> <dt>

*pOutSize* \[out\]
</dt> <dd>

A single **VIDEO\_SIZE** structure that the transform should use to specify the output buffer size it will require. If the transform does not need to specify a size, it should return a failure value for this method.

</dd> </dl>

## Return value

If the transform has specified a size for *pOutSize*, it should return S\_OK; if it has not specified a size, it should return a failure code.

## Remarks

This method is not needed by most transforms.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ISurface Interface**](isurface.md)
</dt> </dl>

 

 





