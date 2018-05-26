---
title: EnableDevice method of the CIM\_LogicalDevice class
description: Requests that the LogicalDevice be enabled or disabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74ae659c-2d29-4b93-a63a-4d7ca9409435
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableDevice method
- EnableDevice method, CIM_LogicalDevice class
- CIM_LogicalDevice class, EnableDevice method
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.EnableDevice
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableDevice method of the CIM\_LogicalDevice class

Requests that the LogicalDevice be enabled or disabled. If successful, the Device's **StatusInfo** property should also reflect the desired state (enabled/disabled). The return code should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

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

**TRUE** if the device is to be enabled, **FALSE** if the device is to be disabled.

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

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

 





