---
title: Protocol Rollover
description: Protocol Rollover
ms.assetid: 61db5e2b-4858-446e-9a27-e0305b46683d
keywords:
- Windows Media Format SDK,protocol rollover
- Advanced Systems Format (ASF),protocol rollover
- ASF (Advanced Systems Format),protocol rollover
- protocol rollover
ms.topic: article
ms.date: 05/31/2018
---

# Protocol Rollover

Protocol rollover is a process whereby the reader object discovers the best streaming protocol available from a server. The reader uses protocol rollover whenever it opens a URL that contains an "mms" scheme.

The reader supports several protocols:

-   Real Time Streaming Protocol (RTSP)
-   Hypertext Transfer Protocol (HTTP)
-   Microsoft Media Server (MMS)

The RTSP and MMS protocols both come in two flavors, one using [*UDP*](wmformat-glossary.md) as the underlying delivery protocol, and the other using TCP.

The reader object always uses TCP for playback control commands, but it can use either TCP or UDP for delivery of the streamed content. UDP is preferred for content delivery, because it imposes less bandwidth overhead than TCP. The TCP protocol ensures reliable transport through the use of "virtual circuits," but the cost of doing so means that TCP is not as well suited for digital media streams, where efficient use of bandwidth is more important that occasional lost packets.

When a URL specifies "mms://", the reader attempts to use the following protocols for data delivery, in the following order:

1.  RTSPU (RTSP using UDP)
2.  RTSPT (RTSP using TCP)
3.  MMSU (MMS using UDP)
4.  MMST (MMS using TCP)
5.  HTTP

HTTP is a one-way protocol based on TCP, and is the protocol used by Web servers. Streaming with HTTP is less efficient that using RTSP. However, most firewalls are configured to accept HTTP requests, whereas they typically reject other streaming protocols.

Windows Media Services 9 Series in Microsoft Windows Server 2003 will reject any MMSU or MMST requests from a Windows Media Format SDK reader, because RTSP is the preferred streaming protocol. Windows Media Services version 4.1 and earlier do not support RTSP. In this case the reader object falls back to MMSU or HTTP.

Protocol rollover does not apply if the URL scheme gives a specific protocol, such as "rtspu://" for RTSPU or "https://" for HTTP. If the URL scheme is "rtsp://", the reader tries RTSPU and RTSPT, but no others.

After the reader opens a file, you can query which protocol it is using by calling the [**IWMReaderAdvanced2::GetProtocolName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getprotocolname) method on the reader. While the content is being streamed or downloaded, this method returns the name as soon as the content is completely cached, the **GetProtocolName** method returns the string "Cache."

To get the names of all the Windows Media server protocols that the reader supports, call the [**IWMReaderNetworkConfig::GetSupportedProtocolName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-getsupportedprotocolname) method on the reader. You can disable one or more of the protocols in the reader's protocol rollover list, using **IWMReaderNetworkConfig** interface. For example, the [**IWMReaderNetworkConfig::SetEnableTCP**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-setenabletcp) method enables or disables the TCP-based protocols, and [**IWMReaderNetworkConfig::SetEnableUDP**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-setenableudp) enables or disables the UDP-based protocols. These methods apply only to protocol rollover; the protocols are still available if the URL scheme contains a specific protocol. There is usually no reason to disable any of the protocols used in protocol rollover; doing so can degrade performance. However, it might be useful for testing.

 

 




