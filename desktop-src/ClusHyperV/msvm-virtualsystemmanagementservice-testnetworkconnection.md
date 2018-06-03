---
title: TestNetworkConnection method of the Msvm\_VirtualSystemManagementService class
description: Tests the network connectivity of a virtual machine in a Windows Network Virtualization environment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ec16c79-68a1-47be-b3c4-dc3b28711be2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- TestNetworkConnection method
- TestNetworkConnection method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, TestNetworkConnection method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.TestNetworkConnection
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TestNetworkConnection method of the Msvm\_VirtualSystemManagementService class

Tests the network connectivity of a virtual machine in a Windows Network Virtualization environment.

## Syntax


```mof
uint32 TestNetworkConnection(
  [in]  Msvm_EthernetPortAllocationSettingData REF TargetNetworkAdapter,
  [in]  boolean                                    IsSender,
  [in]  string                                     SenderIP,
  [in]  string                                     ReceiverIP,
  [in]  string                                     ReceiverMac,
  [in]  uint32                                     IsolationId,
  [in]  uint32                                     SequenceNumber,
  [out] uint32                                     RoundTripTime,
  [out] CIM_ConcreteJob                        REF Job
);
```



## Parameters

<dl> <dt>

*TargetNetworkAdapter* \[in\]
</dt> <dd>

A reference to the [**Msvm\_EthernetPortAllocationSettingData**](https://msdn.microsoft.com/library/windows/desktop/hh850134) that represents the network adapter of the virtual machine.

</dd> <dt>

*IsSender* \[in\]
</dt> <dd>

**true** if to invoke the method at the sender; otherwise, **false**.

</dd> <dt>

*SenderIP* \[in\]
</dt> <dd>

The IP address of the sender.

</dd> <dt>

*ReceiverIP* \[in\]
</dt> <dd>

The IP address of the receiver.

</dd> <dt>

*ReceiverMac* \[in\]
</dt> <dd>

The MAC address of the receiver.

</dd> <dt>

*IsolationId* \[in\]
</dt> <dd>

The isolation ID.

</dd> <dt>

*SequenceNumber* \[in\]
</dt> <dd>

The sequence number.

</dd> <dt>

*RoundTripTime* \[out\]
</dt> <dd>

The round trip time of the network.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**DMTF Reserved** (5 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





