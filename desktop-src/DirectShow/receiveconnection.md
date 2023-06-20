---
description: ReceiveConnection
ms.assetid: '90a6a09a-95e1-4adf-8e0b-269f971aaa67'
title: ReceiveConnection
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ReceiveConnection

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This mechanism enables an output pin to propose a format change to its downstream peer, when the new format requires a larger buffer. The output pin does the following:

1.  Calls [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) on the downstream input pin.
2.  If `ReceiveConnection` succeeds, calls [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) on the input pin.

In addition, the output pin may need to call [**IMemAllocator::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-setproperties) and then decommit and recommit the allocator in order to change buffer sizes. Make sure to deliver all pending samples in the old format before changing the buffer size.

Some MPEG-2 decoders use this mechanism to switch between MPEG-1 and MPEG-2 output or if the video size changes.

 

 



