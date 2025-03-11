---
description: RDMA statistics supported by a network adapter.
ms.assetid: 776258f7-89c0-44d6-aee1-037b2cc3e81a
title: MSFT\_NetAdapter\_RdmaStatistics class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_RdmaStatistics
- MSFT_NetAdapter_RdmaStatistics.InitiatedConnections
- MSFT_NetAdapter_RdmaStatistics.AcceptedConnections
- MSFT_NetAdapter_RdmaStatistics.FailedConnectionAttempts
- MSFT_NetAdapter_RdmaStatistics.ConnectionErrors
- MSFT_NetAdapter_RdmaStatistics.ActiveConnections
- MSFT_NetAdapter_RdmaStatistics.CreatedQueuePairs
- MSFT_NetAdapter_RdmaStatistics.ClosedQueuePairs
- MSFT_NetAdapter_RdmaStatistics.CreatedCompletionQueues
- MSFT_NetAdapter_RdmaStatistics.ClosedCompletionQueues
- MSFT_NetAdapter_RdmaStatistics.CreatedMemoryRegions
- MSFT_NetAdapter_RdmaStatistics.ClosedMemoryRegions
- MSFT_NetAdapter_RdmaStatistics.CreatedMemoryWindows
- MSFT_NetAdapter_RdmaStatistics.ClosedMemoryWindows
- MSFT_NetAdapter_RdmaStatistics.CreatedSharedReceiveQueues
- MSFT_NetAdapter_RdmaStatistics.ClosedSharedReceiveQueues
- MSFT_NetAdapter_RdmaStatistics.InboundReadRequests
- MSFT_NetAdapter_RdmaStatistics.OutboundReadRequests
- MSFT_NetAdapter_RdmaStatistics.InboundWriteRequests
- MSFT_NetAdapter_RdmaStatistics.OutboundWriteRequests
- MSFT_NetAdapter_RdmaStatistics.SendRequests
- MSFT_NetAdapter_RdmaStatistics.ReceiveRequests
- MSFT_NetAdapter_RdmaStatistics.BindRequests
- MSFT_NetAdapter_RdmaStatistics.FastRegisterRequests
- MSFT_NetAdapter_RdmaStatistics.InvalidateRequests
- MSFT_NetAdapter_RdmaStatistics.QueuePairErrors
- MSFT_NetAdapter_RdmaStatistics.CompletionQueueErrors
- MSFT_NetAdapter_RdmaStatistics.InboundBytes
- MSFT_NetAdapter_RdmaStatistics.OutboundBytes
- MSFT_NetAdapter_RdmaStatistics.InboundFrames
- MSFT_NetAdapter_RdmaStatistics.OutboundFrames
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_RdmaStatistics class

RDMA statistics supported by a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetAdapter_RdmaStatistics
{
  uint64 InitiatedConnections;
  uint64 AcceptedConnections;
  uint64 FailedConnectionAttempts;
  uint64 ConnectionErrors;
  uint64 ActiveConnections;
  uint64 CreatedQueuePairs;
  uint64 ClosedQueuePairs;
  uint64 CreatedCompletionQueues;
  uint64 ClosedCompletionQueues;
  uint64 CreatedMemoryRegions;
  uint64 ClosedMemoryRegions;
  uint64 CreatedMemoryWindows;
  uint64 ClosedMemoryWindows;
  uint64 CreatedSharedReceiveQueues;
  uint64 ClosedSharedReceiveQueues;
  uint64 InboundReadRequests;
  uint64 OutboundReadRequests;
  uint64 InboundWriteRequests;
  uint64 OutboundWriteRequests;
  uint64 SendRequests;
  uint64 ReceiveRequests;
  uint64 BindRequests;
  uint64 FastRegisterRequests;
  uint64 InvalidateRequests;
  uint64 QueuePairErrors;
  uint64 CompletionQueueErrors;
  uint64 InboundBytes;
  uint64 OutboundBytes;
  uint64 InboundFrames;
  uint64 OutboundFrames;
};
```

## Members

The **MSFT\_NetAdapter\_RdmaStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_RdmaStatistics** class has these properties.

<dl> <dt>

**AcceptedConnections**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of RDMA connections accepted

</dd> <dt>

**ActiveConnections**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of currently active RDMA connections

</dd> <dt>

**BindRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bind requests

</dd> <dt>

**ClosedCompletionQueues**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of completion queues closed

</dd> <dt>

**ClosedMemoryRegions**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of memory regions closed

</dd> <dt>

**ClosedMemoryWindows**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of memory windows closed

</dd> <dt>

**ClosedQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of queue pairs closed

</dd> <dt>

**ClosedSharedReceiveQueues**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of shared receive queues closed

</dd> <dt>

**CompletionQueueErrors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of completion queues that went into error state

</dd> <dt>

**ConnectionErrors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of RDMA connections that were torn down due to an error

</dd> <dt>

**CreatedCompletionQueues**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of completion queues created

</dd> <dt>

**CreatedMemoryRegions**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of memory regions created

</dd> <dt>

**CreatedMemoryWindows**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of memory windows created

</dd> <dt>

**CreatedQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of queue pairs created

</dd> <dt>

**CreatedSharedReceiveQueues**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of shared receive queues created

</dd> <dt>

**FailedConnectionAttempts**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of failed RDMA connection attempts

</dd> <dt>

**FastRegisterRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of fast-register requests

</dd> <dt>

**InboundBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of layer2 bytes that carry inbound RDMA traffic

</dd> <dt>

**InboundFrames**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of layer2 frames that carry inbound RDMA traffic

</dd> <dt>

**InboundReadRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of inbound read requests

</dd> <dt>

**InboundWriteRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of inbound write requests

</dd> <dt>

**InitiatedConnections**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of RDMA connections initiated

</dd> <dt>

**InvalidateRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of invalidate requests

</dd> <dt>

**OutboundBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of layer2 bytes that carry outbound RDMA traffic

</dd> <dt>

**OutboundFrames**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of layer2 frames that carry outbound RDMA traffic

</dd> <dt>

**OutboundReadRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of outbound read requests

</dd> <dt>

**OutboundWriteRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of outbound write requests

</dd> <dt>

**QueuePairErrors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of queue pairs that went into error state

</dd> <dt>

**ReceiveRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of receive requests

</dd> <dt>

**SendRequests**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of send requests

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




