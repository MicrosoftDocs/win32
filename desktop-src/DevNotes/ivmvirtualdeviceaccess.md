---
description: TBD.
title: IVmVirtualDeviceAccess interface
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore
api_type: 
- COM
api_location: 
- TBD
---

# IVmVirtualDeviceAccess interface

TBD

## Syntax

```c++
[
    object,
    uuid( 3e57bd3c-5a5d-4bdc-a0a6-5b4193d4b719 ),
    pointer_default( unique )
]
interface IVmVirtualDeviceAccess : IUnknown
{
    ...
};
```

## Members

The **IVmVirtualDeviceAccess** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IVmVirtualDeviceAccess** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVmVirtualDeviceAccess** interface has these methods.



| Method                                                   | Description                                                                                                           |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| **ReservedMethod1** |  This method is reserved and is listed here to indicate the offset of other methods in the virtual method table for the interface. |
| **ReservedMethod2** |  This method is reserved and is listed here to indicate the offset of other methods in the virtual method table for the interface. |
| [**RemoteGetDevice**](ivmvirtualdeviceaccess-remotegetdevice.md)                   | TBD |

## Remarks

These functions have no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from TBD.

## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |
| DLL    | TBD |



 

 
