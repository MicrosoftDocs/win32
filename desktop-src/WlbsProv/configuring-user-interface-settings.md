---
title: Configuring User Interface Settings
description: Settings displayed by the Network Load Balancing Properties dialog box.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: afcfcd41-8730-4ea0-bd72-933e32c645cd
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- user interface settings in NLB Failover Cluster
- user interface settings in NLB Failover Cluster ,configuring
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Configuring User Interface Settings

The following sections describe each of the settings displayed on the **Network Load Balancing Properties** dialog box and the [*Provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) classes or methods used to access the same settings:

-   [Configuring Cluster Parameters](configuring-cluster-parameters.md)
-   [Configuring Host Parameters](configuring-host-parameters.md)
-   [Configuring Port Rules](configuring-port-rules.md)

> [!Note]  
> If the Network Load Balancing provider and the Network Load Balancing user interface are used concurrently in the same cluster to make configuration changes, the results are unpredictable. For example, if the remote password is modified through the user interface, the provider may return a **WLBS\_BAD\_PASSW** error when attempting to get or enumerate instances of [**MicrosoftNLB\_Node**](microsoftnlb-node.md). Using the [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md) method of the [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) class or the [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) method of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class will update the provider and remove the error. For the best results, avoid concurrent use of the provider and the user interface.

 

 

 




