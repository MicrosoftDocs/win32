---
title: Msvm\_MemberOfCollection class
description: Represents an association in which a collection aggregates its members.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ea415f28-009f-4146-9ee6-42f96dc5256f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_MemberOfCollection class", "Msvm_MemberOfCollection class, described"]
topic_type:
- apiref
api_name:
- Msvm_MemberOfCollection
- Msvm_MemberOfCollection.Collection
- Msvm_MemberOfCollection.Member
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_MemberOfCollection class

Represents an association in which a collection aggregates its members.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_MemberOfCollection : CIM_MemberOfCollection
{
  CIM_Collection     REF Collection;
  CIM_ManagedElement REF Member;
};
```

## Members

The **Msvm\_MemberOfCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_MemberOfCollection** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Collection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The collection that aggregates members.

This property is inherited from [**CIM\_MemberOfCollection**](cim-memberofcollection.md).

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The member of the collection.

This property is inherited from [**CIM\_MemberOfCollection**](cim-memberofcollection.md).

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

[**CIM\_MemberOfCollection**](cim-memberofcollection.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





