---
title: Win32\_PowerMeter class
description: Provides metering and budgeting information from an underlying power meter.
ms.assetid: 71b82c73-739d-4a7c-bee5-f15b802ec933
keywords:
- Win32_PowerMeter class
- Win32_PowerMeter class, described
topic_type:
- apiref
api_name:
- Win32_PowerMeter
- Win32_PowerMeter.Name
- Win32_PowerMeter.DeviceID
- Win32_PowerMeter.SupportCapabilities
- Win32_PowerMeter.MeterType
- Win32_PowerMeter.SamplingPeriod
- Win32_PowerMeter.MinimumAveragingInterval
- Win32_PowerMeter.MaximumAveragingInterval
- Win32_PowerMeter.AveragingInterval
- Win32_PowerMeter.MinOperatingBudget
- Win32_PowerMeter.MaxOperatingBudget
- Win32_PowerMeter.BudgetWriteable
- Win32_PowerMeter.BudgetEnabled
- Win32_PowerMeter.ConfiguredBudget
- Win32_PowerMeter.BaseUnits
- Win32_PowerMeter.UnitModifier
- Win32_PowerMeter.Hysteresis
api_location:
- UmPoWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_PowerMeter class

The **Win32\_PowerMeter** class provides metering and budgeting information from an underlying power meter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerMeterProvider"), Dynamic]
class Win32_PowerMeter : CIM_NumericSensor
{
  string  Name;
  string  DeviceID;
  uint32  SupportCapabilities;
  uint32  MeterType;
  uint32  SamplingPeriod;
  uint32  MinimumAveragingInterval;
  uint32  MaximumAveragingInterval;
  uint32  AveragingInterval;
  uint32  MinOperatingBudget;
  uint32  MaxOperatingBudget;
  boolean BudgetWriteable;
  boolean BudgetEnabled;
  uint32  ConfiguredBudget;
  uint16  BaseUnits;
  sint32  UnitModifier;
  uint32  Hysteresis;
};
```

## Members

The **Win32\_PowerMeter** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerMeter** class has these properties.

<dl> <dt>

**AveragingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Specifies the averaging interval set in the power meter that is currently configured. Values read through this property are averaged over this interval.

The value of **AveragingInterval** must be between the values specified by the **MinimumAveragingInterval** and **MaximumAveragingInterval** properties, inclusive.

</dd> <dt>

**BaseUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the base unit of the measurements.

> [!Note]  
> Starting in Windows 7 and Windows Server 2008 R2, the **Win32\_PowerMeter** class only supports base units in watts.

 

</dd> <dt>

**BudgetEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Determines whether the power budget is enabled. If this property is **TRUE**, the power budget is enabled.

</dd> <dt>

**BudgetWriteable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines whether this power budget is writeable. If this property is **FALSE**, saving an instance of the **Win32\_PowerMeter** data with a modified **ConfiguredBudget** will fail, and the currently configured budget will not be changed.

</dd> <dt>

**ConfiguredBudget**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Specifies the power budget that is configured for this power meter. This value is marked writeable. The value will take effect when the instance is saved, but only if **BudgetWriteable** is set to **TRUE**. Otherwise, the save will fail.

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier of the power meter. For more information about device IDs, see [Device Identification](http://go.microsoft.com/fwlink/p/?linkid=147815).

</dd> <dt>

**Hysteresis**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the hysteresis margin of the power meter.

</dd> <dt>

**MaximumAveragingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the maximum allowed value for the interval, in milliseconds, over which the power meter averages samples.

</dd> <dt>

**MaxOperatingBudget**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the maximum power budget, in watts, supported by the power meter.

</dd> <dt>

**MeterType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the power measurements reported by the power meter. This property must be set to one of the following values.



| Value                                                                        | Meaning                                                   |
|------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The measurement data is based on input power.<br/>  |
| <dl> <dt>1</dt> </dl> | The measurement data is based on output power.<br/> |



 

</dd> <dt>

**MinimumAveragingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the minimum interval, in milliseconds, over which the power meter averages samples.

</dd> <dt>

**MinOperatingBudget**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the minimum power budget, in watts, supported by the power meter.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the display name of the power meter.

</dd> <dt>

**SamplingPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the sampling period, in milliseconds, of the power meter. This property specifies the frequency with which the power meter reads data from the power supply.

</dd> <dt>

**SupportCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitmask that specifies the supported capabilities of the power meter. This property must be set to one or more of the following values.



| Value                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SupportMeasurement"></span><span id="supportmeasurement"></span><span id="SUPPORTMEASUREMENT"></span><dl> <dt>**SupportMeasurement**</dt> <dt>0</dt> </dl>                                 | Set if the power meter supports power measurement.<br/>                                                                                                                                 |
| <span id="SupportThresholds"></span><span id="supportthresholds"></span><span id="SUPPORTTHRESHOLDS"></span><dl> <dt>**SupportThresholds**</dt> <dt>1</dt> </dl>                                     | Set if the power meter supports power thresholds.<br/>                                                                                                                                  |
| <span id="SupportBudgeting"></span><span id="supportbudgeting"></span><span id="SUPPORTBUDGETING"></span><dl> <dt>**SupportBudgeting**</dt> <dt>2</dt> </dl>                                         | Set if the power meter supports power budgeting.<br/>                                                                                                                                   |
| <span id="SupportOnlyWhenDischarging"></span><span id="supportonlywhendischarging"></span><span id="SUPPORTONLYWHENDISCHARGING"></span><dl> <dt>**SupportOnlyWhenDischarging**</dt> <dt>8</dt> </dl> | Set if the power meter reports data only when the power supply is discharging. This is typically the case on mobile battery systems or some uninterruptible power supplies (UPSs).<br/> |



 

</dd> <dt>

**UnitModifier**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unit modifier that determines the magnitude of the unit. For example, a value of -3 means that the reading is 0.001 times that of the base unit.

</dd> </dl>

## Remarks

The **Win32\_PowerMeter** class is derived from the [**CIM\_NumericSensor**](https://msdn.microsoft.com/library/aa387936) class. It is the primary WMI class for obtaining power consumption and budgeting information from a power meter.

An instance of the **Win32\_PowerMeter** class is associated with the device that is being metered. For example, a power meter that supports power metering and budgeting for the entire system is associated with the instance of the [**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102) class that represents the system.

For more information, see [**CIM\_NumericSensor**](https://msdn.microsoft.com/library/aa387936) and [**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102).

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                 |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>PowerMeterProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UmPoWmi.dll</dt> </dl>            |



 

 





