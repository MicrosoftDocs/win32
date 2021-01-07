---
description: In this version of the example program, a few obvious changes have been made that will take initial strides at improving performance.
ms.assetid: ef9d594c-31fe-44c0-b707-47c01e2c5bf0
title: 'Revision One: Cleaning up the Obvious'
ms.topic: article
ms.date: 05/31/2018
---

# Revision One: Cleaning up the Obvious

In this version of the example program, a few obvious changes have been made that will take initial strides at improving performance. This version of the code is far from performance-tuned, but it is a good incremental step that enables examination of the effects of incrementally better approaches.

> [!WARNING]
> This example of the application provides intentionally poor performance, in order to illustrate performance improvements possible with changes to code. Do not use this code sample in your application; it is for illustration purposes only.

 


```C++
#include <windows.h>

BYTE Set(row, col, bAlive)
{
    SOCKET s = socket(...);
    BYTE byRet = 0;
    BYTE tmp[3];
    tmp[0] = (BYTE)row;
    tmp[1] = (BYTE)col;
    tmp[2] = (BYTE)bAlive;
    bind( s, ... );
    connect( s, ... );
    send( s, &tmp, 3 );
    recv( s, &byRet, 1 );
    closesocket( s );
    return byRet;
}
```



## Changes in this Version

This version reflects the following changes:

-   Removed SNDBUF=0. The 200 millisecond delays due to unbuffered sends and delayed acknowledgments are removed.
-   Removed the Send-Send-Receive behavior. This change eliminates 200-millisecond delays due to Nagle and delayed ACK interactions.
-   Removed little-endian assumption. The bytes are now in order.

## Remaining Problems

In this version, the following problems remain:

-   The application is still connect heavy. Since the 600+ millisecond delays are removed, the application now hits the 12 connects-per-second sustained rate. Many concurrent connections now becomes an issue.
-   The application is still fat; unchanged cells are still propagated to the server.
-   The application still exhibits poor streaming; 3-byte sends are still small sends.
-   The application now sends 2 bytes/RTT, which equals 4 KB/s on directly connected Ethernet. This is not too fast, but TIME-WAIT will likely cause problems first.
-   The overhead is down to 99.3%, which is still not a good overhead percentage.

## Key Performance Metrics

The following key performance metrics are expressed in Round Trip Time (RTT), Goodput, and Protocol Overhead. See the [Network Terminology](network-terminology-2.md) topic for an explanation of these terms.

This version reflect the following performance metrics:

-   Cell Time—2×RTT
-   Goodput—2 bytes/RTT
-   Protocol Overhead—99.3 percent

## Related topics

<dl> <dt>

[Improving a Slow Application](improving-a-slow-application-2.md)
</dt> <dt>

[Network Terminology](network-terminology-2.md)
</dt> <dt>

[The Baseline Version: A Very Poor Performing Application](the-baseline-version-a-very-poor-performing-application-2.md)
</dt> <dt>

[Revision 2: Redesigning for Fewer Connects](revision-2-redesigning-for-fewer-connects-2.md)
</dt> <dt>

[Revision 3: Compressed Block Send](revision-3-compressed-block-send-2.md)
</dt> <dt>

[Future Improvements](future-improvements-2.md)
</dt> </dl>

 

 



