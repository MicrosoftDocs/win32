---
title: CIM\_CollectedMSEs class
description: Represents a generic association between a collection of managed system elements and the members of the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 46542da5-f3b1-48c4-be0a-b14d8f142c7c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_CollectedMSEs class
- CIM_CollectedMSEs class, described
topic_type:
- apiref
api_name:
- CIM_CollectedMSEs
- CIM_CollectedMSEs.Collection
- CIM_CollectedMSEs.Member
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_CollectedMSEs class

Represents a generic association between a collection of managed system elements and the members of the collection.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Core::Collection"), AMENDMENT]
class CIM_CollectedMSEs : CIM_MemberOfCollection
{
  CIM_CollectionOfMSEs     REF Collection;
  CIM_ManagedSystemElement REF Member;
};
```

## Members

The **CIM\_CollectedMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectedMSEs** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_CollectionOfMSEs**](cim-collectionofmses.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Collection")
</dt> </dl>

The collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Member")
</dt> </dl>

The members of the collection.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_MemberOfCollection**](cim-memberofcollection.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





