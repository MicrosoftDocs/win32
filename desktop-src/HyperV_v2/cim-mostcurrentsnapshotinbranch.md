---
Description: Represents an association between a virtual system and the most current snapshot of the system. This association can only exist if the virtual system was create using a snapshot or if a snapshot was created from the virtual system.
ms.assetid: e6040818-84cf-4cec-ab7b-a733fe5d01d2
title: CIM_MostCurrentSnapshotInBranch class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MostCurrentSnapshotInBranch
- CIM_MostCurrentSnapshotInBranch.Antecedent
- CIM_MostCurrentSnapshotInBranch.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_MostCurrentSnapshotInBranch class

Represents an association between a virtual system and the most current snapshot of the system. This association can only exist if the virtual system was create using a snapshot or if a snapshot was created from the virtual system.

## Syntax

``` syntax
[Association, Experimental, Version("2.16.0"), AMENDMENT]
class CIM_MostCurrentSnapshotInBranch : CIM_Dependency
{
  CIM_ComputerSystem           REF Antecedent;
  CIM_VirtualSystemSettingData REF Dependent;
};
```

## Members

The **CIM\_MostCurrentSnapshotInBranch** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MostCurrentSnapshotInBranch** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the instance of [**CIM\_ComputerSystem**](cim-computersystem.md) that represents the virtual system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the instance of [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that represents the virtual system snapshot.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




