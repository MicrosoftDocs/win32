---
title: ISurfaceManager get\_Device method
description: The get\_Device method retrieves the device that owns the surface.
ms.assetid: '94199e41-b96f-4191-88da-1d6ff8332a1e'
keywords: ["get_Device method Windows Movie Maker and DVD Maker", "get_Device method Windows Movie Maker and DVD Maker , ISurfaceManager interface", "ISurfaceManager interface Windows Movie Maker and DVD Maker , get_Device method"]
topic_type:
- apiref
api_name:
- ISurfaceManager.get_Device
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ISurfaceManager::get\_Device method

The **get\_Device** method retrieves the device that owns the surface.

## Syntax


```C++
HRESULT get_Device(
  [out] IDirect3DDevice9 **ppDevice
);
```



## Parameters

<dl> <dt>

*ppDevice* \[out\]
</dt> <dd>

Pointer to a pointer to an **IDirect3DDevice9** interface that manages the current surface.

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

 

 





