---
Description: ReceiveConnection
ms.assetid: 'f17e7d93-ac45-4b8a-98c6-0c76ec7117c9'
title: ReceiveConnection
---

# ReceiveConnection

This mechanism enables an output pin to propose a format change to its downstream peer, when the new format requires a larger buffer. The output pin does the following:

1.  Calls [**IPin::ReceiveConnection**](ipin-receiveconnection.md) on the downstream input pin.
2.  If `ReceiveConnection` succeeds, calls [**IMemInputPin::NotifyAllocator**](imeminputpin-notifyallocator.md) on the input pin.

In addition, the output pin may need to call [**IMemAllocator::SetProperties**](imemallocator-setproperties.md) and then decommit and recommit the allocator in order to change buffer sizes. Make sure to deliver all pending samples in the old format before changing the buffer size.

Some MPEG-2 decoders use this mechanism to switch between MPEG-1 and MPEG-2 output or if the video size changes.

 

 



