---
description: Many applications depend on the timing relationship between media events (for example, DTMF digits received) to determine the nature of a requested operation.
ms.assetid: 8d25a31f-de40-4c74-b8e7-a81fbfd47db2
title: Media Event Timers
ms.topic: article
ms.date: 05/31/2018
---

# Media Event Timers

Many applications depend on the timing relationship between media events (for example, DTMF digits received) to determine the nature of a requested operation. For example, in a voice mail application, two consecutive DTMF "1" digits may mean "back up two segments" or "replay from beginning of message", depending on how much time elapsed between the two digits. In a client/server environment, if the DTMF detection is being performed on a separate processor from the one on which the application is running, latency in the local area network makes it very likely that the timing relationship between media events will be skewed, with the result that these timing-based differences could be lost or become unreliable.

To resolve this issue, several TAPI messages can be timestamped. Because it is the relative timing between these events that is important, the "clock time" of the event is not important, and sub-second timing is involved, these timestamps use the millisecond-resolution "time since Windows started" returned by the [**GetTickCount**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-gettickcount) function. Applications must be aware that this is the tick count on the server (or machine where the service provider directly managing the hardware is running), and is not necessarily the same machine on which the application is executing; thus, the timestamps in these TAPI messages can only be compared to each other, and not to the value returned by **GetTickCount** on the processor on which the application is running.

The TAPI messages that can be timestamped are: [**LINE\_GATHERDIGITS**](line-gatherdigits.md), [**LINE\_GENERATE**](line-generate.md), [**LINE\_MONITORDIGITS**](line-monitordigits.md), [**LINE\_MONITORMEDIA**](line-monitormedia.md), and [**LINE\_MONITORTONE**](line-monitortone.md). The tick count is inserted into *dwParam3* of these messages. If timestamping is not supported by the service provider (which is indicated by the service provider setting *dwParam3* in these messages to 0), then TAPI itself will insert the tick count into *dwParam3* of all of these messages (it can be skewed somewhat, but less than if the application did the same after the messages had traversed an interprocess communication scheme).

 

 
