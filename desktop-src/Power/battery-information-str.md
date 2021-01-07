---
description: Contains battery information.
ms.assetid: 6a236f48-5a06-4537-a769-bd68e5c0eb27
title: BATTERY_INFORMATION structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_INFORMATION
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_INFORMATION structure

Contains battery information. This structure is returned by the [**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md) control code when the BatteryInformation information level is requested.

## Syntax


```C++
typedef struct _BATTERY_INFORMATION {
  ULONG Capabilities;
  UCHAR Technology;
  UCHAR Reserved[3];
  UCHAR Chemistry[4];
  ULONG DesignedCapacity;
  ULONG FullChargedCapacity;
  ULONG DefaultAlert1;
  ULONG DefaultAlert2;
  ULONG CriticalBias;
  ULONG CycleCount;
} BATTERY_INFORMATION, *PBATTERY_INFORMATION;
```



## Members

<dl> <dt>

**Capabilities**
</dt> <dd>

The battery capabilities. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BATTERY_CAPACITY_RELATIVE"></span><span id="battery_capacity_relative"></span><dl> <dt>**BATTERY\_CAPACITY\_RELATIVE**</dt> <dt>0x40000000</dt> </dl>                    | Indicates that the battery capacity and rate information are relative, and not in any specific units. If this bit is not set, the reporting units are milliwatt-hours (mWh) for capacity and milliwatts (mW) for rate. If this bit is set, all references to units in the other battery documentation can be ignored. All rate information is reported in units per hour. For example, if the fully charged capacity is reported as 100, a rate of 200 indicates that the battery will use all of its capacity in half an hour.<br/> |
| <span id="BATTERY_IS_SHORT_TERM"></span><span id="battery_is_short_term"></span><dl> <dt>**BATTERY\_IS\_SHORT\_TERM**</dt> <dt>0x20000000</dt> </dl>                               | Indicates that the normal operation is for a fail-safe function. If this bit is not set the battery is expected to be used during normal system usage.<br/>                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="BATTERY_SET_CHARGE_SUPPORTED"></span><span id="battery_set_charge_supported"></span><dl> <dt>**BATTERY\_SET\_CHARGE\_SUPPORTED**</dt> <dt>0x00000001</dt> </dl>          | Indicates that set information requests of the type BatteryCharge are supported by this battery device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="BATTERY_SET_DISCHARGE_SUPPORTED"></span><span id="battery_set_discharge_supported"></span><dl> <dt>**BATTERY\_SET\_DISCHARGE\_SUPPORTED**</dt> <dt>0x00000002</dt> </dl> | Indicates that set information requests of the type BatteryDischarge are supported by this battery device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="BATTERY_SYSTEM_BATTERY"></span><span id="battery_system_battery"></span><dl> <dt>**BATTERY\_SYSTEM\_BATTERY**</dt> <dt>0x80000000</dt> </dl>                             | Indicates that the battery can provide general power to run the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

</dd> <dt>

**Technology**
</dt> <dd>

The battery technology. This member can be one of the following values.



| Value                                                                        | Meaning                                                    |
|------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Nonrechargeable battery, for example, alkaline.<br/> |
| <dl> <dt>1</dt> </dl> | Rechargeable battery, for example, lead acid.<br/>   |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Chemistry**
</dt> <dd>

An abbreviated character string that indicates the battery's chemistry. This string is not necessarily zero-terminated. The following is a partial list of abbreviations that can be returned and the associated chemistries.



| Unicode string                                                                                                                                           | Meaning                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <span id="PbAc"></span><span id="pbac"></span><span id="PBAC"></span><dl> <dt>**PbAc**</dt> </dl> | Lead Acid<br/>                       |
| <span id="LION"></span><span id="lion"></span><dl> <dt>**LION**</dt> </dl>                        | Lithium Ion<br/>                     |
| <span id="Li-I"></span><span id="li-i"></span><span id="LI-I"></span><dl> <dt>**Li-I**</dt> </dl> | Lithium Ion<br/>                     |
| <span id="NiCd"></span><span id="nicd"></span><span id="NICD"></span><dl> <dt>**NiCd**</dt> </dl> | Nickel Cadmium<br/>                  |
| <span id="NiMH"></span><span id="nimh"></span><span id="NIMH"></span><dl> <dt>**NiMH**</dt> </dl> | Nickel Metal Hydride<br/>            |
| <span id="NiZn"></span><span id="nizn"></span><span id="NIZN"></span><dl> <dt>**NiZn**</dt> </dl> | Nickel Zinc<br/>                     |
| <span id="RAM"></span><span id="ram"></span><dl> <dt>**RAM**</dt> </dl>                           | Rechargeable Alkaline-Manganese<br/> |



 

Other chemistries may appear in the future and your code should be able to handle them.

</dd> <dt>

**DesignedCapacity**
</dt> <dd>

The theoretical capacity of the battery when new, in mWh unless BATTERY\_CAPACITY\_RELATIVE is set. In that case, the units are undefined.

</dd> <dt>

**FullChargedCapacity**
</dt> <dd>

The battery's current fully charged capacity in mWh (or relative). Compare this value to **DesignedCapacity** to estimate the battery's wear.

</dd> <dt>

**DefaultAlert1**
</dt> <dd>

The manufacturer's suggested capacity, in mWh, at which a low battery alert should occur. Definitions of low vary from manufacturer to manufacturer. In general, a warning state will occur before a low state, but you should not assume that it always will. To reduce risk of data loss, this value is usually used as the default setting for the critical battery alarm.

</dd> <dt>

**DefaultAlert2**
</dt> <dd>

The manufacturer's suggested capacity, in mWh, at which a warning battery alert should occur. Definitions of warning vary from manufacturer to manufacturer. In general, a warning state will occur before a low state, but you should not assume that it always will. To reduce risk of data loss, this value is usually used as the default setting for the low battery alarm.

</dd> <dt>

**CriticalBias**
</dt> <dd>

A bias from zero, in mWh, which is applied to battery reporting. Some batteries reserve a small charge that is biased out of the battery's capacity values to show "0" as the critical battery level. Critical bias is analogous to setting a fuel gauge to show "empty" when there are several liters of fuel left.

</dd> <dt>

**CycleCount**
</dt> <dd>

The number of charge/discharge cycles the battery has experienced. This provides a means to determine the battery's wear. If the battery does not support a cycle counter, this member is zero.

</dd> </dl>

## Remarks

Generally, a warning state occurs before a low state, but you should not assume it will. It is possible to poll a battery and find that neither alert level has occurred, and poll the battery again and find it discharged to the extent that both levels have been achieved. This may indicate that you are not polling often enough. It may also indicate that the battery is unable to hold a charge for very long and is discharging more rapidly than you expected. Such a battery may be nearing the end of its useful life, or it may be damaged.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)
</dt> </dl>

 

 




