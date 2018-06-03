---
title: CIM\_NamespaceInManager class
description: NamespaceInManager is an association describing the Namespaces hosted by a CIM ObjectManager.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d75d84e-f36c-42fa-92da-2d50ab5d9a3d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_NamespaceInManager class iSCSI Software Target API
- CIM_NamespaceInManager class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_NamespaceInManager
- CIM_NamespaceInManager.Antecedent
- CIM_NamespaceInManager.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_NamespaceInManager class

NamespaceInManager is an association describing the Namespaces hosted by a CIM ObjectManager.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.7.0"), UMLPackagePath("CIM::Interop")]
class CIM_NamespaceInManager : CIM_HostedDependency
{
  CIM_ObjectManager REF Antecedent;
  CIM_Namespace     REF Dependent;
};
```

## Members

The **CIM\_NamespaceInManager** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_NamespaceInManager** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ObjectManager**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The ObjectManager containing a Namespace.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The Namespace in an ObjectManager.

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> </dl>

 

 





