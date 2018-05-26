---
title: Msvm\_S3DisplayController class
description: Represents the state of the emulated S3 controller that is present in each virtual machine configuration.
ms.assetid: b3129904-7f1a-49f3-9020-d02d2f81a353
keywords:
- Msvm_S3DisplayController class Hyper-V
- Msvm_S3DisplayController class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_S3DisplayController
- Msvm_S3DisplayController.RequestStateChange
- Msvm_S3DisplayController.SetPowerState
- Msvm_S3DisplayController.Reset
- Msvm_S3DisplayController.EnableDevice
- Msvm_S3DisplayController.OnlineDevice
- Msvm_S3DisplayController.QuiesceDevice
- Msvm_S3DisplayController.SaveProperties
- Msvm_S3DisplayController.RestoreProperties
- Msvm_S3DisplayController.Caption
- Msvm_S3DisplayController.ElementName
- Msvm_S3DisplayController.InstallDate
- Msvm_S3DisplayController.Name
- Msvm_S3DisplayController.OperationalStatus
- Msvm_S3DisplayController.StatusDescriptions
- Msvm_S3DisplayController.Status
- Msvm_S3DisplayController.HealthState
- Msvm_S3DisplayController.EnabledState
- Msvm_S3DisplayController.OtherEnabledState
- Msvm_S3DisplayController.RequestedState
- Msvm_S3DisplayController.EnabledDefault
- Msvm_S3DisplayController.TimeOfLastStateChange
- Msvm_S3DisplayController.SystemCreationClassName
- Msvm_S3DisplayController.SystemName
- Msvm_S3DisplayController.CreationClassName
- Msvm_S3DisplayController.DeviceID
- Msvm_S3DisplayController.PowerManagementSupported
- Msvm_S3DisplayController.PowerManagementCapabilities
- Msvm_S3DisplayController.Availability
- Msvm_S3DisplayController.StatusInfo
- Msvm_S3DisplayController.LastErrorCode
- Msvm_S3DisplayController.ErrorDescription
- Msvm_S3DisplayController.ErrorCleared
- Msvm_S3DisplayController.OtherIdentifyingInfo
- Msvm_S3DisplayController.PowerOnHours
- Msvm_S3DisplayController.TotalPowerOnHours
- Msvm_S3DisplayController.IdentifyingDescriptions
- Msvm_S3DisplayController.AdditionalAvailability
- Msvm_S3DisplayController.MaxQuiesceTime
- Msvm_S3DisplayController.LocationIndicator
- Msvm_S3DisplayController.TimeOfLastReset
- Msvm_S3DisplayController.ProtocolSupported
- Msvm_S3DisplayController.MaxNumberControlled
- Msvm_S3DisplayController.ProtocolDescription
- Msvm_S3DisplayController.Description
- Msvm_S3DisplayController.VideoProcessor
- Msvm_S3DisplayController.VideoMemoryType
- Msvm_S3DisplayController.OtherVideoMemoryType
- Msvm_S3DisplayController.NumberOfVideoPages
- Msvm_S3DisplayController.MaxMemorySupported
- Msvm_S3DisplayController.AcceleratorCapabilities
- Msvm_S3DisplayController.CapabilityDescriptions
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

# Msvm\_S3DisplayController class

