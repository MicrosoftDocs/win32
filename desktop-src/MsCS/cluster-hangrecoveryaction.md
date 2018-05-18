---
title: HangRecoveryAction
description: Specifies the recovery action taken by the cluster service in response to a heartbeat countdown timeout.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6025cf9c-c9ab-498c-9a01-59a6350fd80a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["HangRecoveryAction Failover Cluster ,for clusters", "HangRecoveryAction Failover Cluster"]
topic_type:
- apiref
api_name:
- HangRecoveryAction
api_type:
- NA
---

# HangRecoveryAction

Specifies the recovery action taken by the cluster service in response to a heartbeat countdown timeout.



| Attribute            | Value                                                                                                                                                                                                                                                              |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                                                                                                                                                                                                                               |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                                                                                                                                                                                                                 |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/>                                                                                                                                                                                                               |
| Minimum<br/>   | **WatchdogActionDisable** (0)<br/> **Windows Server 2008 R2:  ClussvcHangActionDisable** (0) is the minimum value.<br/>                                                                                                                                |
| Maximum<br/>   | **WatchdogActionLiveDumpAndTerminateProcess** (6)<br/> **Windows Server 2012:  WatchdogActionDebugBreak** (5) is the maximum value.<br/> **Windows Server 2008 R2:  ClussvcHangActionBugCheckMachine** (3) is the maximum value.<br/>            |
| Default<br/>   | **WatchdogActionLiveDumpAndTerminateProcess** (6)<br/> **Windows Server 2012:  WatchdogActionBugCheckOnlyFromNetFt** (3) is the default value.<br/> **Windows Server 2008 R2:  ClussvcHangActionBugCheckMachine** (3) is the default value.<br/> |



 

## Remarks

The constant for this property is **CLUSTER\_HANG\_RECOVERY\_ACTION\_KEYNAME**.

The Cluster network driver maintains a countdown timer that initiates the **HangRecoveryAction** property when it reaches 0 (zero). Whenever the ClusNet driver receives a Cluster service heartbeat, the countdown time is reset to the [**ClusSvcHeartbeatTimeout**](cluster-clussvcheartbeattimeout.md) property. Additionally, when the Cluster service stops for any reason, the Cluster network driver automatically turns off the countdown timer.

The **HangRecoveryAction** property can be set to the following values.



| Value                                                                                                                                                                 | Description                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WatchdogActionDisable**<br/> **Windows Server 2008 R2:** The name of the value is **ClussvcHangActionDisable**.<br/> 0<br/>                       | NetFt WatchDog: Takes no action.<br/> Core Operations WatchDog: Takes no action.<br/> **Windows Server 2008 R2:** Disables the cluster heartbeat and monitoring mechanism.<br/>                                               |
| **WatchdogActionLog**<br/> **Windows Server 2008 R2:** The name of the value is **ClussvcHangActionLog**.<br/> 1<br/>                               | NetFt WatchDog: Logs a system event.<br/> Core Operations WatchDog: Logs a system event.<br/> **Windows Server 2008 R2:** Log an event in the system log of the event viewer when a heartbeat countdown timeout occurs.<br/>  |
| **WatchdogActionTerminateProcess**<br/> **Windows Server 2008 R2:** The name of the value is **ClussvcHangActionTerminateService**.<br/> 2<br/>     | NetFt WatchDog: Terminates the Cluster service.<br/> Core Operations WatchDog: Terminates the cluster service.<br/> **Windows Server 2008 R2:** Terminate the cluster service when a heartbeat countdown timeout occurs.<br/> |
| **WatchdogActionBugCheckOnlyFromNetFt**<br/> **Windows Server 2008 R2:** The name of the value is **ClussvcHangActionBugCheckMachine**.<br/> 3<br/> | NetFt WatchDog: Bugchecks the machine.<br/> Core Operations WatchDog: Terminates the cluster service.<br/> **Windows Server 2008 R2:** Create a system Stop error (BugCheck) when a heartbeat countdown timeout occurs.<br/>  |
| **WatchdogActionBugCheckAlsoFromProcess**<br/> **:** This value is available starting with Windows Server 2012.<br/> 4<br/>                         | NetFt WatchDog: Bugchecks the machine.<br/> Core Operations WatchDog: Bugchecks the machine.<br/>                                                                                                                                   |
| **WatchdogActionDebugBreak**<br/> **:** This value is available starting with Windows Server 2012.<br/> 5<br/>                                      | NetFt WatchDog: Causes a debug break to occur.<br/> Core Operations WatchDog: Causes a debug break to occur.<br/>                                                                                                                   |
| **WatchdogActionLiveDumpAndTerminateProcess**<br/> **:** This value is available starting with Windows 10, version 1703.<br/> 6<br/>                | NetFt WatchDog: Live dumps and terminates the process.<br/> Core Operations WatchDog: Live dumps and terminates the process.<br/>                                                                                                   |



 

> [!Note]  
> In some extreme cases, system services may also stop responding, and actions 1 and 2 may not succeed. In such cases, action 3 (bugcheck) is the only effective recovery measure.

 

If the action is set to cause a bugcheck on the cluster node, Windows stops responding and you receive the Stop error Bugcheck code of 0x9E. The Stop error causes a failover to another cluster node. Additionally, if the node where the Stop error occurs is configured to capture a memory dump file, you may be able to use the information that is contained in the memory dump file to diagnose the cause of the unresponsive cluster node.

The following code is an example of a stack trace from a Kernel dump that the Cluster network driver initiated:

``` syntax
ChildEBP    RetAddr
f9c33ea8    f6e2e11f    nt!KeBugCheckEx+0x19
f9c33ecc    f6e2e836    clusnet!CnpCheckClussvcHang+0xef
f9c33ef0    805070d7    clusnet!CnpHeartBeatDpc+0x47e
f9c33fa4    8050735d    nt!KiTimerExpiration+0x371
f9c33ff4    80543ccf    nt!KiRetireDpcList+0x63
```

The Bugcheck error code is similar to the following error code: BugCheck 9E, {812d5b08, 3c, 0, 0}

> [!Note]  
> You must manually configure the server to generate a memory dump file in response to a Bugcheck.

 

## Examples

The property value portion of a [property list](property-lists.md) entry for **HangRecoveryAction** can be set with the following example code:


```C++
DWORD          ClusSvcHangActionData = 1;
CLUSPROP_DWORD ClusSvcHangActionValue;

ClusSvcHangActionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ClusSvcHangActionValue.cbLength  = sizeof(DWORD);
ClusSvcHangActionValue.dw        = ClusSvcHangActionData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





