---
Description: The WMIEvent class is a base class from which all WMI event classes are derived.
ms.assetid: 0393d3fc-7566-4eda-940e-248d622a903a
title: WMIEvent class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WMIEvent
- WMIEvent.SECURITY_DESCRIPTOR
- WMIEvent.TIME_CREATED
api_type: 
- DllExport
api_location: 
- WmiProv.dll
---

# WMIEvent class

The **WMIEvent** class is a base class from which all WMI event classes are derived.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[]
class WMIEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **WMIEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **WMIEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

## Remarks

The **WMIEvent** class is derived from [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646).

## Requirements



|                                     |                                                                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                                                                                        |
| Namespace<br/>                | Root\\WMI<br/>                                                                                                                                  |
| MOF<br/>                      | <dl> <dt>Wmi.mof; </dt> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl>                                                                |



## See also

<dl> <dt>

[MSMCA Classes](msmca-classes.md)
</dt> <dt>

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> </dl>

 

 




