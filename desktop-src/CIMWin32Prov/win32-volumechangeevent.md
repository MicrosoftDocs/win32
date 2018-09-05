---
Description: The Win32\_VolumeChangeEvent represents a local drive event that results from the addition of a drive letter or mounted drive on the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 38595319-d7a1-4dcd-9ad8-a27cc484b699
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_VolumeChangeEvent class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_VolumeChangeEvent
- Win32_VolumeChangeEvent.SECURITY_DESCRIPTOR
- Win32_VolumeChangeEvent.TIME_CREATED
- Win32_VolumeChangeEvent.EventType
- Win32_VolumeChangeEvent.DriveName
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_VolumeChangeEvent class

The **Win32\_VolumeChangeEvent** [WMI class](https://msdn.microsoft.com/en-us/library/Aa393244(v=VS.85).aspx) represents a local drive event that results from the addition of a drive letter or mounted drive on the computer system. Network drives are not currently supported.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("455CE053-2552-4051-A3E4-C4200DC31B7"), AMENDMENT]
class Win32_VolumeChangeEvent : Win32_DeviceChangeEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint16 EventType;
  string DriveName;
};
```

## Members

The **Win32\_VolumeChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VolumeChangeEvent** class has these properties.

<dl> <dt>

**DriveName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Drive name (letter) that has been added or removed from the system.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("Win32APIDevice Management Messages\|WM\_DEVICECHANGE\|wParam", "Win32APIDevice Management Messages\|WM\_SETTINGCHANGE")
</dt> </dl>

Type of event change notification that has occurred.

This property is inherited from [**Win32\_DeviceChangeEvent**](win32-devicechangeevent.md).

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

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/en-us/library/Aa394634(v=VS.85).aspx). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/en-us/library/Aa394576(v=VS.85).aspx).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format.

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/en-us/library/Aa394634(v=VS.85).aspx).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/Aa389763(v=VS.85).aspx).

</dd> </dl>

## Remarks

The **Win32\_VolumeChangeEvent** class is derived from [**Win32\_DeviceChangeEvent**](win32-devicechangeevent.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_DeviceChangeEvent**](win32-devicechangeevent.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/en-us/library/Dn792258(v=VS.85).aspx)
</dt> </dl>

 

 




