---
description: Network Direct Interface capabilities supported by a network adapter.
ms.assetid: c5f12fec-5eed-4798-9ec6-c16dfb2e1184
title: MSFT\_NetAdapter\_RdmaAdapterInfo class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_RdmaAdapterInfo
- MSFT_NetAdapter_RdmaAdapterInfo.MajorVersionNumber
- MSFT_NetAdapter_RdmaAdapterInfo.MinorVersionNumber
- MSFT_NetAdapter_RdmaAdapterInfo.VendorId
- MSFT_NetAdapter_RdmaAdapterInfo.DeviceId
- MSFT_NetAdapter_RdmaAdapterInfo.MaxRegistrationSize
- MSFT_NetAdapter_RdmaAdapterInfo.MaxWindowSize
- MSFT_NetAdapter_RdmaAdapterInfo.FRMRPageCount
- MSFT_NetAdapter_RdmaAdapterInfo.MaxInitiatorRequestSge
- MSFT_NetAdapter_RdmaAdapterInfo.MaxReceiveRequestSge
- MSFT_NetAdapter_RdmaAdapterInfo.MaxReadRequestSge
- MSFT_NetAdapter_RdmaAdapterInfo.MaxTransferLength
- MSFT_NetAdapter_RdmaAdapterInfo.MaxInlineDataSize
- MSFT_NetAdapter_RdmaAdapterInfo.MaxInboundReadLimit
- MSFT_NetAdapter_RdmaAdapterInfo.MaxOutboundReadLimit
- MSFT_NetAdapter_RdmaAdapterInfo.MaxReceiveQueueDepth
- MSFT_NetAdapter_RdmaAdapterInfo.MaxInitiatorQueueDepth
- MSFT_NetAdapter_RdmaAdapterInfo.MaxSharedReceiveQueueDepth
- MSFT_NetAdapter_RdmaAdapterInfo.MaxCompletionQueueDepth
- MSFT_NetAdapter_RdmaAdapterInfo.LargeRequestThreshold
- MSFT_NetAdapter_RdmaAdapterInfo.MaxCallerData
- MSFT_NetAdapter_RdmaAdapterInfo.MaxCalleeData
- MSFT_NetAdapter_RdmaAdapterInfo.InOrderDMA
- MSFT_NetAdapter_RdmaAdapterInfo.SupportsCompletionQueueResize
- MSFT_NetAdapter_RdmaAdapterInfo.SupportsLoopbackConnections
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_RdmaAdapterInfo class

Network Direct Interface capabilities supported by a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_RdmaAdapterInfo
{
  uint16  MajorVersionNumber;
  uint16  MinorVersionNumber;
  uint32  VendorId;
  uint32  DeviceId;
  uint64  MaxRegistrationSize;
  uint64  MaxWindowSize;
  uint32  FRMRPageCount;
  uint32  MaxInitiatorRequestSge;
  uint32  MaxReceiveRequestSge;
  uint32  MaxReadRequestSge;
  uint32  MaxTransferLength;
  uint32  MaxInlineDataSize;
  uint32  MaxInboundReadLimit;
  uint32  MaxOutboundReadLimit;
  uint32  MaxReceiveQueueDepth;
  uint32  MaxInitiatorQueueDepth;
  uint32  MaxSharedReceiveQueueDepth;
  uint32  MaxCompletionQueueDepth;
  uint32  LargeRequestThreshold;
  uint32  MaxCallerData;
  uint32  MaxCalleeData;
  boolean InOrderDMA;
  boolean SupportsCompletionQueueResize;
  boolean SupportsLoopbackConnections;
};
```

## Members

The **MSFT\_NetAdapter\_RdmaAdapterInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_RdmaAdapterInfo** class has these properties.

<dl> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vendor defined device ID

</dd> <dt>

**FRMRPageCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Fast-register memory region (FRMR) size (in PAGE\_SIZE pages) for which the adapter supports the most number of FRMRs

</dd> <dt>

**InOrderDMA**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the provider writes incoming data into the client's buffer in order, i.e., the last byte position in the client's buffer is guaranteed not to be updated before any prior byte position.

</dd> <dt>

**LargeRequestThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Data size hint (in bytes) above which read and write operations will yield better results than send and receive operations

</dd> <dt>

**MajorVersionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

NDKPI Major Version Number

</dd> <dt>

**MaxCalleeData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size, in bytes, of the private data that can be sent via an accept or reject request

</dd> <dt>

**MaxCallerData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size, in bytes, of the private data that can be sent via a connect request

</dd> <dt>

**MaxCompletionQueueDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of completion entries per completion queue

</dd> <dt>

**MaxInboundReadLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of in-progress incoming read operations per QP

</dd> <dt>

**MaxInitiatorQueueDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of outstanding requests per initiator queue

</dd> <dt>

**MaxInitiatorRequestSge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of SGEs that can be specified in a single request over an initiator queue

</dd> <dt>

**MaxInlineDataSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum amount of inline data in bytes that can be sent in a single send or write request

</dd> <dt>

**MaxOutboundReadLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of in-progress outgoing read operations per QP

</dd> <dt>

**MaxReadRequestSge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of SGEs that can be specified in a read request (This overrides the MaxInitiatorRequestSge value for read requests.)

</dd> <dt>

**MaxReceiveQueueDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of outstanding requests per receive queue

</dd> <dt>

**MaxReceiveRequestSge**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of SGEs that can be specified in a single request over a receive queue

</dd> <dt>

**MaxRegistrationSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size (in bytes) of a single memory registration that the adapter can address.

</dd> <dt>

**MaxSharedReceiveQueueDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of outstanding requests per shared receive queue. 0 means no SRQ support.

</dd> <dt>

**MaxTransferLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum total length that can be referenced by all SGEs in a single send, receive, read, or write request

</dd> <dt>

**MaxWindowSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size (in bytes) for a single memory window

</dd> <dt>

**MinorVersionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

NDKPI Minor Version Number

</dd> <dt>

**SupportsCompletionQueueResize**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the provider supports resizing CQ objects or not. If this is false, CQ resize request must NOT be used by the NDK client.

</dd> <dt>

**SupportsLoopbackConnections**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the provider supports loopback connections (from a local network address on a given RNIC to the same local address on the same RNIC).

</dd> <dt>

**VendorId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Vendor's organizational unique identifier (OUI)

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




