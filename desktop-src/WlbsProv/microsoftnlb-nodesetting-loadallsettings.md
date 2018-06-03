---
title: LoadAllSettings method of the MicrosoftNLB\_NodeSetting class
description: Forces the Network Load Balancing driver to reload, which allows it to update its private copy of the cluster configuration data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5fc07f34-f1fc-4c14-9780-e0b59cce7e9c
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- LoadAllSettings method
- LoadAllSettings method, MicrosoftNLB_NodeSetting class
- MicrosoftNLB_NodeSetting class, LoadAllSettings method
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSetting.LoadAllSettings
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LoadAllSettings method of the MicrosoftNLB\_NodeSetting class

Forces the Network Load Balancing driver to reload, which allows it to update its private copy of the cluster configuration data.

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

Because the Network Load Balancing driver runs "beneath" the operating system, its only opportunity to read and save cluster configuration data is during its initialization. The [**LoadAllSettings**](https://msdn.microsoft.com/library/aa371012) method forces the driver to reload, which updates its private data store and "commits" the changes to the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

This method requires the **wbemPrivilegeLoadDriver** privilege (also known as **SE\_LOAD\_DRIVER** or "SeLoadDriverPrivilege"). For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> <dt>

[**LoadAllSettings Method of the MicrosoftNLB\_ClusterSetting Class**](microsoftnlb-clustersetting-loadallsettings.md)
</dt> </dl>

 

 





