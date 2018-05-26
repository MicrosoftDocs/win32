---
title: Msvm\_ClusterV2ElementConformsToProfile class
description: Defines the registered profile to which the referenced computer system conforms.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c824b9c2-229b-491d-8762-9efc7a1e0a3d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ClusterV2ElementConformsToProfile class
- Msvm_ClusterV2ElementConformsToProfile class, described
topic_type:
- apiref
api_name:
- Msvm_ClusterV2ElementConformsToProfile
- Msvm_ClusterV2ElementConformsToProfile.ConformantStandard
- Msvm_ClusterV2ElementConformsToProfile.ManagedElement
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ClusterV2ElementConformsToProfile class

Defines the registered profile to which the referenced computer system conforms.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class Msvm_ClusterV2ElementConformsToProfile : Msvm_ElementConformsToProfile
{
  Msvm_RegisteredProfile REF ConformantStandard = $SVP;
  Msvm_ComputerSystem    REF ManagedElement;
};
```

## Members

The **Msvm\_ClusterV2ElementConformsToProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ClusterV2ElementConformsToProfile** class has these properties.

<dl> <dt>

**ConformantStandard**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_RegisteredProfile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A reference to the registered profile.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650), **MSFT\_TargetNamespace** ("root\\\\HyperVCluster\\\\v2")
</dt> </dl>

A reference to the computer system that conforms to the registered profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\interop<br/>                                                                               |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_ElementConformsToProfile**](msvm-elementconformstoprofile.md)
</dt> </dl>

 

 





