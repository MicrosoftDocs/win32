---
description: The baseline version of a very poor performing application in Windows Sockets (Winsock).
ms.assetid: 923884c4-f1bd-4f72-983e-6158f368e0dd
title: 'The Baseline Version: A Very Poor Performing Application'
ms.topic: article
ms.date: 05/31/2018
---

# The Baseline Version: A Very Poor Performing Application

The initial, poor performing code sample used to calculate the updates is as follows:

> [!Note]  
> For simplicity, there is no error handling in the following examples. Any production application always checks return values.

 

> [!WARNING]
> The first few examples of the application provide intentionally poor performance, in order to illustrate performance improvements possible with changes to code. Do not use these code samples in your application; they are for illustration purposes only.

 


```C++
#include <windows.h>

BOOL Map[ROWS][COLS];

void LifeUpdate()
{
    ComputeNext( Map );
    for( int i = 0 ; i < ROWS ; ++i )     //serialized
        for( int j = 0 ; j < COLS ; ++j )
            Set( i, j, Map[i][j] );    //chatty
}

BYTE Set(row, col, bAlive)
{
    SOCKET s = socket(...);
    BYTE byRet = 0;
    setsockopt( s, SO_SNDBUF, &Zero, sizeof(int) );
    bind( s, ... );
    connect( s, ... );
    send( s, &row, 1 );
    send( s, &col, 1 );
    send( s, &bAlive, 1 );
    recv( s, &byRet, 1 );
    closesocket( s );
    return byRet;
}
```



In this state, the application has the worst possible network performance. The problems with this version of the sample application include:

-   The application is chatty. Each transaction is too small — cells do not need to be updated one by one.
-   The transactions are strictly serialized, even though the cells could be updated concurrently.
-   The send buffer is set to zero, and the application incurs a 200-millisecond delay for each send — three times per cell.
-   The application is very connect heavy, connecting once for each cell. Applications are limited in the number of connections per second for a given destination because of TIME-WAIT state, but that is not an issue here, since each transaction takes over 600 milliseconds.
-   The application is fat; many transactions have no effect on the server state, because many cells do not change from update to update.
-   The application exhibits poor streaming; small sends consume a lot of CPU and RAM.
-   The application assumes little-endian representation for its sends. This is a natural assumption for the current Windows platform, but can be dangerous for long-lived code.

## Key Performance Metrics

The following performance metrics are expressed in Round Trip Time (RTT), Goodput, and Protocol Overhead. See the [Network Terminology](network-terminology-2.md) topic for an explanation of these terms.

-   Cell time, network time for a single cell update, requires 4\*RTT + 600 milliseconds for Nagle and delayed ACK interactions.
-   Goodput is less than 6 bytes.
-   Protocol Overhead is 99.6%.

## Related topics

<dl> <dt>

[Improving a Slow Application](improving-a-slow-application-2.md)
</dt> <dt>

[Network Terminology](network-terminology-2.md)
</dt> <dt>

[Revision 1: Cleaning up the Obvious](revision-1-cleaning-up-the-obvious-2.md)
</dt> <dt>

[Revision 2: Redesigning for Fewer Connects](revision-2-redesigning-for-fewer-connects-2.md)
</dt> <dt>

[Revision 3: Compressed Block Send](revision-3-compressed-block-send-2.md)
</dt> <dt>

[Future Improvements](future-improvements-2.md)
</dt> </dl>

 

 



