---
title: Msvm\_ElementAllocatedFromPool class
description: Associates an instance of an allocated resource with the resource pool from which it was allocated.
ms.assetid: c729bda9-20a5-4adb-a4d7-adab808a249b
keywords:
- Msvm_ElementAllocatedFromPool class Hyper-V
- Msvm_ElementAllocatedFromPool class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ElementAllocatedFromPool
- Msvm_ElementAllocatedFromPool.Antecedent
- Msvm_ElementAllocatedFromPool.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ElementAllocatedFromPool class

Associates an instance of an allocated resource with the resource pool from which it was allocated.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementAllocatedFromPool : CIM_ElementAllocatedFromPool
{
  CIM_ResourcePool   REF Antecedent;
  CIM_LogicalElement REF Dependent;
};
```

## Members

The **Msvm\_ElementAllocatedFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementAllocatedFromPool** class has these properties.

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

This property is inherited from [**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The allocated resource.

This property is inherited from [**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementAllocatedFromPool** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md)
</dt> <dt>

[**CIM\_ElementAllocatedFromPool**](https://msdn.microsoft.com/library/mt446042)
</dt> <dt>

[**Msvm\_ElementAllocatedFromPool (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850128)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

 





