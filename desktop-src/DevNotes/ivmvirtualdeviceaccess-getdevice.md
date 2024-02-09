---
description: TBD
title: IVmVirtualDeviceAccess::GetDevice method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.GetInfo
api_type: 
- COM
api_location: 
- TBD
---

# IVmVirtualDeviceAccess::GetDevice method

TBD

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

TBD

### DeviceID [in]

TBD

### Device [out, retval]

TBD




## Return value

An HRESULT.

## Remarks 

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from TBD.



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |
| DLL  | TBD |



## See also



 

 
