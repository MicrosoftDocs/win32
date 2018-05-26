---
title: EnableDevice method of the MSCluster\_NetworkInterface class
description: Requests that the device be enabled or disabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2a4c882d-7676-47d6-8db5-7f290ce36589
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method
- EnableDevice method, MSCluster_NetworkInterface class
- MSCluster_NetworkInterface class, EnableDevice method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the MSCluster\_NetworkInterface class

Requests that the LogicalDevice be enabled ("*Enabled* parameter = TRUE) or disabled (= FALSE). If successful, the Device's **StatusInfo** property should also reflect the desired state (enabled/disabled). The return code should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)
</dt> </dl>

 

 





