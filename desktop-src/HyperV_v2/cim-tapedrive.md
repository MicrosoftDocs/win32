---
description: Represents the capabilities and management of a tape drive.
ms.assetid: 8140fd9a-8a12-43b4-bc61-ec143e5d754c
title: CIM_TapeDrive class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_TapeDrive
- CIM_TapeDrive.EOTWarningZoneSize
- CIM_TapeDrive.MaxPartitionCount
- CIM_TapeDrive.Padding
- CIM_TapeDrive.MaxRewindTime
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_TapeDrive class (Hyper-V management)

Represents the capabilities and management of a tape drive.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), UMLPackagePath("CIM::Device::StorageDevices")]
class CIM_TapeDrive : CIM_MediaAccessDevice
{
  uint32 EOTWarningZoneSize;
  uint32 MaxPartitionCount;
  uint32 Padding;
  uint64 MaxRewindTime;
};
```

## Members

The **CIM\_TapeDrive** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_TapeDrive** class has these properties.

<dl> <dt>

**EOTWarningZoneSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The size, in bytes, of the area designated as "end of tape". Access in this area generates an "end of tape" warning.

</dd> <dt>

**MaxPartitionCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum partition count for the tape drive.

</dd> <dt>

**MaxRewindTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("MilliSeconds"), **PUnit** ("second \* 10^-3")
</dt> </dl>

The time, in milliseconds, to move from the most physically distant point on the tape to the beginning.

</dd> <dt>

**Padding**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The number of bytes inserted between blocks on tape media.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md)
</dt> </dl>

 

