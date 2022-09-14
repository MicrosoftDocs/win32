---
description: The TAPI LINE\_CREATE message is sent to inform the application of the creation of a new line device.
ms.assetid: d4735eab-392f-49d9-a1d9-5895d9232624
title: LINE_CREATE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CREATE message

The TAPI **LINE\_CREATE** message is sent to inform the application of the creation of a new line device.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

Unused.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The *hDeviceID* of the newly created device.

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

Older applications (that negotiated TAPI version 1.3) are sent a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message specifying LINEDEVSTATE\_REINIT, which requires them to shut down their use of the API and call [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize) again to obtain the new number of devices. Unlike previous versions of TAPI, however, this version does not require all applications to shut down before allowing applications to reinitialize; reinitialization can take place immediately when a new device is created (complete shutdown is still required when a service provider is removed from the system).

Applications supporting TAPI version 1.4 or later are sent a **LINE\_CREATE** message. This informs them of the existence of the new device and its new device identifier. The application can then choose whether or not to attempt working with the new device at its leisure. This message is sent to all applications supporting this or subsequent versions of the API that have called [**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize) or [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa), including those that do not have any line devices open at the time.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_LINEDEVSTATE**](line-linedevstate.md)
</dt> <dt>

[**lineInitialize**](/windows/desktop/api/Tapi/nf-tapi-lineinitialize)
</dt> <dt>

[**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa)
</dt> </dl>

 

 




