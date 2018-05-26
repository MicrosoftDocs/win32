---
title: MSFT\_CAURun class
description: A dynamic WMI class that represents a cluster synchronization object that CAU relies on for its operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: adba6bd7-dd89-4dbb-bb9b-439c3fdfddab
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAURun class
- MSFT_CAURun class, described
topic_type:
- apiref
api_name:
- MSFT_CAURun
- MSFT_CAURun.OrchestratorGuid
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_CAURun class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a cluster synchronization object that CAU relies on for its operations.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAURun
{
  String OrchestratorGuid;
};
```

## Members

The **MSFT\_CAURun** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAURun** class has these properties.

<dl> <dt>

**OrchestratorGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The identifier for the Update Coordinator that drives Cluster-Aware Updating (CAU) operations. Each Update Coordinator has a unique **OrchestratorGuid** value.

</dd> </dl>

## Remarks

The presence of this object indicates that the associated cluster is currently being updated by an Update Coordinator identified by the **OrchestratorGuid** property. No other Update Coordinator should attempt to update the cluster until this object has been removed. This object is a singleton, and, at most, one of these objects is allowed to be created on a cluster node. This object is persistent, and it is not removed across system restarts. The owner of the object should delete the object after the update operation for the entire cluster has been completed.

Note that the CAU WMI provider automatically removes this object after one hour of inactivity.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAUReportHelper**](msft-caureporthelper.md)
</dt> </dl>

 

 





