---
description: Represents storage drive media and is used to populate the storage drives.
ms.assetid: 06955C09-CA56-4B4C-997B-9B65AF125375
title: Msvm_LogicalDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_LogicalDisk
- Msvm_LogicalDisk.SetPowerState
- Msvm_LogicalDisk.EnableDevice
- Msvm_LogicalDisk.OnlineDevice
- Msvm_LogicalDisk.QuiesceDevice
- Msvm_LogicalDisk.SaveProperties
- Msvm_LogicalDisk.RestoreProperties
- Msvm_LogicalDisk.InstanceID
- Msvm_LogicalDisk.Caption
- Msvm_LogicalDisk.Description
- Msvm_LogicalDisk.ElementName
- Msvm_LogicalDisk.InstallDate
- Msvm_LogicalDisk.Name
- Msvm_LogicalDisk.OperationalStatus
- Msvm_LogicalDisk.StatusDescriptions
- Msvm_LogicalDisk.Status
- Msvm_LogicalDisk.HealthState
- Msvm_LogicalDisk.CommunicationStatus
- Msvm_LogicalDisk.DetailedStatus
- Msvm_LogicalDisk.OperatingStatus
- Msvm_LogicalDisk.PrimaryStatus
- Msvm_LogicalDisk.EnabledState
- Msvm_LogicalDisk.OtherEnabledState
- Msvm_LogicalDisk.RequestedState
- Msvm_LogicalDisk.EnabledDefault
- Msvm_LogicalDisk.TimeOfLastStateChange
- Msvm_LogicalDisk.AvailableRequestedStates
- Msvm_LogicalDisk.TransitioningToState
- Msvm_LogicalDisk.SystemCreationClassName
- Msvm_LogicalDisk.SystemName
- Msvm_LogicalDisk.CreationClassName
- Msvm_LogicalDisk.DeviceID
- Msvm_LogicalDisk.PowerManagementSupported
- Msvm_LogicalDisk.PowerManagementCapabilities
- Msvm_LogicalDisk.Availability
- Msvm_LogicalDisk.StatusInfo
- Msvm_LogicalDisk.LastErrorCode
- Msvm_LogicalDisk.ErrorDescription
- Msvm_LogicalDisk.ErrorCleared
- Msvm_LogicalDisk.OtherIdentifyingInfo
- Msvm_LogicalDisk.PowerOnHours
- Msvm_LogicalDisk.TotalPowerOnHours
- Msvm_LogicalDisk.IdentifyingDescriptions
- Msvm_LogicalDisk.AdditionalAvailability
- Msvm_LogicalDisk.MaxQuiesceTime
- Msvm_LogicalDisk.DataOrganization
- Msvm_LogicalDisk.Purpose
- Msvm_LogicalDisk.Access
- Msvm_LogicalDisk.ErrorMethodology
- Msvm_LogicalDisk.BlockSize
- Msvm_LogicalDisk.NumberOfBlocks
- Msvm_LogicalDisk.ConsumableBlocks
- Msvm_LogicalDisk.IsBasedOnUnderlyingRedundancy
- Msvm_LogicalDisk.SequentialAccess
- Msvm_LogicalDisk.ExtentStatus
- Msvm_LogicalDisk.NoSinglePointOfFailure
- Msvm_LogicalDisk.DataRedundancy
- Msvm_LogicalDisk.PackageRedundancy
- Msvm_LogicalDisk.DeltaReservation
- Msvm_LogicalDisk.Primordial
- Msvm_LogicalDisk.NameFormat
- Msvm_LogicalDisk.NameNamespace
- Msvm_LogicalDisk.OtherNameNamespace
- Msvm_LogicalDisk.OtherNameFormat
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_LogicalDisk class

