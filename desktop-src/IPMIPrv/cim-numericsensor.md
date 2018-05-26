---
title: CIM\_NumericSensor class
description: A Numeric Sensor is capable of returning numeric readings and optionally supports thresholds settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 308284ff-f90a-498a-9b16-8559acebf085
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_NumericSensor class
- CIM_NumericSensor class, described
topic_type:
- apiref
api_name:
- CIM_NumericSensor
- CIM_NumericSensor.Caption
- CIM_NumericSensor.Description
- CIM_NumericSensor.ElementName
- CIM_NumericSensor.InstallDate
- CIM_NumericSensor.Name
- CIM_NumericSensor.OperationalStatus
- CIM_NumericSensor.StatusDescriptions
- CIM_NumericSensor.Status
- CIM_NumericSensor.HealthState
- CIM_NumericSensor.EnabledState
- CIM_NumericSensor.OtherEnabledState
- CIM_NumericSensor.RequestedState
- CIM_NumericSensor.EnabledDefault
- CIM_NumericSensor.TimeOfLastStateChange
- CIM_NumericSensor.SystemCreationClassName
- CIM_NumericSensor.SystemName
- CIM_NumericSensor.CreationClassName
- CIM_NumericSensor.DeviceID
- CIM_NumericSensor.PowerManagementSupported
- CIM_NumericSensor.PowerManagementCapabilities
- CIM_NumericSensor.Availability
- CIM_NumericSensor.StatusInfo
- CIM_NumericSensor.LastErrorCode
- CIM_NumericSensor.ErrorDescription
- CIM_NumericSensor.ErrorCleared
- CIM_NumericSensor.OtherIdentifyingInfo
- CIM_NumericSensor.PowerOnHours
- CIM_NumericSensor.TotalPowerOnHours
- CIM_NumericSensor.IdentifyingDescriptions
- CIM_NumericSensor.AdditionalAvailability
- CIM_NumericSensor.MaxQuiesceTime
- CIM_NumericSensor.SensorType
- CIM_NumericSensor.OtherSensorTypeDescription
- CIM_NumericSensor.PossibleStates
- CIM_NumericSensor.CurrentState
- CIM_NumericSensor.PollingInterval
- CIM_NumericSensor.BaseUnits
- CIM_NumericSensor.UnitModifier
- CIM_NumericSensor.RateUnits
- CIM_NumericSensor.CurrentReading
- CIM_NumericSensor.NominalReading
- CIM_NumericSensor.NormalMax
- CIM_NumericSensor.NormalMin
- CIM_NumericSensor.MaxReadable
- CIM_NumericSensor.MinReadable
- CIM_NumericSensor.Resolution
- CIM_NumericSensor.Tolerance
- CIM_NumericSensor.Accuracy
- CIM_NumericSensor.IsLinear
- CIM_NumericSensor.Hysteresis
- CIM_NumericSensor.LowerThresholdNonCritical
- CIM_NumericSensor.UpperThresholdNonCritical
- CIM_NumericSensor.LowerThresholdCritical
- CIM_NumericSensor.UpperThresholdCritical
- CIM_NumericSensor.LowerThresholdFatal
- CIM_NumericSensor.UpperThresholdFatal
- CIM_NumericSensor.SupportedThresholds
- CIM_NumericSensor.EnabledThresholds
- CIM_NumericSensor.SettableThresholds
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_NumericSensor class

