---
title: Msvm\_ResourcePool class
description: Describes a type of virtual resource available for use in virtual systems.
ms.assetid: e2194e62-1fa1-400b-bd95-dbc3d392c1e3
keywords:
- Msvm_ResourcePool class Hyper-V
- Msvm_ResourcePool class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ResourcePool
- Msvm_ResourcePool.Caption
- Msvm_ResourcePool.Description
- Msvm_ResourcePool.InstallDate
- Msvm_ResourcePool.Name
- Msvm_ResourcePool.OperationalStatus
- Msvm_ResourcePool.Status
- Msvm_ResourcePool.HealthState
- Msvm_ResourcePool.InstanceID
- Msvm_ResourcePool.PoolID
- Msvm_ResourcePool.Primordial
- Msvm_ResourcePool.Capacity
- Msvm_ResourcePool.Reserved
- Msvm_ResourcePool.ResourceType
- Msvm_ResourcePool.ResourceSubType
- Msvm_ResourcePool.AllocationUnits
- Msvm_ResourcePool.ElementName
- Msvm_ResourcePool.StatusDescriptions
- Msvm_ResourcePool.OtherResourceType
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

# Msvm\_ResourcePool class

Describes a type of virtual resource available for use in virtual systems. The resource pool aggregates physical resources and is used to allocate resources to virtual systems. In Hyper-V, all resource pools are primordial, and there is exactly one pool for each specific type of resource which may be allocated to a virtual machine.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ResourcePool : CIM_ResourcePool
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  string   InstanceID = "Microsoft:GUID\Root";
  string   PoolID = "Microsoft:GUID\Root";
  boolean  Primordial = FALSE;
  uint64   Capacity;
  uint64   Reserved;
  uint16   ResourceType = 4;
  string   ResourceSubType;
  string   AllocationUnits = "Megabyte";
  string   ElementName;
  string   StatusDescriptions[] = { "OK" };
  string   OtherResourceType;
};
```

## Members

The **Msvm\_ResourcePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ResourcePool** class has these properties.

<dl> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the resource pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is set to "Megabyte".

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount (in units of **AllocationUnits**) of active reservations that the resource pool can support. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and its value depends on the type of resource being aggregated.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the [**Name**](https://msdn.microsoft.com/library/aa387898) property of the **CIM\_ManagedSystemElement** class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where [**Name**](msvm-keyboard.md) exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

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

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A unique identifier for this resource pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "Microsoft:*GUID*\\Root".

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current status of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to 2 (OK). Hyper-V will only ever use the first element of this array.

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourcePool**](cim-resourcepool.md).**ResourceType**")
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and [**ResourceType**](msvm-processorpool.md) is set to 0 ("Other"). This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is set to **NULL**.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**PoolId**")
</dt> </dl>

This value is referenced by the [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) instances which were allocated from this pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "Microsoft:*GUID*\\Root".

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, "Primordial" indicates whether this resource pool is the base from which resources are drawn and returned in the activity of resource management. Being primordial means that this resource pool shall not be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial resource pools. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291).

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current reservations (in units of **AllocationUnits**) spread across all active allocations from this pool. In a hierarchical configuration, this represents the sum of all descendant resource pool current reservations. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291).

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this pool. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291).

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
</dt> </dl>

The type of resource this resource pool may allocate. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is set to 4 ("Memory").

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

Strings that describe the various [**OperationalStatus**](msvm-bioselement.md) array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "OK". Hyper-V will only ever use the first element of this array.

</dd> </dl>

## Remarks

Access to the **Msvm\_ResourcePool** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ResourcePool**](cim-resourcepool.md)
</dt> <dt>

[**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291)
</dt> <dt>

[**Msvm\_ResourcePool (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850201)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

 





