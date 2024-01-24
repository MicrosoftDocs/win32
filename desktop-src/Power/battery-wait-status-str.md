---
description: Contains information about the conditions under which the battery status is to be retrieved.
ms.assetid: 1750fe0f-ba3d-4118-938c-789c6d62c3f7
title: BATTERY_WAIT_STATUS structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_WAIT_STATUS
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_WAIT\_STATUS structure

Contains information about the conditions under which the battery status is to be retrieved. This structure is used by the [**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md) control code.

## Syntax


```C++
typedef struct _BATTERY_WAIT_STATUS {
  ULONG BatteryTag;
  ULONG Timeout;
  ULONG PowerState;
  ULONG LowCapacity;
  ULONG HighCapacity;
} BATTERY_WAIT_STATUS, *PBATTERY_WAIT_STATUS;
```



## Members

<dl> <dt>

**BatteryTag**
</dt> <dd>

The current battery tag for the battery. Only information for a battery matching the tag can be returned. Whenever this value does not match the battery's current tag, the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) operation will fail with an error code of ERROR\_FILE\_NOT\_FOUND, which indicates to the caller that the battery for which it has a tag is no longer installed The caller may opt to use the [**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md) operation to determine the tag of the newly installed battery, if any. In addition, if the request is in progress when the battery is removed, or the tag changes, the operation is aborted with the status of ERROR\_FILE\_NOT\_FOUND. (See [Battery Tags](battery-information.md) for more information.)

</dd> <dt>

**Timeout**
</dt> <dd>

The number of milliseconds the request will wait for the condition specified by the **PowerState**, **LowCapacity**, and **HighCapacity** members before completing. A value of -1 indicates that the request will wait indefinitely for the conditions to be satisfied. A value of zero indicates that the requested battery information is to be returned immediately, regardless of the other conditions. Any other value indicates that the request should wait that length of time, or until any one of the other conditions is satisfied.

If the computer has entered sleep mode, the clock will continue to run, but exhausting the count will not wake the computer up. If the count is exhausted when the computer is awoken, and other conditions are satisfied, the call will return immediately on awakening.

</dd> <dt>

**PowerState**
</dt> <dd>

Zero, one, or more of the following status bits, which indicate the state of the battery. It is identical to the **PowerState** member of the [**BATTERY\_STATUS**](battery-status-str.md) structure.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <span id="BATTERY_CHARGING"></span><span id="battery_charging"></span><dl> <dt>**BATTERY\_CHARGING**</dt> <dt>0x00000004</dt> </dl>                  | Indicates that the battery is currently charging.<br/>                                         |
| <span id="BATTERY_CRITICAL"></span><span id="battery_critical"></span><dl> <dt>**BATTERY\_CRITICAL**</dt> <dt>0x00000008</dt> </dl>                  | Indicates that battery failure is imminent. See the Remarks section for more information.<br/> |
| <span id="BATTERY_DISCHARGING"></span><span id="battery_discharging"></span><dl> <dt>**BATTERY\_DISCHARGING**</dt> <dt>0x00000002</dt> </dl>         | Indicates that the battery is currently discharging.<br/>                                      |
| <span id="BATTERY_POWER_ON_LINE"></span><span id="battery_power_on_line"></span><dl> <dt>**BATTERY\_POWER\_ON\_LINE**</dt> <dt>0x00000001</dt> </dl> | Indicates that the battery has access to AC power.<br/>                                        |



 

</dd> <dt>

**LowCapacity**
</dt> <dd>

The current battery capacity, in mWh (or relative). This value is identical to the **Capacity** member of the [**BATTERY\_STATUS**](battery-status-str.md) structure.

</dd> <dt>

**HighCapacity**
</dt> <dd>

The current battery capacity, in mWh (or relative). This value is identical to the **Capacity** member of the [**BATTERY\_STATUS**](battery-status-str.md) structure.

</dd> </dl>

## Remarks

Requests for battery information are postponed until one of the following occurs:

-   The time-out expires (assuming **Timeout** is not -1).
-   The battery's current status does not match **PowerState**.
-   The battery's capacity is below **LowCapacity**.
-   The battery's capacity is above **HighCapacity**.
-   The battery tag changes.

When any one of these conditions is satisfied, the data is collected and the operation returns. This allows applications to monitor typical dynamic battery information without polling the device.

Before using either of the two Capacity conditions, make sure the battery supports them by using the [**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md) control code with a time-out of zero. Examine the results to determine if the **Capacity** member is supported (that is, not BATTERY\_UNKNOWN\_CAPACITY).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**BATTERY\_STATUS**](battery-status-str.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md)
</dt> </dl>

 

