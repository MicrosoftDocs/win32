---
title: Msvm\_HostedDependency class
description: Associates a virtual computer system instance with the computer system object that represents the physical hosting system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c94d1628-4ad3-436c-ab43-a0861c2e5fb6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_HostedDependency class
- Msvm_HostedDependency class, described
topic_type:
- apiref
api_name:
- Msvm_HostedDependency
- Msvm_HostedDependency.Antecedent
- Msvm_HostedDependency.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_HostedDependency class

Associates a virtual computer system instance with the computer system object that represents the physical hosting system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_HostedDependency : CIM_HostedDependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **Msvm\_HostedDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_HostedDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The host managed element.

This property is inherited from [**CIM\_HostedDependency**](cim-hosteddependency.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hosted managed element.

This property is inherited from [**CIM\_HostedDependency**](cim-hosteddependency.md).

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





