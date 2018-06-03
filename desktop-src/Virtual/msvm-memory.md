---
title: Msvm\_Memory class
description: Represents the memory currently allocated to a virtual system.
ms.assetid: 7edccb2f-374e-4f1f-a9cf-06d5bd23a972
keywords:
- Msvm_Memory class Hyper-V
- Msvm_Memory class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_Memory
- Msvm_Memory.RequestStateChange
- Msvm_Memory.SetPowerState
- Msvm_Memory.Reset
- Msvm_Memory.EnableDevice
- Msvm_Memory.OnlineDevice
- Msvm_Memory.QuiesceDevice
- Msvm_Memory.SaveProperties
- Msvm_Memory.RestoreProperties
- Msvm_Memory.Caption
- Msvm_Memory.Description
- Msvm_Memory.ElementName
- Msvm_Memory.InstallDate
- Msvm_Memory.OperationalStatus
- Msvm_Memory.Status
- Msvm_Memory.HealthState
- Msvm_Memory.EnabledState
- Msvm_Memory.OtherEnabledState
- Msvm_Memory.RequestedState
- Msvm_Memory.TimeOfLastStateChange
- Msvm_Memory.SystemCreationClassName
- Msvm_Memory.SystemName
- Msvm_Memory.PowerManagementSupported
- Msvm_Memory.PowerManagementCapabilities
- Msvm_Memory.Availability
- Msvm_Memory.StatusInfo
- Msvm_Memory.LastErrorCode
- Msvm_Memory.ErrorDescription
- Msvm_Memory.ErrorCleared
- Msvm_Memory.PowerOnHours
- Msvm_Memory.TotalPowerOnHours
- Msvm_Memory.IdentifyingDescriptions
- Msvm_Memory.AdditionalAvailability
- Msvm_Memory.MaxQuiesceTime
- Msvm_Memory.LocationIndicator
- Msvm_Memory.DataOrganization
- Msvm_Memory.Purpose
- Msvm_Memory.Access
- Msvm_Memory.NumberOfBlocks
- Msvm_Memory.IsBasedOnUnderlyingRedundancy
- Msvm_Memory.SequentialAccess
- Msvm_Memory.ExtentStatus
- Msvm_Memory.NoSinglePointOfFailure
- Msvm_Memory.DataRedundancy
- Msvm_Memory.PackageRedundancy
- Msvm_Memory.DeltaReservation
- Msvm_Memory.Primordial
- Msvm_Memory.Name
- Msvm_Memory.NameFormat
- Msvm_Memory.NameNamespace
- Msvm_Memory.Volatile
- Msvm_Memory.ErrorMethodology
- Msvm_Memory.StartingAddress
- Msvm_Memory.ErrorInfo
- Msvm_Memory.OtherErrorDescription
- Msvm_Memory.CorrectableError
- Msvm_Memory.ErrorTime
- Msvm_Memory.ErrorAccess
- Msvm_Memory.ErrorTransferSize
- Msvm_Memory.ErrorData
- Msvm_Memory.ErrorDataOrder
- Msvm_Memory.ErrorAddress
- Msvm_Memory.SystemLevelAddress
- Msvm_Memory.ErrorResolution
- Msvm_Memory.AdditionalErrorData
- Msvm_Memory.StatusDescriptions
- Msvm_Memory.EnabledDefault
- Msvm_Memory.CreationClassName
- Msvm_Memory.DeviceID
- Msvm_Memory.OtherIdentifyingInfo
- Msvm_Memory.BlockSize
- Msvm_Memory.ConsumableBlocks
- Msvm_Memory.OtherNameNamespace
- Msvm_Memory.OtherNameFormat
- Msvm_Memory.EndingAddress
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_Memory class

