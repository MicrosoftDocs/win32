---
title: IMediaTransform get\_InputCount method
description: The get\_InputCount method enables your transform to report the number of source input streams that it can handle.
ms.assetid: 7d92e627-d156-4448-ab81-b7d7e3cee554
keywords:
- get_InputCount method Windows Movie Maker and DVD Maker
- get_InputCount method Windows Movie Maker and DVD Maker , IMediaTransform interface
- IMediaTransform interface Windows Movie Maker and DVD Maker , get_InputCount method
topic_type:
- apiref
api_name:
- IMediaTransform.get_InputCount
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMediaTransform::get\_InputCount method

The **get\_InputCount** method enables your transform to report the number of source input streams that it can handle.

## Syntax


```C++
HRESULT get_InputCount(
  [out] DWORD *pdwCount
);
```



## Parameters

<dl> <dt>

*pdwCount* \[out\]
</dt> <dd>

**DWORD** pointer that indicates the number of input streams that the transform can process. For effects, this is 1; for transitions, this is 2.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

All input streams must be of the same type.

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

 

 