Represents the state of the emulated S3 controller that is present in each virtual machine configuration. Only one display controller can be active in a virtual machine at any time.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_S3DisplayController : CIM_DisplayController
{
  string   Caption = "Display Controller";
  string   ElementName = "Display Controller";
  datetime InstallDate;
  string   Name = "Display Controller";
  uint16   OperationalStatus[] = 2;
  string   StatusDescriptions[] = { "OK" };
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 2;
  string   OtherEnabledState;
  uint16   RequestedState = 2;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   CreationClassName = "Msvm_S3DisplayController";
  string   DeviceID = "Microsoft:GUID";
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
  uint16   ProtocolSupported = 1;
  uint32   MaxNumberControlled = 1;
  string   ProtocolDescription = "Video";
  string   Description = "Microsoft Emulated Display Controller";
  string   VideoProcessor = "Virtual S3 Video Processor";
  uint16   VideoMemoryType = 2;
  string   OtherVideoMemoryType;
  uint32   NumberOfVideoPages = 1024;
  uint32   MaxMemorySupported = 4194304;
  uint16   AcceleratorCapabilities[] = 2;
  string   CapabilityDescriptions[] = { "Graphics Accelerator" };
};
```

## Members

The **Msvm\_S3DisplayController** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_S3DisplayController** class has these methods.



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

The **Msvm\_S3DisplayController** class has these properties.

<dl> <dt>

**AcceleratorCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_DisplayController**](cim-displaycontroller.md).**CapabilityDescriptions**")
</dt> </dl>

The graphics and 3D capabilities of the display controller. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to 2 (Graphics Accelerator).

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to 6 (Not Applicable).

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

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_DisplayController**](cim-displaycontroller.md).**AcceleratorCapabilities**")
</dt> </dl>

An array of free-form strings that provide more detailed explanations for any of the video accelerator features indicated in the **AcceleratorCapabilities** array. Note that each entry of this array is related to the entry in the **AcceleratorCapabilities** array that is located at the same index. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to "Graphics Accelerator".

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Display Controller".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to "Msvm\_S3DisplayController".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Video\|004.18")
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Microsoft Emulated Display Controller".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to "Microsoft:*GUID*".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Display Controller" by default.

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

The enabled and disabled states of an element. It can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is set to 2 (Enabled) or 3 (Disabled).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Indicates that the element executes or could execute commands, processes any queued commands, and queues new requests.

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

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 5 (OK).

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

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is set to 4 (Not Supported).

</dd> <dt>

**MaxMemorySupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The maximum amount of memory supported, in bytes. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to 4,194,304 (0x400000).

</dd> <dt>

**MaxNumberControlled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port\|004.9")
</dt> </dl>

The maximum number of directly addressable entities that are supported by this controller. A value of 0 should be used if the number is unknown or unlimited. The protocol used by the controller to access controlled devices. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to 1.

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

**NumberOfVideoPages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of video pages supported given the current resolutions and available memory. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to 1024.

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

The enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **null** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

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

**OtherVideoMemoryType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_DisplayController**](cim-displaycontroller.md).**VideoMemoryType**")
</dt> </dl>

The video memory type when the instance's **VideoMemoryType** property is 1 (Other). This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to **NULL**.

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

A free-form string that provides more information that is related to the protocol supported by the controller. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to "Video".

</dd> <dt>

**ProtocolSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port\|004.2", "MIF.DMTF\|Disks\|003.3"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Controller**](cim-controller.md).**ProtocolDescription**")
</dt> </dl>

The protocol used by the controller to access controlled devices. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231) and it is set to 1 (Other).

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. A particular instance of [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) might not support the **RequestStateChange** method. If this occurs, the value 12 (Not Applicable) is used. This property is inherited from **CIM\_EnabledLogicalElement** and it is set to 2 (Enabled), 3 (Disabled), or 12 (Not Applicable).

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Indicates that the element executes or could execute commands, processes any queued commands, and queues new requests.

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

The last time the virtual computer system was powered on. This property is inherited from [**CIM\_Controller**](https://msdn.microsoft.com/library/aa387231).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063).

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

**VideoMemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Video\|004.6"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_DisplayController**](cim-displaycontroller.md).**OtherVideoMemoryType**")
</dt> </dl>

The type of video memory. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to 2 (VRAM).

</dd> <dt>

**VideoProcessor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string that describes the video processor/controller. This property is inherited from [**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810) and it is set to "Virtual S3 Video Processor".

</dd> </dl>

## Remarks

Access to the **Msvm\_S3DisplayController** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_DisplayController**](cim-displaycontroller.md)
</dt> <dt>

[**CIM\_DisplayController**](https://msdn.microsoft.com/library/cc136810)
</dt> <dt>

[Video Classes](video-classes.md)
</dt> </dl>

 

 





