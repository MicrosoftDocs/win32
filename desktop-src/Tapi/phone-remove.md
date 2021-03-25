---
description: The TAPI PHONE\_REMOVE message is sent to inform an application of the removal (deletion from the system) of a phone device.
ms.assetid: 7c888976-65da-477a-b5a6-6e78d5f603b1
title: PHONE_REMOVE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_REMOVE message

The TAPI **PHONE\_REMOVE** message is sent to inform an application of the removal (deletion from the system) of a phone device. Generally, this is not used for temporary removals, such as extraction of PCMCIA devices, but only for permanent removals in which the device would no longer be reported by the service provider if TAPI were reinitialized.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

Reserved. Set to zero.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

Reserved. Set to zero.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Identifier of the phone device that was removed.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Reserved. Set to zero.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Reserved. Set to zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Applications TAPI version 2.0 or later are sent a **PHONE\_REMOVE** message. This informs them that the device has been removed from the system. The **PHONE\_REMOVE** message is preceded by a [**PHONE\_CLOSE**](phone-close.md) message on each phone handle, if the application had the phone open. This message is sent to all applications supporting TAPI version 2.0 or later that have called [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa), including those that do not have any phone devices open at the time.

Older applications (that negotiated TAPI version 1.4 or earlier) are sent a [**PHONE\_STATE**](phone-state.md) message specifying PHONESTATE\_REMOVED, followed by a [**PHONE\_CLOSE**](phone-close.md) message. Unlike the **PHONE\_REMOVE** message, however, these older applications can receive these messages only if they have the phone open when it is removed. If they do not have the phone open, their only indication that the device was removed would be receiving a PHONEERR\_NODEVICE when they attempt to access the device.

After a device has been removed, any attempt to access the device by its device identifier results in a PHONEERR\_NODEVICE error. After all TAPI applications have shutdown so that TAPI can restart, and when TAPI is reinitialized, the removed device no longer occupies a device identifier.

> [!Note]  
> Implementation: it is TAPI that returns this PHONEERR\_NODEVICE message after a PHONE\_REMOVE message is received from a service provider; no further calls are made to that service provider using that phone device identifier.

 

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**PHONE\_CLOSE**](phone-close.md)
</dt> <dt>

[**PHONE\_STATE**](phone-state.md)
</dt> <dt>

[**phoneInitialize**](/windows/desktop/api/Tapi/nf-tapi-phoneinitialize)
</dt> <dt>

[**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa)
</dt> </dl>

 

 




