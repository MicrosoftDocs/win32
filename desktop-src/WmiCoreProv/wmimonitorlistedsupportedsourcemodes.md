---
description: Lists the supported source modes for a video monitor in its monitor descriptor, if any exist.
ms.assetid: cca59d28-bd93-4df2-989e-0516dd8eae83
title: WmiMonitorListedSupportedSourceModes class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorListedSupportedSourceModes
- WmiMonitorListedSupportedSourceModes.Active
- WmiMonitorListedSupportedSourceModes.InstanceName
- WmiMonitorListedSupportedSourceModes.NumOfMonitorSourceModes
- WmiMonitorListedSupportedSourceModes.PreferredMonitorSourceModeIndex
- WmiMonitorListedSupportedSourceModes.MonitorSourceModes
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorListedSupportedSourceModes class

The **WmiMonitorListedSupportedSourceModes** lists the supported source modes for a video monitor in its monitor descriptor, if any exist. For monitors that have no description, this list of modes is generated based on the type of monitor, as specified by the monitor bus driver.

## Syntax

``` syntax
class WmiMonitorListedSupportedSourceModes : MSMonitorClass
{
  boolean             Active;
  string              InstanceName;
  uint16              NumOfMonitorSourceModes;
  uint16              PreferredMonitorSourceModeIndex;
  VideoModeDescriptor MonitorSourceModes[];
};
```

## Members

The **WmiMonitorListedSupportedSourceModes** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorListedSupportedSourceModes** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Name of the specific monitor instance.

</dd> <dt>

**MonitorSourceModes**
</dt> <dd> <dl> <dt>

Data type: **VideoModeDescriptor** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Lists monitor source modes represented by instances of the [**VideoModeDescriptor**](videomodedescriptor.md) class.

</dd> <dt>

**NumOfMonitorSourceModes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of listed supported monitor source mode.

</dd> <dt>

**PreferredMonitorSourceModeIndex**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Preferred monitor source mode index.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




