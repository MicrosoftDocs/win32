---
title: Service Utility Functions
description: The service utility functions manage services for resource DLLs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 16fcc65f-81b3-4126-a56e-4aaee3099b8c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- service utility functions Failover Cluster
- cluster utility functions Failover Cluster ,service utility functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service Utility Functions

The [*service*](https://www.bing.com/search?q=*service*) utility functions manage services for [resource DLLs](resource-dlls.md).

## In this section

<dl> <dt>

[*ResUtilFreeEnvironment*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_free_environment)
</dt> <dd>

Destroys the environment variable block created with [*ResUtilGetEnvironmentWithNetName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_environment_with_net_name). The **PRESUTIL\_FREE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilGetEnvironmentWithNetName*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_environment_with_net_name)
</dt> <dd>

Adjusts environment data for a [resource](resources.md) so that the resource uses a cluster network name to identify its location. The resource must be dependent on a [Network Name](network-name.md) resource. The **PRESUTIL\_GET\_ENVIRONMENT\_WITH\_NET\_NAME** type defines a pointer to this function.

</dd> <dt>

[*ResUtilRemoveResourceServiceEnvironment*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_remove_resource_service_environment)
</dt> <dd>

Removes the environment data from a [service](https://www.bing.com/search?q=service). This function must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_REMOVE\_RESOURCE\_SERVICE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceEnvironment*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_resource_service_environment)
</dt> <dd>

Adjusts the environment data for a [service](https://www.bing.com/search?q=service) so that the service uses a cluster network name to identify its location. This function must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_ENVIRONMENT** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceStartParameters*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_resource_service_start_parameters)
</dt> <dd>

Adjusts the start parameters of a specified [service](https://www.bing.com/search?q=service) so that it will operate correctly as a cluster [resource](resources.md). It must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_START\_PARAMETERS** type defines a pointer to this function.

</dd> <dt>

[*ResUtilSetResourceServiceStartParametersEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_resource_service_start_parameters_ex)
</dt> <dd>

Adjusts the start parameters of a specified [service](https://www.bing.com/search?q=service) so that it operates correctly as a cluster [resource](resources.md). It must be called from a [resource DLL](resource-dlls.md). The **PRESUTIL\_SET\_RESOURCE\_SERVICE\_START\_PARAMETERS\_EX** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStartResourceService*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_start_resource_service)
</dt> <dd>

Starts a [service](https://www.bing.com/search?q=service). The **PRESUTIL\_START\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStopResourceService*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_stop_resource_service)
</dt> <dd>

Stops a named [service](https://www.bing.com/search?q=service). The **PRESUTIL\_STOP\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilStopService*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_stop_service)
</dt> <dd>

Stops a [service](https://www.bing.com/search?q=service) identified by a handle. The **PRESUTIL\_STOP\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilTerminateServiceProcessFromResDll*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_terminate_service_process_from_res_dll)
</dt> <dd>

Attempts to terminate the process of a service being managed as a cluster resource by a resource DLL. The **PRESUTIL\_TERMINATE\_SERVICE\_PROCESS\_FROM\_RES\_DLL** type defines a pointer to this function.

</dd> <dt>

[*ResUtilVerifyResourceService*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_verify_resource_service)
</dt> <dd>

Verifies that a named [service](https://www.bing.com/search?q=service) is starting or currently running. The **PRESUTIL\_VERIFY\_RESOURCE\_SERVICE** type defines a pointer to this function.

</dd> <dt>

[*ResUtilVerifyService*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_verify_service)
</dt> <dd>

Checks if a [service](https://www.bing.com/search?q=service) identified by a handle is starting or currently running. The **PRESUTIL\_VERIFY\_SERVICE** type defines a pointer to this function.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Utility Functions](cluster-utility-functions.md)
</dt> </dl>

 

 




