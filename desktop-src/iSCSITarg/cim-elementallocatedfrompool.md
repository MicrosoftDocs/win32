---
title: CIM\_ElementAllocatedFromPool class
description: ElementAllocatedFromPool associates an instance of CIM\_LogicalElement representing an allocated Resource with the CIM\_ResourcePool from which it was allocated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6b125e1-64a6-40d9-9de6-b9acf89860a9
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ElementAllocatedFromPool class iSCSI Software Target API
- CIM_ElementAllocatedFromPool class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_ElementAllocatedFromPool
- CIM_ElementAllocatedFromPool.Antecedent
- CIM_ElementAllocatedFromPool.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ElementAllocatedFromPool class

ElementAllocatedFromPool associates an instance of CIM\_LogicalElement representing an allocated Resource with the CIM\_ResourcePool from which it was allocated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Experimental, Version("2.15.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_ElementAllocatedFromPool : CIM_Dependency
{
  CIM_ResourcePool   REF Antecedent;
  CIM_LogicalElement REF Dependent;
};
```

## Members

The **CIM\_ElementAllocatedFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementAllocatedFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**CIM\_ResourcePool**](cim-resourcepool.md) containing the resource pool.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_LogicalElement**](cim-logicalelement.md) containing the allocated resource.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





