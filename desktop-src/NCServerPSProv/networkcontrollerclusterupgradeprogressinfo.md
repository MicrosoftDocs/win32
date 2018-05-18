---
title: NetworkControllerClusterUpgradeProgressInfo class
description: Contains network controller cluster upgrade progress information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c12bf8bf-9d4f-412d-9e20-bd36d75210e9'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NetworkControllerClusterUpgradeProgressInfo class", "NetworkControllerClusterUpgradeProgressInfo class, described"]
topic_type:
- apiref
api_name:
- NetworkControllerClusterUpgradeProgressInfo
- NetworkControllerClusterUpgradeProgressInfo.InternalTargetConfigVersion
- NetworkControllerClusterUpgradeProgressInfo.TargetCodeVersion
- NetworkControllerClusterUpgradeProgressInfo.CurrentUpgradingNode
- NetworkControllerClusterUpgradeProgressInfo.NextUpgradingNode
- NetworkControllerClusterUpgradeProgressInfo.UpgradeState
- NetworkControllerClusterUpgradeProgressInfo.FailureReason
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
---

# NetworkControllerClusterUpgradeProgressInfo class

Contains network controller cluster upgrade progress information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), AMENDMENT]
class NetworkControllerClusterUpgradeProgressInfo
{
  string InternalTargetConfigVersion;
  string TargetCodeVersion;
  string CurrentUpgradingNode;
  string NextUpgradingNode;
  string UpgradeState;
  string FailureReason;
};
```

## Members

The **NetworkControllerClusterUpgradeProgressInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerClusterUpgradeProgressInfo** class has these properties.

<dl> <dt>

**CurrentUpgradingNode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node that is currently being upgraded.

</dd> <dt>

**FailureReason**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reason for failure.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Interrupted"></span><span id="interrupted"></span><span id="INTERRUPTED"></span>

**Interrupted** ("Interrupted")


</dt> <dd></dd> <dt>

<span id="HealthCheck"></span><span id="healthcheck"></span><span id="HEALTHCHECK"></span>

**HealthCheck** ("HealthCheck")


</dt> <dd></dd> <dt>

<span id="UpgradeDomainTimeout"></span><span id="upgradedomaintimeout"></span><span id="UPGRADEDOMAINTIMEOUT"></span>

**UpgradeDomainTimeout** ("UpgradeDomainTimeout")


</dt> <dd></dd> <dt>

<span id="OverallUpgradeTimeout"></span><span id="overallupgradetimeout"></span><span id="OVERALLUPGRADETIMEOUT"></span>

**OverallUpgradeTimeout** ("OverallUpgradeTimeout")


</dt> <dd></dd> </dl>

</dd> <dt>

**InternalTargetConfigVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the network controller cluster after the upgrade finishes.

</dd> <dt>

**NextUpgradingNode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node that will be upgraded next.

</dd> <dt>

**TargetCodeVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the service fabric code after the upgrade finishes.

</dd> <dt>

**UpgradeState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of upgrade.

<dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

**Invalid** ("Invalid")


</dt> <dd></dd> <dt>

<span id="RollingBackInProgress"></span><span id="rollingbackinprogress"></span><span id="ROLLINGBACKINPROGRESS"></span>

**RollingBackInProgress** ("RollingBackInProgress")


</dt> <dd></dd> <dt>

<span id="RollingBackCompleted"></span><span id="rollingbackcompleted"></span><span id="ROLLINGBACKCOMPLETED"></span>

**RollingBackCompleted** ("RollingBackCompleted")


</dt> <dd></dd> <dt>

<span id="RollingForwardPending"></span><span id="rollingforwardpending"></span><span id="ROLLINGFORWARDPENDING"></span>

**RollingForwardPending** ("RollingForwardPending")


</dt> <dd></dd> <dt>

<span id="RollingForwardInProgress"></span><span id="rollingforwardinprogress"></span><span id="ROLLINGFORWARDINPROGRESS"></span>

**RollingForwardInProgress** ("RollingForwardInProgress")


</dt> <dd></dd> <dt>

<span id="RollingForwardCompleted"></span><span id="rollingforwardcompleted"></span><span id="ROLLINGFORWARDCOMPLETED"></span>

**RollingForwardCompleted** ("RollingForwardCompleted")


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

**Failed** ("Failed")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