Represents storage drive media and is used to populate the storage drives. The media types supported include virtual hard files, virtual floppy files, ISO files, and physical device media.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_LogicalDisk : CIM_LogicalDisk
{
  string   InstanceID;
  string   Caption;
  uint64   Description;
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[] = 2;
  string   StatusDescriptions[] = { "OK" };
  string   Status;
  uint16   HealthState = 5;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  uint16   AvailableRequestedStates[];
  uint16   TransitioningToState;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  uint16   CreationClassName = "Msvm_LogicalDisk";
  string   DeviceID;
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   Availability = 6;
  uint16   StatusInfo;
  uint32   LastErrorCode;
  string   ErrorDescription;
  boolean  ErrorCleared;
  string   OtherIdentifyingInfo[];
  uint64   PowerOnHours;
  uint64   TotalPowerOnHours;
  string   IdentifyingDescriptions[];
  uint16   AdditionalAvailability[] = { 6 };
  uint64   MaxQuiesceTime;
  uint16   DataOrganization = 2;
  string   Purpose;
  uint16   Access;
  string   ErrorMethodology;
  uint64   BlockSize = 512;
  uint64   NumberOfBlocks = 266338304;
  uint64   ConsumableBlocks = 0;
  boolean  IsBasedOnUnderlyingRedundancy = False;
  boolean  SequentialAccess = False;
  uint16   ExtentStatus[] = { 2 };
  boolean  NoSinglePointOfFailure = False;
  uint16   DataRedundancy = 0;
  uint16   PackageRedundancy = 0;
  uint8    DeltaReservation = 0;
  boolean  Primordial = False;
  uint16   NameFormat = 12;
  uint16   NameNamespace = 8;
  string   OtherNameNamespace;
  string   OtherNameFormat;
};
```

## Members

The **Msvm\_LogicalDisk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_LogicalDisk** class has these methods.



| Method                                                            | Description                              |
|:------------------------------------------------------------------|:-----------------------------------------|
| **EnableDevice**                                                  | This method is not supported.<br/> |
| **OnlineDevice**                                                  | This method is not supported.<br/> |
| **QuiesceDevice**                                                 | This method is not supported.<br/> |
| [**RequestStateChange**](msvm-logicaldisk-requeststatechange.md) | Requests a state change.<br/>      |
| [**Reset**](msvm-logicaldisk-reset.md)                           | Resets the service.<br/>           |
| **RestoreProperties**                                             | This method is not supported.<br/> |
| **SaveProperties**                                                | This method is not supported.<br/> |
| **SetPowerState**                                                 | This method is not supported.<br/> |



 

### Properties

The **Msvm\_LogicalDisk** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the media is readable, writeable, or both. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).



| Value                                                                        | Meaning                |
|------------------------------------------------------------------------------|------------------------|
| <dl> <dt>0</dt> </dl> | Unknown<br/>     |
| <dl> <dt>1</dt> </dl> | Readable.<br/>   |
| <dl> <dt>2</dt> </dl> | Writeable.<br/>  |
| <dl> <dt>3</dt> </dl> | Read/write.<br/> |
| <dl> <dt>4</dt> </dl> | Write once.<br/> |



 

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any additional availability and status of the device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).



| Value                                                                            | Meaning                    |
|----------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>{ 6 }</dt> </dl> | Not applicable.<br/> |



 

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The primary availability and status of the device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).



| Value                                                                        | Meaning                    |
|------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>6</dt> </dl> | Not applicable.<br/> |



 

</dd> <dt>

**AvailableRequestedStates**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the possible values for the *RequestedState* parameter of the [**RequestStateChange**](/previous-versions/windows/desktop/iscsitarg/requeststatechange-cim-enabledlogicalelement) method used to initiate a state change. The values listed will be a subset of the values contained in the **RequestedStatesSupported** property of the associated instance of **CIM\_EnabledLogicalElementCapabilities**, where the values selected are a function of the current state of the [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)) object. This property can be non-**Null** if an implementation is able to advertise the set of possible values as a function of the current state. This property will be **Null** if an implementation is unable to determine the set of possible values as a function of the current state.

This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size, in bytes, of the blocks that form the storage extent. If the block size is variable, then the maximum block size, in bytes, should be specified. If the block size is unknown, or if a block concept is not valid (for example, for aggregate extents, memory, or logical disks), this will contain 1. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

"ISO Disk Image"

"Hard Disk Image"

"Floppy Disk Image"

"CD/DVD Disk"

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ability of the instrumentation to communicate with the underlying managed element. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**ConsumableBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of blocks, of size **BlockSize**, that are available for consumption when layering storage extents using the [**Msvm\_BasedOn**](msvm-basedon.md) association. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the class or subclass used in the creation of an instance. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).

</dd> <dt>

**DataOrganization**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data organization used. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).



| Value                                                                        | Meaning                 |
|------------------------------------------------------------------------------|-------------------------|
| <dl> <dt>2</dt> </dl> | Fixed block.<br/> |



 

</dd> <dt>

**DataRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of complete copies of data currently maintained. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**DeltaReservation**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A percentage that specifies the amount of space that should be reserved in a replica for caching changes. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Complements the **PrimaryStatus** property with additional status detail. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), and it is set to "Microsoft:*GUID*\\*device-specific-data*".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

"ISO Disk Image"

"Hard Disk Image"

"Floppy Disk Image"

"CD/DVD Disk"

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element. It can also indicate the transitions between these requested states. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the error reported in **LastErrorCode** is now cleared. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that provides more information about the error recorded in **LastErrorCode** and information about any corrective actions that can be taken. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the types of error detection and correction supported by this device. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**ExtentStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any additional status information beyond that captured in the **OperationalStatus** and other inherited properties.



| Value                                                                            | Meaning                         |
|----------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>{ 2 }</dt> </dl> | None/Not applicable.<br/> |



 

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely nonfunctional. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of free-form strings that provide explanations and details behind the entries in the **OtherIdentifyingInfo** property array. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), and it is set to **Null**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time the virtual machine configuration was created. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**IsBasedOnUnderlyingRedundancy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the underlying storage extents participate in a storage redundancy group. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last error code reported by the logical device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**MaxQuiesceTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property has been deprecated. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The label by which the object is known. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is the same as the **ElementName** property.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).



| Value                                                                         | Meaning                                 |
|-------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>1</dt> </dl>  | Other<br/>                        |
| <dl> <dt>12</dt> </dl> | Operating system device name<br/> |



 

</dd> <dt>

**NameNamespace**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).



| Value                                                                        | Meaning                                      |
|------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>1</dt> </dl> | Other<br/>                             |
| <dl> <dt>8</dt> </dl> | Operating system device namespace<br/> |



 

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether there exists no single point of failure. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**NumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of consecutive blocks, each block the size of the value contained in the **BlockSize** property, that form the storage extent. Total size of the storage extent can be calculated by multiplying the value of the **BlockSize** property by the value of this property. If the value of **BlockSize** is 1, this property is the total size of the storage extent. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides current status information for the operational condition of the element and can be used for providing more detail with respect to the value of the **EnabledState** property. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("OperationalStatus"), [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed")
</dt> </dl>

The current statuses of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

When the required QoS level for the virtual disk can't be satisfied, the primary status (OperationalStatus\[0\]) is set to Degraded (3) and the OperationalStatus array additionally contains a secondary status value that indicates the specific reason for the QoS condition, according to this table.



| Value                                                                                                                                                                                                    | Description                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="_Insufficient_Throughput___32788_"></span><span id="_insufficient_throughput___32788_"></span><span id="_INSUFFICIENT_THROUGHPUT___32788_"></span> Insufficient Throughput  (32788)<br/> | The requested minimum IOPS rate is currently not available to the device. <br/> |



 

> [!Note]  
> OperationalStatus is also used to report other error or warning conditions (for example, protocol mismatch between VSP and VSC). If multiple conditions exists, the primary status is set Degraded, and one or more secondary status values, in any order starting at index 1, is filled in the array.

 

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

<span id="Protocol_Mismatch"></span><span id="protocol_mismatch"></span><span id="PROTOCOL_MISMATCH"></span>

<span id="Protocol_Mismatch"></span><span id="protocol_mismatch"></span><span id="PROTOCOL_MISMATCH"></span>**Protocol Mismatch** (32775)


</dt> <dd></dd> <dt>

<span id="Communication_Timed_Out"></span><span id="communication_timed_out"></span><span id="COMMUNICATION_TIMED_OUT"></span>

<span id="Communication_Timed_Out"></span><span id="communication_timed_out"></span><span id="COMMUNICATION_TIMED_OUT"></span>**Communication Timed Out** (32783)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

<span id="Insufficient_Throughput"></span><span id="insufficient_throughput"></span><span id="INSUFFICIENT_THROUGHPUT"></span>

<span id="Insufficient_Throughput"></span><span id="insufficient_throughput"></span><span id="INSUFFICIENT_THROUGHPUT"></span>**Insufficient Throughput** (32788)


</dt> <dd></dd> <dt>

<span id="Unknown_QoS_Policy_ID"></span><span id="unknown_qos_policy_id"></span><span id="UNKNOWN_QOS_POLICY_ID"></span>

<span id="Unknown_QoS_Policy_ID"></span><span id="unknown_qos_policy_id"></span><span id="UNKNOWN_QOS_POLICY_ID"></span>**Unknown QoS Policy ID** (32791)


</dt> <dd></dd> <dt>

<span id="QoS_Not_Supported"></span><span id="qos_not_supported"></span><span id="QOS_NOT_SUPPORTED"></span>

<span id="QoS_Not_Supported"></span><span id="qos_not_supported"></span><span id="QOS_NOT_SUPPORTED"></span>**QoS Not Supported** (32792)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

<span id="QoS_Configuration_Mismatch"></span><span id="qos_configuration_mismatch"></span><span id="QOS_CONFIGURATION_MISMATCH"></span>

<span id="QoS_Configuration_Mismatch"></span><span id="qos_configuration_mismatch"></span><span id="QOS_CONFIGURATION_MISMATCH"></span>**QoS Configuration Mismatch** (32793)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> <dt>

<span id="Disk_Full"></span><span id="disk_full"></span><span id="DISK_FULL"></span>

<span id="Disk_Full"></span><span id="disk_full"></span><span id="DISK_FULL"></span>**Disk Full** (32794)


</dt> <dd>

> [!Note]  
> Added in Windows 10.

 

</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property must be set to **Null** when **EnabledState** is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any additional data, beyond device ID information, that could be used to identify a logical device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), and it is set to **Null**.

</dd> <dt>

**OtherNameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the format of the **Name** property when **NameFormat** contains the value 1 (Other). This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**OtherNameNamespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the namespace of the **Name** property when **NameNamespace** contains the value 1 (Other). This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**PackageRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of physical packages that can currently fail without data loss. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The power management capabilities of the device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the device can be power managed. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of consecutive hours that this device has been powered on since its last power cycle. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides high level status information. This property should be used in conjunction with the **DetailedStatus** property to provide high level and detailed health status information for the element and its subcomponents. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the containing system has the ability to create or delete this operational element. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent), and it is set to **False** for file-based media and **True** for pass-through media.

</dd> <dt>

**Purpose**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the media and/or its use. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. A particular instance of [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)) might not support the **RequestStateChange** method. If this occurs, the value 12 (Not Applicable) is used. This property is inherited from **CIM\_EnabledLogicalElement**.

</dd> <dt>

**SequentialAccess**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the storage is sequentially accessed by a media access device. Pass-through tape media is an example of a sequentially accessed storage extent. This property is inherited from [**CIM\_StorageExtent**](/windows/desktop/CIMWin32Prov/cim-storageextent).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the logical device. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping system's creation class name. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier for the scoping virtual machine. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)).

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of hours that this device has been powered. This property is inherited from [**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice), but it is not used.

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the target state to which the instance is transitioning. This property is inherited from [**CIM\_EnabledLogicalElement**](/previous-versions//cc136818(v=vs.85)), but it is not used.

</dd> </dl>

## Remarks

Access to the **Msvm\_LogicalDisk** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LogicalDisk**](cim-logicaldisk.md)
</dt> <dt>

[**CIM\_LogicalDisk**](/windows/desktop/CIMWin32Prov/cim-logicaldisk)
</dt> <dt>

[**Msvm\_StorageAlert**](msvm-storagealert.md)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

