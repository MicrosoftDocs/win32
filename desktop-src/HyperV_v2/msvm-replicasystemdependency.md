---
Description: Represents an association between an instance of the CIM\_ComputerSystem class that represents the virtual machine replica and an instance of the CIM\_ComputerSystem class that represents the test virtual machine replica.
ms.assetid: c3216ddd-7f70-4287-9f7e-1fd7a60b1a0a
title: Msvm\_ReplicaSystemDependency class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicaSystemDependency
- Msvm_ReplicaSystemDependency.Antecedent
- Msvm_ReplicaSystemDependency.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ReplicaSystemDependency class

Represents an association between an instance of the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) class that represents the virtual machine replica and an instance of the **CIM\_ComputerSystem** class that represents the test virtual machine replica.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReplicaSystemDependency : CIM_Dependency
{
  CIM_ComputerSystem REF Antecedent;
  CIM_ComputerSystem REF Dependent;
};
```

## Members

The **Msvm\_ReplicaSystemDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReplicaSystemDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Antecedent")
</dt> </dl>

A reference to an instance of the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) class that represents the virtual machine replica. This property is inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Dependent")
</dt> </dl>

A reference to an instance of the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) class that represents the test virtual machine replica created by the [**Msvm\_ReplicationService.TestReplicaSystem**](testreplicasystem-msvm-replicationservice.md) method. This property is inherited from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




