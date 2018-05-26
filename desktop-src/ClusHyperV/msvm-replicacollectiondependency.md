---
title: Msvm\_ReplicaCollectionDependency class
description: An association between an instance of CIM\_CollectionOfMSEs that represents the replica collection and an instance of CIM\_CollectionOfMSEs that represents the test replica collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24b8376f-58e5-4aec-bb84-937d7559a2a7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ReplicaCollectionDependency class
- Msvm_ReplicaCollectionDependency class, described
topic_type:
- apiref
api_name:
- Msvm_ReplicaCollectionDependency
- Msvm_ReplicaCollectionDependency.Antecedent
- Msvm_ReplicaCollectionDependency.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ReplicaCollectionDependency class

An association between an instance of [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) that represents the replica collection and an instance of **CIM\_CollectionOfMSEs** that represents the test replica collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReplicaCollectionDependency : CIM_Dependency
{
  CIM_CollectionOfMSEs REF Antecedent;
  CIM_CollectionOfMSEs REF Dependent;
};
```

## Members

The **Msvm\_ReplicaCollectionDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReplicaCollectionDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

Reference to the instance of the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) class representing the replica collection.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

Reference to the instance of the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) class representing the test replica collection created by the TestReplicaCollection API.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





