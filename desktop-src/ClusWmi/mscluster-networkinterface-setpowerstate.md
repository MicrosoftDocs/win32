---
title: SetPowerState method of the MSCluster\_NetworkInterface class
description: Defines the desired power state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4aa000a9-f189-4ef6-b9b0-2a165bfe43a9
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, MSCluster_NetworkInterface class
- MSCluster_NetworkInterface class, SetPowerState method
topic_type:
- apiref
api_name:
- MSCluster_NetworkInterface.SetPowerState
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPowerState method of the MSCluster\_NetworkInterface class

Defines the desired power state. The desired power state is specified by setting the *PowerState* parameter to one of the following integer values: 1="Full Power", 2="Power Save - Low Power Mode", 3="Power Save - Standby", 4="Power Save - Other", 5="Power Cycle" or 6="Power Off". The *Time* parameter (for all state changes but 5, "Power Cycle") indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the *PowerState* parameter is equal to 5, "Power Cycle", the *Time* parameter indicates when the Device should power on again. Power off is immediate. **SetPowerState** should return 0 if successful, 1 if the specified *PowerState* and *Time* request is not supported, and some other value if any other error occurred.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

<dt>

1
</dt> <dd>

Full Power

</dd> <dt>

2
</dt> <dd>

Power Save - Low Power Mode

</dd> <dt>

3
</dt> <dd>

Power Save - Standby

</dd> <dt>

4
</dt> <dd>

Power Save - Other

</dd> <dt>

5
</dt> <dd>

Power Cycle

</dd> <dt>

6
</dt> <dd>

Power Off

</dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd></dd> </dl>

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

 

 





