---
description: In this revision, the sample application is redesigned to eliminate unnecessary connects.
ms.assetid: 0db6ded4-0a59-454e-824e-8cd7f0dc9fec
title: 'Revision Two: Redesigning for Fewer Connects'
ms.topic: article
ms.date: 05/31/2018
---

# Revision Two: Redesigning for Fewer Connects

In this revision, the sample application is redesigned to eliminate unnecessary connects.

> [!WARNING]
> This examples of the application also provide intentionally poor performance, in order to illustrate performance improvements possible with changes to code. Do not use this code sample in your application; it is for illustration purposes only.

 


```C++
ComputeNext( Map );
bind( s, ... );
connect( s, ... );
for(int i=0 ; i < ROWS ; ++i)
  for(int j=0 ; j < COLS ; ++j)
  {
    BYTE tmp[3];
    tmp[0] = i;
    tmp[1] = j;
    tmp[2] = Map[i][j];
    send( s, tmp, 3 );
    recv( s, &byRet, 1 );
  }
closesocket( s );
```



## Remaining Problems

The changes in Revision Two redesigned the application to make only one connect per update. The application still includes the following performance issues:

-   The application is still serialized and chatty.
-   The application still has a fat design; there are many sends that require no operation in this design.
-   The sends are still only 3 bytes, which is poor streaming.

## Key Performance Metrics

The following performance metrics are expressed in Round Trip Time (RTT), Goodput, and Protocol Overhead. See the [Network Terminology](network-terminology-2.md) topic for an explanation of these terms.

This version reflects the following performance metrics:

-   Cell Time — 1\*RTT
-   Goodput — 4 bytes/RTT
-   Protocol Overhead — 96.8%

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

[Revision 3: Compressed Block Send](revision-3-compressed-block-send-2.md)
</dt> <dt>

[Future Improvements](future-improvements-2.md)
</dt> </dl>

 

 



