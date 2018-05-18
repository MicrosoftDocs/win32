---
title: MSCluster\_ClusterService class
description: Service class for the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c8510b8d-3d19-4e48-a5ae-52250cbb60fc'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterService class", "MSCluster_ClusterService class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterService
- MSCluster_ClusterService.ElementName
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterService class

Service class for the cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("MSCLUSTEREXT"), AMENDMENT]
class MSCluster_ClusterService
{
  string ElementName;
};
```

## Members

The **MSCluster\_ClusterService** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ClusterService** class has these methods.



| Method                                                                                | Description                                                                  |
|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**AddHealthProviders**](mscluster-clusterservice-addhealthproviders.md)             | Add health providers to health service<br/>                            |
| [**ClusterIsReadyForUpgrade**](clusterisreadyforupgrade-mscluster-clusterservice.md) | Determines whether the cluster's functional level can be updated.<br/> |
| [**CreateCloudWitness**](mscluster-clusterservice-createcloudwitness.md)             | Creates a cloud witness quorum resource in the cluster<br/>            |
| [**CreateVmReservation**](mscluster-clusterservice-createvmreservation.md)           | Reserves a virtual machine in the cluster.<br/>                        |
| [**DisableHealth**](mscluster-clusterservice-disablehealth.md)                       | Disables the health service in the cluster.<br/>                       |
| [**EnableHealth**](enablehealth-mscluster-clusterservice.md)                         | Enables the health service in the cluster.<br/>                        |
| [**GetPlacementScore**](mscluster-clusterservice-getplacementscore.md)               | Gets the placement score for a virtual machine.<br/>                   |
| [**RemoveHealthProviders**](mscluster-clusterservice-removehealthproviders.md)       | Remove health providers from health service<br/>                       |
| [**RemoveVmReservation**](mscluster-clusterservice-removevmreservation.md)           | Removes the reservation of a virtual machine in the cluster.<br/>      |
| [**UpdateCloudWitnessKey**](mscluster-clusterservice-updatecloudwitnesskey.md)       | Updates the account key associated with the cloud witness<br/>         |
| [**UpdateFunctionalLevel**](updatefunctionallevel-mscluster-clusterservice.md)       | Updates the cluster's functional level.<br/>                           |



 

### Properties

The **MSCluster\_ClusterService** class has these properties.

<dl> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Id that uniquely identifies the cluster service.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



 

 





