---
title: Msvm\_RecoveryPointOfVirtualSystemCollection class
description: Associates the Msvm\_CollectionRecoveryPoint to the corresponding Msvm\_VirtualSystemCollection objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73d1e9b9-a23c-4720-8172-a4d71acb3f78
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_RecoveryPointOfVirtualSystemCollection class
- Msvm_RecoveryPointOfVirtualSystemCollection class, described
topic_type:
- apiref
api_name:
- Msvm_RecoveryPointOfVirtualSystemCollection
- Msvm_RecoveryPointOfVirtualSystemCollection.Antecedent
- Msvm_RecoveryPointOfVirtualSystemCollection.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_RecoveryPointOfVirtualSystemCollection class

Associates the [**Msvm\_CollectionRecoveryPoint**](msvm-collectionrecoverypoint.md) to the corresponding [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_RecoveryPointOfVirtualSystemCollection : CIM_Dependency
{
  CIM_CollectionOfMSEs REF Antecedent;
  CIM_Collection       REF Dependent;
};
```

## Members

The **Msvm\_RecoveryPointOfVirtualSystemCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_RecoveryPointOfVirtualSystemCollection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

Antecedent [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) representing the independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Collection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

Dependent [**CIM\_Collection**](cim-collection.md) representing the object that is dependent on the *Antecedent*.

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

 

 





