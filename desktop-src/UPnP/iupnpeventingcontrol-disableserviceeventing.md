---
title: IUPnPEventingControl::DisableServiceEventing method (upnp.h)
description: Causes UPnP services to be created without setting up event callback functions and without subscribing to event sources.
ms.topic: reference
ms.date: 09/12/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUPnPEventingControl::DisableServiceEventing
api_type: 
- COM
api_location: 
- upnp.h
---

# IUPnPEventingControl::DisableServiceEventing method

Causes UPnP services to be created without setting up event callback functions and without subscribing to event sources.

## Syntax


```C++
HRESULT DisableServiceEventing();
```



## Parameters

None.

## Return value

The return value is S_OK on success. Otherwise, it is an **HRESULT** value.

## Remarks

This function is currently not defined in a Windows SDK header. The following definition can be used to invoke the function.

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

The [IUPnPEventingControl](iupnpeventingcontrol.md) interface is obtained by calling **QueryInterface** on the same object that provides an implementation of the [IUPnPDeviceFinder](nn-upnp-iupnpdevicefinder) or [IUPnPDescriptionDocument](nn-upnp-iupnpdescriptiondocument) interfaces, after which **DisableServiceEventing** can be called on it.


## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>N/A</dt> </dl>    |
| Minimum supported client | Windows version 1803 |
| Minimum supported server | Windows version 1803 |
