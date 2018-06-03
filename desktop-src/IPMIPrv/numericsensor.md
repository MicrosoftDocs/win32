---
title: NumericSensor class
description: Represents an analog type of sensor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28cd780e-3de1-4cc5-8301-33e6aba87722
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- IPMI provider Windows Remote Management
- NumericSensor class
- NumericSensor class, described
topic_type:
- apiref
api_name:
- NumericSensor
- NumericSensor.Caption
- NumericSensor.Description
- NumericSensor.ElementName
- NumericSensor.InstallDate
- NumericSensor.Name
- NumericSensor.OperationalStatus
- NumericSensor.StatusDescriptions
- NumericSensor.Status
- NumericSensor.HealthState
- NumericSensor.OtherEnabledState
- NumericSensor.RequestedState
- NumericSensor.EnabledDefault
- NumericSensor.SystemCreationClassName
- NumericSensor.SystemName
- NumericSensor.CreationClassName
- NumericSensor.DeviceID
- NumericSensor.PowerManagementSupported
- NumericSensor.PowerManagementCapabilities
- NumericSensor.Availability
- NumericSensor.StatusInfo
- NumericSensor.LastErrorCode
- NumericSensor.ErrorDescription
- NumericSensor.TotalPowerOnHours
- NumericSensor.IdentifyingDescriptions
- NumericSensor.AdditionalAvailability
- NumericSensor.MaxQuiesceTime
- NumericSensor.SensorType
- NumericSensor.OtherSensorTypeDescription
- NumericSensor.PossibleStates
- NumericSensor.CurrentState
- NumericSensor.PollingInterval
- NumericSensor.BaseUnits
- NumericSensor.UnitModifier
- NumericSensor.RateUnits
- NumericSensor.CurrentReading
- NumericSensor.NominalReading
- NumericSensor.NormalMax
- NumericSensor.NormalMin
- NumericSensor.Resolution
- NumericSensor.Tolerance
- NumericSensor.Accuracy
- NumericSensor.IsLinear
- NumericSensor.Hysteresis
- NumericSensor.LowerThresholdNonCritical
- NumericSensor.EnabledThresholds
- NumericSensor.SettableThresholds
- NumericSensor.EnabledState
- NumericSensor.TimeOfLastStateChange
- NumericSensor.ErrorCleared
- NumericSensor.LowerThresholdCritical
- NumericSensor.LowerThresholdFatal
- NumericSensor.MaxReadable
- NumericSensor.MinReadable
- NumericSensor.OtherIdentifyingInfo
- NumericSensor.PowerOnHours
- NumericSensor.SupportedThresholds
- NumericSensor.UpperThresholdCritical
- NumericSensor.UpperThresholdNonCritical
- NumericSensor.UpperThresholdFatal
api_location:
- IpmiPrv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NumericSensor class

