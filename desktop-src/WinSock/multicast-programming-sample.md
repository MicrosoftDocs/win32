---
Description: Multicast Programming Sample
ms.assetid: 87a6d3bb-3827-4a84-ba2d-c7bd2dd73eb2
title: Multicast Programming Sample
ms.topic: article
ms.date: 05/31/2018
---

# Multicast Programming Sample

The following sample code illustrates how to include multicast functionality to a Windows Sockets application using socket options.


```C++
#define WIN32_LEAN_AND_MEAN

#include <winsock2.h>
#include <Ws2tcpip.h>
#include <mswsock.h>

#define u_int32 UINT32  // Unix uses u_int32

// Need to link with Ws2_32.lib
#pragma comment (lib, "Ws2_32.lib")


int                  /* OUT: whatever setsockopt() returns */
join_source_group(int sd, u_int32 grpaddr, 
   u_int32 srcaddr, u_int32 iaddr)
{
   struct ip_mreq_source imr; 
   
   imr.imr_multiaddr.s_addr  = grpaddr;
   imr.imr_sourceaddr.s_addr = srcaddr;
   imr.imr_interface.s_addr  = iaddr;
   return setsockopt(sd, IPPROTO_IP, IP_ADD_SOURCE_MEMBERSHIP, (char *) &imr, sizeof(imr));  
}

int
leave_source_group(int sd, u_int32 grpaddr, 
   u_int32 srcaddr, u_int32 iaddr)
{
   struct ip_mreq_source imr;

   imr.imr_multiaddr.s_addr  = grpaddr;
   imr.imr_sourceaddr.s_addr = srcaddr;
   imr.imr_interface.s_addr  = iaddr;
   return setsockopt(sd, IPPROTO_IP, IP_DROP_SOURCE_MEMBERSHIP, (char *) &imr, sizeof(imr));
}
```



 # consumer
 
 ```C++
 #include <stdio.h>

#include <WinSock2.h>
#include <WS2tcpip.h>
#include <Windows.h>



#pragma comment(lib,"Ws2_32.lib")

#define CHANNEL_IP "225.233.233.233"
#define CHANNEL_PORT 7777

int main(int argc, char* argv[]) {

    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup error\n");
        return SOCKET_ERROR;
    }
    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0);

    int yes = 1;
    setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, (char*)(&yes), sizeof(yes));

    struct sockaddr_in addr = { 0 };
    addr.sin_family = AF_INET;
    addr.sin_port = htons(CHANNEL_PORT);//Multicast port

    //Note: The multicast address cannot be monitored on Windows, it must be used with ordinary sockets
    //      Linux can monitor multicast addresses, such as 225.233.233.233, which is different from Windows

    //addr.sin_addr.s_addr = htons(INADDR_ANY); // Windows and Linux can
    inet_pton(AF_INET, "0.0.0.0", &addr.sin_addr);// Windows and Linux can
    //inet_pton(AF_INET, "225.233.233.233", &addr.sin_addr); Windows error, Linux can

    bind(sock, (struct sockaddr*)(&addr), sizeof(addr));


    //int ttl = 64;
    //setsockopt(sock, IPPROTO_IP, IP_MULTICAST_TTL, reinterpret_cast<char*>(&ttl), sizeof(ttl));


    //Note:  IP_MULTICAST_LOOP Windows is different from Linux. Windows is used for receiving and Linux is used for sending
    //int loop = 0;
    //setsockopt(sock, IPPROTO_IP, IP_MULTICAST_LOOP, reinterpret_cast<char*>(&loop), sizeof(loop));


    //Join multicast

    //struct ip_mreq mreq;
    //inet_pton(AF_INET, CHANNEL_IP, &mreq.imr_multiaddr);

    //// Note that if you have multiple network cards, INADDR_ANY will choose one of them, which may be different from what you expected
    //mreq.imr_interface.s_addr = htonl(INADDR_ANY);
    //setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, reinterpret_cast<char*>(&mreq), sizeof(mreq));


    //struct ip_mreq_source imr;
    //inet_pton(AF_INET, CHANNEL_IP, &imr.imr_multiaddr);
    //inet_pton(AF_INET, "192.168.1.2", &imr.imr_sourceaddr);// OK
    ////imr.imr_sourceaddr.s_addr = htonl(INADDR_ANY); // Error, specific address must be specified

    // Note that if you have multiple network cards, INADDR_ANY will choose one of them, which may be different from what you expected
    //imr.imr_interface.s_addr = htonl(INADDR_ANY);
    //auto n = setsockopt(sock, IPPROTO_IP, IP_ADD_SOURCE_MEMBERSHIP, (char*)&imr, sizeof(imr));

    // Add all local IPv4 addresses to multicast

    {
        char hostname[256] = { 0 };
        gethostname(hostname, sizeof(hostname) - 1);

        struct addrinfo hints;
        memset(&hints, 0, sizeof(hints));
        hints.ai_flags = 0;
        hints.ai_family = AF_INET;
        hints.ai_socktype = SOCK_RAW;
        hints.ai_protocol = IPPROTO_ICMP;

        struct addrinfo* feed_server = NULL;
        int err = getaddrinfo(hostname, NULL, &hints, &feed_server);
        if (err != 0) {
            printf("getaddrinfo failed with error: %d\n", err);
            WSACleanup();
            return 1;
        }

        int count = 0;
        struct addrinfo* res = NULL;
        for (res = feed_server; res != NULL; res = res->ai_next) {
            char buf[255] = { 0 };
            if (res->ai_family == AF_INET) {
                inet_ntop(AF_INET, &((struct sockaddr_in*)(res->ai_addr))->sin_addr, buf, sizeof(buf));

                {
                    struct ip_mreq mreq;
                    inet_pton(AF_INET, CHANNEL_IP, &mreq.imr_multiaddr);
                    mreq.imr_interface.s_addr = ((struct sockaddr_in*)(res->ai_addr))->sin_addr.s_addr;
                    setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, (char*)(&mreq), sizeof(mreq));
                }
            }
            else if (res->ai_family == AF_INET6) {
                inet_ntop(AF_INET6, &((struct sockaddr_in6*)(res->ai_addr))->sin6_addr, buf, sizeof(buf));
            }
            printf("hostaddr: %s\n", buf);
            count++;
        }
        freeaddrinfo(feed_server);
        feed_server = NULL;
        printf("count: %d\n", count);
    }

    static char buf[65535];
    struct sockaddr_in from;
    socklen_t from_len = sizeof(from);
    while (1) {
        memset(buf, 0, sizeof(buf));
        auto len = recvfrom(sock, buf, sizeof(buf), 0, (struct sockaddr*)(&from), &from_len);
        if (len == -1) {
            printf("recvfrom error: %d\n", WSAGetLastError());
            WSACleanup();
            return -1;
        }
        char remote_addr[128] = { 0 };
        inet_ntop(AF_INET, &from.sin_addr, remote_addr, sizeof(remote_addr));

        printf("remote address: %s  ", remote_addr);
        printf("msg: %s\n", buf);
    }
    closesocket(sock);
    WSACleanup();
    return 0;
}


 ```
 
 # producer
 
 ```C++
 #include <stdio.h>

#include <WinSock2.h>
#include <WS2tcpip.h>
#include <Windows.h>



#pragma comment(lib,"Ws2_32.lib")

#define CHANNEL_IP "225.233.233.233"
#define CHANNEL_PORT 7777

int main(int argc, char* argv[]) {

    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup error\n");
        return SOCKET_ERROR;
    }

    char msg[] = "Alice foo foo !";


    //If there are multiple network cards, one will be selected by default, which is inconsistent with our expectations
    //So you need to traverse the network card to send
    {
        char hostname[256] = { 0 };
        gethostname(hostname, sizeof(hostname) - 1);

        struct addrinfo hints;
        memset(&hints, 0, sizeof(hints));
        hints.ai_flags = 0;
        hints.ai_family = AF_INET;
        hints.ai_socktype = SOCK_RAW;
        hints.ai_protocol = IPPROTO_ICMP;

        struct addrinfo* feed_server = NULL;
        int err = getaddrinfo(hostname, NULL, &hints, &feed_server);
        if (err != 0) {
            printf("getaddrinfo failed with error: %d\n", err);
            WSACleanup();
            return 1;
        }

        int count = 0;
        struct addrinfo* res = NULL;
        for (res = feed_server; res != NULL; res = res->ai_next) {
            char buf[255] = { 0 };
            if (res->ai_family == AF_INET) {
                inet_ntop(AF_INET, &((struct sockaddr_in*)(res->ai_addr))->sin_addr, buf, sizeof(buf));

                {
                    SOCKET sock = socket(AF_INET, SOCK_DGRAM, 0);

                    int ttl = 64;
                    setsockopt(sock, IPPROTO_IP, IP_MULTICAST_TTL, (char*)(&ttl), sizeof(ttl));

                    struct sockaddr_in addr;
                    addr.sin_family = AF_INET;
                    addr.sin_port = htons(CHANNEL_PORT);
                    inet_pton(AF_INET, CHANNEL_IP, (struct sockaddr*)(&addr.sin_addr));

                    setsockopt(sock, IPPROTO_IP, IP_MULTICAST_IF, (char*)(((struct sockaddr_in*)(res->ai_addr))->sin_addr.s_addr), sizeof(((struct sockaddr_in*)(res->ai_addr))->sin_addr.s_addr));

                    // sendto
                    sendto(sock, msg, sizeof(msg), 0, (struct sockaddr*)(&addr), sizeof(addr));

                    closesocket(sock);
                }
            }
            else if (res->ai_family == AF_INET6) {
                inet_ntop(AF_INET6, &((struct sockaddr_in6*)(res->ai_addr))->sin6_addr, buf, sizeof(buf));
            }
            printf("hostaddr: %s\n", buf);
            count++;
        }
        freeaddrinfo(feed_server);
        feed_server = NULL;
        printf("count: %d\n", count);
    }

    WSACleanup();
    return 0;
}
 ```

 



