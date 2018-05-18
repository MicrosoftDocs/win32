---
title: SetPowerState method of the CIM\_UnitaryComputerSystem class
description: SetPowerState defines the desired power state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2582163d-98a3-4748-834e-322b6f63727e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetPowerState method", "SetPowerState method, CIM_UnitaryComputerSystem class", "CIM_UnitaryComputerSystem class, SetPowerState method"]
---

# SetPowerState method of the CIM\_UnitaryComputerSystem class

SetPowerState defines the desired power state of a ComputerSystem and its running OperatingSystem, and when the system should be put into that state. The PowerState parameter is specified as one of the valid integer values defined for the property, PowerState. The Time parameter (for all state changes but 5, "Power Cycle") indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the PowerState parameter is equal to 5, "Power Cycle", the Time parameter indicates when the system should power on again. Power off is immediate.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Time* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Return value

Returns 0 if successful, 1 if the specified *PowerState* and *Time* values are not supported, or some other value if any other error occurred.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md)
</dt> </dl>

 

 





