---
title: MSCluster\_NodeToHostedService class
description: A dynamic association WMI class that represents a service managed by the cluster as a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a05af1a3-e500-4333-a32c-30db54321c95'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_NodeToHostedService class", "MSCluster_NodeToHostedService class, described"]
topic_type:
- apiref
api_name:
- MSCluster_NodeToHostedService
- MSCluster_NodeToHostedService.Antecedent
- MSCluster_NodeToHostedService.Dependent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_NodeToHostedService class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a service managed by the [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) as a [resource](https://msdn.microsoft.com/library/aa372152).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{B3C77CEF-67E7-4112-A757-CB072D44EBA3}"), AMENDMENT]
class MSCluster_NodeToHostedService : CIM_HostedService
{
  MSCluster_Node    REF Antecedent;
  MSCluster_Service REF Dependent;
};
```

## Members

The **MSCluster\_NodeToHostedService** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_NodeToHostedService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The node hosting the service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The hosted service.

</dd> </dl>

## Remarks

The **MSCluster\_NodeToHostedService** class is derived from the **CIM\_HostedService** class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





