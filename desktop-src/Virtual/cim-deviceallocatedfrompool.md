---
title: CIM\_DeviceAllocatedFromPool class
description: AllocatedFromStoragePool is an association describing how LogicalElements are allocated from underlying StoragePools. These elements typically would be subclasses of StorageExtents or StoragePools.
ms.assetid: 6a6e6989-f257-4207-95c0-4f3c4db4f019
keywords:
- CIM_DeviceAllocatedFromPool class Hyper-V
- CIM_DeviceAllocatedFromPool class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_DeviceAllocatedFromPool
- CIM_DeviceAllocatedFromPool.Dependent
- CIM_DeviceAllocatedFromPool.Antecedent
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

# CIM\_DeviceAllocatedFromPool class

AllocatedFromStoragePool is an association describing how LogicalElements are allocated from underlying StoragePools. These elements typically would be subclasses of StorageExtents or StoragePools.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Association]
class CIM_DeviceAllocatedFromPool : CIM_Dependency
{
  CIM_LogicalDevice REF Dependent;
  CIM_ResourcePool  REF Antecedent;
};
```

## Members

The **CIM\_DeviceAllocatedFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DeviceAllocatedFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The dependent object in this association.

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

 

 





