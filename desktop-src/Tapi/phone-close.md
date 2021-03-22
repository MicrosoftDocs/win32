---
description: The TAPI PHONE\_CLOSE message is sent when an open phone device has been forcibly closed as part of resource reclamation. The device handle is no longer valid once this message has been sent.
ms.assetid: 84650abf-235e-4792-a67d-2f0f08b85a32
title: PHONE_CLOSE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_CLOSE message

The TAPI **PHONE\_CLOSE** message is sent when an open phone device has been forcibly closed as part of resource reclamation. The device handle is no longer valid once this message has been sent.


```C++
            
```



## Parameters

<dl> <dt>

*hPhone* 
</dt> <dd>

A handle to the open phone device that was closed. The handle is no longer valid after this message has been sent.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The application's callback instance that provided when opening the phone device.

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

The **PHONE\_CLOSE** message is only sent to an application after an open phone has been forcibly closed. This can be done to prevent a single application from monopolizing a phone device for too long. Whether the phone can be reopened immediately after a forced close is device specific.

An open phone device can also be forcibly closed after the user has modified the configuration of that phone or its driver. If the user wants the configuration changes to be effective immediately (as opposed to after the next system restart), and these changes affect the application's current view of the device (such as a change in device capabilities), then a service provider can forcibly close the phone device.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




