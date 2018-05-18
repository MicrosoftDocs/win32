---
title: Service Utility Functions
description: The service utility functions manage services for resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '16fcc65f-81b3-4126-a56e-4aaee3099b8c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["service utility functions Failover Cluster", "cluster utility functions Failover Cluster ,service utility functions"]
---

# Service Utility Functions

The [*service*](s-gly.md#-wolf-service-gly) utility functions manage services for [resource DLLs](resource-dlls.md).

## In this section

<dl> <dt>

[*ResUtilFreeEnvironment*](resutilfreeenvironment.md)
</dt> <dd>

Destroys the environment variable block created with [*ResUtilGetEnvironmentWithNetName*](resutilgetenvironmentwithnetname.md). The **PRESUTIL\_FREE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetEnvironmentWithNetName*](resutilgetenvironmentwithnetname.md)
</dt> <dd>

Adjusts environment data for a [resource](resources.md) so that the resource uses a cluster network name to identify its location. The resource must be dependent on a [Network Name](network-name.md) resource. The **PRESUTIL\_GET\_ENVIRONMENT\_WITH\_NET\_NAME** type defines a pointer to this function.

</dd> <dt>

[*ResUtilRemoveResourceServiceEnvironment*](resutilremoveresourceserviceenvironment.md)
</dt> <dd>

Removes the environment data from a [service](s-gly.md#-wolf-service-gly). This function must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_REMOVE\_RESOURCE\_SERVICE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceEnvironment*](resutilsetresourceserviceenvironment.md)
</dt> <dd>

Adjusts the environment data for a [service](s-gly.md#-wolf-service-gly) so that the service uses a cluster network name to identify its location. This function must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceStartParameters*](resutilsetresourceservicestartparameters.md)
</dt> <dd>

Adjusts the start parameters of a specified [service](s-gly.md#-wolf-service-gly) so that it will operate correctly as a cluster [resource](resources.md). It must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_START\_PARAMETERS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceStartParametersEx*](resutilsetresourceservicestartparametersex.md)
</dt> <dd>

Adjusts the start parameters of a specified [service](s-gly.md#-wolf-service-gly) so that it operates correctly as a cluster [resource](resources.md). It must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_START\_PARAMETERS\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStartResourceService*](resutilstartresourceservice.md)
</dt> <dd>

Starts a [service](s-gly.md#-wolf-service-gly). The **PRESUTIL\_START\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStopResourceService*](resutilstopresourceservice.md)
</dt> <dd>

Stops a named [service](s-gly.md#-wolf-service-gly). The **PRESUTIL\_STOP\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStopService*](resutilstopservice.md)
</dt> <dd>

Stops a [service](s-gly.md#-wolf-service-gly) identified by a handle. The **PRESUTIL\_STOP\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilTerminateServiceProcessFromResDll*](resutilterminateserviceprocessfromresdll.md)
</dt> <dd>

Attempts to terminate the process of a service being managed as a cluster resource by a resource DLL. The **PRESUTIL\_TERMINATE\_SERVICE\_PROCESS\_FROM\_RES\_DLL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilVerifyResourceService*](resutilverifyresourceservice.md)
</dt> <dd>

Verifies that a named [service](s-gly.md#-wolf-service-gly) is starting or currently running. The **PRESUTIL\_VERIFY\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilVerifyService*](resutilverifyservice.md)
</dt> <dd>

Checks if a [service](s-gly.md#-wolf-service-gly) identified by a handle is starting or currently running. The **PRESUTIL\_VERIFY\_SERVICE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




