---
title: SetPowerState method of the Msvm\_ComputerSystem class
description: Deprecated description Sets the power state of the computer.This method is deprecated. Instead, use the RequestPowerStateChange method in the CIM\_PowerManagementService class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ffcb1faf-7eb7-4217-9081-87cc57ff7c53
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, Msvm_ComputerSystem class
- Msvm_ComputerSystem class, SetPowerState method
topic_type:
- apiref
api_name:
- Msvm_ComputerSystem.SetPowerState
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the Msvm\_ComputerSystem class

**Deprecated description:** Sets the power state of the computer.

This method is deprecated. Instead, use the **RequestPowerStateChange** method in the **CIM\_PowerManagementService** class.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint32   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

The new state of the computer system.

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

</dd> <dt>

7
</dt> <dd>

Hibernate

</dd> <dt>

8
</dt> <dd>

Soft Off

</dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

A regular date-time value or an interval value that indicates when to set the power state. If this is property contains an interval value, the interval must begin when the method invocation is received.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> </dl>

 

 





