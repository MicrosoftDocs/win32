---
description: The Win32\_DeviceChangeEvent abstract WMI class represents device change events that result from the addition, removal, or modification of devices on the computer system.
ms.assetid: 78155357-4231-4ded-980e-89feeb864ef2
ms.tgt_platform: multiple
title: Win32_DeviceChangeEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_DeviceChangeEvent
- Win32_DeviceChangeEvent.SECURITY_DESCRIPTOR
- Win32_DeviceChangeEvent.TIME_CREATED
- Win32_DeviceChangeEvent.EventType
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_DeviceChangeEvent class

The **Win32\_DeviceChangeEvent** abstract [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents device change events that result from the addition, removal, or modification of devices on the computer system. This includes changes in the hardware configuration (docking and undocking), the hardware state, or newly mapped devices (mapping of a network drive). For example, a device has changed when a WM\_DEVICECHANGE message is sent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("0DE6AAF8-49F1-4868-B3D4-61CB69BA4322"), AMENDMENT]
class Win32_DeviceChangeEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint16 EventType;
};
```

## Members

The **Win32\_DeviceChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DeviceChangeEvent** class has these properties.

<dl> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32APIDevice Management Messages\|WM\_DEVICECHANGE\|wParam", "Win32APIDevice Management Messages\|WM\_SETTINGCHANGE")
</dt> </dl>

Type of event change notification that has occurred.

<dt>

<span id="Configuration_Changed"></span><span id="configuration_changed"></span><span id="CONFIGURATION_CHANGED"></span>

**Configuration Changed** (1)


</dt> <dd></dd> <dt>

<span id="Device_Arrival"></span><span id="device_arrival"></span><span id="DEVICE_ARRIVAL"></span>

**Device Arrival** (2)


</dt> <dd></dd> <dt>

<span id="Device_Removal"></span><span id="device_removal"></span><span id="DEVICE_REMOVAL"></span>

**Device Removal** (3)


</dt> <dd></dd> <dt>

<span id="Docking"></span><span id="docking"></span><span id="DOCKING"></span>

**Docking** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event). For more information about constants used to set this security descriptor, see [WMI Security Constants](/windows/desktop/WmiSdk/wmi-security-constants).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format.

This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **Win32\_DeviceChangeEvent** is an abstract class derived from [**\_\_ExtrinsicEvent**](/windows/desktop/WmiSdk/--extrinsicevent).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](/windows/desktop/WmiSdk/--extrinsicevent)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

