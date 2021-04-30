---
description: ReceiveConnection
ms.assetid: '90a6a09a-95e1-4adf-8e0b-269f971aaa67'
title: ReceiveConnection
ms.topic: article
ms.date: 05/31/2018
---

# ReceiveConnection

This mechanism enables an output pin to propose a format change to its downstream peer, when the new format requires a larger buffer. The output pin does the following:

1.  Calls [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) on the downstream input pin.
2.  If `ReceiveConnection` succeeds, calls [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) on the input pin.

In addition, the output pin may need to call [**IMemAllocator::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-setproperties) and then decommit and recommit the allocator in order to change buffer sizes. Make sure to deliver all pending samples in the old format before changing the buffer size.

Some MPEG-2 decoders use this mechanism to switch between MPEG-1 and MPEG-2 output or if the video size changes.

 

 



