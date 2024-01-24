---
description: TAPI sends the PHONE\_DEVSPECIFIC message to an application to notify the application about device-specific events occurring at the phone. The meaning of the message and the interpretation of the parameters is implementation-defined.
ms.assetid: e3e803dd-b041-48b7-9acf-a89989370204
title: PHONE_DEVSPECIFIC message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_DEVSPECIFIC message

TAPI sends the **PHONE\_DEVSPECIFIC** message to an application to notify the application about device-specific events occurring at the phone. The meaning of the message and the interpretation of the parameters is implementation-defined.


```C++
            
```



## Parameters

<dl> <dt>

*hPhone* 
</dt> <dd>

A handle to the phone device.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The application's callback instance provided when opening the phone device.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Device specific.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Device specific.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Device specific.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




