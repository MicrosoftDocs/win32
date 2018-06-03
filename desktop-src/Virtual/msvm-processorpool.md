---
title: Msvm\_ProcessorPool class
description: Aggregates the processor resources that may be allocated to a virtual system.
ms.assetid: eda54edc-2ecc-4ec9-93c1-25d7a6acf09a
keywords:
- Msvm_ProcessorPool class Hyper-V
- Msvm_ProcessorPool class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ProcessorPool
- Msvm_ProcessorPool.Caption
- Msvm_ProcessorPool.Description
- Msvm_ProcessorPool.InstallDate
- Msvm_ProcessorPool.Name
- Msvm_ProcessorPool.OperationalStatus
- Msvm_ProcessorPool.Status
- Msvm_ProcessorPool.HealthState
- Msvm_ProcessorPool.InstanceID
- Msvm_ProcessorPool.Primordial
- Msvm_ProcessorPool.Capacity
- Msvm_ProcessorPool.Reserved
- Msvm_ProcessorPool.ResourceType
- Msvm_ProcessorPool.OtherResourceType
- Msvm_ProcessorPool.ResourceSubType
- Msvm_ProcessorPool.AllocationUnits
- Msvm_ProcessorPool.ElementName
- Msvm_ProcessorPool.StatusDescriptions
- Msvm_ProcessorPool.PoolID
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

# Msvm\_ProcessorPool class

Aggregates the processor resources that may be allocated to a virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ProcessorPool : CIM_ResourcePool
{
  string   Caption = "Processor Resource Pool";
  string   Description = "Resource Pool used to allocate Microsoft Virtual Processor Pool resources to a virtual machine";
  datetime InstallDate;
  string   Name = "Processor Resource Pool";
  uint16   OperationalStatus[] = 2;
  string   Status;
  uint16   HealthState = 5;
  string   InstanceID = "Microsoft:GUID\Root";
  boolean  Primordial = FALSE;
  uint64   Capacity = 100000;
  uint64   Reserved = 0;
  uint16   ResourceType = 3;
  string   OtherResourceType;
  string   ResourceSubType = "Microsoft Processor";
  string   AllocationUnits = "Processor Cores";
  string   ElementName = "Processor Resource Pool";
  string   StatusDescriptions[] = { "OK" };
  string   PoolID = "GUID";
};
```

## Members

The **Msvm\_ProcessorPool** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_ProcessorPool** class has these methods.



| Method                                                                          | Description                                                                                                                                                             |
|:--------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CalculatePossibleReserve**](calculatepossiblereserve-msvm-processorpool.md) | Used to find the actual processor reserve.<br/> **Windows Server 2008:** Before Windows Server 2008 R2, this method does nothing and always returns 0.<br/> |



 

### Properties

The **Msvm\_ProcessorPool** class has these properties.

<dl> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the resource pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "Processor Cores".

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount (in units of **AllocationUnits**) of reservations that the resource pool can support. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to 100000.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Processor Resource Pool".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Resource Pool used to allocate Microsoft Virtual Processor Pool resources to a virtual machine".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the [**Name**](https://msdn.microsoft.com/library/aa387898) property of the **CIM\_ManagedSystemElement** class is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where [**Name**](msvm-keyboard.md) exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and it is always set to "Processor Resource Pool".

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

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and it is always set to "Processor Resource Pool".

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

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourcePool**](cim-resourcepool.md).**ResourceType**")
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and **ResourceType** is set to 0 (Other). This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to **NULL**.

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**PoolId**")
</dt> </dl>

This value is referenced by the [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) instances which were allocated from this pool. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "*GUID*".

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this resource pool is the base from which resources are drawn and returned in the activity of resource management. Being primordial means that this resource pool shall not be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial resource pools. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291).

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current reservations (in units of **AllocationUnits**) spread across all active allocations from this pool. In a hierarchical configuration, this represents the sum of all descendant resource pool current reservations. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to 0.

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this pool. For example, this may be used to distinguish different models of the same resource type. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to "Microsoft Processor".

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md).**OtherResourceType**")
</dt> </dl>

The type of resource this resource pool may allocate. This property is inherited from [**CIM\_ResourcePool**](https://msdn.microsoft.com/library/mt432291) and it is always set to 3 (CPU).

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

</dd> </dl>

## Remarks

Access to the **Msvm\_ProcessorPool** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[Processor Classes](processor-classes.md)
</dt> </dl>

 

 





