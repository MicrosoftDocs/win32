---
description: The TAPI LINE\_DEVSPECIFICEX message is sent to notify the application about device-specific events occurring on a line, address, or call. The meaning of the message and the interpretation of the parameters are device specific.
ms.assetid: 137e91fd-a09e-430c-9d46-8e5be65f03d1
title: LINE_DEVSPECIFICEX message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_DEVSPECIFICEX message

The TAPI **LINE\_DEVSPECIFICEX** message is sent to notify the application about device-specific events occurring on a line, address, or call. The meaning of the message and the interpretation of the parameters are device specific.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to either a line device or call. This parameter is device specific.

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

The **LINE\_DEVSPECIFICEX** message is used by a service provider in conjunction with the [**lineDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-linedevspecific) function. Its meaning is device specific.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




