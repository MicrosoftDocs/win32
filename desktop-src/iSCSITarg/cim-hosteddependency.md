---
title: CIM\_HostedDependency class
description: HostedDependency defines a ManagedElement in the context of another ManagedElement in which it resides.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e2e37f61-ea4f-4240-82ca-6df8a076da70'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedDependency class iSCSI Software Target API", "CIM_HostedDependency class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_HostedDependency
- CIM_HostedDependency.Antecedent
- CIM_HostedDependency.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_HostedDependency class

HostedDependency defines a ManagedElement in the context of another ManagedElement in which it resides.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Core::CoreElements")]
class CIM_HostedDependency : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **CIM\_HostedDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**CIM\_ManagedElement**](cim-managedelement.md) containing the scoping ManagedElement.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_ManagedElement**](cim-managedelement.md) containing the hosted ManagedElement.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





