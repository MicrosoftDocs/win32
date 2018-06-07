---
title: Example Code for Implementing a Winsock Service with an RnR Publication
description: The following code example implements the example Winsock service with RnR publication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8800ba76-f24c-4aa7-ba31-97eaf884130c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Windows Sockets Registration and Resolution AD , Example Code, Implementing a Winsock Service with an RnR Publication
- Implementing a Winsock Service with an RnR Publication AD , Example Code
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Implementing a Winsock Service with an RnR Publication

The following code example implements the example Winsock service with RnR publication.

This sample uses the **serverRegister** function defined in the [Example Code for Publishing the RnR Connection Point](example-code-for-publishing-the-rnr-connection-point.md) topic and the **serverUnregister** function defined in the [Example Code for Removing the RnR Connection Point](example-code-for-removing-the-rnr-connection-point.md) topic.


```C++
//  Add Ws2_32.lib to the projecty.

#include <stdafx.>
#include <winsock2.h>
#include <stdio.h>

//  {A9033BC1-ECA4-11cf-A054-00AA006C33ED}
static GUID SVCID_EXAMPLE_SERVICE = 
{ 0xa9033bc1, 0xeca4, 0x11cf, { 0xa0, 0x54, 0x0, 0xaa, 0x0, 0x6c, 0x33, 0xed } };

INT serverRegister(SOCKADDR *sa, 
                   GUID *pServiceID, 
                   LPTSTR pszServiceInstanceName, 
                   LPTSTR pszServiceInstanceComment);
INT serverUnregister(SOCKADDR *sa, 
                     GUID *pServiceID, 
                     LPTSTR pszServiceInstanceName, 
                     LPTSTR pszServiceInstanceComment);

//  Entry point for the application.
int main(void) 
{
    LPTSTR pszServiceInstanceName = TEXT("Example Service Instance");
    LPTSTR pszServiceInstanceComment = TEXT("ExampleService instance registered in the directory service through RnR");

    //  Data structures used to initialize Winsock.
    WSADATA wsData;
    WORD wVer = MAKEWORD(2,2);

    //  Data structures used to setup communications.
    SOCKET s, newsock;
    SOCKADDR sa;
    struct hostent *he;
    char szName[255];
    struct sockaddr_in sa_in;
    INT ilen;
    ULONG icmd;
    ULONG ulLen;

    //  Miscellaneous variables
    INT status;
    WCHAR wszRecvBuf[100];

    memset(wszRecvBuf,0,sizeof(wszRecvBuf));

    //  Begin: Init Winsock2
    status = WSAStartup(wVer,&amp;wsData);
    if (status != NO_ERROR)
    {
        return -1;
    }

    //  Create the socket.
    s = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
    if (INVALID_SOCKET == s) 
    {
        printf("Failed to create socket: %d\n",WSAGetLastError());
        WSACleanup();
        return -1;
    }

    //  Disable non-blocking I/O for this example.
    icmd = 0;   
    status = ioctlsocket(s,FIONBIO,&amp;icmd);

    //  Bind the socket to a dynamically assigned port.
    sa.sa_family=AF_INET;
    memset(sa.sa_data,0,sizeof(sa.sa_data));

    status = bind(s,&amp;sa,sizeof(sa));

    //  Convert the port to the local host byte order.
    ilen = sizeof(sa_in);
    status = getsockname(s,(struct sockaddr *)&amp;sa_in,&amp;ilen);
    if (status == NO_ERROR) 
    {
        printf("Server: Bound to port %d\n",ntohs(sa_in.sin_port));
    }

    //  Identify the net address to fill in to register ourselves
    //  in the directory service. Explicitly call the ANSI text version 
    //  because gethostbyname does not recognize Unicode.

    ilen = sizeof(szName);
    GetComputerNameA(szName,&amp;ulLen);
    he = gethostbyname(szName);

    //  Put the address in the SOCKADDR structure.
    sa_in.sin_addr.S_un.S_addr = *((long *)(he->h_addr));

    //  Listen for connections. SOMAXCONN tells the provider to queue
    //  a "reasonable" number of connections.
    status = listen(s,SOMAXCONN);
    if (status != NO_ERROR) 
    {
        printf("Failed to set socket listening: %d\n",
                WSAGetLastError());
        WSACleanup();
        return -1;
    }

    //  Register this instance with RnR.
    status = serverRegister((SOCKADDR *)&amp;sa_in, 
        &amp;SVCID_EXAMPLE_SERVICE, 
        pszServiceInstanceName, 
        pszServiceInstanceComment);
    if (status != NO_ERROR) 
    {
        printf("Failed to register instance: %d\n",WSAGetLastError());
        WSACleanup();
        return -1;
    }
    printf("Server: Registered instance in the directory service\n");

    //  Block waiting for a connection. For simplicity, this example
    //  is single-threaded. In a real service, spin off one or more threads
    //  here to call AcceptEx here and process the connections through a
    //  completion port.  
    ilen = sizeof(sa);
    newsock = accept(s,&amp;sa,&amp;ilen);
    if (newsock == INVALID_SOCKET) 
    {
        printf("Failed to create socket: %d\n",WSAGetLastError());
    }
    else
    {
        printf("Server: There is a client connection\n");

        //  Receive a message from the client and end.
        status = recv(newsock,(char *)wszRecvBuf,sizeof(wszRecvBuf),0);
        if (status > 0)
        {
            printf("Server: Received: %S\n",wszRecvBuf);
        }
    }

    //  Unregister and end.
    printf("Unregistering and shutting down.\n");
    status = serverUnregister((SOCKADDR *)&amp;sa_in, 
        &amp;SVCID_EXAMPLE_SERVICE, 
        pszServiceInstanceName, 
        pszServiceInstanceComment);

    WSACleanup();

    return 0;
}

//  The server Unregister function removes the rnr connection point.
INT serverUnregister(SOCKADDR *sa, 
                     GUID *pServiceID, 
                     LPTSTR pszServiceInstanceName, 
                     LPTSTR pszServiceInstanceComment)
{
    DWORD ret;
    WSAVERSION Version;
    WSAQUERYSET QuerySet;
    CSADDR_INFO CSAddrInfo[1];
    SOCKADDR sa_local;

    memset(&amp;QuerySet, 0, sizeof(QuerySet));
    memset(&amp;CSAddrInfo, 0, sizeof(CSAddrInfo));
    memset(&amp;sa_local, 0, sizeof(SOCKADDR));
    sa_local.sa_family = AF_INET;

    //  Build the CSAddrInfo structure to contain address
    //  data. This is what clients use to create a connection.
    //
    //  Be aware that the LocalAddr is set to zero because
    //  dynamically assigned port numbers are used.
    //
    CSAddrInfo[0].LocalAddr.iSockaddrLength = sizeof(SOCKADDR);
    CSAddrInfo[0].LocalAddr.lpSockaddr = &amp;sa_local;
    CSAddrInfo[0].RemoteAddr.iSockaddrLength = sizeof(SOCKADDR);
    CSAddrInfo[0].RemoteAddr.lpSockaddr = sa;
    CSAddrInfo[0].iSocketType = SOCK_STREAM;
    CSAddrInfo[0].iProtocol = PF_INET;

    QuerySet.dwSize = sizeof(WSAQUERYSET);
    QuerySet.lpServiceClassId = pServiceID;
    QuerySet.lpszServiceInstanceName = pszServiceInstanceName;
    QuerySet.lpszComment = pszServiceInstanceComment;
    QuerySet.lpVersion = &amp;Version;
    QuerySet.lpVersion->dwVersion = 2;
    QuerySet.lpVersion->ecHow = COMP_NOTLESS;
    QuerySet.dwNameSpace = NS_NTDS;
    QuerySet.dwNumberOfCsAddrs = 1;
    QuerySet.lpcsaBuffer = CSAddrInfo;

    ret = WSASetService( &amp;QuerySet,
                         RNRSERVICE_DEREGISTER,
                         SERVICE_MULTIPLE);

    return(ret);
}

//  The serverRegister function publishes the rnr connection point.
INT serverRegister(SOCKADDR * sa, 
                   GUID *pServiceID, 
                   LPTSTR pszServiceInstanceName, 
                   LPTSTR pszServiceInstanceComment)
{
    DWORD ret;
    WSAVERSION Version;
    WSAQUERYSET QuerySet;
    CSADDR_INFO CSAddrInfo[1];
    SOCKADDR sa_local;

    memset(&amp;QuerySet, 0, sizeof(QuerySet));
    memset(&amp;CSAddrInfo, 0, sizeof(CSAddrInfo));
    memset(&amp;sa_local, 0, sizeof(SOCKADDR));
    sa_local.sa_family = AF_INET;

    //  Build the CSAddrInfo structure to contain address
    //  data that clients use to establish a connection.
    //
    //  Be aware that LocalAddr is set to zero because dynamically
    //  assigned port numbers are used.
    //
    CSAddrInfo[0].LocalAddr.iSockaddrLength = sizeof(SOCKADDR);
    CSAddrInfo[0].LocalAddr.lpSockaddr = &amp;sa_local;
    CSAddrInfo[0].RemoteAddr.iSockaddrLength = sizeof(SOCKADDR);
    CSAddrInfo[0].RemoteAddr.lpSockaddr = sa;
    CSAddrInfo[0].iSocketType = SOCK_STREAM;
    CSAddrInfo[0].iProtocol = PF_INET;

    QuerySet.dwSize = sizeof(WSAQUERYSET);
    QuerySet.lpServiceClassId = pServiceID;
    QuerySet.lpszServiceInstanceName = pszServiceInstanceName;
    QuerySet.lpszComment = pszServiceInstanceComment;
    QuerySet.lpVersion = &amp;Version;
    QuerySet.lpVersion->dwVersion = 2;
    QuerySet.lpVersion->ecHow = COMP_NOTLESS;
    QuerySet.dwNameSpace = NS_NTDS;
    QuerySet.dwNumberOfCsAddrs = 1;
    QuerySet.lpcsaBuffer = CSAddrInfo;

    ret = WSASetService( &amp;QuerySet,
                         RNRSERVICE_REGISTER,
                         SERVICE_MULTIPLE);

    return(ret);
}
```



 

 




