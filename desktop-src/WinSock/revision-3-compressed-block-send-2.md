---
description: In this version of the application, a compressed block send of the data is used. This change results in significant performance improvement.
ms.assetid: 3f0a129b-5b67-4334-a0aa-cd80ee7018b9
title: 'Revision Three: Compressed Block Send'
ms.topic: article
ms.date: 05/31/2018
---

# Revision Three: Compressed Block Send

In this version of the application, a compressed block send of the data is used. This change results in significant performance improvement.


```C++
BYTE tmp[3*ROWS*COLS];
FIELD Old = Map;
ComputeNext( Map );
n=Compact(Map,Old,tmp);
bind( s, ... );
connect( s, ... );
send( s, tmp, 3*n );
//can't do recv(s,tmp,n)
for(int i=0; i < n; )
    recv( s, tmp+i, n-i );
closesocket( s );
```



## Changes in this Version

This version reflects the following changes:

-   Cell updates are no longer serialized.
-   Since a block send is used, the application is no longer chatty.
-   Data compression is used, resulting in a less fat application.

There is still an issue with this version of the application; the risk of deadlock exists since a large send is used with no receives. The server sends one byte for every 3 bytes received. This could cause a deadlock if the receive buffer size is less than 1000 bytes for this sample application.

## Key Performance Metrics

The following performance metrics are expressed in Round Trip Time (RTT), Goodput, and Protocol Overhead. See the [Network Terminology](network-terminology-2.md) topic for an explanation of these terms.

This version reflects the following performance metrics:

-   Cell Time — .002\*RTT
-   Goodput — 2 Kilobytes/RTT
-   Protocol Overhead — 14%

Of the 14% overhead, 6% is from the Ethernet headers and the other 8% is from the connection startup and teardown.

## Related topics

<dl> <dt>

[Improving a Slow Application](improving-a-slow-application-2.md)
</dt> <dt>

[Network Terminology](network-terminology-2.md)
</dt> <dt>

[The Baseline Version: A Very Poor Performing Application](the-baseline-version-a-very-poor-performing-application-2.md)
</dt> <dt>

[Revision 1: Cleaning up the Obvious](revision-1-cleaning-up-the-obvious-2.md)
</dt> <dt>

[Revision 2: Redesigning for Fewer Connects](revision-2-redesigning-for-fewer-connects-2.md)
</dt> <dt>

[Future Improvements](future-improvements-2.md)
</dt> </dl>

 

 



