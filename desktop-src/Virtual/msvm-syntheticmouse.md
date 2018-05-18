---
title: Msvm\_SyntheticMouse class
description: Represents a synthetic mouse device.
ms.assetid: '0d97b94d-8820-420e-9087-005bd14f9d9e'
keywords: ["RequestStateChange method Hyper-V", "RequestStateChange method Hyper-V , Msvm_SyntheticMouse class", "Msvm_SyntheticMouse class Hyper-V , RequestStateChange method", "Msvm_SyntheticMouse class Hyper-V", "Msvm_SyntheticMouse class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_SyntheticMouse
- Msvm_SyntheticMouse.RequestStateChange
- Msvm_SyntheticMouse.SetPowerState
- Msvm_SyntheticMouse.Reset
- Msvm_SyntheticMouse.EnableDevice
- Msvm_SyntheticMouse.OnlineDevice
- Msvm_SyntheticMouse.QuiesceDevice
- Msvm_SyntheticMouse.SaveProperties
- Msvm_SyntheticMouse.RestoreProperties
- Msvm_SyntheticMouse.Caption
- Msvm_SyntheticMouse.Description
- Msvm_SyntheticMouse.InstallDate
- Msvm_SyntheticMouse.Name
- Msvm_SyntheticMouse.OperationalStatus
- Msvm_SyntheticMouse.Status
- Msvm_SyntheticMouse.HealthState
- Msvm_SyntheticMouse.EnabledState
- Msvm_SyntheticMouse.OtherEnabledState
- Msvm_SyntheticMouse.RequestedState
- Msvm_SyntheticMouse.EnabledDefault
- Msvm_SyntheticMouse.TimeOfLastStateChange
- Msvm_SyntheticMouse.SystemCreationClassName
- Msvm_SyntheticMouse.SystemName
- Msvm_SyntheticMouse.PowerManagementSupported
- Msvm_SyntheticMouse.PowerManagementCapabilities
- Msvm_SyntheticMouse.Availability
- Msvm_SyntheticMouse.StatusInfo
- Msvm_SyntheticMouse.LastErrorCode
- Msvm_SyntheticMouse.ErrorDescription
- Msvm_SyntheticMouse.ErrorCleared
- Msvm_SyntheticMouse.PowerOnHours
- Msvm_SyntheticMouse.TotalPowerOnHours
- Msvm_SyntheticMouse.AdditionalAvailability
- Msvm_SyntheticMouse.MaxQuiesceTime
- Msvm_SyntheticMouse.LocationIndicator
- Msvm_SyntheticMouse.IsLocked
- Msvm_SyntheticMouse.PointingType
- Msvm_SyntheticMouse.NumberOfButtons
- Msvm_SyntheticMouse.Resolution
- Msvm_SyntheticMouse.ElementName
- Msvm_SyntheticMouse.StatusDescriptions
- Msvm_SyntheticMouse.CreationClassName
- Msvm_SyntheticMouse.DeviceID
- Msvm_SyntheticMouse.OtherIdentifyingInfo
- Msvm_SyntheticMouse.IdentifyingDescriptions
- Msvm_SyntheticMouse.Handedness
- Msvm_SyntheticMouse.AbsoluteCoordinates
- Msvm_SyntheticMouse.HorizontalPosition
- Msvm_SyntheticMouse.VerticalPosition
- Msvm_SyntheticMouse.ScrollPosition
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_SyntheticMouse class

Represents a synthetic mouse device.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SyntheticMouse : CIM_PointingDevice
{
  string   Caption = "Mouse";
  string   Description = "Microsoft Synthetic Mouse";
  datetime InstallDate;
  string   Name = "Mouse";
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 2;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName = "GUID";
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   Availability;
  uint16   StatusInfo;
  uint32   LastErrorCode;
  string   ErrorDescription;
  boolean  ErrorCleared;
  uint64   PowerOnHours;
  uint64   TotalPowerOnHours;
  uint16   AdditionalAvailability[] = 6;
  uint64   MaxQuiesceTime;
  uint16   LocationIndicator = 4;
  boolean  IsLocked = False;
  uint16   PointingType = 3;
  uint8    NumberOfButtons = 5;
  uint32   Resolution;
  string   ElementName = "Mouse";
  string   StatusDescriptions[] = "OK";
  string   CreationClassName = "Msvm_SyntheticMouse";
  string   DeviceID = "Microsoft:GUID";
  string   OtherIdentifyingInfo[];
  string   IdentifyingDescriptions[];
  uint16   Handedness = 2;
  boolean  AbsoluteCoordinates = True;
  sint32   HorizontalPosition;
  sint32   VerticalPosition;
  sint32   ScrollPosition;
};
```

## Members

The **Msvm\_SyntheticMouse** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_SyntheticMouse** class has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClickButton**](clickbutton-msvm-syntheticmouse.md)                 | Performs a mouse click of the specified button. This is equivalent to calling [**SetButtonState**](setbuttonstate-msvm-syntheticmouse.md) twice, first to press the button, and again to release it.<br/>                                                           |
| **EnableDevice**                                                       | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| [**GetButtonState**](getbuttonstate-msvm-syntheticmouse.md)           | Gets the current button state (up or down) of a specified button.<br/>                                                                                                                                                                                               |
| **OnlineDevice**                                                       | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| **QuiesceDevice**                                                      | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| **RequestStateChange**                                                 | Requests that the state of the element be changed to the value specified in the [**RequestedState**](msvm-keyboard.md) parameter. This method is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and returns 1 (Not Supported).<br/> |
| **Reset**                                                              | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| **RestoreProperties**                                                  | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| **SaveProperties**                                                     | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| [**SetAbsolutePosition**](setabsoluteposition-msvm-syntheticmouse.md) | Sets the horizontal and vertical position of the mouse cursor.<br/>                                                                                                                                                                                                  |
| [**SetButtonState**](setbuttonstate-msvm-syntheticmouse.md)           | Sets whether the specified mouse button is currently pressed.<br/>                                                                                                                                                                                                   |
| **SetPowerState**                                                      | This method is not supported.<br/>                                                                                                                                                                                                                                   |
| [**SetScrollPosition**](setscrollposition-msvm-syntheticmouse.md)     | Changes the z-coordinate of the wheel control of the mouse. Values written to this property are always relative coordinate offsets.<br/>                                                                                                                             |



 

### Properties

The **Msvm\_SyntheticMouse** class has these properties.

<dl> <dt>

**AbsoluteCoordinates**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the device operates on absolute coordinates. If not set, the device's coordinates are relative. This property is set to **True**.

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

Any additional availability and status of the device, beyond that specified in the **Availability** property. The **Availability** property denotes the primary status and availability of the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to 6 (Not Applicable).

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**", "[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**AdditionalAvailability**")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Mouse".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "Msvm\_SyntheticMouse".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Synthetic Mouse".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

An address or other identifying information to uniquely name the logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "Microsoft:*GUID*".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the [**Name**](https://msdn.microsoft.com/library/aa387898) property of the **CIM\_ManagedSystemElement** class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where [**Name**](msvm-keyboard.md) exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Mouse".

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the **EnabledState** of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

The enabled and disabled states of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is set to 2 (Enabled) if the guest VM supports a synthetic mouse and 3 (Disabled) if it does not (for example, DOS).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Indicates that the element executes or could execute commands, processes any queued commands, and queues new requests.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


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

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.ErrorDescription")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**Handedness**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The configuration of the pointing device for right-hand or left-hand operation. This property is inherited from [**CIM\_PointingDevice**](https://msdn.microsoft.com/library/aa387970) and it is always set to 2 (Right Handed Operation).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 5 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> </dl>

</dd> <dt>

**HorizontalPosition**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The absolute x-coordinate of the pointing device.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**OtherIdentifyingInfo**")
</dt> </dl>

An array of free-form strings that provide explanations and details behind the entries in the [**OtherIdentifyingInfo**](msvm-keyboard.md) array. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to **NULL**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date and time at which the virtual system was created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**IsLocked**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the device is locked, preventing user input or output. This property is inherited from [**CIM\_UserDevice**](https://msdn.microsoft.com/library/aa388653) and it is set to **False**.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.LastErrorCode")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**LocationIndicator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_AlarmDevice**](https://msdn.microsoft.com/library/aa386576).**AlarmState**", "**CIM\_AlarmDevice**.**AudioIndicatorIsDisabled**", "**CIM\_AlarmDevice**.**VisualIndicatorIsDisabled**", "**CIM\_AlarmDevice**.**MotionIndicatorIsDisabled**")
</dt> </dl>

The state of an indicator that is part of a device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to 4 (Not Supported).

</dd> <dt>

**MaxQuiesceTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MilliSeconds")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "Mouse".

</dd> <dt>

**NumberOfButtons**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Pointing Device\|003.4")
</dt> </dl>

The number of buttons on the pointing device. This property is inherited from [**CIM\_PointingDevice**](https://msdn.microsoft.com/library/aa387970) and it is always set to 5.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current status of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 2 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **NULL** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**IdentifyingDescriptions**")
</dt> </dl>

Any additional data, beyond device ID information, that could be used to identify a logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to **NULL**.

</dd> <dt>

**PointingType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Pointing Device\|003.1")
</dt> </dl>

The type of pointing device. This property is inherited from [**CIM\_PointingDevice**](https://msdn.microsoft.com/library/aa387970) and it is always set to 3 (Mouse).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities.PowerCapabilities")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.PowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 12.

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)


</dt> <dd>

Indicates that this instance does not support the **RequestedState** property.

</dd> </dl>

</dd> <dt>

**Resolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Counts per Inch")
</dt> </dl>

The resolution of the primary video surface. This property is inherited from [**CIM\_PointingDevice**](https://msdn.microsoft.com/library/aa387970).

</dd> <dt>

**ScrollPosition**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Mickeys")
</dt> </dl>

The z-coordinate position of the mouse device.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describe the various [**OperationalStatus**](msvm-bioselement.md) array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "OK".

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.4")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The creation class name of the scoping system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "Msvm\_ComputerSystem".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the scoping system. This value corresponds to the value of the [**Name**](msvm-computersystem.md) property of the **Msvm\_ComputerSystem** class for the scoping virtual system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "*GUID*".

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.TotalPowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**VerticalPosition**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The absolute y-coordinate of the pointing device.

</dd> </dl>

## Remarks

Access to the **Msvm\_SyntheticMouse** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PointingDevice**](cim-pointingdevice.md)
</dt> <dt>

[**CIM\_PointingDevice**](https://msdn.microsoft.com/library/aa387970)
</dt> <dt>

[Input Classes](input-classes.md)
</dt> </dl>

 

 





