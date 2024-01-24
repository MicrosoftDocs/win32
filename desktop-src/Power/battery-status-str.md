---
description: Contains the current state of the battery.
ms.assetid: 514906a1-9d7a-40cb-9798-84f6b93d7bfe
title: BATTERY_STATUS structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_STATUS
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_STATUS structure

Contains the current state of the battery. This structure is used by the [**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md) control code.

## Syntax


```C++
typedef struct _BATTERY_STATUS {
  ULONG PowerState;
  ULONG Capacity;
  ULONG Voltage;
  LONG  Rate;
} BATTERY_STATUS, *PBATTERY_STATUS;
```



## Members

<dl> <dt>

**PowerState**
</dt> <dd>

The battery state. This member can be zero, one, or more of the following values.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <span id="BATTERY_CHARGING"></span><span id="battery_charging"></span><dl> <dt>**BATTERY\_CHARGING**</dt> <dt>0x00000004</dt> </dl>                  | Indicates that the battery is currently charging.<br/>                                         |
| <span id="BATTERY_CRITICAL"></span><span id="battery_critical"></span><dl> <dt>**BATTERY\_CRITICAL**</dt> <dt>0x00000008</dt> </dl>                  | Indicates that battery failure is imminent. See the Remarks section for more information.<br/> |
| <span id="BATTERY_DISCHARGING"></span><span id="battery_discharging"></span><dl> <dt>**BATTERY\_DISCHARGING**</dt> <dt>0x00000002</dt> </dl>         | Indicates that the battery is currently discharging.<br/>                                      |
| <span id="BATTERY_POWER_ON_LINE"></span><span id="battery_power_on_line"></span><dl> <dt>**BATTERY\_POWER\_ON\_LINE**</dt> <dt>0x00000001</dt> </dl> | Indicates that the system has access to AC power, so no batteries are being discharged.<br/>   |



 

</dd> <dt>

**Capacity**
</dt> <dd>

The current battery capacity, in mWh (or relative). This value can be used to generate a "gas gauge" display by dividing it by **FullChargedCapacity** member of the [**BATTERY\_INFORMATION**](battery-information-str.md) structure. If the capacity is unavailable, this member is BATTERY\_UNKNOWN\_CAPACITY.

</dd> <dt>

**Voltage**
</dt> <dd>

The current battery voltage across the battery terminals, in millivolts (mv). If the voltage is unavailable, this member is BATTERY\_UNKNOWN\_VOLTAGE.

</dd> <dt>

**Rate**
</dt> <dd>

The current rate of battery charge or discharge. This value will be in milliwatts unless the battery rate information is relative, in which case it will be in arbitrary units per hour. To determine if battery information is relative, examine the BATTERY\_CAPACITY\_RELATIVE flag in the **Capabilities** member of the [**BATTERY\_INFORMATION**](battery-information-str.md) structure. A nonzero, positive rate indicates charging; a negative rate indicates discharging. Some batteries report only discharging rates. If the rate is unavailable, this member is BATTERY\_UNKNOWN\_RATE. If the state of the battery or power source changes, the rate may become available.

</dd> </dl>

## Remarks

The BATTERY\_CRITICAL flag in the **PowerState** member of this structure indicates a hardware "battery critical" condition. This critical level is set by the battery manufacturer, not by the user in the "critical battery alarm." It generally means that the battery system has calculated that the battery is totally drained, and any power being drawn is beyond what is expected.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**BATTERY\_INFORMATION**](battery-information-str.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md)
</dt> </dl>

 

 




