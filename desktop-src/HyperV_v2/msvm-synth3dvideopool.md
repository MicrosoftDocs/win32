---
description: Contains information about the synthetic 3-D video graphics processing units (GPUs) available on the host system.
ms.assetid: 771A42C3-4888-49DF-A389-161A2D0E3DBD
title: Msvm_Synth3dVideoPool class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Synth3dVideoPool
- Msvm_Synth3dVideoPool.InstanceID
- Msvm_Synth3dVideoPool.Caption
- Msvm_Synth3dVideoPool.Description
- Msvm_Synth3dVideoPool.ElementName
- Msvm_Synth3dVideoPool.InstallDate
- Msvm_Synth3dVideoPool.Name
- Msvm_Synth3dVideoPool.OperationalStatus
- Msvm_Synth3dVideoPool.StatusDescriptions
- Msvm_Synth3dVideoPool.Status
- Msvm_Synth3dVideoPool.HealthState
- Msvm_Synth3dVideoPool.CommunicationStatus
- Msvm_Synth3dVideoPool.DetailedStatus
- Msvm_Synth3dVideoPool.OperatingStatus
- Msvm_Synth3dVideoPool.PrimaryStatus
- Msvm_Synth3dVideoPool.PoolID
- Msvm_Synth3dVideoPool.Primordial
- Msvm_Synth3dVideoPool.Capacity
- Msvm_Synth3dVideoPool.Reserved
- Msvm_Synth3dVideoPool.ResourceType
- Msvm_Synth3dVideoPool.OtherResourceType
- Msvm_Synth3dVideoPool.ResourceSubType
- Msvm_Synth3dVideoPool.AllocationUnits
- Msvm_Synth3dVideoPool.ConsumedResourceUnits
- Msvm_Synth3dVideoPool.CurrentlyConsumedResource
- Msvm_Synth3dVideoPool.MaxConsumableResource
- Msvm_Synth3dVideoPool.Is3dVideoSupported
- Msvm_Synth3dVideoPool.IsSLATCapable
- Msvm_Synth3dVideoPool.IsGPUCapable
- Msvm_Synth3dVideoPool.DirectXVersion
- Msvm_Synth3dVideoPool.RequiredMinimumDirectXVersion
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_Synth3dVideoPool class

