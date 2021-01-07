---
description: Represents a change in the brightness of a monitor.
ms.assetid: c2eb5630-a52f-4ad4-aaee-1cc8afef8c9e
title: WmiMonitorBrightnessEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorBrightnessEvent
- WmiMonitorBrightnessEvent.Active
- WmiMonitorBrightnessEvent.Brightness
- WmiMonitorBrightnessEvent.InstanceName
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorBrightnessEvent class

The **WmiMonitorBrightnessEvent** WMI event class represents a change in the brightness of a monitor.

## Syntax

``` syntax
class WmiMonitorBrightnessEvent : WMIEvent
{
  boolean Active;
  uint8   Brightness;
  string  InstanceName;
};
```

## Members

The **WmiMonitorBrightnessEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorBrightnessEvent** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the active monitor.

</dd> <dt>

**Brightness**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current monitor brightness as a percentage.

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
</dt> <dt>

[**WmiMonitorBrightness**](wmimonitorbrightness.md)
</dt> <dt>

[Receiving a WMI Event](/windows/desktop/WmiSdk/receiving-a-wmi-event)
</dt> </dl>

 

