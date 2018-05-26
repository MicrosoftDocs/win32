---
title: CIM\_ResourceAllocationFromPool class
description: Represents an association in which a CIM\_ResourceAllocationSettingData instance is allocated from a resource pool.
ms.assetid: 326c28af-78cb-417b-bee8-a87e06bcb598
keywords:
- CIM_ResourceAllocationFromPool class Hyper-V
- CIM_ResourceAllocationFromPool class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_ResourceAllocationFromPool
- CIM_ResourceAllocationFromPool.Antecedent
- CIM_ResourceAllocationFromPool.Dependent
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ResourceAllocationFromPool class

Represents an association in which a [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instance is allocated from a resource pool.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Experimental, Association, Version("2.13.0"), AMENDMENT]
class CIM_ResourceAllocationFromPool : CIM_Dependency
{
  CIM_ResourcePool                  REF Antecedent;
  CIM_ResourceAllocationSettingData REF Dependent;
};
```

## Members

The **CIM\_ResourceAllocationFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ResourceAllocationFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The resource pool.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The resource allocation data.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





