---
title: Network Load Balancing WMI Classes
description: Network Load Balancing (NLB) has the following WMI classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 80e50b1c-7bb7-425d-ad14-c08d62a1d25d
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Network Load Balancing Provider Failover Cluster ,reference,WMI classes Failover Cluster
- WMI classes Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Network Load Balancing WMI Classes

Network Load Balancing (NLB) has the following [*WMI classes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly).



| WMI class                                                                                  | Description                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)<br/>             | Represents data that identifies the NLB cluster.<br/>                                                                                                                                                                            |
| [**MicrosoftNLB\_ConvergedEvent**](https://msdn.microsoft.com/library/bb736302)<br/>            | Represents a NLB cluster [*converged*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly) event.<br/>                                                                                                                                 |
| [**MicrosoftNLB\_ConvergingEvent**](https://msdn.microsoft.com/library/bb736303)<br/>          | Represents a NLB cluster [*converging*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly) event.<br/>                                                                                                                                |
| [**MicrosoftNLB\_ExtendedStatus**](microsoftnlb-extendedstatus.md)<br/>             | The [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) uses this class to report error codes specific to NLB.<br/>                                                                                                       |
| [**MicrosoftNLB\_Node**](microsoftnlb-node.md)<br/>                                 | Represents an instance of a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) within a NLB cluster.<br/>                                                                                                                    |
| [**MicrosoftNLB\_NodeControlEvent**](https://msdn.microsoft.com/library/bb736304)<br/>        | Represents an event signaling a change in status of the NLB node.<br/>                                                                                                                                                           |
| [**MicrosoftNLB\_NodeNodeSetting**](microsoftnlb-nodenodesetting.md)<br/>           | Associates an instance of the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class to an instance of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class.<br/>                                              |
| [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)<br/>                   | Represents the configuration data specific to a node.<br/>                                                                                                                                                                       |
| [**MicrosoftNLB\_NodeSettingPortRule**](microsoftnlb-nodesettingportrule.md)<br/>   | Associates an instance of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class to instances of classes derived from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).<br/>                             |
| [**MicrosoftNLB\_PortControlEvent**](https://msdn.microsoft.com/library/bb736305)<br/>        | Represents an event signaling a change in status in the port rule.<br/>                                                                                                                                                          |
| [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md)<br/>                         | Deprecated use the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class.<br/>                                                                                                                                      |
| [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416)<br/>                    | An abstract base class from which classes that represent [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) are derived. This class supersedes the [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) class.<br/> |
| [**MicrosoftNLB\_PortRuleDisabled**](microsoftnlb-portruledisabled.md)<br/>         | Deprecated use the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class.<br/>                                                                                                                                      |
| [**MicrosoftNLB\_PortRuleFailover**](microsoftnlb-portrulefailover.md)<br/>         | Deprecated use the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class.<br/>                                                                                                                                      |
| [**MicrosoftNLB\_PortRuleLoadbalanced**](microsoftnlb-portruleloadbalanced.md)<br/> | Deprecated use the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class.<br/>                                                                                                                                      |
| [**MicrosoftNLB\_ShutdownEvent**](https://msdn.microsoft.com/library/bb736306)<br/>              | Represents a NLB cluster shutdown event.<br/>                                                                                                                                                                                    |
| [**MicrosoftNLB\_StartupEvent**](https://msdn.microsoft.com/library/bb736307)<br/>                | Represents a NLB cluster startup event.<br/>                                                                                                                                                                                     |



 

 

 





