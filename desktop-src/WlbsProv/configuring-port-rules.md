---
title: Configuring Port Rules
description: On the Port Rules tab of the Network Load Balancing Properties dialog, the filtering mode of a port rule is a configurable property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5a36446-823e-4bb8-89ea-9665fec8d851
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- port rules in NLB Failover Cluster
- port rules in NLB Failover Cluster ,configuring
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Configuring Port Rules

On the **Port Rules** tab of the **Network Load Balancing Properties** dialog, the [*filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-1-gly) of a [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) is a configurable property. The Network Load Balancing (NLB) [*Provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) does not define a corresponding property. Instead, each filtering mode is represented by a specific class derived from [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416). To access the settings of a port rule, you must create an instance of that class.



| Filtering mode                                                                            | Class to use                                                                               |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [*Multiple-host filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-8-gly)<br/> | [**MicrosoftNLB\_PortRuleLoadbalanced**](microsoftnlb-portruleloadbalanced.md)<br/> |
| [*Single-host filtering mode*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-18-gly)<br/> | [**MicrosoftNLB\_PortRuleFailover**](microsoftnlb-portrulefailover.md)<br/>         |
| Disabled<br/>                                                                       | [**MicrosoftNLB\_PortRuleDisabled**](microsoftnlb-portruledisabled.md)<br/>         |



 

The remaining settings shown on the **Port Rules** tab of the **Network Load Balancing Properties** dialog are accessed using the properties of the [**MicrosoftNLB\_PortRuleEx**](https://msdn.microsoft.com/library/aa371416) class as shown in the following table.



| Setting                        | Property                                 |
|--------------------------------|------------------------------------------|
| Port range<br/>          | **StartPort** and **EndPort**<br/> |
| Protocols<br/>           | **Protocol**<br/>                  |
| Affinity<br/>            | **Affinity**<br/>                  |
| Load weight<br/>         | **LoadWeight**<br/>                |
| Equal load checkbox<br/> | **EqualLoad**<br/>                 |
| Handling priority<br/>   | **Priority**<br/>                  |



 

 

 





