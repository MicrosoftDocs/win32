---
title: Generic Application
description: The Generic Application resource type manages cluster-unaware applications as cluster resources \ 8212;as well as cluster-aware applications that are not associated with custom resource types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '98e2476b-885f-46ae-974a-d0c93a033ef1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,Generic Application", "Generic Application resource type Failover Cluster"]
---

# Generic Application

The Generic Application [resource type](resource-types.md) manages [*cluster-unaware applications*](c-gly.md#-wolf-cluster-unaware-application-gly) as cluster resources—as well as [cluster-aware applications](cluster-aware-applications.md) that are not associated with [custom resource types](custom-resource-types.md). The Generic Application [resource DLL](resource-dlls.md) provides only very basic application control. For example, it checks for application failure by determining whether the application's process still exists and takes the application [*offline*](o-gly.md#-wolf-offline-gly) by terminating the process.

The following table summarizes the characteristics of the Generic Application resource type.



| Characteristic                                        | Description                                                                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | None                                                                                                                                   |
| Required [private properties](private-properties.md) | [**CommandLine**](generic-applications-commandline.md), [**CurrentDirectory**](generic-applications-currentdirectory.md)             |
| Optional private properties                           | [**InteractWithDesktop**](generic-applications-interactwithdesktop.md), [**UseNetworkName**](generic-applications-usenetworkname.md) |



 

 

 




