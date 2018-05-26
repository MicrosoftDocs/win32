---
title: Msvm\_Keyboard class
description: Represents a keyboard device.
ms.assetid: eb1cac54-536b-4de1-9307-255634758b90
keywords:
- Msvm_Keyboard class Hyper-V
- Msvm_Keyboard class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_Keyboard
- Msvm_Keyboard.RequestStateChange
- Msvm_Keyboard.SetPowerState
- Msvm_Keyboard.Reset
- Msvm_Keyboard.EnableDevice
- Msvm_Keyboard.OnlineDevice
- Msvm_Keyboard.QuiesceDevice
- Msvm_Keyboard.SaveProperties
- Msvm_Keyboard.RestoreProperties
- Msvm_Keyboard.Caption
- Msvm_Keyboard.Description
- Msvm_Keyboard.InstallDate
- Msvm_Keyboard.Name
- Msvm_Keyboard.OperationalStatus
- Msvm_Keyboard.StatusDescriptions
- Msvm_Keyboard.Status
- Msvm_Keyboard.HealthState
- Msvm_Keyboard.EnabledState
- Msvm_Keyboard.RequestedState
- Msvm_Keyboard.TimeOfLastStateChange
- Msvm_Keyboard.SystemCreationClassName
- Msvm_Keyboard.SystemName
- Msvm_Keyboard.PowerManagementSupported
- Msvm_Keyboard.PowerManagementCapabilities
- Msvm_Keyboard.Availability
- Msvm_Keyboard.StatusInfo
- Msvm_Keyboard.LastErrorCode
- Msvm_Keyboard.ErrorDescription
- Msvm_Keyboard.ErrorCleared
- Msvm_Keyboard.PowerOnHours
- Msvm_Keyboard.TotalPowerOnHours
- Msvm_Keyboard.AdditionalAvailability
- Msvm_Keyboard.MaxQuiesceTime
- Msvm_Keyboard.LocationIndicator
- Msvm_Keyboard.IsLocked
- Msvm_Keyboard.ElementName
- Msvm_Keyboard.OtherEnabledState
- Msvm_Keyboard.EnabledDefault
- Msvm_Keyboard.CreationClassName
- Msvm_Keyboard.DeviceID
- Msvm_Keyboard.OtherIdentifyingInfo
- Msvm_Keyboard.IdentifyingDescriptions
- Msvm_Keyboard.Layout
- Msvm_Keyboard.NumberOfFunctionKeys
- Msvm_Keyboard.Password
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_Keyboard class

