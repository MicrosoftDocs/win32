---
description: TBD
title: IVmVirtualDeviceAccess::RemoteGetDevice method
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

# IVmVirtualDeviceAccess::RemoteGetDevice method

TBD

## Syntax


```C++
HRESULT RemoteGetDevice(
    [in]  REFGUID    CategoryID,
    [in]  REFGUID    DeviceID,
    [out] IUnknown** Device,
    [out] IUnknown** ErrorInfo
);
```



## Parameters

### CategoryID [in]

TBD

### DeviceID [in]

TBD

### Device [in]

TBD

### ErrorInfo [in]

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



 

 
