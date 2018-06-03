---
title: Msvm\_ResourceAllocationFromPool class
description: Associates an instance of a resource allocation with the resource pool from which it is allocated.
ms.assetid: 4273743d-ef56-4a51-a2b9-2562689783fa
keywords:
- Msvm_ResourceAllocationFromPool class Hyper-V
- Msvm_ResourceAllocationFromPool class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ResourceAllocationFromPool
- Msvm_ResourceAllocationFromPool.Antecedent
- Msvm_ResourceAllocationFromPool.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_ResourceAllocationFromPool class

Associates an instance of a resource allocation with the resource pool from which it is allocated.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ResourceAllocationFromPool : CIM_ResourceAllocationFromPool
{
  CIM_ResourcePool                  REF Antecedent;
  CIM_ResourceAllocationSettingData REF Dependent;
};
```

## Members

The **Msvm\_ResourceAllocationFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ResourceAllocationFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The resource pool.

This property is inherited from [**CIM\_ResourceAllocationFromPool**](cim-resourceallocationfrompool.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource allocation data.

This property is inherited from [**CIM\_ResourceAllocationFromPool**](cim-resourceallocationfrompool.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ResourceAllocationFromPool** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationFromPool**](cim-resourceallocationfrompool.md)
</dt> <dt>

[**CIM\_ResourceAllocationFromPool**](https://msdn.microsoft.com/library/mt146213)
</dt> <dt>

[**Msvm\_ResourceAllocationFromPool (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850199)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

 





