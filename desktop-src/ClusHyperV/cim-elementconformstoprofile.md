---
title: CIM\_ElementConformsToProfile class
description: Represents an association in which a managed element conforms to the standard of a registered profile.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '05cc1b0f-db2c-406e-9a9e-a6712cf52e43'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ElementConformsToProfile class", "CIM_ElementConformsToProfile class, described"]
topic_type:
- apiref
api_name:
- CIM_ElementConformsToProfile
- CIM_ElementConformsToProfile.ConformantStandard
- CIM_ElementConformsToProfile.ManagedElement
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_ElementConformsToProfile class

Represents an association in which a managed element conforms to the standard of a registered profile. This association usually applies to a higher level instance, such as a system, namespace, or service. When applied to a higher level instance, all constituent parts MUST behave appropriately in support of the ManagedElement's conformance to the named RegisteredProfile.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Interop")]
class CIM_ElementConformsToProfile
{
  CIM_RegisteredProfile REF ConformantStandard;
  CIM_ManagedElement    REF ManagedElement;
};
```

## Members

The **CIM\_ElementConformsToProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementConformsToProfile** class has these properties.

<dl> <dt>

**ConformantStandard**
</dt> <dd> <dl> <dt>

Data type: **CIM\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The registered profile to which the managed element conforms.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The managed element that conforms to the registered profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





