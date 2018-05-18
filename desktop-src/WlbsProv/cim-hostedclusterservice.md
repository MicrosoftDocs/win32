---
title: CIM\_HostedClusterService class
description: Defines the hosting cluster for a clustering service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '963b2542-179c-4c0b-b612-eb626003b304'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedClusterService class", "CIM_HostedClusterService class, described"]
topic_type:
- apiref
api_name:
- CIM_HostedClusterService
- CIM_HostedClusterService.Antecedent
- CIM_HostedClusterService.Dependent
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_HostedClusterService class

Defines the hosting cluster for a clustering service. Since this relationship is subclassed from CIM\_HostedService, it inherits the scoping/naming scheme defined for CIM\_Service - where a service is weak to its hosting system. In this case, a clustering service must be weak to its hosting cluster system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class CIM_HostedClusterService : CIM_HostedService
{
  CIM_Cluster           REF Antecedent;
  CIM_ClusteringService REF Dependent;
};
```

## Members

The **CIM\_HostedClusterService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedClusterService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Cluster**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The cluster

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ClusteringService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The service that is hosted on the cluster.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> </dl>

 

 





