---
description: The TAPI LINE\_DEVSPECIFICFEATURE message is sent to notify the application about device-specific events occurring on a line, address, or call. The meaning of the message and the interpretation of the parameters are device specific.
ms.assetid: 5f1a4da2-1a2a-4a18-8a69-82d27ddca9cf
title: LINE_DEVSPECIFICFEATURE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_DEVSPECIFICFEATURE message

The TAPI **LINE\_DEVSPECIFICFEATURE** message is sent to notify the application about device-specific events occurring on a line, address, or call. The meaning of the message and the interpretation of the parameters are device specific.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to either a line device or call. This is device specific.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

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

## Remarks

The **LINE\_DEVSPECIFICFEATURE** message is used by a service provider in conjunction with the [**lineDevSpecificFeature**](/windows/desktop/api/Tapi/nf-tapi-linedevspecificfeature) function. Its meaning is device specific.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




