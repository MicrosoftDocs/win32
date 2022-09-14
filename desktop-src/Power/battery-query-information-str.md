---
description: Contains battery query information.
ms.assetid: ef5466fe-7de8-48cd-ad48-5774d7a4bb46
title: BATTERY_QUERY_INFORMATION structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_QUERY_INFORMATION
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_QUERY\_INFORMATION structure

Contains battery query information. This structure is used with the [**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md) control code to specify the type of information to return.

## Syntax


```C++
typedef struct _BATTERY_QUERY_INFORMATION {
  ULONG                           BatteryTag;
  BATTERY_QUERY_INFORMATION_LEVEL InformationLevel;
  LONG                            AtRate;
} BATTERY_QUERY_INFORMATION, *PBATTERY_QUERY_INFORMATION;
```



## Members

<dl> <dt>

**BatteryTag**
</dt> <dd>

The current battery tag for the battery. Only information for a battery matching the tag can be returned. Whenever this value does not match the battery's current tag, the IOCTL request will be completed with ERROR\_FILE\_NOT\_FOUND. This indicates to the caller that the battery associated with the tag longer exists. The caller may opt to use the [**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md) operation to determine the tag of the newly installed battery, if one exists. (See [Battery Tags](battery-information.md) for more information.)

When a query information request is made, this value is verified. In addition, if the request is in progress while this value changes, the request is aborted with the status of ERROR\_FILE\_NOT\_FOUND.

</dd> <dt>

**InformationLevel**
</dt> <dd>

The level of the battery information being queried. The data returned by the IOCTL depends on this value. This member can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BatteryDeviceName"></span><span id="batterydevicename"></span><span id="BATTERYDEVICENAME"></span><dl> <dt>**BatteryDeviceName**</dt> <dt>4</dt> </dl>                                                 | Null-terminated Unicode string that contains the battery's name.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="BatteryEstimatedTime"></span><span id="batteryestimatedtime"></span><span id="BATTERYESTIMATEDTIME"></span><dl> <dt>**BatteryEstimatedTime**</dt> <dt>3</dt> </dl>                                     | A **ULONG** that specifies the estimated battery run time, in seconds. If the rate of drain provided in the **AtRate** member of the **BATTERY\_QUERY\_INFORMATION** structure is zero, this calculation is based on the present rate of drain. If **AtRate** is nonzero, the time returned is the expected run time for the given rate. If the estimated time is unknown (for example, the battery is not discharging and the **AtRate** specified was zero), the return value is BATTERY\_UNKNOWN\_TIME. Note that this value is not very accurate on some battery systems, and may vary widely depending on present power usage, which could be affected by disk activity and other factors. There is no notification mechanism for changes in this value.<br/> |
| <span id="BatteryGranularityInformation"></span><span id="batterygranularityinformation"></span><span id="BATTERYGRANULARITYINFORMATION"></span><dl> <dt>**BatteryGranularityInformation**</dt> <dt>1</dt> </dl> | An array of [**BATTERY\_REPORTING\_SCALE**](/windows/desktop/api/WinNT/ns-winnt-battery_reporting_scale) structures, never more than four entries.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="BatteryInformation"></span><span id="batteryinformation"></span><span id="BATTERYINFORMATION"></span><dl> <dt>**BatteryInformation**</dt> <dt>0</dt> </dl>                                             | A [**BATTERY\_INFORMATION**](battery-information-str.md) structure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="BatteryManufactureDate"></span><span id="batterymanufacturedate"></span><span id="BATTERYMANUFACTUREDATE"></span><dl> <dt>**BatteryManufactureDate**</dt> <dt>5</dt> </dl>                             | A [**BATTERY\_MANUFACTURE\_DATE**](battery-manufacture-date-str.md) structure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="BatteryManufactureName"></span><span id="batterymanufacturename"></span><span id="BATTERYMANUFACTURENAME"></span><dl> <dt>**BatteryManufactureName**</dt> <dt>6</dt> </dl>                             | Null-terminated Unicode string that specifies the name of the manufacturer of the battery.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="BatterySerialNumber"></span><span id="batteryserialnumber"></span><span id="BATTERYSERIALNUMBER"></span><dl> <dt>**BatterySerialNumber**</dt> <dt>8</dt> </dl>                                         | Null-terminated Unicode string that specifies the battery's serial number.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="BatteryTemperature"></span><span id="batterytemperature"></span><span id="BATTERYTEMPERATURE"></span><dl> <dt>**BatteryTemperature**</dt> <dt>2</dt> </dl>                                             | A **ULONG** that specifies the battery's current temperature, in 10ths of a degree Kelvin.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="BatteryUniqueID"></span><span id="batteryuniqueid"></span><span id="BATTERYUNIQUEID"></span><dl> <dt>**BatteryUniqueID**</dt> <dt>7</dt> </dl>                                                         | Null-terminated Unicode string that uniquely identifies the battery. This value can be used to track a specific battery. In the case of smart batteries, this ID would be the concatenation of the manufacturer's name, device name, date of manufacture, and a printable representation of the serial number. <br/> This value is not intended to be displayed to the user.<br/>                                                                                                                                                                                                                                                                                                                                                                            |



 

</dd> <dt>

**AtRate**
</dt> <dd>

This member is used only if **InformationLevel** is BatteryEstimatedTime.

If this member is nonzero, it is a rate of drain that will be used to calculate the time until the battery is discharged for the BatteryEstimatedTime of an individual battery. It must be specified in mW, and must be a negative value to represent a battery discharge rate.

</dd> </dl>

## Remarks

Some information about batteries is optional or may be meaningless for some batteries. If the particular type of data requested is not available for the current battery, then ERROR\_INVALID\_FUNCTION is returned.

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

[**BATTERY\_MANUFACTURE\_DATE**](battery-manufacture-date-str.md)
</dt> <dt>

[**BATTERY\_REPORTING\_SCALE**](/windows/desktop/api/WinNT/ns-winnt-battery_reporting_scale)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md)
</dt> </dl>

 

 




