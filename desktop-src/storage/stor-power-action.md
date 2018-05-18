---
title: STOR\_POWER\_ACTION enumeration
description: The STOR\_POWER\_ACTION enumerator indicates the power state that the system is about to enter during a power transition.
ms.assetid: 'ffc7c1ec-faec-4383-ab69-844cf68d054f'
keywords: ["STOR_POWER_ACTION enumeration Storage Devices", "PSTOR_POWER_ACTION enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_POWER_ACTION
api_location:
- storport.h
api_type:
- HeaderDef
---

# STOR\_POWER\_ACTION enumeration

The STOR\_POWER\_ACTION enumerator indicates the power state that the system is about to enter during a power transition.

## Syntax


```C++
typedef enum  { 
  StorPowerActionNone           = 0,
  StorPowerActionReserved       = 1,
  StorPowerActionSleep          = 2,
  StorPowerActionHibernate      = 3,
  StorPowerActionShutdown       = 4,
  StorPowerActionShutdownReset  = 5,
  StorPowerActionShutdownOff    = 6,
  StorPowerActionWarmEject      = 7
} STOR_POWER_ACTION, *PSTOR_POWER_ACTION;
```



## Constants

<dl> <dt>

<span id="StorPowerActionNone"></span><span id="storpoweractionnone"></span><span id="STORPOWERACTIONNONE"></span>**StorPowerActionNone**
</dt> <dd>

No system shutdown is about to occur.

</dd> <dt>

<span id="StorPowerActionReserved"></span><span id="storpoweractionreserved"></span><span id="STORPOWERACTIONRESERVED"></span>**StorPowerActionReserved**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="StorPowerActionSleep"></span><span id="storpoweractionsleep"></span><span id="STORPOWERACTIONSLEEP"></span>**StorPowerActionSleep**
</dt> <dd>

The system is entering standby.

</dd> <dt>

<span id="StorPowerActionHibernate"></span><span id="storpoweractionhibernate"></span><span id="STORPOWERACTIONHIBERNATE"></span>**StorPowerActionHibernate**
</dt> <dd>

The system is entering hibernation.

</dd> <dt>

<span id="StorPowerActionShutdown"></span><span id="storpoweractionshutdown"></span><span id="STORPOWERACTIONSHUTDOWN"></span>**StorPowerActionShutdown**
</dt> <dd>

The system is shutting down, but the type of shutdown is not known.

</dd> <dt>

<span id="StorPowerActionShutdownReset"></span><span id="storpoweractionshutdownreset"></span><span id="STORPOWERACTIONSHUTDOWNRESET"></span>**StorPowerActionShutdownReset**
</dt> <dd>

The system is shutting down and resetting.

</dd> <dt>

<span id="StorPowerActionShutdownOff"></span><span id="storpoweractionshutdownoff"></span><span id="STORPOWERACTIONSHUTDOWNOFF"></span>**StorPowerActionShutdownOff**
</dt> <dd>

The system is shutting down and powering off.

</dd> <dt>

<span id="StorPowerActionWarmEject"></span><span id="storpoweractionwarmeject"></span><span id="STORPOWERACTIONWARMEJECT"></span>**StorPowerActionWarmEject**
</dt> <dd>

The system is preparing for ejection.

</dd> </dl>

## Requirements



|                   |                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h, Minitape.h, or Srb.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_POWER\_REQUEST\_BLOCK**](scsi-power-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_POWER_ACTION%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






