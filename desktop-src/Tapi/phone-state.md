---
description: TAPI sends the PHONE\_STATE message to an application whenever the status of a phone device changes.
ms.assetid: 74e74b62-8387-4056-83e6-2350b3da4077
title: PHONE_STATE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_STATE message

TAPI sends the **PHONE\_STATE** message to an application whenever the status of a phone device changes.


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

The phone state that has changed. This parameter uses one of the [**PHONESTATE\_ constants**](phonestate--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

Phone state-dependent information detailing the status change. This parameter is not used if multiple flags are set in *dwParam1*, because multiple status items have changed. The application should invoke [**phoneGetStatus**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatus) to obtain a complete set of information.

If *dwParam1* is PHONESTATE\_OWNER, *dwParam2* contains the new number of owners.

If *dwParam1* is PHONESTATE\_MONITORS, *dwParam2* contains the new number of monitors.

If *dwParam1* is PHONESTATE\_LAMP, *dwParam2* contains the button/lamp identifier of the lamp that has changed.

If *dwParam1* is PHONESTATE\_RINGMODE, *dwParam2* contains the new ring mode.

If *dwParam1* is PHONESTATE\_HANDSET, SPEAKER or HEADSET, *dwParam2* contains the new hookswitch mode of that hookswitch device. This parameter uses one of the [**PHONEHOOKSWITCHMODE\_ constants**](phonehookswitchmode--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

No return value.

## Remarks

Sending the **PHONE\_STATE** message to the application can be controlled and queried using [**phoneSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonesetstatusmessages) and [**phoneGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatusmessages). By default, this message is disabled for all state changes except for PHONESTATE\_REINIT, which cannot be disabled. This message is sent to all applications that have a handle to the phone, including those that called [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen) with the *dwPrivileges* parameter set to PHONEPRIVILEGE\_OWNER or PHONEPRIVILEGE\_MONITOR.

A **PHONE\_STATE** message with an Owners and/or Monitors indication is sent to applications that already have a handle for the phone. This can be the result of another application changing ownership or monitorship of the phone device with [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen), [**phoneClose**](/windows/desktop/api/Tapi/nf-tapi-phoneclose) or [**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown).

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**PHONE\_CLOSE**](phone-close.md)
</dt> <dt>

[**PHONECAPS**](/windows/desktop/api/Tapi/ns-tapi-phonecaps)
</dt> <dt>

[**phoneClose**](/windows/desktop/api/Tapi/nf-tapi-phoneclose)
</dt> <dt>

[**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps)
</dt> <dt>

[**phoneGetStatus**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatus)
</dt> <dt>

[**phoneGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatusmessages)
</dt> <dt>

[**phoneInitialize**](/windows/desktop/api/Tapi/nf-tapi-phoneinitialize)
</dt> <dt>

[**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa)
</dt> <dt>

[**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen)
</dt> <dt>

[**phoneSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonesetstatusmessages)
</dt> <dt>

[**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown)
</dt> </dl>

 

 




