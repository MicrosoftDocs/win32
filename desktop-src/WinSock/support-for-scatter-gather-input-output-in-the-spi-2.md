---
description: The WSPSend, WSPSendTo, WSPRecv, and WSPRecvFrom routines all take an array of client buffers as input parameters and thus may be used for scatter/gather (or vectored) I/O.
ms.assetid: ecd3d2f1-74b1-42f7-8402-3170112e3aca
title: Support for Scatter/Gather Input/Output in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Support for Scatter/Gather Input/Output in the SPI

The [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)), [**WSPSendTo**](/previous-versions/windows/desktop/legacy/ms742291(v=vs.85)), [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)), and [**WSPRecvFrom**](/previous-versions/windows/desktop/legacy/ms742287(v=vs.85)) routines all take an array of client buffers as input parameters and thus may be used for scatter/gather (or vectored) I/O. This can be very useful in instances where portions of each message being transmitted consist of one or more fixed length header components in addition to a message body. Such header components need not be concatenated into a single contiguous buffer prior to sending. Likewise on receiving, the header components can be automatically split off into separate buffers, leaving the message body pure.

Utilizing lists of buffers instead of a single buffer does not change the boundaries that apply to receive operations. For message-oriented protocols, a receive operation completes whenever a single message has been received, regardless of how many or few of the supplied buffers were used. Likewise for stream-oriented protocols, a receive completes when an unspecified quantity of bytes arrives over the network, not necessarily when all of the supplied buffers are full.

 

 
