---
description: Lists the frequency ranges supported by the monitor.
ms.assetid: e4713650-5f8c-4808-8b4f-1d29c54ab4e3
title: WmiMonitorListedFrequencyRanges class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorListedFrequencyRanges
- WmiMonitorListedFrequencyRanges.Active
- WmiMonitorListedFrequencyRanges.InstanceName
- WmiMonitorListedFrequencyRanges.NumOfMonitorFreqRanges
- WmiMonitorListedFrequencyRanges.MonitorFreqRanges
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WmiMonitorListedFrequencyRanges class

The **WmiMonitorListedFrequencyRanges** WMI class lists the frequency ranges supported by the monitor. These ranges are found in Video Input Definition of Video Electronics Standard Association (VESA) Enhanced Extended Display Identification Data (E-EDID) block or in the Windows INF file that contains device driver data.

## Syntax

``` syntax
class WmiMonitorListedFrequencyRanges : MSMonitorClass
{
  boolean                  Active;
  string                   InstanceName;
  uint16                   NumOfMonitorFreqRanges;
  FrequencyRangeDescriptor MonitorFreqRanges[];
};
```

## Members

The **WmiMonitorListedFrequencyRanges** class has these types of members:

-   [Properties](#properties)

### Properties

The **WmiMonitorListedFrequencyRanges** class has these properties.

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

**MonitorFreqRanges**
</dt> <dd> <dl> <dt>

Data type: **FrequencyRangeDescriptor** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of monitor frequency ranges represented by instances of the [**FrequencyRangeDescriptor**](frequencyrangedescriptor.md) class.

</dd> <dt>

**NumOfMonitorFreqRanges**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of listed supported monitor frequency ranges.

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

 

 




