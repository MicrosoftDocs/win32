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
- NA
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




## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |




## See also



 

 
