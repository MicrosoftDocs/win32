---
description: Contains battery information to be set.
ms.assetid: 535e56cb-2bab-458a-84a8-2d9a4d96412b
title: BATTERY_SET_INFORMATION structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_SET_INFORMATION
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_SET\_INFORMATION structure

Contains battery information to be set. This structure is used with the [**IOCTL\_BATTERY\_SET\_INFORMATION**](ioctl-battery-set-information.md) control code.

## Syntax


```C++
typedef struct _BATTERY_SET_INFORMATION {
  ULONG                         BatteryTag;
  BATTERY_SET_INFORMATION_LEVEL InformationLevel;
  UCHAR                         Buffer[1];
} BATTERY_SET_INFORMATION, *PBATTERY_SET_INFORMATION;
```



## Members

<dl> <dt>

**BatteryTag**
</dt> <dd>

The current battery tag for the battery. Information for a battery matching the tag can only be returned. Whenever this value does not match the battery's current tag, the IOCTL request will be completed with ERROR\_FILE\_NOT\_FOUND, which indicates to the caller that the battery for which it has a tag for no longer exists. The caller may opt to use the [**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md) operation to determine the tag of the newly installed battery, if one exists. (See [Battery Tags](battery-information.md) for more information.)

When a query information request is made, this value is verified. In addition, if the request is in progress while this value changes, the request is aborted with the status of ERROR\_FILE\_NOT\_FOUND.

</dd> <dt>

**InformationLevel**
</dt> <dd>

The battery information to be set. The type of data in the **Buffer** member depends on the value of this member. This member can be one of the following values.



| Value                                                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BatteryCharge"></span><span id="batterycharge"></span><span id="BATTERYCHARGE"></span><dl> <dt>**BatteryCharge**</dt> <dt>1</dt> </dl>                         | Informs the battery device that the user has requested that the battery should be charging at this time. For example, with a smart battery/charger/selector, the application could charge one battery at a time. The **Buffer** member of this structure is ignored.<br/>                                                                      |
| <span id="BatteryCriticalBias"></span><span id="batterycriticalbias"></span><span id="BATTERYCRITICALBIAS"></span><dl> <dt>**BatteryCriticalBias**</dt> <dt>0</dt> </dl> | Sets the battery's critical bias adjustment. Note it is not envisioned that this value would normally be changed by software, and is present in the interfaces only as a maintenance feature. Not all batteries can maintain such a setting, and the battery information should be read to confirm that the battery accepted the setting.<br/> |
| <span id="BatteryDischarge"></span><span id="batterydischarge"></span><span id="BATTERYDISCHARGE"></span><dl> <dt>**BatteryDischarge**</dt> <dt>2</dt> </dl>             | Informs the battery device that the user has requested that the battery be discharging at this time. For example, this could be used to indicate which battery the user currently wants to power the system. The **Buffer** member of this structure is ignored.<br/>                                                                          |



 

</dd> <dt>

**Buffer**
</dt> <dd>

The battery information to be set. The data depends on the value of **InformationLevel**.

</dd> </dl>

## Remarks

The **BATTERY\_SET\_INFORMATION** structure is a variable-length structure, and you must allocate a buffer of suitable size for the information to be included in the structure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_BATTERY\_SET\_INFORMATION**](ioctl-battery-set-information.md)
</dt> </dl>

 

 




