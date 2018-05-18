---
title: Standard Return Values
description: Return values used by the Network Load Balancer provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4d261082-6cdf-418f-b986-cbdd9c596023'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["standard return values Failover Cluster", "return values Failover Cluster", "WLBS_OK", "WLBS_ALREADY", "WLBS_DRAIN_STOP", "WLBS_BAD_PARAMS", "WLBS_NOT_FOUND", "WLBS_STOPPED", "WLBS_CONVERGING", "WLBS_CONVERGED", "WLBS_DEFAULT", "WLBS_DRAINING", "WLBS_SUSPENDED", "WLBS_MEDIA_DISCONNECTED", "WLBS_REBOOT", "WLBS_INIT_ERROR", "WLBS_BAD_PASSW", "WLBS_IO_ERROR", "WLBS_TIMEOUT", "WLBS_PORT_OVERLAP", "WLBS_BAD_PORT_PARAMS", "WLBS_MAX_PORT_RULES", "WLBS_TRUNCATED", "WLBS_REG_ERROR"]
---

# Standard Return Values

The Network Load Balancing Provider communicates status and error information as follows:

-   All WMI operations that produce an error create an **\_\_ExtendedStatus** object. Depending on the source of the error, the **StatusCode** property of the **\_\_ExtendedStatus** object may contain one of the values listed below.
-   The [**MicrosoftNLB\_Node**](microsoftnlb-node.md) methods also generate the following values which are returned through the **ReturnValue** property of **IWbemClassObject**.



| Value           | Error code                               | Description                                                                                                                                                                   |
|-----------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1000<br/> | **WLBS\_OK**<br/>                  | The operation completed successfully.<br/>                                                                                                                              |
| 1001<br/> | **WLBS\_ALREADY**<br/>             | The specified target is already in the state that the requested operation would produce.<br/>                                                                           |
| 1002<br/> | **WLBS\_DRAIN\_STOP**<br/>         | One or more [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) reported a drain stop operation.<br/>                                                               |
| 1003<br/> | **WLBS\_BAD\_PARAMS**<br/>         | Bad configuration parameters in a node's registry prevented the node from starting cluster operations.<br/>                                                             |
| 1004<br/> | **WLBS\_NOT\_FOUND**<br/>          | The specified port number was not found in any [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly).<br/>                                                        |
| 1005<br/> | **WLBS\_STOPPED**<br/>             | Cluster operations have stopped on at least one node.<br/>                                                                                                              |
| 1006<br/> | **WLBS\_CONVERGING**<br/>          | The [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) is [*converging*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly).<br/>                                     |
| 1007<br/> | **WLBS\_CONVERGED**<br/>           | The cluster has converged successfully.<br/>                                                                                                                            |
| 1008<br/> | **WLBS\_DEFAULT**<br/>             | The specified node has converged as the [*default host*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-9-gly).<br/>                                                            |
| 1009<br/> | **WLBS\_DRAINING**<br/>            | One or more nodes are [*draining*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-11-gly).<br/>                                                                                |
| 1013<br/> | **WLBS\_SUSPENDED**<br/>           | Cluster operations have been suspended on one or more nodes.<br/>                                                                                                       |
| 1014<br/> | **WLBS\_MEDIA\_DISCONNECTED**<br/> | The network adapter cable is disconnected.<br/>                                                                                                                         |
| 1050<br/> | **WLBS\_REBOOT**<br/>              | The node must be rebooted for the specified configuration changes to take effect.<br/>                                                                                  |
| 1100<br/> | **WLBS\_INIT\_ERROR**<br/>         | An internal error prevented initialization of the cluster control module.<br/>                                                                                          |
| 1101<br/> | **WLBS\_BAD\_PASSW**<br/>          | The specified password was not accepted by the cluster.<br/>                                                                                                            |
| 1102<br/> | **WLBS\_IO\_ERROR**<br/>           | A local I/O error prevents communication with the Network Load Balancing driver.<br/>                                                                                   |
| 1103<br/> | **WLBS\_TIMEOUT**<br/>             | The requested operation timed out without receiving a response from the specified node.<br/>                                                                            |
| 1150<br/> | **WLBS\_PORT\_OVERLAP**<br/>       | At least one of the port numbers in the specified [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) is currently listed in at least one other port rule.<br/> |
| 1151<br/> | **WLBS\_BAD\_PORT\_PARAMS**<br/>   | The settings for one or more port rules contain one or more invalid values.<br/>                                                                                        |
| 1152<br/> | **WLBS\_MAX\_PORT\_RULES**<br/>    | The cluster contains the maximum number of port rules.<br/>                                                                                                             |
| 1153<br/> | **WLBS\_TRUNCATED**<br/>           | The return value has been truncated.<br/>                                                                                                                               |
| 1154<br/> | **WLBS\_REG\_ERROR**<br/>          | An internal registry access error occurred.<br/>                                                                                                                        |



 

 

 





