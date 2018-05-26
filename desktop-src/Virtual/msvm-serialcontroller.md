---
title: Msvm\_SerialController class
description: Represents the capabilities and management of the serial controller.
ms.assetid: 9a02b435-889e-4fe2-a20d-c4793c8cf48e
keywords:
- Msvm_SerialController class Hyper-V
- Msvm_SerialController class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SerialController
- Msvm_SerialController.RequestStateChange
- Msvm_SerialController.SetPowerState
- Msvm_SerialController.Reset
- Msvm_SerialController.EnableDevice
- Msvm_SerialController.OnlineDevice
- Msvm_SerialController.QuiesceDevice
- Msvm_SerialController.SaveProperties
- Msvm_SerialController.RestoreProperties
- Msvm_SerialController.Caption
- Msvm_SerialController.Description
- Msvm_SerialController.ElementName
- Msvm_SerialController.InstallDate
- Msvm_SerialController.Name
- Msvm_SerialController.OperationalStatus
- Msvm_SerialController.Status
- Msvm_SerialController.HealthState
- Msvm_SerialController.EnabledState
- Msvm_SerialController.OtherEnabledState
- Msvm_SerialController.RequestedState
- Msvm_SerialController.TimeOfLastStateChange
- Msvm_SerialController.SystemCreationClassName
- Msvm_SerialController.SystemName
- Msvm_SerialController.CreationClassName
- Msvm_SerialController.DeviceID
- Msvm_SerialController.PowerManagementSupported
- Msvm_SerialController.PowerManagementCapabilities
- Msvm_SerialController.Availability
- Msvm_SerialController.StatusInfo
- Msvm_SerialController.LastErrorCode
- Msvm_SerialController.ErrorDescription
- Msvm_SerialController.ErrorCleared
- Msvm_SerialController.OtherIdentifyingInfo
- Msvm_SerialController.PowerOnHours
- Msvm_SerialController.TotalPowerOnHours
- Msvm_SerialController.IdentifyingDescriptions
- Msvm_SerialController.AdditionalAvailability
- Msvm_SerialController.MaxQuiesceTime
- Msvm_SerialController.LocationIndicator
- Msvm_SerialController.TimeOfLastReset
- Msvm_SerialController.ProtocolSupported
- Msvm_SerialController.MaxNumberControlled
- Msvm_SerialController.ProtocolDescription
- Msvm_SerialController.Capabilities
- Msvm_SerialController.CapabilityDescriptions
- Msvm_SerialController.Security
- Msvm_SerialController.StatusDescriptions
- Msvm_SerialController.EnabledDefault
- Msvm_SerialController.CapabilitiesDescriptions
- Msvm_SerialController.MaxBaudRate
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

# Msvm\_SerialController class

