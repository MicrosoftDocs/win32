---
description: Using Secure Socket Extensions
ms.assetid: 'd5e2f9d0-c61f-42d3-b62b-6c75b221ae24'
title: Using Secure Socket Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Using Secure Socket Extensions

The following example code demonstrates the usage of the Winsock secure socket extension functions.

## Securing a Socket


```C++
#define WIN32_LEAN_AND_MEAN

#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <winsock2.h>
#include <mstcpip.h>
#include <ws2tcpip.h>
#include <rpc.h>
#include <ntdsapi.h>
#include <stdio.h>
#include <tchar.h>

#define RECV_DATA_BUF_SIZE 256

// Link with ws2_32.lib
#pragma comment(lib, "Ws2_32.lib")

// link with fwpuclnt.lib for Winsock secure socket extensions
#pragma comment(lib, "fwpuclnt.lib")

// link with ntdsapi.lib for DsMakeSpn function
#pragma comment(lib, "ntdsapi.lib")

// The following function assumes that Winsock 
// has already been initialized

int
SecureTcpConnect(IN const struct sockaddr *serverAddr,
                 IN ULONG serverAddrLen,
                 IN const wchar_t * serverSPN,
                 IN const SOCKET_SECURITY_SETTINGS * securitySettings,
                 IN ULONG settingsLen)
/**
Routine Description:

    This routine creates a TCP client socket, securely connects to the 
    specified server, sends & receives data from the server, and then closes 
    the socket

Arguments:

    serverAddr - a pointer to the sockaddr structure for the server.

    serverAddrLen - length of serverAddr in bytes

    serverSPN - a NULL-terminated string representing the SPN 
               (service principal name) of the server host computer

    securitySettings - pointer to the socket security settings that should be
                       applied to the connection

    serverAddrLen - length of securitySettings in bytes

Return Value:

    Winsock error code indicating the status of the operation, or NO_ERROR if 
    the operation succeeded.

--*/
{
    int iResult = 0;
    int sockErr = 0;
    SOCKET sock = INVALID_SOCKET;

    WSABUF wsaBuf = { 0 };
    char *dataBuf = "12345678";
    DWORD bytesSent = 0;
    char recvBuf[RECV_DATA_BUF_SIZE] = { 0 };

    DWORD bytesRecvd = 0;
    DWORD flags = 0;
    SOCKET_PEER_TARGET_NAME *peerTargetName = NULL;
    DWORD serverSpnStringLen = (DWORD) wcslen(serverSPN);
    DWORD peerTargetNameLen = sizeof (SOCKET_PEER_TARGET_NAME) +
        (serverSpnStringLen * sizeof (wchar_t));

    //-----------------------------------------
    // Create a TCP socket
    sock = WSASocket(serverAddr->sa_family,
                     SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
    if (sock == INVALID_SOCKET) {
        iResult = WSAGetLastError();
        wprintf(L"WSASocket returned error %ld\n", iResult);
        goto cleanup;
    }
    //-----------------------------------------
    // Turn on security for the socket.
    sockErr = WSASetSocketSecurity(sock,
                                   securitySettings, settingsLen, NULL, NULL);
    if (sockErr == SOCKET_ERROR) {
        iResult = WSAGetLastError();
        wprintf(L"WSASetSocketSecurity returned error %ld\n", iResult);
        goto cleanup;
    }
    //-----------------------------------------
    // Specify the server SPN
    peerTargetName = (SOCKET_PEER_TARGET_NAME *) HeapAlloc(GetProcessHeap(),
                               HEAP_ZERO_MEMORY, peerTargetNameLen);
    if (!peerTargetName) {
        iResult = ERROR_NOT_ENOUGH_MEMORY;
        wprintf(L"Out of memory\n");
        goto cleanup;
    }
    // Use the security protocol as specified by the settings
    peerTargetName->SecurityProtocol = securitySettings->SecurityProtocol;
    // Specify the server SPN 
    peerTargetName->PeerTargetNameStringLen = serverSpnStringLen;
    RtlCopyMemory((BYTE *) peerTargetName->AllStrings,
                  (BYTE *) serverSPN, serverSpnStringLen * sizeof (wchar_t)
        );

    sockErr = WSASetSocketPeerTargetName(sock,
                                         peerTargetName,
                                         peerTargetNameLen, NULL, NULL);
    if (sockErr == SOCKET_ERROR) {
        iResult = WSAGetLastError();
        wprintf(L"WSASetSocketPeerTargetName returned error %ld\n", iResult);
        goto cleanup;
    }
    //-----------------------------------------
    // Connect to the server
    sockErr = WSAConnect(sock,
                         serverAddr, serverAddrLen, NULL, NULL, NULL, NULL);
    if (sockErr == SOCKET_ERROR) {
        iResult = WSAGetLastError();
        wprintf(L"WSAConnect returned error %ld\n", iResult);
        goto cleanup;
    }
    // At this point a secure connection must have been established.
    wprintf(L"Secure connection established to the server\n");

    //-----------------------------------------
    // Send some data securely
    wsaBuf.len = (ULONG) strlen(dataBuf);
    wsaBuf.buf = dataBuf;
    sockErr = WSASend(sock, &wsaBuf, 1, &bytesSent, 0, NULL, NULL);
    if (sockErr == SOCKET_ERROR) {
        iResult = WSAGetLastError();
        wprintf(L"WSASend returned error %ld\n", iResult);
        goto cleanup;
    }
    wprintf(L"Sent %d bytes of data to the server\n", bytesSent);

    //-----------------------------------------
    // Receive server's response securely
    wsaBuf.len = RECV_DATA_BUF_SIZE;
    wsaBuf.buf = recvBuf;
    sockErr = WSARecv(sock, &wsaBuf, 1, &bytesRecvd, &flags, NULL, NULL);
    if (sockErr == SOCKET_ERROR) {
        iResult = WSAGetLastError();
        wprintf(L"WSARecv returned error %ld\n", iResult);
        goto cleanup;
    }
    wprintf(L"Received %d bytes of data from the server\n", bytesRecvd);

  cleanup:
    if (sock != INVALID_SOCKET) {
        //This will trigger the cleanup of all IPsec filters and policies that
        //were added for this socket. The cleanup will happen only after all
        //outstanding data has been sent out on the wire.
        closesocket(sock);
    }
    if (peerTargetName) {
        HeapFree(GetProcessHeap(), 0, peerTargetName);
    }
    return iResult;
}

```