Represents a keyboard device. Keyboards are logical devices that are always present in a virtual system, and thus are not allocated through a resource pool. One instance is always present in a virtual computer system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_Keyboard : CIM_UserDevice
{
  string   Caption = "Keyboard";
  string   Description = "Microsoft Virtual Keyboard";
  datetime InstallDate;
  string   Name = "Keyboard";
  uint16   OperationalStatus[] = 2;
  string   StatusDescriptions[] = { "OK" };
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  uint16   RequestedState = 12;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName = "GUID";
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   Availability;
  uint16   StatusInfo;
  uint32   LastErrorCode;
  string   ErrorDescription;
  boolean  ErrorCleared;
  uint64   PowerOnHours;
  uint64   TotalPowerOnHours;
  uint16   AdditionalAvailability[] = 6;
  uint64   MaxQuiesceTime;
  uint16   LocationIndicator = 4;
  boolean  IsLocked = False;
  string   ElementName = "Keyboard";
  string   OtherEnabledState;
  uint16   EnabledDefault = 2;
  string   CreationClassName = "Msvm_Keyboard";
  string   DeviceID = "Microsoft:GUID";
  string   OtherIdentifyingInfo[];
  string   IdentifyingDescriptions[];
  string   Layout = "00000409";
  uint16   NumberOfFunctionKeys = 12;
  uint16   Password = 5;
};
```

## Members

The **Msvm\_Keyboard** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_Keyboard** class has these methods.



| Method                                                 | Description                                                                                                                                                                                                       |
|:-------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EnableDevice**                                       | This method is not supported.<br/>                                                                                                                                                                          |
| [**IsKeyPressed**](iskeypressed-msvm-keyboard.md)     | Determines whether the specified key is pressed.<br/>                                                                                                                                                       |
| **OnlineDevice**                                       | This method is not supported.<br/>                                                                                                                                                                          |
| [**PressKey**](presskey-msvm-keyboard.md)             | Sets the state of the specified key to "pressed".<br/>                                                                                                                                                      |
| **QuiesceDevice**                                      | This method is not supported.<br/>                                                                                                                                                                          |
| [**ReleaseKey**](releasekey-msvm-keyboard.md)         | Clears the "pressed" state of the specified key.<br/>                                                                                                                                                       |
| **RequestStateChange**                                 | This method is not supported.<br/>                                                                                                                                                                          |
| **Reset**                                              | This method is not supported.<br/>                                                                                                                                                                          |
| **RestoreProperties**                                  | This method is not supported.<br/>                                                                                                                                                                          |
| **SaveProperties**                                     | This method is not supported.<br/>                                                                                                                                                                          |
| **SetPowerState**                                      | This method is not supported.<br/>                                                                                                                                                                          |
| [**TypeCtrlAltDel**](typectrlaltdel-msvm-keyboard.md) | Sends the CTRL+ALT+DEL key sequence.<br/>                                                                                                                                                                   |
| [**TypeKey**](typekey-msvm-keyboard.md)               | Types the specified key. This is equivalent to calling [**PressKey**](presskey-msvm-keyboard.md) followed by [**ReleaseKey**](releasekey-msvm-keyboard.md).<br/>                                          |
| [**TypeScancodes**](msvm-keyboard-typescancodes.md)   | Simulates a key sequence using scan codes.<br/> **Windows Server 2008:** The [**TypeScancodes**](msvm-keyboard-typescancodes.md) method is not supported until Windows Server 2008 R2.<br/>          |
| [**TypeText**](typetext-msvm-keyboard.md)             | Types the specified text string. This is equivalent to calling [**PressKey**](presskey-msvm-keyboard.md) followed by [**ReleaseKey**](releasekey-msvm-keyboard.md) for each character in the string.<br/> |



 

### Properties

The **Msvm\_Keyboard** class has these properties.

<dl> <dt>

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

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Keyboard".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "Msvm\_Keyboard".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Virtual Keyboard".

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

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the [**Name**](https://msdn.microsoft.com/library/aa387898) property of the **CIM\_ManagedSystemElement** class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Keyboard".

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

The enabled and disabled states of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 5 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)


</dt> <dd>

Indicates the element does not support to be enabled or disabled.

</dd> </dl>

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

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**OtherIdentifyingInfo**")
</dt> </dl>

An array of free-form strings that provide explanations and details behind the entries in the **OtherIdentifyingInfo** array. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to **NULL**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date and time when the virtual system was created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

**Layout**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string indicating the format and layout of the keyboard. This property is set to "00000409".

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

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "Keyboard".

</dd> <dt>

**NumberOfFunctionKeys**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of function keys on the keyboard. This property is set to 12.

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

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **NULL** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

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

**Password**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether a hardware-level password is enabled at the keyboard, preventing local input. This property is set to 5 (Not Implemented).

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

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "OK".

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

The scoping system's creation class name. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to "Msvm\_ComputerSystem".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping system's name. This value corresponds to the value of the **Name** property of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class for the scoping virtual system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "*GUID*".

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time when the enabled state of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

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

</dd> </dl>

## Remarks

Access to the **Msvm\_Keyboard** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_UserDevice**](cim-userdevice.md)
</dt> <dt>

[**CIM\_UserDevice**](https://msdn.microsoft.com/library/aa388653)
</dt> <dt>

[Input Classes](input-classes.md)
</dt> </dl>

 

 





