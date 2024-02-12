---
description: Causes the Virtual Machine Worker to return the specified virtual device.
title: IVmVirtualDeviceAccess::GetDevice method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmVirtualDeviceAccess::GetDevice
api_type: 
- COM
api_location: 
- vmprox.dll
---

# IVmVirtualDeviceAccess::GetDevice method

Causes the Virtual Machine Worker to return the specified virtual device.

## Syntax


```C++
HRESULT GetDevice(
    [in]          REFGUID    CategoryID,
    [in]          REFGUID    DeviceID,
    [out, retval] IUnknown** Device
);

```



## Parameters

### CategoryID [in]

The device category ID.

### DeviceID [in]

The device instance ID.

### Device [out, retval]

Receives a pointer to an **IUnknown** interface representing the device.


## Return value

An HRESULT.

## Remarks 

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from TBD.



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |
| DLL  | vmprox.dll |



## See also



 

 
