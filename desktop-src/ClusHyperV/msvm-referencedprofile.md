---
title: Msvm\_ReferencedProfile class
description: Used to associate an instance CIM\_RegisteredProfile with an instance of CIM\_RegisteredProfile of another profile that references the dependent profile as a related profile.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a149e8df-5b7d-4b18-89e6-1b49b6a49b7c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ReferencedProfile class
- Msvm_ReferencedProfile class, described
topic_type:
- apiref
api_name:
- Msvm_ReferencedProfile
- Msvm_ReferencedProfile.Antecedent
- Msvm_ReferencedProfile.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ReferencedProfile class

Used to associate an instance [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) with an instance of **CIM\_RegisteredProfile** of another profile that references the dependent profile as a related profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class Msvm_ReferencedProfile : CIM_ReferencedProfile
{
  CIM_RegisteredProfile REF Antecedent;
  CIM_RegisteredProfile REF Dependent;
};
```

## Members

The **Msvm\_ReferencedProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReferencedProfile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) instance that is referenced by the **Dependent** profile.

This property is inherited from [**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) instance that references other profiles.

This property is inherited from [**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\Interop<br/>                                                                               |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ReferencedProfile**](https://msdn.microsoft.com/library/ee309374)
</dt> </dl>

 

 





