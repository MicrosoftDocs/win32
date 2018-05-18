---
title: ISurfaceManager get\_Monitor method
description: The get\_Monitor method retrieves a handle to the display monitor.
ms.assetid: 'e8703cd8-7321-42cb-93f6-2623bb5d06aa'
keywords: ["get_Monitor method Windows Movie Maker and DVD Maker", "get_Monitor method Windows Movie Maker and DVD Maker , ISurfaceManager interface", "ISurfaceManager interface Windows Movie Maker and DVD Maker , get_Monitor method"]
topic_type:
- apiref
api_name:
- ISurfaceManager.get_Monitor
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ISurfaceManager::get\_Monitor method

The **get\_Monitor** method retrieves a handle to the display monitor.

## Syntax


```C++
HRESULT get_Monitor(
  [out] HMONITOR *phMon
);
```



## Parameters

<dl> <dt>

*phMon* \[out\]
</dt> <dd>

A pointer to a handle to the display monitor.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

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

 

 





