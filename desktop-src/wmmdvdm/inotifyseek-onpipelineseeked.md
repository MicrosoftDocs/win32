---
title: INotifySeek OnPipelineSeeked method
description: The OnPipelineSeeked method alerts the application that there will be a discontinuity because of a seek operation in the stream.
ms.assetid: 09d51336-0fcb-41f2-b1c7-12463bcfc0f8
keywords:
- OnPipelineSeeked method Windows Movie Maker and DVD Maker
- OnPipelineSeeked method Windows Movie Maker and DVD Maker , INotifySeek interface
- INotifySeek interface Windows Movie Maker and DVD Maker , OnPipelineSeeked method
topic_type:
- apiref
api_name:
- INotifySeek.OnPipelineSeeked
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

# INotifySeek::OnPipelineSeeked method

The **OnPipelineSeeked** method alerts the application that there will be a discontinuity because of a seek operation in the stream.

## Syntax


```C++
HRESULT OnPipelineSeeked();
```



## Parameters

This method has no parameters.

## Return value

The application's return value will not be processed by Windows Movie Maker.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**INotifySeek Interface**](inotifyseek.md)
</dt> </dl>

 

 





