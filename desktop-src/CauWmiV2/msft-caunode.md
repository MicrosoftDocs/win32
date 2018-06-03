---
title: MSFT\_CAUNode class
description: A dynamic WMI class that represents operations performed on a cluster node that are specific to CAU features and supported only for CAU scenarios.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 49b84ff7-4444-4d1a-a8c6-5a80e86a3ce3
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAUNode class
- MSFT_CAUNode class, described
topic_type:
- apiref
api_name:
- MSFT_CAUNode
- MSFT_CAUNode.OrchestratorGuid
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_CAUNode class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents operations performed on a cluster node that are specific to CAU features and supported only for CAU scenarios.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAUNode
{
  String OrchestratorGuid;
};
```

## Members

The **MSFT\_CAUNode** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_CAUNode** class has these methods.



| Method                                                        | Description                                                                |
|:--------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**DownloadUpdates**](downloadupdates-msft-caunode.md)       | Downloads updates to the node.<br/>                                  |
| [**InstallUpdates**](installupdates-msft-caunode.md)         | Installs updates to the node.<br/>                                   |
| [**RebootRequired**](rebootrequired-msft-caunode.md)         | Gets a value that indicates whether the node must be restarted.<br/> |
| [**RunUpdateInstaller**](runupdateinstaller-msft-caunode.md) | Runs the update installer out of process on the node.<br/>           |
| [**ScanUpdates**](scanupdates-msft-caunode.md)               | Scans for applicable updates.<br/>                                   |



 

### Properties

The **MSFT\_CAUNode** class has these properties.

<dl> <dt>

**OrchestratorGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The identifier for the Update Coordinator that represents an instance of a Cluster-Aware Updating (CAU) Node object. Each Update Coordinator has a unique **OrchestratorGuid** value.

</dd> </dl>

## Remarks

This object is a singleton, and, at most, one of these objects is allowed to be created on a cluster node. This object is persistent, and it is not removed across system restarts. The owner of the object should delete the object once the update operation for the node has been completed.

Note that the CAU WMI provider automatically removes this object after one hour of inactivity.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



 

 





