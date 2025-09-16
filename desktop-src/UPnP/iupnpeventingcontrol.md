---
title: IUPnPEventingControl interface (upnp.h)
description: Enables the caller to disable eventing for UPnP services created for UPnP devices.
ms.topic: reference
ms.date: 09/12/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUPnPEventingControl
api_type: 
- COM
api_location: 
- upnp.h
---

# IUPnPEventingControl interface

Enables the caller to disable eventing for UPnP services created for UPnP devices.


## Members

The **IUPnPEventingControl** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUPnPEventingControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IUPnPEventingControl** interface has these methods.



| Method                                      | Description                                                                                        |
|:--------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**DisableServiceEventing**](iupnpeventingcontrol-disableserviceeventing.md) | Causes UPnP services to be created without setting up event callback functions and without subscribing to event sources. |

## Remarks

This interface is currently not defined in a Windows SDK header. The following definition can be used to instantiate the interface.

```cpp
[
    object,
    uuid(29B4FDFE-201B-4581-BAA5-88A2CC12668E),
    oleautomation,
    pointer_default(unique),
]
interface IUPnPEventingControl : IUnknown
{
    HRESULT DisableServiceEventing();
}
```

This interface is obtained by calling **QueryInterface** on the same object that provides an implementation of the [IUPnPDeviceFinder](/windows/win32/api/upnp/nn-upnp-iupnpdevicefinder) or [IUPnPDescriptionDocument](/windows/win32/api/upnp/nn-upnp-iupnpdescriptiondocument)interfaces, after which [DisableServiceEventing](iupnpeventingcontrol-disableserviceeventing.md) can be called on it.

## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>N/A</dt> </dl>    |
| Minimum supported client | Windows version 1803 |
| Minimum supported server | Windows version 1803 |
