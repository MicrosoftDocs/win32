---
title: IUPnPEventingControl interface (upnp.h)
description: Enables the caller to disable eventing for UPnP services created for UPnP devices.
ms.topic: reference
ms.date: 09/12/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumPStoreProviders
api_type: 
- COM
api_location: 
- upnp.h
---

# IUPnPEventingControl interface

Enables the caller to disable eventing for UPnP services created for UPnP devices.


## Members

The **IUPnPEventingControl** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IEnumPStoreProviders** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumPStoreProviders** interface has these methods.



| Method                                      | Description                                                                                        |
|:--------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**DisableServiceEventing**](iupnpeventingcontrol-disableserviceeventing.md) | Causes UPnP services to be created without setting up event callback functions and without subscribing to event sources. |

## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>upnp.h</dt> </dl>    |
| Minimum supported client | Windows version 1803 |
| Minimum supported server | Windows version 1803 |
