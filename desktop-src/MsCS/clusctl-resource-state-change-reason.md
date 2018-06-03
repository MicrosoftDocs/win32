---
title: CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code
description: Under certain circumstances, the cluster sends the CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON \ 32;control code to a resource DLL immediately before calling the Offline or Terminate entry-point function, providing the DLL with the reason for the state change.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3261c8eb-b88b-428a-8a2b-684e0967f9de
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STATE_CHANGE_REASON control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STATE_CHANGE_REASON
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code

Under certain circumstances, the cluster sends the CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON [control code](about-control-codes.md) to a [resource DLL](resource-dlls.md) immediately before calling the [**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine) or [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine) entry-point function, providing the DLL with the reason for the state change. Because the control code is internal, applications cannot use it in a control code function.

## Parameters

This control code has no parameters.

## Return value

This control code does not return a value.

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON (0x0150004e) as follows.



| Component                 | Bit location     | Value                                                  |
|---------------------------|------------------|--------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>            |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                 |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                      |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>              |
| Type bit<br/>       | 20<br/>    | Internal (0x1)<br/>                              |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STATE\_CHANGE\_REASON** (0x50004e)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>               |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Optional. By default, resource DLLs do not receive the CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code under any circumstances. To receive the control code, a resource DLL must report the following characteristic: **CLUS\_CHAR\_REQUIRES\_STATE\_CHANGE\_REASON**.

For information on how to report characteristics for your resource DLL see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md).

The CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code gives resource DLLs the option of implementing different shutdown procedures in response to different shutdown conditions. For example, a resource DLL may implement a graceful, clean shutdown under most circumstances, but if the [Cluster service](cluster-service.md) stops unexpectedly, the DLL may implement a fast and dirty brute-force shutdown to facilitate faster failover.

To support CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code in your resource DLL, perform the following steps:

-   Initialize a [**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clusctl_resource_state_change_reason_struct) structure for each resource managed by the resource DLL. Typically this structure is included in the resource DLL's resource structure.
-   In your implementation of [*ResourceControl*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine):

    -   Handle the [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md) control code and return a value that includes **CLUS\_CHAR\_REQUIRES\_STATE\_CHANGE\_REASON**.
    -   Handle the CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON control code and store the reason code passed in the *lpInBuffer* parameter in the **eReason** member of the resource structure.

-   When implementing [**Offline**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-poffline_routine) and [**Terminate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pterminate_routine), read the **eReason** member of the resource structure and, if this member is not **eResourceStateChangeReasonUnknown** (from the [**CLUSTER\_RESOURCE\_STATE\_CHANGE\_REASON**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_state_change_reason) enumeration), perform any necessary operations. Before returning from **Offline** or **Terminate**, reset the **eReason** member of the resource structure to **eResourceStateChangeReasonUnknown**.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Internal Resource Control Codes](internal-resource-control-codes.md)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dt>

[**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clusctl_resource_state_change_reason_struct)
</dt> <dt>

[**CLUSTER\_RESOURCE\_STATE\_CHANGE\_REASON**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_state_change_reason)
</dt> </dl>

 

 





