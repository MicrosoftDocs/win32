---
description: The SO\_EXCLUSIVEADDRUSE socket option prevents other sockets from being forcibly bound to the same address and port.
ms.assetid: ce0d8188-54be-46e8-8753-d0680f690b84
title: SO_EXCLUSIVEADDRUSE socket option (Winsock2.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SO\_EXCLUSIVEADDRUSE socket option

The SO\_EXCLUSIVEADDRUSE socket option prevents other sockets from being forcibly bound to the same address and port.

## Syntax

The SO\_EXCLUSIVEADDRUSE option prevents other sockets from being forcibly bound to the same address and port, a practice enabled by the SO\_REUSEADDR socket option. Such reuse can be executed by malicious applications to disrupt the application. The SO\_EXCLUSIVEADDRUSE option is very useful to system services requiring high availability.

The following code example illustrates setting this option.


```C++
#ifndef UNICODE
#define UNICODE
#endif

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>
#include <stdlib.h>             // Needed for _wtoi

#pragma comment(lib, "Ws2_32.lib")

int __cdecl wmain(int argc, wchar_t ** argv)
{
    WSADATA wsaData;
    int iResult = 0;
    int iError = 0;

    SOCKET s = INVALID_SOCKET;
    SOCKADDR_IN saLocal;
    int iOptval = 0;

    int iFamily = AF_UNSPEC;
    int iType = 0;
    int iProtocol = 0;

    int iPort = 0;

    // Validate the parameters
    if (argc != 5) {
        wprintf(L"usage: %ws <addressfamily> <type> <protocol> <port>\n", argv[0]);
        wprintf(L"    opens a socket for the specified family, type, & protocol\n");
        wprintf(L"    sets the SO_EXCLUSIVEADDRUSE socket option on the socket\n");
        wprintf(L"    then tries to bind the port specified on the command-line\n");
        wprintf(L"%ws example usage\n", argv[0]);
        wprintf(L"   %ws 0 2 17 5150\n", argv[0]);
        wprintf(L"   where AF_UNSPEC=0 SOCK_DGRAM=2 IPPROTO_UDP=17  PORT=5150\n",
                argv[0]);
        wprintf(L"   %ws 2 1 17 5150\n", argv[0]);
        wprintf(L"   where AF_INET=2 SOCK_STREAM=1 IPPROTO_TCP=6  PORT=5150\n", argv[0]);
        wprintf(L"   See the documentation for the socket function for other values\n");
        return 1;
    }

    iFamily = _wtoi(argv[1]);
    iType = _wtoi(argv[2]);
    iProtocol = _wtoi(argv[3]);

    iPort = _wtoi(argv[4]);

    if (iFamily != AF_INET && iFamily != AF_INET6) {
        wprintf(L"Address family must be either AF_INET (2) or AF_INET6 (23)\n");
        return 1;
    }

    if (iPort <= 0 || iPort >= 65535) {
        wprintf(L"Port specified must be greater than 0 and less than 65535\n");
        return 1;
    }
    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        wprintf(L"WSAStartup failed with error: %d\n", iResult);
        return 1;
    }
    // Create the socket
    s = socket(iFamily, iType, iProtocol);
    if (s == INVALID_SOCKET) {
        wprintf(L"socket failed with error: %ld\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }
    // Set the exclusive address option
    iOptval = 1;
    iResult = setsockopt(s, SOL_SOCKET, SO_EXCLUSIVEADDRUSE,
                         (char *) &iOptval, sizeof (iOptval));
    if (iResult == SOCKET_ERROR) {
        wprintf(L"setsockopt for SO_EXCLUSIVEADDRUSE failed with error: %ld\n",
                WSAGetLastError());
    }

    saLocal.sin_family = (ADDRESS_FAMILY) iFamily;
    saLocal.sin_port = htons( (u_short) iPort);
    saLocal.sin_addr.s_addr = htonl(INADDR_ANY);

    // Bind the socket
    iResult = bind(s, (SOCKADDR *) & saLocal, sizeof (saLocal));
    if (iResult == SOCKET_ERROR) {

        // Most errors related to setting SO_EXCLUSIVEADDRUSE
        //    will occur at bind.
        iError = WSAGetLastError();
        if (iError == WSAEACCES)
            wprintf(L"bind failed with WSAEACCES (access denied)\n");
        else
            wprintf(L"bind failed with error: %ld\n", iError);

    } else {
        wprintf(L"bind on socket with SO_EXCLUSIVEADDRUSE succeeded to port: %ld\n",
                iPort);
    }

    // cleanup
    closesocket(s);
    WSACleanup();

    return 0;
}

```



To have any effect, the SO\_EXCLUSIVADDRUSE option must be set before the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function is called (this also applies to the SO\_REUSEADDR option). Table 1 lists the effects of setting the SO\_EXCLUSIVEADDRUSE option. Wildcard indicates binding to the wildcard address, such as 0.0.0.0 for IPv4 and :: for IPv6. Specific indicates binding to a specific interface, such as binding an IP address assigned to an adapter. Specific2 indicates binding to a specific address other than the address bound to in the Specific case.

> [!Note]  
> The Specific2 case is applicable only when the first bind is performed with a specific address; for the case in which the first socket is bound to the wildcard, the entry for Specific covers all specific address cases.

 

For example, consider a computer with two IP interfaces: 10.0.0.1 and 10.99.99.99. If the first bind is to 10.0.0.1 and port 5150 with the SO\_EXCLUSIVEADDRUSE option set, then the second bind to 10.99.99.99 and port 5150 with any or no options set succeeds. However, if the first socket is bound to the wildcard address (0.0.0.0) and port 5150 with SO\_EXCLUSIVEADDRUSE set, any subsequent bind to the same port—regardless of IP address—will fail with either WSAEADDRINUSE (10048) or WSAEACCESS (10013), depending on which options were set on the second bind socket.

### Bind Behavior with Various Options Set



Second bind

First bind

*SO\_EXCLUSIVEADDRUSE*

*No options* or *SO\_REUSEADDR*

*Wildcard*

*Specific*

*Wildcard*

*Specific*

${ROWSPAN3}$*SO\_EXCLUSIVEADDRUSE*${REMOVE}$  

*Wildcard*

Fail (10048)

Fail (10048)

Fail (10048)

Fail (10048)

*Specific*

Fail (10048)

Fail (10048)

Fail (10048)

Fail (10048)

*Specific2*

n/a

Success

n/a

Success

${ROWSPAN3}$*No options*${REMOVE}$  

*Wildcard*

Fail (10048)

Fail (10048)

Fail (10048)

Fail (10048)

*Specific*

Fail (10048)

Fail (10048)

Fail (10048)

Fail (10048)

*Specific2*

n/a

Success

n/a

Success

${ROWSPAN3}$*SO\_REUSEADDR*${REMOVE}$  

*Wildcard*

Fail (10013)

Fail (10013)

Success\*

Success

*Specific*

Fail (10013)

Fail (10013)

Success

Success\*

*Specific2*

n/a

Success

n/a

Success

\* The behavior is undefined as to which socket will receive packets.



 

In the case where the first bind sets no options or SO\_REUSEADDR, and the second bind performs a SO\_REUSEADDR, the second socket has overtaken the port and behavior regarding which socket will receive packets is undetermined. SO\_EXCLUSIVEADDRUSE was introduced to address this situation.

A socket with SO\_EXCLUSIVEADDRUSE set cannot always be reused immediately after socket closure. For example, if a listening socket with the exclusive flag set accepts a connection after which the listening socket is closed, another socket cannot bind to the same port as the first listening socket with the exclusive flag until the accepted connection is no longer active.

This situation can be quite complicated; even though the socket has been closed, the underlying transport may not terminate its connection. Even after the socket is closed, the system must send all of the buffered data, transmit a graceful disconnect to the peer, and wait for a graceful disconnect from the peer. It is therefore possible that the underlying transport may never release the connection, such as when the peer advertises a zero-size window, or other such attacks. In the previous example, the listening socket was closed after a client connection was accepted. Now even if the client connection is closed, the port still may not be reused if the client connection remains in an active state because of unacknowledged data, and so forth.

To avoid this situation, applications should ensure a graceful shutdown: call [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) with the SD\_SEND flag, then wait in a [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) loop until zero bytes are returned. Doing so avoids the problem associated with port reuse, guarantees all data was received by the peer, and assures the peer that all its data was successfully received.

The SO\_LINGER option may be set on a socket to prevent the port going into one of the active wait states; however, doing so is discouraged because it can lead to undesired effects, because it can cause the connection to be reset. For example, if data has been received but not yet acknowledged by the peer, and the local computer closes the socket with SO\_LINGER set, the connection is reset and the peer discards the unacknowledged data. Also, picking a suitable time to linger is difficult; a value too small results in many aborted connections, while a large timeout can leave the system vulnerable to denial of service attacks by establishing many connections, and thereby stalling numerous application threads.

> [!Note]  
> A socket that is using the SO\_EXCLUSIVEADDRUSE option must be shut down properly prior to closing it. Failure to do so can cause a denial of service attack if the associated service needs to restart.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Winsock2.h</dt> </dl> |



 

 




