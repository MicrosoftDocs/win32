---
description: The TAPI PHONE\_CREATE message is sent to inform applications of the creation of a new phone device.
ms.assetid: 62895b10-76ce-456e-ad02-e2b7764616a8
title: PHONE_CREATE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_CREATE message

The TAPI **PHONE\_CREATE** message is sent to inform applications of the creation of a new phone device.


```C++
            
```



## Parameters

<dl> <dt>

*hPhone* 
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

Applications that negotiated API version 1.3 are sent a [**PHONE\_STATE**](phone-state.md) message specifying PHONESTATE\_REINIT, which requires them to shut down their use of the API and call [**phoneInitialize**](/windows/desktop/api/Tapi/nf-tapi-phoneinitialize) again to obtain the new number of devices. However, TAPI version 1.4 and above do not require all applications to shut down before allowing applications to reinitialize; reinitialization can take place immediately when a new device is created.

Applications supporting TAPI version 1.4 or later are sent a **PHONE\_CREATE** message. This informs them of the existence of the new device and its new device identifier. The application can then choose whether or not to attempt working with the new device at its leisure.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**PHONE\_STATE**](phone-state.md)
</dt> <dt>

[**phoneInitialize**](/windows/desktop/api/Tapi/nf-tapi-phoneinitialize)
</dt> <dt>

[**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa)
</dt> </dl>

 

 




