---
title: Msvm\_ElementConformsToProfile class
description: Defines the registered profile to which the referenced computer system conforms.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6b614bd0-9509-4187-84d1-ce108ccb6022
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ElementConformsToProfile class
- Msvm_ElementConformsToProfile class, described
topic_type:
- apiref
api_name:
- Msvm_ElementConformsToProfile
- Msvm_ElementConformsToProfile.ConformantStandard
- Msvm_ElementConformsToProfile.ManagedElement
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ElementConformsToProfile class

Defines the registered profile to which the referenced computer system conforms.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class Msvm_ElementConformsToProfile : CIM_ElementConformsToProfile
{
  Msvm_RegisteredProfile REF ConformantStandard;
  Msvm_ComputerSystem    REF ManagedElement;
};
```

## Members

The **Msvm\_ElementConformsToProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementConformsToProfile** class has these properties.

<dl> <dt>

**ConformantStandard**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_RegisteredProfile**](msvm-registeredprofile.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A reference to the registered profile.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A reference to the computer system that conforms to the registered profile.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ElementConformsToProfile**](https://msdn.microsoft.com/library/mt130382)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





