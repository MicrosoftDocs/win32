---
description: Tests the network connectivity of a VM in a Windows network virtualization environment.
ms.assetid: 37d4c34d-406e-4c52-afce-b0eef754eeb3
title: TestNetworkConnection method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.TestNetworkConnection
api_type: 
- COM
api_location: 
- vmms.exe
---

# TestNetworkConnection method of the Msvm\_VirtualSystemManagementService class

Tests the network connectivity of a VM in a Windows network virtualization environment.

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

Reference to a [**Msvm\_EthernetPortAllocationSettingData**](msvm-ethernetportallocationsettingdata.md) describing the target network adapter.

</dd> <dt>

*IsSender* \[in\]
</dt> <dd>

Indicates whether this method is being invoked at the sender or the receiver.

</dd> <dt>

*SenderIP* \[in\]
</dt> <dd>

The sender IP address.

</dd> <dt>

*ReceiverIP* \[in\]
</dt> <dd>

The sender Mac address.

</dd> <dt>

*ReceiverMac* \[in\]
</dt> <dd>

The sender Mac address.

</dd> <dt>

*IsolationId* \[in\]
</dt> <dd>

The Isolation ID.

</dd> <dt>

*SequenceNumber* \[in\]
</dt> <dd>

The Isolation ID.

</dd> <dt>

*RoundTripTime* \[out\]
</dt> <dd>

The round trip time.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

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

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097..32767)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

