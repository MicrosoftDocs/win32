---
title: Win32_SessionBrokerTargetEvent class
description: Represents a change to a session broker target.
ms.assetid: ee3ae0ed-eb8b-4777-9b9e-0e50722cf52a
ms.tgt_platform: multiple
keywords:
- Win32_SessionBrokerTargetEvent class Remote Desktop Services
- Win32_SessionBrokerTargetEvent class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionBrokerTargetEvent
- Win32_SessionBrokerTargetEvent.SECURITY_DESCRIPTOR
- Win32_SessionBrokerTargetEvent.TIME_CREATED
- Win32_SessionBrokerTargetEvent.ChangeType
- Win32_SessionBrokerTargetEvent.PluginName
- Win32_SessionBrokerTargetEvent.TargetName
- Win32_SessionBrokerTargetEvent.FarmName
- Win32_SessionBrokerTargetEvent.Guid
- Win32_SessionBrokerTargetEvent.Environment
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionBrokerTargetEvent class

Represents a change to a session broker target.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Win32_SessionBrokerTargetEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ChangeType;
  string PluginName;
  string TargetName;
  string FarmName;
  string Guid;
  string Environment;
};
```

## Members

The **Win32\_SessionBrokerTargetEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionBrokerTargetEvent** class has these properties.

<dl> <dt>

**ChangeType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the change that occurred. This can be one of the following values.

<dt>

1 (0x1)
</dt> <dd>

The type of change is not specified.

</dd> <dt>

2 (0x2)
</dt> <dd>

The external IP address has changed.

</dd> <dt>

4 (0x4)
</dt> <dd>

The internal IP address has changed.

</dd> <dt>

8 (0x8)
</dt> <dd>

The target was joined.

</dd> <dt>

16 (0x10)
</dt> <dd>

The target was removed.

</dd> <dt>

32 (0x20)
</dt> <dd>

The state of the target has changed.

</dd> <dt>

64 (0x40)
</dt> <dd>

The target is idle.

</dd> </dl>

</dd> <dt>

**Environment**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The environment name. In the case of a virtual machine (VM) target, this could be the VM host name.

**Windows Server 2008 R2:** This property is unavailable prior to Windows Server 2012

</dd> <dt>

**FarmName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the farm the target belongs to.

**Windows Server 2008 R2:** This property is unavailable prior to Windows Server 2012

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID of the target.

**Windows Server 2008 R2:** This property is unavailable prior to Windows Server 2012

</dd> <dt>

**PluginName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the plug-in.

**Windows Server 2008 R2:** This property is unavailable prior to Windows Server 2012

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event). For more information about constants used to set this security descriptor, see [WMI Security Constants](/windows/desktop/WmiSdk/wmi-security-constants).

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the target.

**Windows Server 2008 R2:** This property is unavailable prior to Windows Server 2012

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



 