Represents the capabilities and management of the serial controller. Serial controllers are logical devices that are always present in a virtual system, and thus are not allocated through a resource pool. One serial controller instance is always present in a virtual computer system. Serial controllers have a fixed number of port instances. This implementation supports two ports per controller.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SerialController : CIM_SerialController
{
  string   Caption = "Serial Controller";
  string   Description = "Microsoft Virtual Serial Controller";
  string   ElementName = "Serial Controller";
  datetime InstallDate;
  string   Name = "Serial Controller";
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   CreationClassName = "Msvm_SerialController";
  string   DeviceID = "Microsoft:<GUID>";
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
  uint16   AdditionalAvailability[] = 6;
  uint64   MaxQuiesceTime;
  uint16   LocationIndicator = 4;
  datetime TimeOfLastReset;
  uint16   ProtocolSupported = 26;
  uint32   MaxNumberControlled = 2;
  string   ProtocolDescription;
  uint16   Capabilities[] = 5;
  string   CapabilityDescriptions[];
  uint16   Security = 3;
  string   StatusDescriptions[] = { "OK" };
  uint16   EnabledDefault = 2;
  string   CapabilitiesDescriptions[] = { "16550 compatible" };
  uint32   MaxBaudRate = 115200;
};
```

## Members

The **Msvm\_SerialController** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_SerialController** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **EnableDevice**       | This method is not supported.<br/> |
| **OnlineDevice**       | This method is not supported.<br/> |
| **QuiesceDevice**      | This method is not supported.<br/> |
| **RequestStateChange** | This method is not supported.<br/> |
| **Reset**              | This method is not supported.<br/> |
| **RestoreProperties**  | This method is not supported.<br/> |
| **SaveProperties**     | This method is not supported.<br/> |
| **SetPowerState**      | This method is not supported.<br/> |



 

### Properties

The **Msvm\_SerialController** class has these properties.

<dl> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to 6 ("Not Applicable").

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**", "[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**AdditionalAvailability**")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to **NULL**.

</dd> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Serial Ports\|004.7"), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SerialController**](cim-serialcontroller.md).**CapabilityDescriptions**")
</dt> </dl>

The buffering and other capabilities of the serial controller that might be inherent in the chip hardware. This property is inherited from [**CIM\_SerialController**](https://msdn.microsoft.com/library/aa388440) and it is set to 5 (16550 compatible).

</dd> <dt>

**CapabilitiesDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of free-form strings that provides more detailed explanations for any of the serial controller features that are indicated in the **Capabilities** array. This property is inherited from [**CIM\_SerialController**](https://msdn.microsoft.com/library/aa388440) and it is set to "16550 compatible".

</dd> <dt>

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SerialController**](cim-serialcontroller.md).**Capabilities**")
</dt> </dl>

An array that contains more detailed explanations for serial controller features in the **Capabilities** array. The items in the **CapabilityDescriptions** array correlate to those in the **Capabilities** array.

This property is inherited from [**CIM\_SerialController**](cim-serialcontroller.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Serial Controller".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to "Msvm\_SerialController".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Virtual Serial Controller".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to "Microsoft:*&lt;GUID&gt;*".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Serial Controller".

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

The enabled and disabled states of an element. It can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 5 (Not Applicable).

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

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 5.

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

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to **NULL**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date and time the virtual machine configuration was created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to 4 ("Not Supported").

</dd> <dt>

**MaxBaudRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits per Second"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Serial Ports\|004.6")
</dt> </dl>

The maximum baud rate, in bits per second, that is supported by the serial controller. This property is inherited from [**CIM\_SerialController**](https://msdn.microsoft.com/library/aa388440) and it is set to 115200.

</dd> <dt>

**MaxNumberControlled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port\|004.9")
</dt> </dl>

The maximum number of directly addressable entities that are supported by this controller. A value of 0 should be used if the number is unknown or unlimited. The protocol used by the controller to access controlled devices. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to 2.

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

The label by which the object is known. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is the same as the **ElementName** property.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current statuses of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to 2 (OK).

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

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to **NULL**.

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

**ProtocolDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port\|004.3"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Controller**](cim-controller.md).**ProtocolSupported**")
</dt> </dl>

A free-form string that provides more information that is related to the protocol supported by the controller. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to **NULL**.

</dd> <dt>

**ProtocolSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port\|004.2", "MIF.DMTF\|Disks\|003.3"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Controller**](cim-controller.md).**ProtocolDescription**")
</dt> </dl>

The protocol used by the controller to access controlled devices. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to 26 (IEEE-488).

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. A particular instance of [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) might not support the **RequestedStateChange** method. If this occurs, the value 12 (Not Applicable) is used. This property is inherited from **CIM\_EnabledLogicalElement** and it is always set to 12 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)


</dt> <dd>

Indicates that this instance does not support the **RequestedState** property.

</dd> </dl>

</dd> <dt>

**Security**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Serial Ports\|004.9")
</dt> </dl>

The operational security for the controller. This property is inherited from [**CIM\_SerialController**](https://msdn.microsoft.com/library/aa388440) and it is set to 3 (None).

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

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and each array element is always set to "OK".

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

The unique identifier for the scoping virtual system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**TimeOfLastReset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time the virtual computer system was powered on. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to **NULL**.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

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

Access to the **Msvm\_SerialController** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_SerialController**](cim-serialcontroller.md)
</dt> <dt>

[**CIM\_SerialController**](https://msdn.microsoft.com/library/aa388440)
</dt> <dt>

[Serial Devices Classes](serial-devices-classes.md)
</dt> </dl>

 

 





