---
title: CIM\_BasedOn class
description: Represents an association between a higher level CIM\_StorageExtent object and a lower level CIM\_StorageExtent object. For example a CIM\_ProtectedSpaceExtent object is a part of a CIM\_PhysicalExtent object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a7318f5f-8fb3-4e59-af96-805d0ff8f04e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_BasedOn class", "CIM_BasedOn class, described"]
topic_type:
- apiref
api_name:
- CIM_BasedOn
- CIM_BasedOn.Antecedent
- CIM_BasedOn.Dependent
- CIM_BasedOn.StartingAddress
- CIM_BasedOn.EndingAddress
- CIM_BasedOn.OrderIndex
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_BasedOn class

Represents an association between a higher level **CIM\_StorageExtent** object and a lower level **CIM\_StorageExtent** object. For example a [**CIM\_ProtectedSpaceExtent**](https://msdn.microsoft.com/library/aa387988) object is a part of a [**CIM\_PhysicalExtent**](https://msdn.microsoft.com/library/aa387964) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Core::StorageExtent")]
class CIM_BasedOn : CIM_Dependency
{
  CIM_StorageExtent REF Antecedent;
  CIM_StorageExtent REF Dependent;
  uint64                StartingAddress;
  uint64                EndingAddress;
  uint16                OrderIndex;
};
```

## Members

The **CIM\_BasedOn** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BasedOn** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_StorageExtent**](cim-storageextent.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The lower level **CIM\_StorageExtent** object.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_StorageExtent**](cim-storageextent.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The higher level **CIM\_StorageExtent** object.

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address that indicates where in lower level storage, the higher level **CIM\_StorageExtent** object ends. This property is useful when mapping non-contiguous **CIM\_StorageExtent** objects into a higher level grouping.

</dd> <dt>

**OrderIndex**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An index that is used to specify the order of **CIM\_BasedOn** associations in a collection; otherwise "0" indicates no order. **CIM\_BasedOn** instances with the same dependent value should place unique values in the **OrderIndex** property. The lowest **OrderIndex** value specifies the first member of the collection.

An example of the use of this property is to define a RAID-0 striped array of 3 disks. The resultant RAID array is a storage extent that is dependent on the storage extents that describe each of the 3 disks. The **OrderIndex** value of each **CIM\_BasedOn** association from the disk extents to the RAID array could be specified as 1, 2, and 3 to indicate the order in which the disk extents are used to access the RAID data.

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address that indicates where in lower level storage, the higher level **CIM\_StorageExtent** object begins.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