Represents an analog type of sensor. The **SensorType** property differentiates between numeric sensors.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("IPMIPrv"), UUID("{7be7579b-4370-4a75-857c-9e789d1aff8a}"), AMENDMENT]
class NumericSensor : CIM_NumericSensor
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
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
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
  uint32   Resolution;
  sint32   Tolerance;
  sint32   Accuracy;
  boolean  IsLinear;
  uint32   Hysteresis;
  sint32   LowerThresholdNonCritical;
  uint16   EnabledThresholds[];
  uint16   SettableThresholds[];
  uint16   EnabledState = 5;
  datetime TimeOfLastStateChange;
  boolean  ErrorCleared;
  sint32   LowerThresholdCritical;
  sint32   LowerThresholdFatal;
  sint32   MaxReadable;
  sint32   MinReadable;
  string   OtherIdentifyingInfo[];
  uint64   PowerOnHours;
  string   SupportedThresholds[];
  sint32   UpperThresholdCritical;
  sint32   UpperThresholdNonCritical;
  sint32   UpperThresholdFatal;
};
```

## Members

The **NumericSensor** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **NumericSensor** class has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>EnableDevice</strong>](numericsensor-enabledevice.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the [<strong>RequestStateChange</strong>](numericsensor-requeststatechange.md) method.
</blockquote>
<br/> Enable or disables the numeric sensor.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>GetNonLinearFactors</strong>](numericsensor-getnonlinearfactors.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated and should not be used.
</blockquote>
<br/> Retrieves data collected by the numeric sensor.<br/> This method is inherited from <strong>CIM_NumericSensor</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnlineDevice</strong>](numericsensor-onlinedevice.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the [<strong>RequestStateChange</strong>](numericsensor-requeststatechange.md) method.
</blockquote>
<br/> Brings the numeric sensor online so it can accept requests, or offline so it can no longer accept requests.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>QuiesceDevice</strong>](numericsensor-quiescedevice.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the [<strong>RequestStateChange</strong>](numericsensor-requeststatechange.md) method.
</blockquote>
<br/> Temporarily suspends activity on the numeric sensor, or re-enables the activity.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RequestStateChange</strong>](numericsensor-requeststatechange.md)</td>
<td style="text-align: left;">Initiates a requests to change the state of the numeric sensor.<br/> This method is inherited from [<strong>CIM_EnabledLogicalElement</strong>](cim-enabledlogicalelement.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Reset</strong>](numericsensor-reset.md)</td>
<td style="text-align: left;">Resets the numeric sensor.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RestoreDefaultThresholds</strong>](numericsensor-restoredefaultthresholds.md)</td>
<td style="text-align: left;">Resets the values of numeric sensor thresholds to the hardware default values.<br/> This method is inherited from <strong>CIM_NumericSensor</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RestoreProperties</strong>](numericsensor-restoreproperties.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the <strong>ApplyConfiguration</strong> property of the <strong>CIM_ConfigurationData</strong> class.
</blockquote>
<br/> Restores a previous configuration and state of the numeric sensor.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SaveProperties</strong>](numericsensor-saveproperties.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the <strong>ConfigurationInformation</strong> property of the <strong>CIM_ConfigurationData</strong> class.
</blockquote>
<br/> Saves the configuration and state of the numeric sensor.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SetPowerState</strong>](numericsensor-setpowerstate.md)</td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
This method is deprecated. Instead we recommend that you use the <strong>SetPowerState</strong> property of the <strong>CIM_PowerManagementService</strong> class.
</blockquote>
<br/> Sets the power state of the numeric sensor.<br/> This method is inherited from [<strong>CIM_LogicalDevice</strong>](cim-logicaldevice.md).<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **NumericSensor** class has these properties.

<dl> <dt>

**Accuracy**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hundredths of Percent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.19", "MIF.DMTF\|Electrical Current Probe\|001.19", "MIF.DMTF\|Voltage Probe\|001.19")
</dt> </dl>

Indicates the accuracy of the Sensor for the measured property. Its value is recorded as plus/minus hundredths of a percent. **Accuracy**, along with **Resolution**, is used to calculate the actual value of the measured physical property. **Accuracy** may vary depending on whether the Device is linear over its dynamic range.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

Additional availability and status of the Device, beyond that specified in the **Availability** property. The **Availability** property denotes the primary status and availability of the Device. In some cases, this will not be sufficient to denote the complete status of the Device. In those cases, the **AdditionalAvailability** property can be used to provide further information. For example, a Device's primary **Availability** may be "Off line" (value=8), but it may also be in a low power state (**AdditonalAvailability** value=14), or the Device could be running Diagnostics (**AdditionalAvailability** value=5, "In Test").

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

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

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**", "[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**AdditionalAvailability**")
</dt> </dl>

The primary availability and status of the Device. (Additional status information can be specified using the **AdditionalAvailability** array property.) For example, the **Availability** property indicates that the Device is running and has full power (value=3), or is in a warning (4), test (5), degraded (10) or power save state (values 13-15 and 17). Regarding the Power Save states, these are defined as follows: Value 13 ("Power Save - Unknown") indicates that the Device is known to be in a power save mode, but its exact status in this mode is unknown; 14 ("Power Save - Low Power Mode") indicates that the Device is in a power save state but still functioning, and may exhibit degraded performance; 15 ("Power Save - Standby") describes that the Device is not functioning but could be brought to full power 'quickly'; and value 17 ("Power Save - Warning") indicates that the Device is in a warning state, though also in a power save mode.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

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

</dd> <dt>

**BaseUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_NumericSensor**](cim-numericsensor.md).**UnitModifier**", "**CIM\_NumericSensor**.**RateUnits**")
</dt> </dl>

The base unit of the values returned by this Sensor. All the values returned by this Sensor are represented in the units obtained by (**BaseUnits** \* 10 raised to the power of the **UnitModifier**). For example, if **BaseUnits** is Volts and the **UnitModifier** is -6, then the units of the values returned are MicroVolts. However, if the **RateUnits** property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if **RateUnits** is set to "Per Second", then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the [**Units**](https://msdn.microsoft.com/library/aa393650) qualifier.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

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

The **Caption** property is a short textual description (one- line string) of the object.

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

**CreationClassName** indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

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

The current value indicated by the Sensor.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**CurrentState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

The current state indicated by the Sensor. This is always one of the "**PossibleStates**".

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **Description** property provides a textual description of the object.

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

An address or other identifying information to uniquely name the LogicalDevice.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name IN ADDITION TO its key properties/identity data, and description information.

Note that ManagedSystemElement's Name property is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information MAY be present in both the **Name** and **ElementName** properties.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

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

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

Indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, **Shutting Down** (value=4) and **Starting** (value=10) are transient states between **Enabled** and **Disabled**.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

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

The element is in the process of going to a Disabled state.

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

The element is enabled but in a restricted mode. The behavior of the element is similar to the Enabled state (2), but it processes only a restricted set of commands. All other requests are queued.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (10)


</dt> <dd>

The element is in the process of going to an Enabled state (2). New requests are queued.

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

</dd> <dt>

**EnabledThresholds**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array representing the thresholds that are currently enabled for this Sensor.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

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

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead we recommend that you use the **OperationalStatus** property from the [**CIM\_ManagedSystemElement**](https://www.bing.com/search?q=**CIM\_ManagedSystemElement**) class.

 

Indicates whether an error reported by the **LastErrorCode** property is cleared. This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.ErrorDescription")
</dt> </dl>

**ErrorDescription** is a free-form string supplying more information about the error recorded in **LastErrorCode**, and information on any corrective actions that may be taken.

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

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined:

"Non-recoverable Error" (30) - The element has completed failed and recovery is not possible. All functionality provided by this element has been lost.

"Critical Failure" (25) - The element is non-functional and recovery MAY NOT be possible.

"Major Failure" (20) - The element is failing. It is possible the some or all of the functionality of this component is degraded or not working.

"Minor Failure" (15) - All functionality is available but some MAY be degraded.

"Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element may not be operating at optimal performance or it may be reporting recoverable errors.

"OK" (5) - The element is fully functional and is operating within normal operational parameters and without error.

"Unknown" (0) - The implementation can not report on **HealthState** at this time.

DMTF has reserved the unused portion of the continuum for additional **HealthState**s in the future.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (5)


</dt> <dd></dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

**Degraded/Warning** (10)


</dt> <dd></dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

**Minor failure** (15)


</dt> <dd></dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

**Major failure** (20)


</dt> <dd></dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

**Critical failure** (25)


</dt> <dd></dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-recoverable error** (30)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>31 65535</dd> </dl>

</dd> <dt>

**Hysteresis**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the margin built around the thresholds. This margin prevents unnecessary state changes when the Sensor reading may fluctuate very close to its thresholds. This could be due to the Sensor's tolerance/accuracy/resolution or due to environmental factors. Once a threshold is crossed, the state of the Sensor should change. However, the state should not fluctuate between the old and new states unless the Sensor's change in the reading exceeds the **Hysteresis** value. The units for this measurement are determined by **BaseUnit**\***UnitModifier**/**RateUnit**.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**OtherIdentifyingInfo**")
</dt> </dl>

An array of free-form strings providing explanations and details behind the entries in the **OtherIdentifyingInfo** array. Note, each entry of this array is related to the entry in **OtherIdentifyingInfo** that is located at the same index.

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

Indicates that the Sensor is linear over its dynamic range.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.LastErrorCode")
</dt> </dl>

**LastErrorCode** captures the last error code reported by the LogicalDevice.

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

A value that specifies a range that determines whether the sensor is operating under **Normal**, **NonCritical**, **Critical** or **Fatal** conditions. If **CurrentReading** is between **LowerThresholdCritical** and **LowerThresholdFatal**, then the current state is noncritical. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: 500

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**LowerThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.15", "MIF.DMTF\|Electrical Current Probe\|001.15", "MIF.DMTF\|Voltage Probe\|001.15")
</dt> </dl>

A value that specifies a range that determines whether the sensor is operating under **Normal**, **NonCritical**, **Critical**, or **Fatal** conditions. If **CurrentReading** is below **LowerThresholdFatal**, then the current state is fatal. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: -1279

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**LowerThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.11", "MIF.DMTF\|Electrical Current Probe\|001.11", "MIF.DMTF\|Voltage Probe\|001.11")
</dt> </dl>

The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under **Normal**, **NonCritical**, **Critical** or **Fatal** conditions. If **CurrentReading** is between **LowerThresholdNonCritical** and **UpperThresholdNonCritical**, then the Sensor is reporting a normal value. If **CurrentReading** is between **LowerThresholdNonCritical** and **LowerThresholdCritical**, then the **CurrentState** is **NonCritical**.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**MaxQuiesceTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MilliSeconds")
</dt> </dl>

The **MaxQuiesceTime** property has been deprecated. When evaluating the use of Quiesce, it was determine that this single property is not adequate for describing when a device will automatically exit a quiescent state. In fact, the most likely scenario for a device to exit a quiescent state was determined to be based on the number of outstanding requests queued rather than on a maximum time. This will be re-evaluated and repositioned later.

Maximum time in milliseconds, that a Device can run in a "Quiesced" state. A Device's state is defined in its **Availability** and **AdditionalAvailability** properties, where "Quiesced" is conveyed by the value 21. What occurs at the end of the time limit is device-specific. The Device may unquiesce, may offline or take other action. A value of 0 indicates that a Device can remain quiesced indefinitely.

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

The largest value of the measure property that can be read by the numeric sensor. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: 1270

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**MinReadable**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.10", "MIF.DMTF\|Electrical Current Probe\|001.10", "MIF.DMTF\|Voltage Probe\|001.10")
</dt> </dl>

The smallest value of the measured property that can be read by the numeric sensor. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: -1279

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The **Name** property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a [**Key**](https://msdn.microsoft.com/library/aa392157) property.

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

**NominalReading** indicates the 'normal' or expected value for the [**NumericSensor**](cim-numericsensor.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**NormalMax**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.7", "MIF.DMTF\|Electrical Current Probe\|001.7", "MIF.DMTF\|Voltage Probe\|001.7")
</dt> </dl>

**NormalMax** provides guidance for the user as to the normal maximum range for the [**NumericSensor**](cim-numericsensor.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**NormalMin**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.8", "MIF.DMTF\|Electrical Current Probe\|001.8", "MIF.DMTF\|Voltage Probe\|001.8")
</dt> </dl>

**NormalMin** provides guidance for the user as to the normal minimum range for the [**NumericSensor**](cim-numericsensor.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

Indicates the current status(es) of the element. Various operational statuses are defined. Many of the enumeration's values are self- explanatory. However, a few are not and are described in more detail.

"Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, etc.

"Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future.

"In Service" describes an element being configured, maintained, cleaned, or otherwise administered.

"No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

"Lost Communication" indicates that the ManagedSystemElement is known to exist and has been contacted successfully in the past, but is currently unreachable.

"Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the element's state and configuration may need to be updated.

"Dormant" indicates that the element is inactive or quiesced.

"Supporting Entity in Error" describes that this element may be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower layer networking problems.

"Completed" indicates the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can till if the complete operation passed (Completed with OK), and failure (Completed with Error). Completed with Degraded would imply the operation finished, but did not complete OK or report an error.

"Power Mode" indicates the element has additional power model information contained in the Associated PowerManagementService association.

**OperationalStatus** replaces the **Status** property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier since it required the DEPRECATED qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly RECOMMENDED that providers/instrumentation provide BOTH the Status and **OperationalStatus** properties. Further, the first value of **OperationalStatus** SHOULD contain the primary status for the element. When instrumented, **Status** (since it is single-valued) SHOULD also provide the primary status of the element.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** (4)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

**In Service** (11)


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (14)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

**Supporting Entity in Error** (16)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (17)


</dt> <dd></dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

**Power Mode** (18)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>19 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property must be set to null when **EnabledState** is any value other than 1.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**IdentifyingDescriptions**")
</dt> </dl>

Information that identifies the numeric sensor, other than a **DeviceID**. This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**OtherSensorTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Sensor**](cim-sensor.md).**SensorType**")
</dt> </dl>

A string describing the Sensor type - used when the **SensorType** property is set to "Other".

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

The polling interval that the Sensor hardware or the instrumentation uses to determine the current state of the Sensor.

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

**PossibleStates** enumerates the string outputs of the Sensor. For example, a "Switch" Sensor may output the states "On", or "Off". Another implementation of the Switch may output the states "Open", and "Close". Another example is a **NumericSensor** supporting thresholds. This Sensor can report the states like "Normal", "Upper Fatal", "Lower Non-Critical", etc. A **NumericSensor** that does not publish readings and thresholds, but stores this data internally, can still report its states.

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

An enumerated array describing the power management capabilities of the Device. The use of this property has been deprecated. Instead, the PowerCapabilites property in an associated PowerManagementCapabilities class should be used.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

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

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities")
</dt> </dl>

Boolean indicating that the Device can be power managed. The use of this property has been deprecated. Instead, the existence of an associated PowerManagementCapabilities class (associated using the ElementCapabilities relationship) indicates that power management is supported.

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

> [!Note]  
> This property is deprecated. Instead we recommend that you use the **PowerOnHours** property from the**CIM\_PoweredStatisticalData** class.

 

The number of consecutive hours that the numeric sensor has been powered, since its last power cycle. This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**RateUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_NumericSensor**](cim-numericsensor.md).**UnitModifier**", "**CIM\_NumericSensor**.*BaseUnits*")
</dt> </dl>

Specifies if the units returned by this Sensor are rate units. All the values returned by this Sensor are represented in the units obtained by (**BaseUnits** \* 10 raised to the power of the **UnitModifier**). This is true unless this property (**RateUnits**) has a value different than **None** (0). For example, if **BaseUnits** is **Volts** (5) and the **UnitModifier** is -6, then the units of the values returned are MicroVolts. But, if the **RateUnits** property is set to a value other than **None** (0), then the units are further qualified as rate units. In the above example, if **RateUnits** is set to **Per Second** (3), then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier. Any implementation of CurrentReading should be qualified with either a Counter or a Gauge qualifier, depending on the characteristics of the sensor being modeled.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

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

**RequestedState** is an integer enumeration that indicates the last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. Note that when **EnabledState** is set to 5 ("Not Applicable"), then this property has no meaning. By default, the **RequestedState** of the element is 5 ("No Change"). Refer to the **EnabledState** property description for explanations of the values in the **RequestedState** enumeration. It should be noted that there are two new values in **RequestedState** that build on the statuses of **EnabledState**. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. This property is set as the result of a method invocation (such as [**StartService**](https://msdn.microsoft.com/library/aa393655) or [**StopService**](https://msdn.microsoft.com/library/aa393668) on [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. A particular instance of [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/cc136818) might not support [**RequestStateChange**](https://msdn.microsoft.com/library/mt432433). If this occurs, the value 12 ("Not Applicable") is used.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

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

</dd> <dt>

**Resolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.17", "MIF.DMTF\|Electrical Current Probe\|001.17", "MIF.DMTF\|Voltage Probe\|001.17")
</dt> </dl>

**Resolution** indicates the ability of the Sensor to resolve differences in the measured property. The units for this measurement are determined by **BaseUnit**\***UnitModifier**/**RateUnit**.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**SensorType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Sensor**](cim-sensor.md).**OtherSensorTypeDescription**")
</dt> </dl>

The Type of the Sensor, e.g. Voltage or Temperature Sensor. If the type is set to "Other", then the **OtherSensorType** Description can be used to further identify the type, or if the Sensor has numeric readings, then the type of the Sensor can be implicitly determined by the **Units**. A description of the different Sensor types is as follows: A Temperature Sensor measures the environmental temperature. Voltage and Current Sensors measure electrical voltage and current readings. A Tachometer measures speed/revolutions of a Device. For example, a Fan Device can have an associated Tachometer which measures its speed. A Counter is a general purpose Sensor that measures some numerical property of a Device. A Counter value can be cleared, but it never decreases. A Switch Sensor has states like Open/Close, On/Off, or Up/Down. A Lock has states of Locked/Unlocked. Humidity, Smoke Detection and Air Flow Sensors measure the equivalent environmental characteristics. A Presence Sensor detects the presence of a PhysicalElement.

This property is inherited from [**CIM\_Sensor**](cim-sensor.md).

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

</dd> <dt>

**SettableThresholds**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array representing the writable thresholds supported by Sensor.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

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

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the object. Various operational and non-operational statuses are defined. This property is deprecated in lieu of **OperationalStatus**, which includes the same semantics in its enumeration. This change is made for 3 reasons: 1) **Status** is more correctly defined as an array. This overcomes the limitation of describing status via a single value, when it is really a multi-valued property (for example, an element may be OK AND Stopped. 2) A [**MaxLen**](https://msdn.microsoft.com/library/aa393650) of 10 is too restrictive and leads to unclear enumerated values. And, 3) The change to a **uint16** data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property and did not want to modify their code. Therefore, Status was grandfathered into the Schema. Use of the Deprecated qualifier allows the maintenance of the existing property, but also permits an improved definition using **OperationalStatus**.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> <dt>



 ("No Contact")


</dt> <dd></dd> <dt>



 ("Lost Comm")


</dt> <dd></dd> <dt>



 ("Stopped")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings describing the various **OperationalStatus** array values. For example, if "Stopping" is the value assigned to **OperationalStatus**, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in **OperationalStatus**.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.4")
</dt> </dl>

The **StatusInfo** property indicates whether the Logical Device is in an enabled (value = 3), disabled (value = 4) or some other (1) or unknown (2) state. If this property does not apply to the LogicalDevice, the value, 5 ("Not Applicable"), should be used. StatusInfo has been deprecated in lieu of a more clearly named property with additional enumerated values (**EnabledState**), that is inherited from ManagedSystemElement.

If a Device is ("Enabled")(value=3), it has been powered up, and is configured and operational. The Device may or may not be functionally active, depending on whether its **Availability** (or **AdditionalAvailability**) indicate that it is ("Running/Full Power")(value=3) or ("Off line") (value=8). In an enabled but offline mode, a Device may be performing out-of-band requests, such as running Diagnostics. If ("Disabled") **StatusInfo** value=4), a Device can only be "enabled" or powered off. In a personal computer environment, ("Disabled") means that the Device's driver is not available in the stack. In other environments, a Device can be disabled by removing its configuration file. A disabled device is physically present in a System and consuming resources, but can not be communicated with until a load of a driver, a load of a configuration file or some other "enabling" activity has occurred.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

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

</dd> <dt>

**SupportedThresholds**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the thresholds supported by the numeric sensor. For more information, see **SettableThresholds** and **EnabledThresholds**. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

This property can contain the following values.

<dt>

<span id="LowerThresholdNonCritical"></span><span id="lowerthresholdnoncritical"></span><span id="LOWERTHRESHOLDNONCRITICAL"></span>

**LowerThresholdNonCritical** ("0")


</dt> <dd></dd> <dt>

<span id="UpperThresholdNonCritical"></span><span id="upperthresholdnoncritical"></span><span id="UPPERTHRESHOLDNONCRITICAL"></span>

**UpperThresholdNonCritical** ("1")


</dt> <dd></dd> <dt>

<span id="LowerThresholdCritical"></span><span id="lowerthresholdcritical"></span><span id="LOWERTHRESHOLDCRITICAL"></span>

**LowerThresholdCritical** ("2")


</dt> <dd></dd> <dt>

<span id="UpperThresholdCritical"></span><span id="upperthresholdcritical"></span><span id="UPPERTHRESHOLDCRITICAL"></span>

**UpperThresholdCritical** ("3")


</dt> <dd></dd> <dt>

<span id="LowerThresholdFatal"></span><span id="lowerthresholdfatal"></span><span id="LOWERTHRESHOLDFATAL"></span>

**LowerThresholdFatal** ("4")


</dt> <dd></dd> <dt>

<span id="UpperThresholdFatal"></span><span id="upperthresholdfatal"></span><span id="UPPERTHRESHOLDFATAL"></span>

**UpperThresholdFatal** ("5")


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
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

The date or time when the enabled state of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**Tolerance**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_NumericSensor**](cim-numericsensor.md).**Resolution**", "**CIM\_NumericSensor**.**Accuracy**")
</dt> </dl>

This property is being deprecated in lieu of using the **Resolution** and **Accuracy** properties.

Indicates the tolerance of the Sensor for the measured property. **Tolerance**, along with **Resolution** and **Accuracy**, is used to calculate the actual value of the measured physical property. **Tolerance** may vary depending on whether the Device is linear over its dynamic range.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

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

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_NumericSensor**](cim-numericsensor.md).**BaseUnits**", "**CIM\_NumericSensor**.**RateUnits**")
</dt> </dl>

The unit multiplier for the values returned by this Sensor. All the values returned by this Sensor are represented in the units obtained by (**BaseUnits** \* 10 raised to the power of the **UnitModifier**). For example, if **BaseUnits** is **Volts** (5) and the **UnitModifier** is -6, then the units of the values returned are MicroVolts. However, if the **RateUnits** property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if **RateUnits** is set to **Per Second** (3), then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier.

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md).

</dd> <dt>

**UpperThresholdCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.14", "MIF.DMTF\|Electrical Current Probe\|001.14", "MIF.DMTF\|Voltage Probe\|001.14")
</dt> </dl>

A value that specifies a range that determines whether the sensor is operating under **Normal**, **NonCritical**, **Critical**, or **Fatal** conditions. If **CurrentReading** is between **UpperThresholdCritical** and **UpperThresholdFatal**, then the current state is critical. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: 550

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**UpperThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.16", "MIF.DMTF\|Electrical Current Probe\|001.16", "MIF.DMTF\|Voltage Probe\|001.16")
</dt> </dl>

A value that specifies a range that determines whether the sensor is operating under **Normal**, **NonCritical**, **Critical**, or **Fatal** conditions. If **CurrentReading** is above **UpperThresholdFatal**, then the current state is fatal. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: 1270

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> <dt>

**UpperThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Temperature Probe\|002.12", "MIF.DMTF\|Electrical Current Probe\|001.12", "MIF.DMTF\|Voltage Probe\|001.12")
</dt> </dl>

A value that specifies a range that determines whether the sensor is operating under **Normal**, **NonCritical**, **Critical**, or **Fatal** conditions. If **CurrentReading** is between **UpperThresholdNonCritical** and **UpperThresholdCritical**, then the current state is noncritical. This property is inherited from [**CIM\_NumericSensor**](https://www.bing.com/search?q=**CIM\_NumericSensor**).

Example: 500

This property is inherited from [**CIM\_NumericSensor**](cim-numericsensor.md) .

</dd> </dl>

## Remarks

All values returned by the numeric sensor are represented in the units obtained by the **BaseUnits** property, multiplied by 10, raised to the power of the **UnitModifier** property. For example, if **BaseUnits** is volts and **UnitModifier** is -6, then the units of the values returned are microvolts. However, if the **RateUnits** property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if **RateUnits** is set to "Per second", then the values returned by the sensor are in microvolts/second.

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

[**CIM\_NumericSensor**](cim-numericsensor.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





