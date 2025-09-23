---
description: RDMA missing performance counter information for a network adapter.
ms.assetid: e8482b60-484f-46f3-9085-e8fbae3f379f
title: MSFT\_NetAdapter\_RdmaMissingCounterInfo class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_RdmaMissingCounterInfo
- MSFT_NetAdapter_RdmaMissingCounterInfo.ConnectPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.AcceptPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.ConnectFailurePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.ConnectionErrorPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.ActiveConnectionPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairCreatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairClosePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.CompletionQueueCreatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.CompletionQueueClosePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.MemoryRegionCreatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.MemoryRegionClosePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.MemoryWindowCreatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.MemoryWindowClosePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.SharedReceiveQueueCreatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.SharedReceiveQueueClosePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairIncomingReadPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairOutgoingReadPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairIncomingWritePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairOutgoingWritePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairSendPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairReceivePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairBindPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairFastRegisterPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairInvalidatePerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.QueuePairErrorPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.CompletionQueueErrorPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.RDMAInOctetsPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.RDMAOutOctetsPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.RDMAInFramesPerformanceCounterMissing
- MSFT_NetAdapter_RdmaMissingCounterInfo.RDMAOutFramesPerformanceCounterMissing
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_RdmaMissingCounterInfo class

RDMA missing performance counter information for a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_RdmaMissingCounterInfo
{
  boolean ConnectPerformanceCounterMissing;
  boolean AcceptPerformanceCounterMissing;
  boolean ConnectFailurePerformanceCounterMissing;
  boolean ConnectionErrorPerformanceCounterMissing;
  boolean ActiveConnectionPerformanceCounterMissing;
  boolean QueuePairCreatePerformanceCounterMissing;
  boolean QueuePairClosePerformanceCounterMissing;
  boolean CompletionQueueCreatePerformanceCounterMissing;
  boolean CompletionQueueClosePerformanceCounterMissing;
  boolean MemoryRegionCreatePerformanceCounterMissing;
  boolean MemoryRegionClosePerformanceCounterMissing;
  boolean MemoryWindowCreatePerformanceCounterMissing;
  boolean MemoryWindowClosePerformanceCounterMissing;
  boolean SharedReceiveQueueCreatePerformanceCounterMissing;
  boolean SharedReceiveQueueClosePerformanceCounterMissing;
  boolean QueuePairIncomingReadPerformanceCounterMissing;
  boolean QueuePairOutgoingReadPerformanceCounterMissing;
  boolean QueuePairIncomingWritePerformanceCounterMissing;
  boolean QueuePairOutgoingWritePerformanceCounterMissing;
  boolean QueuePairSendPerformanceCounterMissing;
  boolean QueuePairReceivePerformanceCounterMissing;
  boolean QueuePairBindPerformanceCounterMissing;
  boolean QueuePairFastRegisterPerformanceCounterMissing;
  boolean QueuePairInvalidatePerformanceCounterMissing;
  boolean QueuePairErrorPerformanceCounterMissing;
  boolean CompletionQueueErrorPerformanceCounterMissing;
  boolean RDMAInOctetsPerformanceCounterMissing;
  boolean RDMAOutOctetsPerformanceCounterMissing;
  boolean RDMAInFramesPerformanceCounterMissing;
  boolean RDMAOutFramesPerformanceCounterMissing;
};
```

## Members

The **MSFT\_NetAdapter\_RdmaMissingCounterInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_RdmaMissingCounterInfo** class has these properties.

<dl> <dt>

**AcceptPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Accept performance counter missing

</dd> <dt>

**ActiveConnectionPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ActiveConnection performance counter missing

</dd> <dt>

**CompletionQueueClosePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CompletionQueueClose performance counter missing

</dd> <dt>

**CompletionQueueCreatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CompletionQueueCreate performance counter missing

</dd> <dt>

**CompletionQueueErrorPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CompletionQueueError performance counter missing

</dd> <dt>

**ConnectFailurePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ConnectFailure performance counter missing

</dd> <dt>

**ConnectionErrorPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ConnectionError performance counter missing

</dd> <dt>

**ConnectPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Connect performance counter missing

</dd> <dt>

**MemoryRegionClosePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MemoryRegionClose performance counter missing

</dd> <dt>

**MemoryRegionCreatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MemoryRegionCreate performance counter missing

</dd> <dt>

**MemoryWindowClosePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MemoryWindowClose performance counter missing

</dd> <dt>

**MemoryWindowCreatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MemoryWindowCreate performance counter missing

</dd> <dt>

**QueuePairBindPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairBind performance counter missing

</dd> <dt>

**QueuePairClosePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairClose performance counter missing

</dd> <dt>

**QueuePairCreatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairCreate performance counter missing

</dd> <dt>

**QueuePairErrorPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairError performance counter missing

</dd> <dt>

**QueuePairFastRegisterPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairFastRegister performance counter missing

</dd> <dt>

**QueuePairIncomingReadPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairIncomingRead performance counter missing

</dd> <dt>

**QueuePairIncomingWritePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairIncomingWrite performance counter missing

</dd> <dt>

**QueuePairInvalidatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairInvalidate performance counter missing

</dd> <dt>

**QueuePairOutgoingReadPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairOutgoingRead performance counter missing

</dd> <dt>

**QueuePairOutgoingWritePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairOutgoingWrite performance counter missing

</dd> <dt>

**QueuePairReceivePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairReceive performance counter missing

</dd> <dt>

**QueuePairSendPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

QueuePairSend performance counter missing

</dd> <dt>

**RDMAInFramesPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RDMAInFrames performance counter missing

</dd> <dt>

**RDMAInOctetsPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RDMAInOctets performance counter missing

</dd> <dt>

**RDMAOutFramesPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RDMAOutFrames performance counter missing

</dd> <dt>

**RDMAOutOctetsPerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RDMAOutOctets performance counter missing

</dd> <dt>

**SharedReceiveQueueClosePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SharedReceiveQueueClose performance counter missing

</dd> <dt>

**SharedReceiveQueueCreatePerformanceCounterMissing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SharedReceiveQueueCreate performance counter missing

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




