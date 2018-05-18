---
title: LoadAllSettings method of the MicrosoftNLB\_ClusterSetting class
description: Forces the Network Load Balancing (NLB) driver to reload, which allows it to update its private copy of the cluster configuration data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b31d50cf-cb28-499b-bf3f-8ec7929b9416'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["LoadAllSettings method", "LoadAllSettings method, MicrosoftNLB_ClusterSetting class", "MicrosoftNLB_ClusterSetting class, LoadAllSettings method"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterSetting.LoadAllSettings
api_location:
- WlbsProv.dll
api_type:
- COM
---

# LoadAllSettings method of the MicrosoftNLB\_ClusterSetting class

Forces the Network Load Balancing (NLB) driver to reload, which allows it to update its private copy of the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) configuration data.

## Syntax


```mof
uint32 LoadAllSettings();
```



## Parameters

This method has no parameters.

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

<dl> <dt>

**WLBS\_OK** (1000)
</dt> <dt>

**WLBS\_REBOOT** (1050)
</dt> </dl>

## Remarks

Because the NLB driver runs beneath the operating system, its only opportunity to read and save cluster configuration data is during its initialization. The **LoadAllSettings** method forces the driver to reload, which updates its private data store and commits the changes to that node of the cluster. The **LoadAllSettings** method should be called on each node of the cluster.

This method requires the **wbemPrivilegeLoadDriver** privilege (also known as **SE\_LOAD\_DRIVER** or "SeLoadDriverPrivilege"). For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> <dt>

[**LoadAllSettings Method of the MicrosoftNLB\_NodeSetting Class**](microsoftnlb-nodesetting-loadallsettings.md)
</dt> </dl>

 

 





