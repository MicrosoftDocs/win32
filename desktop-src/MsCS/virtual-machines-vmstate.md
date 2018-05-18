---
title: VmState
description: Mirrors the EnabledState property of the Msvm\_ComputerSystem class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '78d7bd69-411e-4b1d-a5b9-f2e596306920'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["VmState Failover Cluster ,for virtual machines", "VmState Failover Cluster"]
topic_type:
- apiref
api_name:
- VmState
api_type:
- NA
---

# VmState

Mirrors the **EnabledState** property of the [**Msvm\_ComputerSystem**](https://msdn.microsoft.com/library/cc136822) class. The following table summarizes the attributes of the **VmState** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | TBD                                       |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 65536                                     |
| Default   | 0                                         |



 

## Remarks

The following table summarizes the values for **VmState**.



| Name                 | Value                  | Description                                             |
|----------------------|------------------------|---------------------------------------------------------|
| Unknown<br/>   | 0 (Default)<br/> | The state of the VM could not be determined.<br/> |
| Enabled<br/>   | 2<br/>           | The VM is running.<br/>                           |
| Disabled<br/>  | 3<br/>           | The VM is turned off.<br/>                        |
| Paused<br/>    | 32768<br/>       | The VM is paused.<br/>                            |
| Suspended<br/> | 32769<br/>       | The VM is in a saved state.<br/>                  |
| Starting<br/>  | 32770<br/>       | The VM is starting.<br/>                          |
| Saving<br/>    | 32773<br/>       | The VM is saving its state.<br/>                  |
| Stopping<br/>  | 32774<br/>       | The VM is turning off.<br/>                       |
| Pausing<br/>   | 32776<br/>       | The VM is pausing.<br/>                           |
| Resuming<br/>  | 32777<br/>       | The VM is resuming from a paused state.<br/>      |



 

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**Msvm\_ComputerSystem**](https://msdn.microsoft.com/library/cc136822)
</dt> </dl>

 

 





