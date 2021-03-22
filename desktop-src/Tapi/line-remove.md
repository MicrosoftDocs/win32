---
description: The TAPI LINE\_REMOVE message is sent to inform an application of the removal (deletion from the system) of a line device.
ms.assetid: 21b912d6-34aa-4ac0-b019-be3c851cc96d
title: LINE_REMOVE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_REMOVE message

The TAPI **LINE\_REMOVE** message is sent to inform an application of the removal (deletion from the system) of a line device. Generally, this is not used for temporary removals, such as extraction of PCMCIA devices, but only for permanent removals in which the device would no longer be reported by the service provider if TAPI were reinitialized.


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

Identifier of the line device that was removed.

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

Applications supporting TAPI version 2.0 or later are sent a **LINE\_REMOVE** message. This informs them that the device has been removed from the system. The **LINE\_REMOVE** message is preceded by a [**LINE\_CLOSE**](line-close.md) message on each line handle, if the application had the line open. This message is sent to all applications supporting TAPI version 2.0 or later that have called [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa), including those that do not have any line devices open at the time.

Older applications are sent a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message specifying LINEDEVSTATE\_REMOVED, followed by a LINE\_CLOSE message. Unlike the **LINE\_REMOVE** message, however, these older applications can receive these messages only if they have the line open when it is removed. If they do not have the line open, their only indication that the device was removed would be receiving a LINEERR\_NODEVICE error when they attempt to access the device.

After a device has been removed, any attempt to access the device by its device identifier results in a LINEERR\_NODEVICE error. After all TAPI applications have shutdown so that TAPI can restart, and when TAPI is reinitialized, the removed device no longer occupies a device identifier.

> [!Note]  
> Implementation: it is TAPI that returns this LINEERR\_NODEVICE; after a **LINE\_REMOVE** message is received from a service provider; no further calls are made to that service provider using that line device identifier.

 

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CLOSE**](line-close.md)
</dt> <dt>

[**LINE\_LINEDEVSTATE**](line-linedevstate.md)
</dt> <dt>

[**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa)
</dt> </dl>

 

 




