---
description: Represents the brightness parameters of a computer monitor.
ms.assetid: 01fa3efc-2a1d-4405-989f-2c180842c6b9
title: WmiMonitorBrightness class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorBrightness
- WmiMonitorBrightness.Active
- WmiMonitorBrightness.CurrentBrightness
- WmiMonitorBrightness.InstanceName
- WmiMonitorBrightness.Level
- WmiMonitorBrightness.Levels
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorBrightness class

The **WmiMonitorBrightness** WMI class represents the brightness parameters of a computer monitor.

## Syntax

``` syntax
class WmiMonitorBrightness : MSMonitorClass
{
  boolean Active;
  uint8   CurrentBrightness;
          InstanceName;
  uint8   Level[];
  uint32  Levels;
};
```

## Members

The **WmiMonitorBrightness** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorBrightness** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the target monitor is active.

</dd> <dt>

**CurrentBrightness**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current brightness. This value must be a value taken from *Levels*.

Example: 100

</dd> <dt>

InstanceName
</dt> <dd> <dl> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: Key
</dt> </dl>

Name of the specific monitor instance.

</dd> <dt>

**Level**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array containing the possible brightness levels.

Example: \[0, 1, 2, ..., 100\].

</dd> <dt>

**Levels**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of brightness levels the monitor supports, as described in *Level*.

Example: 101

</dd> </dl>

## Examples

For more information and code samples on using this class in PowerShell, see [Use PowerShell to Report and Set Monitor Brightness](https://blogs.technet.com/b/heyscriptingguy/archive/2013/07/25/use-powershell-to-report-and-set-monitor-brightness.aspx).

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

 

 




