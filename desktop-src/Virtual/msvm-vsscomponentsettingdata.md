---
title: Msvm\_VssComponentSettingData class
description: Represents the configured state of the Volume Shadow Copy Service (VSS) service.
ms.assetid: 'bf6ee020-69de-4240-9e2a-b6bca684a108'
keywords: ["Msvm_VssComponentSettingData class Hyper-V", "Msvm_VssComponentSettingData class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VssComponentSettingData
- Msvm_VssComponentSettingData.Caption
- Msvm_VssComponentSettingData.Description
- Msvm_VssComponentSettingData.InstanceID
- Msvm_VssComponentSettingData.ElementName
- Msvm_VssComponentSettingData.ResourceType
- Msvm_VssComponentSettingData.OtherResourceType
- Msvm_VssComponentSettingData.PoolID
- Msvm_VssComponentSettingData.ConsumerVisibility
- Msvm_VssComponentSettingData.HostResource
- Msvm_VssComponentSettingData.AllocationUnits
- Msvm_VssComponentSettingData.VirtualQuantity
- Msvm_VssComponentSettingData.Reservation
- Msvm_VssComponentSettingData.AutomaticAllocation
- Msvm_VssComponentSettingData.AutomaticDeallocation
- Msvm_VssComponentSettingData.Parent
- Msvm_VssComponentSettingData.Connection
- Msvm_VssComponentSettingData.Address
- Msvm_VssComponentSettingData.MappingBehavior
- Msvm_VssComponentSettingData.EnabledState
- Msvm_VssComponentSettingData.ResourceSubType
- Msvm_VssComponentSettingData.Limit
- Msvm_VssComponentSettingData.Weight
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VssComponentSettingData class

Represents the configured state of the Volume Shadow Copy Service (VSS) service.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VssComponentSettingData : CIM_ResourceAllocationSettingData
{
  string  Caption = "VSS";
  string  Description = "Microsoft VSS Service Setting Data";
  string  InstanceID = "Microsoft:GUID\device-specific data";
  string  ElementName = "VSS";
  uint16  ResourceType = 1;
  string  OtherResourceType = "Microsoft VSS Component";
  string  PoolID;
  uint16  ConsumerVisibility = 3;
  string  HostResource[];
  string  AllocationUnits = "Integration Components";
  uint64  VirtualQuantity = 1;
  uint64  Reservation = 1;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  uint16  EnabledState = 2;
  string  ResourceSubType;
  uint64  Limit = 1;
  uint32  Weight = 0;
};
```

## Members

The **Msvm\_VssComponentSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VssComponentSettingData** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The address of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to "Integration Components".

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Indicates whether the resource will be automatically allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **True**.

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Indicates whether the resource will be automatically de-allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **True**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one- line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "VSS".

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The thing to which this resource is connected. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The consumers visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 3 (Virtualized).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "Microsoft VSS Service Setting Data".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and it is set to "VSS". Changing this property will change the element name of the associated logical device derivative.

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and has a default value of 2 (Enabled).

This is a read-only property, but it can be changed using the [**ModifyVirtualSystemResources**](modifyvirtualsystemresources-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>



 (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("CIM\_LogicalDevice")
</dt> </dl>

Exposes specific assignment to host or underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) and is always set to "Microsoft:*GUID*\\*device-specific data*".

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The upper bound, or maximum amount of resource that will be granted for this allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 1.

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Indicates how this resource maps to underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**ResourceType**")
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value 1 (Other). This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to "Microsoft VSS Component".

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The parent of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourcePool**](cim-resourcepool.md).**PoolId**")
</dt> </dl>

The ID of the resource pool from which the resource is allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The amount of resource guaranteed to be available for this allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 1.

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **NULL**.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
</dt> </dl>

The type of resource this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 1 (Other).

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The quantity of resources presented to the consumer. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 1.

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A relative priority for this allocation in relation to other allocations from the same resource pool. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 0.

</dd> </dl>

## Remarks

Access to the **Msvm\_VssComponentSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)
</dt> <dt>

[Integration Services Classes](integration-components-classes.md)
</dt> </dl>

 

 