## Querying the Security on a Socket


```C++
#ifndef UNICODE
#define UNICODE
#endif

#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <winsock2.h>
#include <mstcpip.h>
#include <ws2tcpip.h>
#include <stdio.h>

// Link with ws2_32.lib
#pragma comment(lib, "Ws2_32.lib")

// link with fwpuclnt.lib for Winsock secure socket extensions
#pragma comment(lib, "fwpuclnt.lib")

#define MALLOC(x) HeapAlloc(GetProcessHeap(), 0, (x))
#define FREE(x) HeapFree(GetProcessHeap(), 0, (x))

/* Note: could also use malloc() and free() */

// The following function assumes that Winsock 
// has already been initialized

int QueryTcpSocketSecurity(IN SOCKET sock)
{
    int iResult = 0;
    SOCKET_SECURITY_QUERY_INFO *queryInfo = NULL;
    ULONG infoLength = 0;

    //First query the number of bytes to allocate
    iResult = WSAQuerySocketSecurity(sock, NULL, NULL, NULL, &infoLength, NULL, NULL);

    if ((iResult == SOCKET_ERROR) && (WSAGetLastError() == WSAEFAULT)) {
        //Allocate the space
        queryInfo = (SOCKET_SECURITY_QUERY_INFO *) MALLOC(infoLength);
        if (!queryInfo) {
            wprintf(L"Unable to allocate memory\n");
            return 1;
        }
    } else {
        wprintf(L"WSAQuerySocketSecurity failed with %u\n", WSAGetLastError());
        return 1;
    }

    //Get the IPsec info
    iResult = WSAQuerySocketSecurity(sock, NULL, NULL, queryInfo, &infoLength, NULL, NULL);

    if (iResult) {
        wprintf(L"WSAQuerySocketSecurity failed with %u\n", WSAGetLastError());
        if (queryInfo)
            FREE(queryInfo);
        return 1;
    }

    // Now queryInfo contains various pieces of information about the
    // security applied to the socket. For instance a server application
    // will be able to access the client access token and impersonate  
    // the client if it wants.

    // Note that the SecurityQueryTemplate parameter passed to the 
    // WSAQuerySocketSecurity function would need to have the
    // PeerTokenAccessMask member set in the 
    // SOCKET_SECURITY_QUERY_TEMPLATE struct to request 
    // the return of the PeerApplicationAccessTokenHandle or 
    // PeerMachineAccessTokenHandle members in the queryInfo struct
    // returned by WSAQuerySocketSecurit

    // When done, free the memory allocation and exit
    if (queryInfo)
        FREE(queryInfo);
    return iResult;
}

```



## Related topics

<dl> <dt>

[About Windows Filtering Platform](../fwp/about-windows-filtering-platform.md)
</dt> <dt>

[Advanced Winsock Samples Using Secure Socket Extensions](advanced-winsock-samples-using-secure-socket-extensions.md)
</dt> <dt>

[Application Layer Enforcement (ALE)](../fwp/application-layer-enforcement--ale-.md)
</dt> <dt>

[IPsec Configuration](../fwp/ipsec-configuration.md)
</dt> <dt>

[IPsec Functions](../fwp/fwp-ipsec-functions.md)
</dt> <dt>

[Security Support Provider Interface (SSPI)](../rpc/security-support-provider-interface-sspi-.md)
</dt> <dt>

[Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md)
</dt> <dt>

[Windows Filtering Platform API Functions](../fwp/fwp-functions.md)
</dt> <dt>

[Winsock Secure Socket Extensions](winsock-secure-socket-extensions.md)
</dt> </dl>

 

 