Represents the memory currently allocated to a virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_Memory : CIM_Memory
{
  string   Caption = "Memory";
  string   Description = "Memory";
  string   ElementName = "Memory";
  datetime InstallDate;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 5;
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
  string   IdentifyingDescriptions[];
  uint16   AdditionalAvailability[];
  uint64   MaxQuiesceTime;
  uint16   LocationIndicator;
  uint16   DataOrganization = 2;
  string   Purpose = "System Memory";
  uint16   Access = 3;
  uint64   NumberOfBlocks;
  boolean  IsBasedOnUnderlyingRedundancy = False;
  boolean  SequentialAccess = False;
  uint16   ExtentStatus[] = 2;
  boolean  NoSinglePointOfFailure = False;
  uint16   DataRedundancy = 1;
  uint16   PackageRedundancy = 0;
  uint8    DeltaReservation = 0;
  boolean  Primordial = FALSE;
  string   Name = "GUID";
  uint16   NameFormat = 0;
  uint16   NameNamespace = 0;
  boolean  Volatile = TRUE;
  string   ErrorMethodology;
  uint64   StartingAddress = 0;
  uint16   ErrorInfo;
  string   OtherErrorDescription;
  boolean  CorrectableError;
  datetime ErrorTime;
  uint16   ErrorAccess;
  uint32   ErrorTransferSize;
  uint8    ErrorData[];
  uint16   ErrorDataOrder;
  uint64   ErrorAddress;
  boolean  SystemLevelAddress;
  uint64   ErrorResolution;
  uint8    AdditionalErrorData[];
  string   StatusDescriptions[] = "OK";
  uint16   EnabledDefault = 2;
  string   CreationClassName = "Msvm_Memory";
  string   DeviceID = "Microsoft:GUID";
  string   OtherIdentifyingInfo[];
  uint64   BlockSize = 1048576;
  uint64   ConsumableBlocks;
  string   OtherNameNamespace;
  string   OtherNameFormat;
  uint64   EndingAddress;
};
```

## Members

The **Msvm\_Memory** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_Memory** class has these methods.



| Method                 | Description                                                                                                                                                                                                                                                     |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EnableDevice**       | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |
| **OnlineDevice**       | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |
| **QuiesceDevice**      | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |
| **RequestStateChange** | Requests that the state of the element be changed to the value specified in the [**RequestedState**](msvm-keyboard.md) parameter. This method is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is not used.<br/> |
| **Reset**              | Requests a reset of the logical device. This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                       |
| **RestoreProperties**  | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |
| **SaveProperties**     | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |
| **SetPowerState**      | This method is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is not used.<br/>                                                                                                                                               |



 

### Properties

The **Msvm\_Memory** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the read/write properties of the media. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is set to 3 (Read/Write Supported) by default.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>

**Readable** (1)


</dt> <dd></dd> <dt>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>

**Writeable** (2)


</dt> <dd></dd> <dt>

<span id="Read_Write_Supported"></span><span id="read_write_supported"></span><span id="READ_WRITE_SUPPORTED"></span>

**Read/Write Supported** (3)


</dt> <dd></dd> <dt>

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>

**Write Once** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

Any additional availability and status of the device, beyond that specified in the **Availability** property. The **Availability** property denotes the primary status and availability of the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to {6} (Not Applicable).

</dd> <dt>

**AdditionalErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.AdditionalErrorData"), **OctetString**, [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Device\|005.18", "MIF.DMTF\|Physical Memory Array\|001.13"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**", "[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**AdditionalAvailability**")
</dt> </dl>

The availability and status of the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Host Storage\|001.4", "MIB.IETF\|HOST-RESOURCES-MIB.hrStorageAllocationUnits", "MIF.DMTF\|Storage Devices\|001.5")
</dt> </dl>

The size, in bytes, of the blocks that form the storage extent. If variable block size, then the maximum block size, in bytes, should be specified. If the block size is unknown, or if a block concept is not valid (for example, for aggregate extents, memory, or logical disks), enter a 1 (one). This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 1048576.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Memory".

</dd> <dt>

**ConsumableBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of blocks, of size **BlockSize**, which are available for consumption when layering storage extents using the BasedOn association. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **NULL**.

</dd> <dt>

**CorrectableError**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.CorrectableError"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Physical Memory Array\|001.8")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "Msvm\_Memory".

</dd> <dt>

**DataOrganization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data organization used. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 2.

</dd> <dt>

**DataRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageSetting**](https://msdn.microsoft.com/library/mt432372).**DataRedundancyGoal**", "**CIM\_StorageSetting**.**DataRedundancyMax**", "**CIM\_StorageSetting**.**DataRedundancyMin**")
</dt> </dl>

The number of complete copies of data that is currently maintained. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 1.

</dd> <dt>

**DeltaReservation**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageSetting**](https://msdn.microsoft.com/library/mt432372).**DeltaReservationGoal**", "**CIM\_StorageSetting**.**DeltaReservationMax**", "**CIM\_StorageSetting**.**DeltaReservationMin**")
</dt> </dl>

The current value for delta reservation. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 0.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Memory".

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

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the **Name** property of the [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is set to "Memory".

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

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("KiloBytes"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.4", "MIF.DMTF\|Memory Device Mapped Addresses\|001.5")
</dt> </dl>

The ending address of the contiguous memory block. Since the **StartingAddress** property is always 0, this value always reflects the total amount of memory in the virtual system.

</dd> <dt>

**ErrorAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorAccess"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Physical Memory Array\|001.10")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**ErrorAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.StartingAddress"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Device\|005.19", "MIF.DMTF\|Physical Memory Array\|001.14")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

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

**ErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorData"), **OctetString**, [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Physical Memory Array\|001.12"), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**ErrorDataOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorDataOrder")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

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

**ErrorInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorInfo"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Device\|005.12", "MIF.DMTF\|Physical Memory Array\|001.8"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Memory**](cim-memory.md).**OtherErrorDescription**")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Physical Memory Array\|001.7")
</dt> </dl>

A free-form string that describes the type of error detection and correction supported by this storage extent. This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) and it is always set to **NULL**.

</dd> <dt>

**ErrorResolution**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorResolution"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Device\|005.21", "MIF.DMTF\|Physical Memory Array\|001.15")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**ErrorTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorTime")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it not used.

</dd> <dt>

**ErrorTransferSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.ErrorTransferSize"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Physical Memory Array\|001.11")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**ExtentStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Storage extents have additional status information beyond that captured in the **OperationalStatus** and other properties, inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898). This additional information (for example, "Protection Disabled", value=9) is captured in the **VolumeStatus** property. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 2 (None/Not Applicable).

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

The date and time at which the virtual system was created. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**IsBasedOnUnderlyingRedundancy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, indicates whether the underlying storage extent(s) participate in a Storage Redundancy Group. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **False**.

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

The state of an indicator that is part of a device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="On"></span><span id="on"></span><span id="ON"></span>

**On** (2)


</dt> <dd></dd> <dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>

**Off** (3)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (4)


</dt> <dd></dd> </dl>

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

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10\| VPD 83, Association 0 \| Identifier"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**NameFormat**", "**CIM\_StorageExtent**.**NameNamespace**")
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to "*GUID*".

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**Name**", "**CIM\_StorageExtent**.**NameNamespace**", "**CIM\_StorageExtent**.**OtherNameFormat**")
</dt> </dl>

This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 0.

</dd> <dt>

**NameNamespace**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("SPC.INCITS-T10\| VPD 83, Association 0 \| Identifier"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**Name**", "**CIM\_StorageExtent**.**OtherNameNamespace**", "**CIM\_StorageExtent**.**NameFormat**")
</dt> </dl>

This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 0.

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageSetting**](https://msdn.microsoft.com/library/mt432372).**NoSinglePointOfFailure**")
</dt> </dl>

Indicates whether there exists no single point of failure. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **False**.

</dd> <dt>

**NumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Host Storage\|001.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrStorageSize")
</dt> </dl>

A calculated value that represents the total amount of memory divided by the **BlockSize**. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

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

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **null** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to **NULL**.

</dd> <dt>

**OtherErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.OtherErrorDescription"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Memory**](cim-memory.md).**ErrorInfo**")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

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

**OtherNameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**NameFormat**")
</dt> </dl>

The namespace of the **Name** property when the **NameFormat** property includes the value 1 (Other"). This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **NULL**.

</dd> <dt>

**OtherNameNamespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageExtent**](cim-storageextent.md).**NameNamespace**")
</dt> </dl>

The namespace of the **Name** property when the **NameNamespace** property includes the value 1 (Other). This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **NULL**.

</dd> <dt>

**PackageRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_StorageSetting**](https://msdn.microsoft.com/library/mt432372).**PackageRedundancyGoal**", "**CIM\_StorageSetting**.**PackageRedundancyMax**", "**CIM\_StorageSetting**.**PackageRedundancyMin**")
</dt> </dl>

The number of physical packages that can currently fail without data loss. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to 0.

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

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, indicates whether the containing system does not have the ability to create or delete this operational element. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496).

</dd> <dt>

**Purpose**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|HOST-RESOURCES-MIB.hrStorageDescr")
</dt> </dl>

A free-form string that describes the media and its use. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to "System Memory".

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and it is always set to 5 (No Change).

<dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>**No Change** (5)


</dt> <dd>

No state change has been requested.

</dd> </dl>

</dd> <dt>

**SequentialAccess**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, indicates whether the storage is sequentially accessed by a media access device. A tape partition is an example of a sequentially accessed storage extent. Storage volumes, disk partitions and logical disks represent randomly accessed extents. This property is inherited from [**CIM\_StorageExtent**](https://msdn.microsoft.com/library/aa388496) and it is always set to **False**.

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("KiloBytes"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.3", "MIF.DMTF\|Memory Device Mapped Addresses\|001.4")
</dt> </dl>

The beginning address referenced by an application or operating system and mapped by a memory controller for this memory object. This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) and it is always set to 0.

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

Strings that describes the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "OK".

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

**SystemLevelAddress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_MemoryError.SystemLevelAddress")
</dt> </dl>

This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) but it is not used.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The scoping system's name. This value corresponds to the value of the [**Name**](msvm-computersystem.md) property of the **Msvm\_ComputerSystem** class for the scoping virtual system. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and it is always set to "*GUID*".

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the virtual machine's state was last modified. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063).

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.TotalPowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)but it is not used.

</dd> <dt>

**Volatile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether memory is volatile. This property is inherited from [**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904) and it is always set to **TRUE**.

</dd> </dl>

## Remarks

Access to the **Msvm\_Memory** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_Memory**](cim-memory.md)
</dt> <dt>

[**CIM\_Memory**](https://msdn.microsoft.com/library/aa387904)
</dt> <dt>

[Memory Classes](memory-classes.md)
</dt> </dl>

 

 





