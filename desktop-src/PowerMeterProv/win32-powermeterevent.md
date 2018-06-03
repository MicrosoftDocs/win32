---
title: Win32\_PowerMeterEvent class
description: Provides metering and budgeting information.
ms.assetid: 9db06d75-7056-4fef-93b9-3288df94eabc
keywords:
- Win32_PowerMeterEvent class
- Win32_PowerMeterEvent class, described
topic_type:
- apiref
api_name:
- Win32_PowerMeterEvent
- Win32_PowerMeterEvent.EventSource
- Win32_PowerMeterEvent.EventType
api_location:
- UmPoWmi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PowerMeterEvent class

The **Win32\_PowerMeterEvent** class provides metering and budgeting information. This class represents a change in the power meter. This information includes changes in the meter's capabilities, changes in the meter's configuration, or notification that a configured threshold has been crossed.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerMeterProvider"), Dynamic]
class Win32_PowerMeterEvent : __ExtrinsicEvent
{
  CIM_PowerMeter REF EventSource;
  uint32             EventType;
};
```

## Members

The **Win32\_PowerMeterEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerMeterEvent** class has these properties.

<dl> <dt>

**EventSource**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PowerMeter**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the [**Win32\_PowerMeter**](win32-powermeter.md) object from which this event originated.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of event. The following events are possible.



| Value                                                                        | Meaning                                                                                            |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The metering or budgeting capabilities of the power meter have changed.<br/>                 |
| <dl> <dt>1</dt> </dl> | The power level has exceeded the power meter's current threshold.<br/>                       |
| <dl> <dt>2</dt> </dl> | The metering or budgeting configuration of the power meter have changed.<br/>                |
| <dl> <dt>3</dt> </dl> | The power budget has either reached or exceeded the power meter's current budget level.<br/> |
| <dl> <dt>4</dt> </dl> | The averaging interval of the power meter has been changed.<br/>                             |



 

</dd> </dl>

## Remarks

The **Win32\_PowerMeterEvent** class is derived from the [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646) WMI class. For more information, see [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646).

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                 |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>PowerMeterProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UmPoWmi.dll</dt> </dl>            |



 

 





