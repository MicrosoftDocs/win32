---
description: Using the COM+ CRM in a Cluster Environment
ms.assetid: 753461c5-880c-4df0-b552-b962dc06524f
title: Using the COM+ CRM in a Cluster Environment
ms.topic: article
ms.date: 05/31/2018
---

# Using the COM+ CRM in a Cluster Environment

When developing COM+ CRMs to work in cluster environments, the main factor to consider is whether a specific CRM cares which node of the cluster it is operating on. For example, if the resource managed by the CRM is the machine file system or registry, any changes are specific to the node that the CRM server application is running on at the time. In this case, failover of the CRM server application to another node would not be desirable. In a different case, where the CRM is managing some resource common to the cluster, failover of the CRM server application to another node is useful.

The default directory location for CRM log files is the same directory as the DTC log file. On clusters, the DTC log file is placed on a shared disk that is failed over between the nodes of the cluster. This means that the default behavior for CRM server applications is to failover between nodes of the cluster. Therefore, if a specific CRM requires the alternative behavior of not failing over between nodes, the location of the CRM log file for that particular CRM server application should be changed.

In addition, if failover is required for the CRM application, it should be configured as a generic application in a cluster group. Its dependency should be DTC.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