A Numeric Sensor is capable of returning numeric readings and optionally supports thresholds settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), UUID("{4c7acd5c-b440-442a-8c85-9c09bc36ada8}"), AMENDMENT]
class CIM_NumericSensor : CIM_Sensor
{
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   DeviceID;
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   Availability;
  uint16   StatusInfo;
  uint32   LastErrorCode;
  string   ErrorDescription;
  boolean  ErrorCleared;
  string   OtherIdentifyingInfo[];
  uint64   PowerOnHours;
  uint64   TotalPowerOnHours;
  string   IdentifyingDescriptions[];
  uint16   AdditionalAvailability[];
  uint64   MaxQuiesceTime;
  uint16   SensorType;
  string   OtherSensorTypeDescription;
  string   PossibleStates[];
  string   CurrentState;
  uint64   PollingInterval;
  uint16   BaseUnits;
  sint32   UnitModifier;
  uint16   RateUnits;
  sint32   CurrentReading;
  sint32   NominalReading;
  sint32   NormalMax;
  sint32   NormalMin;
  sint32   MaxReadable;
  sint32   MinReadable;
  uint32   Resolution;
  sint32   Tolerance;
  sint32   Accuracy;
  boolean  IsLinear;
  uint32   Hysteresis;
  sint32   LowerThresholdNonCritical;
  sint32   UpperThresholdNonCritical;
  sint32   LowerThresholdCritical;
  sint32   UpperThresholdCritical;
  sint32   LowerThresholdFatal;
  sint32   UpperThresholdFatal;
  uint16   SupportedThresholds[];
  uint16   EnabledThresholds[];
  uint16   SettableThresholds[];
};
```

## Members

The **CIM\_NumericSensor** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_NumericSensor** class has these methods.



| Method                                                                         | Description                                                                                                                                                                                                                                                                                                                   |
|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnableDevice**](cim-numericsensor-enabledevice.md)                         | This method is deprecated. Instead, use the **RequestStateChange** method.<br/> Requests that the logical device be enabled.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                                                       |
| [**GetNonLinearFactors**](cim-numericsensor-getnonlinearfactors.md)           | The use of this method is deprecated. Instead use the GetInstance operation.<br/>                                                                                                                                                                                                                                       |
| [**OnlineDevice**](cim-numericsensor-onlinedevice.md)                         | This method is deprecated. Instead, use the **RequestStateChange** method.<br/> Requests that the logical device be brought online.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                                                |
| [**QuiesceDevice**](cim-numericsensor-quiescedevice.md)                       | This method is deprecated. Instead, use the **RequestStateChange** method.<br/> Requests that the logical device cleanly cease all current activity.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                               |
| [**RequestStateChange**](cim-numericsensor-requeststatechange.md)             | Requests that the state of the element be changed to the specified value.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/>                                                                                                                                |
| [**Reset**](cim-numericsensor-reset.md)                                       | Requests a reset of the LogicalDevice.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                                                                                                                                                                   |
| [**RestoreDefaultThresholds**](cim-numericsensor-restoredefaultthresholds.md) | This method resets the values of the thresholds to hardware defaults.<br/>                                                                                                                                                                                                                                              |
| [**RestoreProperties**](cim-numericsensor-restoreproperties.md)               | This method is deprecated. Instead, use the ConfigurationData subclass of SettingData.<br/> Requests that the logical device re-establish its configuration, setup and/or state information from a backing store.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>  |
| [**SaveProperties**](cim-numericsensor-saveproperties.md)                     | This method is deprecated. Instead, use the ConfigurationData subclass of SettingData.<br/> Requests that the logical device capture its current configuration, setup and/or state information in a backing store.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/> |
| [**SetPowerState**](cim-numericsensor-setpowerstate.md)                       | Sets the power state of the Device. The use of this method has been deprecated. Instead, use the **SetPowerState** method in the associated Power Management Service class.<br/> This method is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).<br/>                                              |



 

### Properties

The **CIM\_NumericSensor** class has these properties.

<dl> <dt>

**Accuracy**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hundredths of Percent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.19", "MIF.DMTF\|Electrical Current Probe\|001.19", "MIF.DMTF\|Voltage Probe\|001.19")
</dt> </dl>

The accuracy of the sensor for the measured property. Its value indicates plus or minus hundredths of a percent. Accuracy may vary depending on whether the device is linear over its dynamic range.

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogicalDevice.Availability")
</dt> </dl>

Additional information beyond that specified in the **Availability** property.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>

**Running/Full Power** (3)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (4)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (5)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (6)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

**Power Off** (7)


</dt> <dd></dd> <dt>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>

**Off Line** (8)


</dt> <dd></dd> <dt>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>

**Off Duty** (9)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (10)


</dt> <dd></dd> <dt>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>

**Not Installed** (11)


</dt> <dd></dd> <dt>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>

**Install Error** (12)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

**Power Save - Unknown** (13)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

**Power Save - Low Power Mode** (14)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

**Power Save - Standby** (15)


</dt> <dd></dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

**Power Cycle** (16)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

**Power Save - Warning** (17)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** (18)


</dt> <dd></dd> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>

**Not Ready** (19)


</dt> <dd></dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

**Not Configured** (20)


</dt> <dd></dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

**Quiesced** (21)


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "CIM\_ManagedSystemElement.OperationalStatus", "CIM\_EnabledLogicalElement.EnabledState"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogicalDevice.AdditionalAvailability")
</dt> </dl>

The primary availability and status of the Device.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>

**Running/Full Power** (3)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (4)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (5)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (6)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

**Power Off** (7)


</dt> <dd></dd> <dt>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>

**Off Line** (8)


</dt> <dd></dd> <dt>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>

**Off Duty** (9)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (10)


</dt> <dd></dd> <dt>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>

**Not Installed** (11)


</dt> <dd></dd> <dt>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>

**Install Error** (12)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

**Power Save - Unknown** (13)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

**Power Save - Low Power Mode** (14)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

**Power Save - Standby** (15)


</dt> <dd></dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

**Power Cycle** (16)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

**Power Save - Warning** (17)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** (18)


</dt> <dd></dd> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>

**Not Ready** (19)


</dt> <dd></dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

**Not Configured** (20)


</dt> <dd></dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

**Quiesced** (21)


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**BaseUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UnitModifier", "CIM\_NumericSensor.RateUnits")
</dt> </dl>

The base unit of the values returned by this sensor.

All the values returned by this Sensor are represented in the units obtained by **BaseUnits** \* 10 to the power of the **UnitModifier**.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Degrees_C"></span><span id="degrees_c"></span><span id="DEGREES_C"></span>

**Degrees C** (2)


</dt> <dd></dd> <dt>

<span id="Degrees_F"></span><span id="degrees_f"></span><span id="DEGREES_F"></span>

**Degrees F** (3)


</dt> <dd></dd> <dt>

<span id="Degrees_K"></span><span id="degrees_k"></span><span id="DEGREES_K"></span>

**Degrees K** (4)


</dt> <dd></dd> <dt>

<span id="Volts"></span><span id="volts"></span><span id="VOLTS"></span>

**Volts** (5)


</dt> <dd></dd> <dt>

<span id="Amps"></span><span id="amps"></span><span id="AMPS"></span>

**Amps** (6)


</dt> <dd></dd> <dt>

<span id="Watts"></span><span id="watts"></span><span id="WATTS"></span>

**Watts** (7)


</dt> <dd></dd> <dt>

<span id="Joules"></span><span id="joules"></span><span id="JOULES"></span>

**Joules** (8)


</dt> <dd></dd> <dt>

<span id="Coulombs"></span><span id="coulombs"></span><span id="COULOMBS"></span>

**Coulombs** (9)


</dt> <dd></dd> <dt>

<span id="VA"></span><span id="va"></span>

**VA** (10)


</dt> <dd></dd> <dt>

<span id="Nits"></span><span id="nits"></span><span id="NITS"></span>

**Nits** (11)


</dt> <dd></dd> <dt>

<span id="Lumens"></span><span id="lumens"></span><span id="LUMENS"></span>

**Lumens** (12)


</dt> <dd></dd> <dt>

<span id="Lux"></span><span id="lux"></span><span id="LUX"></span>

**Lux** (13)


</dt> <dd></dd> <dt>

<span id="Candelas"></span><span id="candelas"></span><span id="CANDELAS"></span>

**Candelas** (14)


</dt> <dd></dd> <dt>

<span id="kPa"></span><span id="kpa"></span><span id="KPA"></span>

**kPa** (15)


</dt> <dd></dd> <dt>

<span id="PSI"></span><span id="psi"></span>

**PSI** (16)


</dt> <dd></dd> <dt>

<span id="Newtons"></span><span id="newtons"></span><span id="NEWTONS"></span>

**Newtons** (17)


</dt> <dd></dd> <dt>

<span id="CFM"></span><span id="cfm"></span>

**CFM** (18)


</dt> <dd></dd> <dt>

<span id="RPM"></span><span id="rpm"></span>

**RPM** (19)


</dt> <dd></dd> <dt>

<span id="Hertz"></span><span id="hertz"></span><span id="HERTZ"></span>

**Hertz** (20)


</dt> <dd></dd> <dt>

<span id="Seconds"></span><span id="seconds"></span><span id="SECONDS"></span>

**Seconds** (21)


</dt> <dd></dd> <dt>

<span id="Minutes"></span><span id="minutes"></span><span id="MINUTES"></span>

**Minutes** (22)


</dt> <dd></dd> <dt>

<span id="Hours"></span><span id="hours"></span><span id="HOURS"></span>

**Hours** (23)


</dt> <dd></dd> <dt>

<span id="Days"></span><span id="days"></span><span id="DAYS"></span>

**Days** (24)


</dt> <dd></dd> <dt>

<span id="Weeks"></span><span id="weeks"></span><span id="WEEKS"></span>

**Weeks** (25)


</dt> <dd></dd> <dt>

<span id="Mils"></span><span id="mils"></span><span id="MILS"></span>

**Mils** (26)


</dt> <dd></dd> <dt>

<span id="Inches"></span><span id="inches"></span><span id="INCHES"></span>

**Inches** (27)


</dt> <dd></dd> <dt>

<span id="Feet"></span><span id="feet"></span><span id="FEET"></span>

**Feet** (28)


</dt> <dd></dd> <dt>

<span id="Cubic_Inches"></span><span id="cubic_inches"></span><span id="CUBIC_INCHES"></span>

**Cubic Inches** (29)


</dt> <dd></dd> <dt>

<span id="Cubic_Feet"></span><span id="cubic_feet"></span><span id="CUBIC_FEET"></span>

**Cubic Feet** (30)


</dt> <dd></dd> <dt>

<span id="Meters"></span><span id="meters"></span><span id="METERS"></span>

**Meters** (31)


</dt> <dd></dd> <dt>

<span id="Cubic_Centimeters"></span><span id="cubic_centimeters"></span><span id="CUBIC_CENTIMETERS"></span>

**Cubic Centimeters** (32)


</dt> <dd></dd> <dt>

<span id="Cubic_Meters"></span><span id="cubic_meters"></span><span id="CUBIC_METERS"></span>

**Cubic Meters** (33)


</dt> <dd></dd> <dt>

<span id="Liters"></span><span id="liters"></span><span id="LITERS"></span>

**Liters** (34)


</dt> <dd></dd> <dt>

<span id="Fluid_Ounces"></span><span id="fluid_ounces"></span><span id="FLUID_OUNCES"></span>

**Fluid Ounces** (35)


</dt> <dd></dd> <dt>

<span id="Radians"></span><span id="radians"></span><span id="RADIANS"></span>

**Radians** (36)


</dt> <dd></dd> <dt>

<span id="Steradians"></span><span id="steradians"></span><span id="STERADIANS"></span>

**Steradians** (37)


</dt> <dd></dd> <dt>

<span id="Revolutions"></span><span id="revolutions"></span><span id="REVOLUTIONS"></span>

**Revolutions** (38)


</dt> <dd></dd> <dt>

<span id="Cycles"></span><span id="cycles"></span><span id="CYCLES"></span>

**Cycles** (39)


</dt> <dd></dd> <dt>

<span id="Gravities"></span><span id="gravities"></span><span id="GRAVITIES"></span>

**Gravities** (40)


</dt> <dd></dd> <dt>

<span id="Ounces"></span><span id="ounces"></span><span id="OUNCES"></span>

**Ounces** (41)


</dt> <dd></dd> <dt>

<span id="Pounds"></span><span id="pounds"></span><span id="POUNDS"></span>

**Pounds** (42)


</dt> <dd></dd> <dt>

<span id="Foot-Pounds"></span><span id="foot-pounds"></span><span id="FOOT-POUNDS"></span>

**Foot-Pounds** (43)


</dt> <dd></dd> <dt>

<span id="Ounce-Inches"></span><span id="ounce-inches"></span><span id="OUNCE-INCHES"></span>

**Ounce-Inches** (44)


</dt> <dd></dd> <dt>

<span id="Gauss"></span><span id="gauss"></span><span id="GAUSS"></span>

**Gauss** (45)


</dt> <dd></dd> <dt>

<span id="Gilberts"></span><span id="gilberts"></span><span id="GILBERTS"></span>

**Gilberts** (46)


</dt> <dd></dd> <dt>

<span id="Henries"></span><span id="henries"></span><span id="HENRIES"></span>

**Henries** (47)


</dt> <dd></dd> <dt>

<span id="Farads"></span><span id="farads"></span><span id="FARADS"></span>

**Farads** (48)


</dt> <dd></dd> <dt>

<span id="Ohms"></span><span id="ohms"></span><span id="OHMS"></span>

**Ohms** (49)


</dt> <dd></dd> <dt>

<span id="Siemens"></span><span id="siemens"></span><span id="SIEMENS"></span>

**Siemens** (50)


</dt> <dd></dd> <dt>

<span id="Moles"></span><span id="moles"></span><span id="MOLES"></span>

**Moles** (51)


</dt> <dd></dd> <dt>

<span id="Becquerels"></span><span id="becquerels"></span><span id="BECQUERELS"></span>

**Becquerels** (52)


</dt> <dd></dd> <dt>

<span id="PPM__parts_million_"></span><span id="ppm__parts_million_"></span><span id="PPM__PARTS_MILLION_"></span>

**PPM (parts/million)** (53)


</dt> <dd></dd> <dt>

<span id="Decibels"></span><span id="decibels"></span><span id="DECIBELS"></span>

**Decibels** (54)


</dt> <dd></dd> <dt>

<span id="DbA"></span><span id="dba"></span><span id="DBA"></span>

**DbA** (55)


</dt> <dd></dd> <dt>

<span id="DbC"></span><span id="dbc"></span><span id="DBC"></span>

**DbC** (56)


</dt> <dd></dd> <dt>

<span id="Grays"></span><span id="grays"></span><span id="GRAYS"></span>

**Grays** (57)


</dt> <dd></dd> <dt>

<span id="Sieverts"></span><span id="sieverts"></span><span id="SIEVERTS"></span>

**Sieverts** (58)


</dt> <dd></dd> <dt>

<span id="Color_Temperature_Degrees_K"></span><span id="color_temperature_degrees_k"></span><span id="COLOR_TEMPERATURE_DEGREES_K"></span>

**Color Temperature Degrees K** (59)


</dt> <dd></dd> <dt>

<span id="Bits"></span><span id="bits"></span><span id="BITS"></span>

**Bits** (60)


</dt> <dd></dd> <dt>

<span id="Bytes"></span><span id="bytes"></span><span id="BYTES"></span>

**Bytes** (61)


</dt> <dd></dd> <dt>

<span id="Words__data_"></span><span id="words__data_"></span><span id="WORDS__DATA_"></span>

**Words (data)** (62)


</dt> <dd></dd> <dt>

<span id="DoubleWords"></span><span id="doublewords"></span><span id="DOUBLEWORDS"></span>

**DoubleWords** (63)


</dt> <dd></dd> <dt>

<span id="QuadWords"></span><span id="quadwords"></span><span id="QUADWORDS"></span>

**QuadWords** (64)


</dt> <dd></dd> <dt>

<span id="Percentage"></span><span id="percentage"></span><span id="PERCENTAGE"></span>

**Percentage** (65)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**CurrentReading**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.5", "MIF.DMTF\|Electrical Current Probe\|001.5", "MIF.DMTF\|Voltage Probe\|001.5")
</dt> </dl>

The current value indicated by the sensor.

</dd> <dt>

**CurrentState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

The current state reported by the Sensor. This is always one of the **PossibleStates**.

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

An address or other identifying information to unique to the logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the **EnabledState** of an element. By default, the element is **Enabled** (2).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="No_Default"></span><span id="no_default"></span><span id="NO_DEFAULT"></span>

**No Default** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>8 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.OtherEnabledState")
</dt> </dl>

Indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (4) and starting (10) are transient states between enabled and disabled.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

The element is or could be executing commands, will process any queued commands, and queues new requests.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


</dt> <dd>

The element will not execute commands and will drop any new requests.

</dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (4)


</dt> <dd>

The element is in the process of going to a **Disabled** state.

</dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)


</dt> <dd>

The element does not support being enabled or disabled.

</dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>**Enabled but Offline** (6)


</dt> <dd>

The element might be completing commands, and will drop any new requests.

</dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (7)


</dt> <dd>

The element is in a test state.

</dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>**Deferred** (8)


</dt> <dd>

The element might be completing commands, but will queue any new requests.

</dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)


</dt> <dd>

The element is enabled but in a restricted mode. The behavior of the element is similar to the **Enabled** (2) state, but it processes only a restricted set of commands. All other requests are queued.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (10)


</dt> <dd>

The element is in the process of going to an **Enabled** (2) state. New requests are queued.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**EnabledThresholds**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of the thresholds that are currently enabled for this sensor.

<dt>

<span id="LowerThresholdNonCritical"></span><span id="lowerthresholdnoncritical"></span><span id="LOWERTHRESHOLDNONCRITICAL"></span>

**LowerThresholdNonCritical** (0)


</dt> <dd></dd> <dt>

<span id="UpperThresholdNonCritical"></span><span id="upperthresholdnoncritical"></span><span id="UPPERTHRESHOLDNONCRITICAL"></span>

**UpperThresholdNonCritical** (1)


</dt> <dd></dd> <dt>

<span id="LowerThresholdCritical"></span><span id="lowerthresholdcritical"></span><span id="LOWERTHRESHOLDCRITICAL"></span>

**LowerThresholdCritical** (2)


</dt> <dd></dd> <dt>

<span id="UpperThresholdCritical"></span><span id="upperthresholdcritical"></span><span id="UPPERTHRESHOLDCRITICAL"></span>

**UpperThresholdCritical** (3)


</dt> <dd></dd> <dt>

<span id="LowerThresholdFatal"></span><span id="lowerthresholdfatal"></span><span id="LOWERTHRESHOLDFATAL"></span>

**LowerThresholdFatal** (4)


</dt> <dd></dd> <dt>

<span id="UpperThresholdFatal"></span><span id="upperthresholdfatal"></span><span id="UPPERTHRESHOLDFATAL"></span>

**UpperThresholdFatal** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Whether the error reported in **LastErrorCode** is now cleared.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.ErrorDescription")
</dt> </dl>

More information about the error in **LastErrorCode**, and any corrective actions that may be taken.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The implementation can not report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and is operating within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element may not be operating at optimal performance or it may be reporting recoverable errors.

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

All functionality is available but some may be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

The element is failing. It is possible the some or all of the functionality of this component is degraded or not working.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

The element is non-functional and recovery may not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

The element has completed failed and recovery is not possible. All functionality provided by this element has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Hysteresis**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A margin around the thresholds to prevent unnecessary state changes when the **CurrentReading** fluctuates very closely to a threshold. When a threshold is crossed, the state of the sensor should change. However, the state should not fluctuate between the old and new states unless the change in the reading exceeds the hysteresis value. The units for this measurement are determined by BaseUnit\*UnitModifier/RateUnit.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogicalDevice.OtherIdentifyingInfo")
</dt> </dl>

Explanations and details about the entries in the **OtherIdentifyingInfo** array. Note, each entry of this array is related to the entry in **OtherIdentifyingInfo** that is located at the same index.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A **datetime** value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**IsLinear**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the Sensor is linear over its dynamic range.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.LastErrorCode")
</dt> </dl>

The last error code reported by the logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**LowerThresholdCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.13", "MIF.DMTF\|Electrical Current Probe\|001.13", "MIF.DMTF\|Voltage Probe\|001.13")
</dt> </dl>

If the **CurrentReading** is between **LowerThresholdCritical** and **LowerThresholdFatal**, then the **CurrentState** is **Critical**. The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> <dt>

**LowerThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.15", "MIF.DMTF\|Electrical Current Probe\|001.15", "MIF.DMTF\|Voltage Probe\|001.15")
</dt> </dl>

If the **CurrentReading** is below **LowerThresholdFatal**, then the **CurrentState** is **Fatal**.

The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> <dt>

**LowerThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.11", "MIF.DMTF\|Electrical Current Probe\|001.11", "MIF.DMTF\|Voltage Probe\|001.11")
</dt> </dl>

If **CurrentReading** is between **LowerThresholdNonCritical** and **UpperThresholdNonCritical**, the sensor is reporting a normal value. If **CurrentReading** is between **LowerThresholdNonCritical** and **LowerThresholdCritical**, then the **CurrentState** is **NonCritical**.

The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> <dt>

**MaxQuiesceTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MilliSeconds")
</dt> </dl>

Deprecated. The maximum time in milliseconds, that a Device can run in a **Quiesced** state. A Device's state is defined in its **Availability** and **AdditionalAvailability** properties. What occurs at the end of the time limit is device-specific. A value of 0 indicates that a Device can remain quiesced indefinitely.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**MaxReadable**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.9", "MIF.DMTF\|Electrical Current Probe\|001.9", "MIF.DMTF\|Voltage Probe\|001.9")
</dt> </dl>

The largest value that can be read by the numeric sensor.

</dd> <dt>

**MinReadable**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.10", "MIF.DMTF\|Electrical Current Probe\|001.10", "MIF.DMTF\|Voltage Probe\|001.10")
</dt> </dl>

The smallest value that can be read by the numeric sensor.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. In subclasses the **Name** property can be overridden to be a Key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**NominalReading**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.6", "MIF.DMTF\|Electrical Current Probe\|001.6", "MIF.DMTF\|Voltage Probe\|001.6")
</dt> </dl>

The normal or expected value for the numeric sensor.

</dd> <dt>

**NormalMax**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.7", "MIF.DMTF\|Electrical Current Probe\|001.7", "MIF.DMTF\|Voltage Probe\|001.7")
</dt> </dl>

The maximum value in the normal range for the numeric sensor.

</dd> <dt>

**NormalMin**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.8", "MIF.DMTF\|Electrical Current Probe\|001.8", "MIF.DMTF\|Voltage Probe\|001.8")
</dt> </dl>

The minimum value in the normal range for the numeric sensor.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

Indicates the current status of the element. Various operational statuses are defined. Many of the enumeration's values are self- explanatory.

**OperationalStatus** replaces the **Status** property to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. Due to the widespread use of the existing **Status** property in management applications, it is strongly recommended that providers/instrumentation provide both the **Status** and **OperationalStatus** properties. Further, the first value of **OperationalStatus** should contain the primary status for the element. When instrumented, **Status** should also provide the primary status of the element since it is single-valued.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

The element is functioning, but needs attention. Examples of **Stressed** states are overload and overheated.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

The element is functioning nominally but predicting a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

Implies a clean and orderly stop

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

The element is being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

The monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

The element is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

Implies an abrupt stop where the element's state and configuration may need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

The element is inactive or quiesced.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

This element may be **OK** but another element on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

The element has completed its operation. This value should be combined with either **OK**, **Error**, or **Degraded** so that a client can tell if the complete operation succeeded or not. **Completed** with **Degraded** would imply the operation finished, but did not complete **OK** or report an error.

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

The element has additional power model information contained in the Associated PowerManagementService association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is **Other** (1). This property must be set to null when **EnabledState** is any value other than 1.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LogicalDevice.IdentifyingDescriptions")
</dt> </dl>

Additional data, beyond the **DeviceID** property, that could be used to identify a logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**OtherSensorTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Sensor.SensorType")
</dt> </dl>

When the **SensorType** property is set to **Other**, describes the sensor type.

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**PollingInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("NanoSeconds")
</dt> </dl>

The interval that the sensor hardware or the instrumentation is polled to determine the current state of the sensor.

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**PossibleStates**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

An array of strings naming the possible states reported by the sensor. For example, "Normal", "NonCritical", "Critical", and "Fatal".

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities.PowerCapabilities")
</dt> </dl>

The power management capabilities of the Device. This property is deprecated. Instead, use the **PowerCapabilites** property in an associated power management capabilities class.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (1)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

**Power Saving Modes Entered Automatically** (4)


</dt> <dd></dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

**Power State Settable** (5)


</dt> <dd></dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

**Power Cycling Supported** (6)


</dt> <dd></dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

**Timed Power On Supported** (7)


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities")
</dt> </dl>

Whether the Device can be power managed. This property is deprecated. Instead, the existence of an associated power management capabilities class indicates that power management is supported.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.PowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

The number of consecutive hours that this Device has been powered, since its last power cycle.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**RateUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UnitModifier", "CIM\_NumericSensor.BaseUnits")
</dt> </dl>

If other than **None** the units returned by this Sensor are rate units.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Per_MicroSecond"></span><span id="per_microsecond"></span><span id="PER_MICROSECOND"></span>

**Per MicroSecond** (1)


</dt> <dd></dd> <dt>

<span id="Per_MilliSecond"></span><span id="per_millisecond"></span><span id="PER_MILLISECOND"></span>

**Per MilliSecond** (2)


</dt> <dd></dd> <dt>

<span id="Per_Second"></span><span id="per_second"></span><span id="PER_SECOND"></span>

**Per Second** (3)


</dt> <dd></dd> <dt>

<span id="Per_Minute"></span><span id="per_minute"></span><span id="PER_MINUTE"></span>

**Per Minute** (4)


</dt> <dd></dd> <dt>

<span id="Per_Hour"></span><span id="per_hour"></span><span id="PER_HOUR"></span>

**Per Hour** (5)


</dt> <dd></dd> <dt>

<span id="Per_Day"></span><span id="per_day"></span><span id="PER_DAY"></span>

**Per Day** (6)


</dt> <dd></dd> <dt>

<span id="Per_Week"></span><span id="per_week"></span><span id="PER_WEEK"></span>

**Per Week** (7)


</dt> <dd></dd> <dt>

<span id="Per_Month"></span><span id="per_month"></span><span id="PER_MONTH"></span>

**Per Month** (8)


</dt> <dd></dd> <dt>

<span id="Per_Year"></span><span id="per_year"></span><span id="PER_YEAR"></span>

**Per Year** (9)


</dt> <dd></dd> </dl>

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. Note that when **EnabledState** is set to 5 ("Not Applicable"), then this property has no meaning. By default, the **RequestedState** of the element is **No Change** (5). This property is set as the result of a method invocation, such as [**StartService**](https://msdn.microsoft.com/library/aa393655) or [**StopService**](https://msdn.microsoft.com/library/aa393668) on [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>

**No Change** (5)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**Resolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.17", "MIF.DMTF\|Electrical Current Probe\|001.17", "MIF.DMTF\|Voltage Probe\|001.17")
</dt> </dl>

The ability of the sensor to resolve differences in the measured property. The units for this measurement are determined by BaseUnit\*UnitModifier/RateUnit.

</dd> <dt>

**SensorType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Sensor.OtherSensorTypeDescription")
</dt> </dl>

The Type of the Sensor. If set to **Other**, then the **OtherSensorTypeDescription** property identifies the type.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Temperature"></span><span id="temperature"></span><span id="TEMPERATURE"></span>

**Temperature** (2)


</dt> <dd></dd> <dt>

<span id="Voltage"></span><span id="voltage"></span><span id="VOLTAGE"></span>

**Voltage** (3)


</dt> <dd></dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>

**Current** (4)


</dt> <dd></dd> <dt>

<span id="Tachometer"></span><span id="tachometer"></span><span id="TACHOMETER"></span>

**Tachometer** (5)


</dt> <dd></dd> <dt>

<span id="Counter"></span><span id="counter"></span><span id="COUNTER"></span>

**Counter** (6)


</dt> <dd></dd> <dt>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>

**Switch** (7)


</dt> <dd></dd> <dt>

<span id="Lock"></span><span id="lock"></span><span id="LOCK"></span>

**Lock** (8)


</dt> <dd></dd> <dt>

<span id="Humidity"></span><span id="humidity"></span><span id="HUMIDITY"></span>

**Humidity** (9)


</dt> <dd></dd> <dt>

<span id="Smoke_Detection"></span><span id="smoke_detection"></span><span id="SMOKE_DETECTION"></span>

**Smoke Detection** (10)


</dt> <dd></dd> <dt>

<span id="Presence"></span><span id="presence"></span><span id="PRESENCE"></span>

**Presence** (11)


</dt> <dd></dd> <dt>

<span id="Air_Flow"></span><span id="air_flow"></span><span id="AIR_FLOW"></span>

**Air Flow** (12)


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**SettableThresholds**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of the writable thresholds supported by this sensor.

<dt>

<span id="LowerThresholdNonCritical"></span><span id="lowerthresholdnoncritical"></span><span id="LOWERTHRESHOLDNONCRITICAL"></span>

**LowerThresholdNonCritical** (0)


</dt> <dd></dd> <dt>

<span id="UpperThresholdNonCritical"></span><span id="upperthresholdnoncritical"></span><span id="UPPERTHRESHOLDNONCRITICAL"></span>

**UpperThresholdNonCritical** (1)


</dt> <dd></dd> <dt>

<span id="LowerThresholdCritical"></span><span id="lowerthresholdcritical"></span><span id="LOWERTHRESHOLDCRITICAL"></span>

**LowerThresholdCritical** (2)


</dt> <dd></dd> <dt>

<span id="UpperThresholdCritical"></span><span id="upperthresholdcritical"></span><span id="UPPERTHRESHOLDCRITICAL"></span>

**UpperThresholdCritical** (3)


</dt> <dd></dd> <dt>

<span id="LowerThresholdFatal"></span><span id="lowerthresholdfatal"></span><span id="LOWERTHRESHOLDFATAL"></span>

**LowerThresholdFatal** (4)


</dt> <dd></dd> <dt>

<span id="UpperThresholdFatal"></span><span id="upperthresholdfatal"></span><span id="UPPERTHRESHOLDFATAL"></span>

**UpperThresholdFatal** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_ManagedSystemElement.OperationalStatus"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the object. This property is deprecated in favor of **OperationalStatus**, which includes the same semantics in its enumeration.

"OK"

"Error"

"Degraded"

"Unknown"

"Pred Fail"

"Starting"

"Stopping"

"Service"

"Stressed"

"NonRecover"

"No Contact"

"Lost Comm"

"Stopped"

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Strings describing the various **OperationalStatus** array values.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_EnabledLogicalElement.EnabledState"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.4")
</dt> </dl>

The state of the Logical Device. This property is deprecated. Instead, use the inherited **EnabledState** property.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> </dl>

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**SupportedThresholds**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of the thresholds supported by this sensor.

<dt>

<span id="LowerThresholdNonCritical"></span><span id="lowerthresholdnoncritical"></span><span id="LOWERTHRESHOLDNONCRITICAL"></span>

**LowerThresholdNonCritical** (0)


</dt> <dd></dd> <dt>

<span id="UpperThresholdNonCritical"></span><span id="upperthresholdnoncritical"></span><span id="UPPERTHRESHOLDNONCRITICAL"></span>

**UpperThresholdNonCritical** (1)


</dt> <dd></dd> <dt>

<span id="LowerThresholdCritical"></span><span id="lowerthresholdcritical"></span><span id="LOWERTHRESHOLDCRITICAL"></span>

**LowerThresholdCritical** (2)


</dt> <dd></dd> <dt>

<span id="UpperThresholdCritical"></span><span id="upperthresholdcritical"></span><span id="UPPERTHRESHOLDCRITICAL"></span>

**UpperThresholdCritical** (3)


</dt> <dd></dd> <dt>

<span id="LowerThresholdFatal"></span><span id="lowerthresholdfatal"></span><span id="LOWERTHRESHOLDFATAL"></span>

**LowerThresholdFatal** (4)


</dt> <dd></dd> <dt>

<span id="UpperThresholdFatal"></span><span id="upperthresholdfatal"></span><span id="UPPERTHRESHOLDFATAL"></span>

**UpperThresholdFatal** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.CreationClassName"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's **CreationClassName**.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.Name"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping System's **Name**.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When the enabled state of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**Tolerance**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_NumericSensor.Resolution", "CIM\_NumericSensor.Accuracy")
</dt> </dl>

This property is deprecated. Instead, use the **Resolution** and **Accuracy** properties.

The tolerance of the sensor for the measured property.

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.TotalPowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

The total number of hours that this Device has been powered.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**UnitModifier**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.BaseUnits", "CIM\_NumericSensor.RateUnits")
</dt> </dl>

The unit multiplier for the values returned by this sensor. All the values returned by this Sensor are represented in the units calculated by **BaseUnits** \* 10 to the power of the **UnitModifier**.

</dd> <dt>

**UpperThresholdCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.14", "MIF.DMTF\|Electrical Current Probe\|001.14", "MIF.DMTF\|Voltage Probe\|001.14")
</dt> </dl>

If the **CurrentReading** is between **UpperThresholdCritical** and **UpperThresholdFatal**, then the **CurrentState** is **Critical**.

The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> <dt>

**UpperThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.16", "MIF.DMTF\|Electrical Current Probe\|001.16", "MIF.DMTF\|Voltage Probe\|001.16")
</dt> </dl>

If the **CurrentReading** is above **UpperThresholdFatal**, then the **CurrentState** is **Fatal**.

The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> <dt>

**UpperThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.12", "MIF.DMTF\|Electrical Current Probe\|001.12", "MIF.DMTF\|Voltage Probe\|001.12")
</dt> </dl>

If the **CurrentReading** is between **LowerThresholdNonCritical** and **UpperThresholdNonCritical**, then the **CurrentState** is **Normal**. If the **CurrentReading** is between **UpperThresholdNonCritical** and **UpperThresholdCritical**, then the **CurrentState** is **NonCritical**.

The threshold values collectively specify the **CurrentReading** value ranges corresponding to the **CurrentState** values.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Sensor**](cim-sensor.md)
</dt> </dl>

 

 





