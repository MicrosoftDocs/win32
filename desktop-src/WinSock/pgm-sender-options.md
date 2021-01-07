---
description: PGM senders are provided with certain default settings that affect the performance of data transmission, and how long data is buffered to account for packet loss and associated PGM client retransmission requests.
ms.assetid: 56b15eac-ea0d-4d18-b5f6-2f1a7b1bb25f
title: PGM Sender Options
ms.topic: article
ms.date: 05/31/2018
---

# PGM Sender Options

PGM senders are provided with certain default settings that affect the performance of data transmission, and how long data is buffered to account for packet loss and associated PGM client retransmission requests. The following paragraphs describe these default settings.

## Window Size and Transmission Rate

The capability to set window size and transmission rate enables applications to control the amount of data the transport buffers for retransmission, and the rate at which the byte-stream is transmitted.

Retransmission data is stored in a file, therefore the maximum window size is limited by disk space usable by the transport. The default window size is 10MB. Although it is possible for a send or message size to exceed the window or buffer size, the data stream remain uninterrupted; the send is pended until the all the data has been sent out.

> [!Note]  
> The maximum buffer space is limited by the maximum number of packets that can be held in the window at any given time, which is equal to 2^31 – 1.

 

The transmission rate is the combined outflow of original data packets (ODATA), retransmitted data packets (RDATA) and transport-specific bookkeeping packets (SPMs), expressed per second. If the rate limit is set to 56 kilobits per sec by default. The default window size is 10 megabytes, with a default rate of 56 kilobits per second. Due to the relationship between the three members of the [**RM\_SEND\_WINDOW**](/windows/desktop/api/Wsrm/ns-wsrm-rm_send_window) structure, the default window size is therefore 1428 seconds. See **RM\_SEND\_WINDOW** for more information.

## Window Advance Rate

The window advance rate is set by the [RM\_SENDER\_WINDOW\_ADV\_RATE](socket-options.md) socket option. This option enables applications to specify the increment at which the PGM sender's window is advanced, expressed as a nonzero percentage value of the window size. The default value is 15%, and the maximum rate is 50%. If the PGM sender has repair data pending that falls in the space of the increment window, the window is advanced partially as each repair packet in the window is sent out.

## Forward Error Correction (FEC)

Forward error correction is set through use of the RM\_USE\_FEC socket option. This socket option enables the PGM sender to send repair packets as parity packets instead of regular data packets. Doing so minimizes the number of repair packets sent to repair different sequences lost by multiple receivers from within the same data group. Enabling FEC is only set on the PGM sender. PGM receivers automatically follow the policy set by the sender. For a detailed discussion on FEC, refer to the PGM RFC located on the [IETF](https://www.ietf.org/) website.

 

 



