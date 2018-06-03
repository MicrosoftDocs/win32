---
title: MSCluster\_ValidationStatus class
description: Provides methods for generating the validation report file name as well as retrieving the result of the cluster or node validation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 878C4E2C-0060-4663-9350-9B663C445535
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ValidationStatus class
- MSCluster_ValidationStatus class, described
topic_type:
- apiref
api_name:
- MSCluster_ValidationStatus
- MSCluster_ValidationStatus.Id
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ValidationStatus class

Provides methods for generating the validation report file name as well as retrieving the result of the cluster or node validation.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{6071D542-A431-4B9C-B94B-61BEA8707DE7}"), AMENDMENT]
class MSCluster_ValidationStatus
{
  string Id;
};
```

## Members

The **MSCluster\_ValidationStatus** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ValidationStatus** class has these methods.



| Method                                                                              | Description                                                           |
|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**GetNodeStatus**](mscluster-validationstatus-getnodestatus.md)                   | Gets the validation status of the nodes not yet clustered.<br/> |
| [**GetStatus**](mscluster-validationstatus-getstatus.md)                           | Gets the status of the cluster validation.<br/>                 |
| [**IsValidationSuccessful**](mscluster-validationstatus-isvalidationsuccessful.md) | Indicates whether validation has succeeded.<br/>                |



 

### Properties

The **MSCluster\_ValidationStatus** class has these properties.

<dl> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The id of the validation Status.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





