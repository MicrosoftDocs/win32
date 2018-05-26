---
title: PS\_NetworkController class
description: Represents the Network Controller server provider functions for node level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7ce0f9a9-c997-45e6-9577-05154d6f883a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_NetworkController class
- PS_NetworkController class, described
topic_type:
- apiref
api_name:
- PS_NetworkController
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_NetworkController class

Represents the Network Controller server provider functions for node level.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class PS_NetworkController
{
};
```

## Members

The **PS\_NetworkController** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_NetworkController** class has these methods.



| Method                                                                                        | Description                                                                    |
|:----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**AcquireUpdateLock**](ps-networkcontroller-acquireupdatelock.md)                           | Acquires a Network Controller update lock.<br/>                          |
| [**DeployApplication**](deployapplication-ps-networkcontroller.md)                           | Deploys the Network Controller application on the cluster.<br/>          |
| [**GetApplicationConfiguration**](getapplicationconfiguration-ps-networkcontroller.md)       | Retrieves Network Controller application configuration information.<br/> |
| [**GetClusterConfiguration**](getclusterconfiguration-ps-networkcontroller.md)               | Retrieves Network Controller cluster configuration.<br/>                 |
| [**GetClusterUpgradeProgress**](ps-networkcontroller-getclusterupgradeprogress.md)           | This method gets the Network Controller upgrade status<br/>              |
| [**PerformClusterNodeOperation**](performclusternodeoperation-ps-networkcontroller.md)       | Performs cluster node-specific operations.<br/>                          |
| [**RecoverClusterFromQuorumLoss**](recoverclusterfromquorumloss-ps-networkcontroller.md)     | Recovers the services of Network Controller from quorum loss.<br/>       |
| [**ReleaseUpdateLock**](ps-networkcontroller-releaseupdatelock.md)                           | Releases a Network Controller update lock.<br/>                          |
| [**RemoveTemporaryServices**](ps-networkcontroller-removetemporaryservices.md)               | Removes the temporary services from Network Controller.<br/>             |
| [**UndeployApplication**](undeployapplication-ps-networkcontroller.md)                       | Undeploys the Network Controller application on the cluster.<br/>        |
| [**UpdateApplicationConfiguration**](updateapplicationconfiguration-ps-networkcontroller.md) | Updates the Network Controller application configuration.<br/>           |
| [**UpdateClusterConfiguration**](updateclusterconfiguration-ps-networkcontroller.md)         | Updates the Network Controller cluster configuration.<br/>               |
| [**UpgradeApplication**](ps-networkcontroller-upgradeapplication.md)                         | Upgrades the Network Controller.<br/>                                    |
| [**UpgradeClusterCode**](ps-networkcontroller-upgradeclustercode.md)                         | Upgrades the Service Fabric cluster code.<br/>                           |
| [**UpgradeClusterConfiguration**](ps-networkcontroller-upgradeclusterconfiguration.md)       | Upgrades the Network Controller cluster.<br/>                            |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





