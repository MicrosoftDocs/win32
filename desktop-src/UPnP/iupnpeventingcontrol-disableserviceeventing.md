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

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>upnp.h</dt> </dl>    |
| Minimum supported client | Windows version 1803 |
| Minimum supported server | Windows version 1803 |
