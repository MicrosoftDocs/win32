---
title: IMsTscAxEvents OnRequestContainerMinimize method
description: Called when the user presses the Minimize button on the connection bar in full-screen mode. The firing of this event is a request that the container application minimize itself.
ms.assetid: fc052f9b-cf59-4d5a-ba39-571627b72f2a
ms.tgt_platform: multiple
keywords:
- OnRequestContainerMinimize method Remote Desktop Services
- OnRequestContainerMinimize method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnRequestContainerMinimize method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnRequestContainerMinimize
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnRequestContainerMinimize method

Called when the user presses the **Minimize** button on the connection bar in full-screen mode. The firing of this event is a request that the container application minimize itself.

## Syntax


```C++
void OnRequestContainerMinimize();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method will only be called if the container-handled full-screen mode is enabled - see [**IMsTscAdvancedSettings::put\_ContainerHandledFullScreen**](imstscadvancedsettings-containerhandledfullscreen.md) for more information.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





