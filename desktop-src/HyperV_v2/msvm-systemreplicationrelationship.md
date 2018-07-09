---
Description: Represents an association between an instance of Msvm\_ComputerSystem that represents the virtual machine and an instance of Msvm\_ReplicationRelationship that represents a replication relationship of the virtual machine.
ms.assetid: 23E7BF91-9527-434C-A571-05879E83950E
title: Msvm\_SystemReplicationRelationship class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SystemReplicationRelationship
- Msvm_SystemReplicationRelationship.Antecedent
- Msvm_SystemReplicationRelationship.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SystemReplicationRelationship class

Represents an association between an instance of [**Msvm\_ComputerSystem**](msvm-computersystem.md) that represents the virtual machine and an instance of [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) that represents a replication relationship of the virtual machine. This class derives from the [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemReplicationRelationship : CIM_Dependency
{
  Msvm_ComputerSystem          REF Antecedent;
  Msvm_ReplicationRelationship REF Dependent;
};
```

## Members

The **Msvm\_SystemReplicationRelationship** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SystemReplicationRelationship** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Antecedent")
</dt> </dl>

Reference to the instance of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represents the virtual machine.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ReplicationRelationship**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Dependency.Dependent")
</dt> </dl>

Reference to the instance of the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class that represents the replication relationship of a virtual system.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238)
</dt> </dl>

 

 




