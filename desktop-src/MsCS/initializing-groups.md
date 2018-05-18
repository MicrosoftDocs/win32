---
title: Initializing Groups
description: Your resources may have a number of dependencies, required private properties, or optimal common property settings, and will probably need to be published to clients through a failover cluster instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff3e3e1e-d632-463d-9005-c327451d43bb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["groups Failover Cluster ,initializing"]
---

# Initializing Groups

Your [resources](resources.md) may have a number of [dependencies](resource-dependencies.md), required [private properties](private-properties.md), or optimal [common property](common-properties.md) settings, and will probably need to be published to clients through a [failover cluster instance](virtual-servers.md).

After installing the files and registering the new [resource types](resource-types.md), your cluster-aware setup application can work with the administrator to configure sample resources and [groups](groups.md). Using an interactive format such as a Wizard is often the best solution because:

-   You will need the administrator to supply information such as IP addresses and network names.
-   The administrator will need to learn how to configure and troubleshoot your resources. An interactive procedure allows you to emphasize the critical configuration steps.

 

 




