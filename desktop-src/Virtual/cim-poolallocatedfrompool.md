---
title: CIM\_PoolAllocatedFromPool class
description: TBD
ms.assetid: '7d422abc-8db1-49e8-830c-382d0b71ae1d'
keywords: ["CIM_PoolAllocatedFromPool class Hyper-V", "CIM_PoolAllocatedFromPool class Hyper-V , described"]
---

# CIM\_PoolAllocatedFromPool class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Experimental, Association, Version("2.13.0")]
class CIM_PoolAllocatedFromPool : CIM_Dependency
{
  CIM_ResourcePool REF Dependent;
  CIM_ResourcePool REF Antecedent;
};
```

## Members

The **CIM\_PoolAllocatedFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PoolAllocatedFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

TBD

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