Contains information about the synthetic 3-D video graphics processing units (GPUs) available on the host system. This class is only used with host systems that support RemoteFX.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_Synth3dVideoPool : CIM_ResourcePool
{
  string   InstanceID;
  string   Caption = "3D Display Controller Resource Pool";
  string   Description = "Resource pool used to allocate synthetic 3D video controller resources to a virtual machine.";
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[];
  string   StatusDescriptions[] = {"OK"};
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   PoolID;
  boolean  Primordial = True;
  uint64   Capacity;
  uint64   Reserved = 0;
  uint16   ResourceType;
  string   OtherResourceType;
  string   ResourceSubType = "Microsoft:Hyper-V:Synthetic 3D Display Controller";
  string   AllocationUnits = "count";
  string   ConsumedResourceUnits = "count";
  uint64   CurrentlyConsumedResource;
  uint64   MaxConsumableResource;
  boolean  Is3dVideoSupported;
  boolean  IsSLATCapable;
  boolean  IsGPUCapable;
  string   DirectXVersion;
  string   RequiredMinimumDirectXVersion;
};
```

## Members

The **Msvm\_Synth3dVideoPool** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_Synth3dVideoPool** class has these methods.



| Method                                                                                             | Description                                                                               |
|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**CalculateVideoMemoryRequirements**](msvm-synth3dvideopool-calculatevideomemoryrequirements.md) | Calculates the amount of video memory required for a RemoteFX virtual machine.<br/> |



 

### Properties

The **Msvm\_Synth3dVideoPool** class has these properties.

<dl> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the resource pool. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount (in units of **AllocationUnits**) of active reservations that the resource pool can support. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ability of the instrumentation to communicate with the underlying managed element. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)
</dt> <dt>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>**Communication OK** (2)
</dt> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (3)
</dt> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (4)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**ConsumedResourceUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the units for the **MaxConsumableResource** and the **CurrentlyConsumedResource** properties. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**CurrentlyConsumedResource**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the amount of resource that the resource pool currently presents to consumers. This property is different from the **Reserved** property in that it describes the consumers view of the resource, while the **Reserved** property describes the producers view of the resource. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
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

Compliments the **PrimaryStatus** property with additional status detail. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (0)
</dt> <dt>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>**No Additional Information** (1)
</dt> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (2)
</dt> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (3)
</dt> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (4)
</dt> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (5)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**DirectXVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](/windows/desktop/WmiSdk/standard-qualifiers) (1024)
</dt> </dl>

Specifies the lowest version of DirectX that is supported by the cards within the resource pool.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property allows each instance to define a display name in addition to its key properties, identity data, and description information. The [**Name**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement) property of the **CIM\_ManagedSystemElement** class is also defined as a display name, but it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a display name, without inconsistencies. Where [**Name**](msvm-keyboard.md) exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is always set to 5 (OK).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time at which the virtual machine was created. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

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

**Is3dVideoSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether 3-D video is supported by the host system. Contains a nonzero value if 3-D video is supported, or zero otherwise. To support 3-D video, the RemoteFX host must have second level address translation (SLAT) capabilities and have at least one physical GPU that supports RemoteFX.

</dd> <dt>

**IsGPUCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the host has GPUs that support RemoteFX and whether their DirectX versions meet the minimum requirement.

</dd> <dt>

**IsSLATCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

Specifies whether the host has a second level address translation (SLAT) capable CPU.

> [!Note]  
> Deprecated in Windows 10, version 1703 and Windows Server 2016.

 

</dd> <dt>

**MaxConsumableResource**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the maximum amount of consumable resource that the resource pool can present to consumers. This property is different from the **Capacity** property in that it describes the consumers view of the resource, while the **Capacity** property describes the producers view of the resource. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (1024)
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides current status information for the operational condition of the element and can be used for providing more detail with respect to the value of the **EnabledState** property. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)
</dt> <dt>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>**Servicing** (2)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)
</dt> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (4)
</dt> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (5)
</dt> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (6)
</dt> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (7)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (8)
</dt> <dt>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>**Migrating** (9)
</dt> <dt>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>**Emigrating** (10)
</dt> <dt>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>**Immigrating** (11)
</dt> <dt>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>**Snapshotting** (12)
</dt> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (13)
</dt> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (14)
</dt> <dt>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>**Transitioning** (15)
</dt> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (16)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the element. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is always set to 2 (OK). Hyper-V will only ever use the first element of this array.

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and [**ResourceType**](msvm-processorpool.md) is set to 0 ("Other"). This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)), and it is set to **Null**.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This value is referenced by the [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata) instances which were allocated from this pool. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)), and it is always set to "Microsoft:*GUID*\\Root".

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides high level status information. This property should be used in conjunction with the **DetailedStatus** property to provide high level and detailed health status of the element and its subcomponents. A **Null** value indicates that this property is not implemented. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (1)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this resource pool is the base from which resources are drawn and returned in the activity of resource management; otherwise, **False**. Being primordial means that this resource pool cannot be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial resource pools. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**RequiredMinimumDirectXVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MAXLEN**](/windows/desktop/WmiSdk/standard-qualifiers) (1024)
</dt> </dl>

Specifies the lowest version of DirectX that is required by the cards within the resource pool.

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current reservations (in units of **AllocationUnits**) spread across all active allocations from this pool. In a hierarchical configuration, this represents the sum of all descendant resource pool current reservations. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific subtype for this pool. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)).

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of resource this resource pool can allocate. This property is inherited from [**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85)), and it is always set to 4 ("Memory").

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Strings that describe the various [**OperationalStatus**](msvm-bioselement.md) array values. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and it is always set to "OK". Hyper-V will only ever use the first element of this array.

</dd> </dl>

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

[**CIM\_ResourcePool**](cim-resourcepool.md)
</dt> </dl>

 

