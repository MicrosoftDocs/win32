---
title: Cluster-Aware Updating Provider Reference
description: The WMI provider for the Cluster-Aware Updating (CAU) tool allows you to coordinate with CAU when performing non-CAU updates, and it provides the back-end implementation of the default plug-in, which uses the Windows Update Agent (WUA) to scan, download, and install updates through Windows Management Instrumentation (WMI). This documentation assumes you are familiar with the concept of WMI and have experience writing WMI scripts and applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0483B3D5-1ED6-4638-9CE7-44D9E03EF3E3
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster-Aware Updating Provider Reference

The WMI provider for the Cluster-Aware Updating (CAU) tool allows you to coordinate with CAU when performing non-CAU updates, and it provides the back-end implementation of the default plug-in, which uses the Windows Update Agent (WUA) to scan, download, and install updates through Windows Management Instrumentation (WMI). This documentation assumes you are familiar with the concept of WMI and have experience writing WMI scripts and applications.

The CAU provider defines the following classes.



| Class                                                                                       | Description                                                                                                     |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md)<br/>             | Represents the result from the [**DownloadUpdates**](downloadupdates-msft-caunode.md) method.<br/>       |
| [**MSFT\_CAU\_InstallUpdateInfo**](msft-cau-installupdateinfo.md)<br/>               | Represents the result from the [**InstallUpdates**](installupdates-msft-caunode.md) method.<br/>         |
| [**MSFT\_CAU\_ScanUpdateInfo**](msft-cau-scanupdateinfo.md)<br/>                     | Represents the result from the [**ScanUpdates**](scanupdates-msft-caunode.md) method.<br/>               |
| [**MSFT\_CAU\_Update\_Installer\_Result**](msft-cau-update-installer-result.md)<br/> | Contains the result and return codes for the update installer.<br/>                                       |
| [**MSFT\_CAUNode**](msft-caunode.md)<br/>                                            | Represents WUA-related operations performed on a cluster node.<br/>                                       |
| [**MSFT\_CAUReportHelper**](msft-caureporthelper.md)<br/>                            | Represents operations to retrieve and save an updating run report.<br/>                                   |
| [**MSFT\_CAURun**](msft-caurun.md)<br/>                                              | Represents operations performed for an entire cluster.<br/>                                               |
| [**MSFT\_CAURun\_Report\_Chunk**](msft-caurun-report-chunk.md)<br/>                  | Represents a chunk of input or output to be processed by the helper class of an updating run report.<br/> |
| [**MSFT\_CAURun\_Report\_ID**](msft-caurun-report-id.md)<br/>                        | Identifies an updating run report.<br/>                                                                   |



 

 

 





