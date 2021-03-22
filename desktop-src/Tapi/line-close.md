---
description: The TAPI LINE\_CLOSE message is sent when the specified line device has been forcibly closed. The line device handle or any call handles for calls on the line are no longer valid once this message has been sent.
ms.assetid: f254e331-d574-4fa7-8447-6e4535d3d773
title: LINE_CLOSE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CLOSE message

The TAPI **LINE\_CLOSE** message is sent when the specified line device has been forcibly closed. The line device handle or any call handles for calls on the line are no longer valid once this message has been sent.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the line device that was closed. This handle is no longer valid.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_CLOSE** message is sent to any application only after the TAPI service provider (TSP) has forcibly closed an open line. Whether or not the line can be reopened immediately after a forced close is device-specific.

The causing condition can be a significant change of state, a hardware error, a loss of connection to a server, or even potentially to prevent a single application from monopolizing a line device for too long. A line device can also be forcibly closed after the user has modified the configuration of that line or its driver. If the user wants the configuration changes to be effective immediately (as opposed to after the next system restart), and they affect the application's current view of the device (such as a change in device capabilities), then a service provider can forcibly close the line device.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




