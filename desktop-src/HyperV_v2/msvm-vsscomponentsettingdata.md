---
Description: Represents the configured state of the Volume Shadow Copy Service (VSS) service.
ms.assetid: FAE8E8F7-525A-4E5A-91B3-B73343337352
title: Msvm\_VssComponentSettingData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_VssComponentSettingData class

Represents the configured state of the Volume Shadow Copy Service (VSS) service.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VssComponentSettingData : CIM_ResourceAllocationSettingData
{
  string  InstanceID;
  string  Caption = "VSS";
  string  Description = "Microsoft VSS Service Setting Data";
  string  ElementName = "VSS";
  uint16  ResourceType = 1;
  string  OtherResourceType = "Microsoft:Hyper-V:VSS Component";
  string  ResourceSubType;
  string  PoolID;
  uint16  ConsumerVisibility = 3;
  string  HostResource;
  string  AllocationUnits = "count";
  uint64  VirtualQuantity = 1;
  uint64  Reservation = 1;
  uint64  Limit = 1;
  uint32  Weight = 0;
  boolean AutomaticAllocation = True;
  boolean AutomaticDeallocation = True;
  string  Parent;
  string  Connection[];
  string  Address;
  uint16  MappingBehavior;
  string  AddressOnParent;
  string  VirtualQuantityUnits = "count";
  uint16  EnabledState = 2;
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
</dt> </dl>

The address of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**AddressOnParent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the address of this resource in the context of the parent. The **Parent** and **AddressOnParent** properties are used to describe the controller relationship as well as the ordering of devices on a controller. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**AllocationUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The units of allocation used by the **Reservation** and **Limit** properties. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**AutomaticAllocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**AutomaticDeallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the resource will be automatically de-allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**Connection**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The thing to which this resource is connected. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**ConsumerVisibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The consumers visibility to the allocated resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).



| Value                                                                        | Meaning                |
|------------------------------------------------------------------------------|------------------------|
| <dl> <dt>3</dt> </dl> | Virtualized<br/> |



 

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The enabled and disabled states of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/cc136818) and has a default value of 2 (Enabled).

This is a read-only property, but it can be changed by using the [**ModifyResourceSettings**](modifyresourcesettings-msvm-virtualsystemmanagementservice.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

<dt>



 (2)


</dt> <dd>

Enabled

</dd> <dt>

3
</dt> <dd>

Disabled

</dd> </dl>

</dd> <dt>

**HostResource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Exposes a specific assignment to host or underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **Null**.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The upper bound, or maximum amount of resource that will be granted for this allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**MappingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how this resource maps to underlying resources. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**OtherResourceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the resource type when a well-defined value is not available and **ResourceType** has the value 1 (Other). This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent of the resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the resource pool from which the resource is allocated. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Reservation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of resource guaranteed to be available for this allocation. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**ResourceSubType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes an implementation specific sub-type for this resource. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to **Null**.

</dd> <dt>

**ResourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of resource this allocation setting represents. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) and is always set to 1 (Other).



| Value                                                                        | Meaning          |
|------------------------------------------------------------------------------|------------------|
| <dl> <dt>1</dt> </dl> | Other<br/> |



 

</dd> <dt>

**VirtualQuantity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The quantity of resources presented to the consumer. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**VirtualQuantityUnits**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unit of measurement for this resource allocation. The value of this property is a legal value of the Programmatic Units qualifier as defined in Annex C.1 of DSP0004 V2.5 or later. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A relative priority for this allocation in relation to other allocations from the same resource pool. This property is inherited from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).

</dd> </dl>

## Remarks

Access to the **Msvm\_VssComponentSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dt>

[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)
</dt> </dl>

 

 




