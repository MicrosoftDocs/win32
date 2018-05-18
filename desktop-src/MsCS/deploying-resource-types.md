---
title: Manually Deploying Resource Types
description: Once you have created a resource DLL and a Cluster Administrator extension DLL, the next step is to deploy the new resource types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fdcdf58c-0f93-4b50-97a7-61c140e1cc1e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,deploying"]
---

# Manually Deploying Resource Types

Once you have created a [resource DLL](resource-dlls.md) and a [Cluster Administrator](cluster-administrator.md) extension DLL, the next step is to deploy the new [resource types](resource-types.md). Typically, you deploy manually when designing and testing the resource type and create a [*cluster-aware*](c-gly.md#-wolf-cluster-aware-application-gly) setup application to deploy the finished product. No matter how you accomplish the deployment, the following list describes the end result:

-   Each [*cluster*](c-gly.md#-wolf-cluster-gly) [node](nodes.md) has a local installation of the application, service, or device to be managed as a [*highly available*](h-gly.md#-wolf-high-availability-gly) resource. This includes the application binaries, COM and ActiveX components, registry and crypto keys, and other files necessary to run the application.
-   Each cluster node has a local copy of your resource DLL under the same path and filename.
-   Each cluster node and each remote non-clustered system that will be used to administer the cluster must have local copies of your extension DLL under the same path and filename.
-   Your resource DLL and extension DLL are registered with the cluster.
-   Your extension DLL is registered with COM on every system containing a copy of the DLL.

The following procedure describes how to deploy resource types manually. For information on deploying resource types through setup applications, see [Creating Cluster-Aware Setup Applications](creating-cluster-aware-setup-applications.md).

**To deploy resource types manually**

1.  Install the application files on each node. For more information on this process see [Installing Files](installing-files.md).
2.  Copy your resource DLL to each cluster node, using the same path and filename on each node.
3.  Copy the extension DLL to each cluster node and to each remote system that will be using Cluster Administrator to administer the cluster. Use the same path and filename on each system.
4.  From any cluster node, enter the following PowerShell cmdlet code once for each resource type supported by your resource DLL:

    **Add-ClusterResourceType -Name** *MyResourceTypeName* **-Dll** *path***\\***dllname*

    Specify the path to the location of your DLL (see step 2.). If no path is specified, it defaults to %SystemRoot%\\Cluster.

    **Windows Server 2008:  **

    The Add-ClusterResourceType PowerShell cmdlet is unavailable. Use the following Cluster.exe command instead:

    **cluster restype** *MyResourceTypeName* **/create /dll:** *path***\\***dllname*

5.  From any cluster node, call RegSvr32 using the following syntax:

    **RegSvr32** *drive***:\\***path***\\***MyExtensionDLLName*

 

 




