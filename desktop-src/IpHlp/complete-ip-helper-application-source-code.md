---
description: The following is the complete source code for the IP Helper application. Additional error checking has been added to source code.
ms.assetid: c0290660-8a18-4d5c-8f0a-df15da1a9167
title: Complete IP Helper Application Source Code
ms.topic: article
ms.date: 05/31/2018
---

# Complete IP Helper Application Source Code

The following is the complete source code for the IP Helper application. Additional error checking has been added to source code.


```C++
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>

#include <winsock2.h>
#include <ws2tcpip.h>

#include <iphlpapi.h>

#include <stdio.h>
#include <time.h>

// Need to link with Iphlpapi.lib and Ws2_32.lib
#pragma comment(lib, "iphlpapi.lib")
#pragma comment(lib, "ws2_32.lib")

#define MALLOC(x) HeapAlloc(GetProcessHeap(), 0, (x))
#define FREE(x) HeapFree(GetProcessHeap(), 0, (x))
/* Note: could also use malloc() and free() */

int main()
{

    /* Some general variables */
    ULONG ulOutBufLen;
    DWORD dwRetVal;
    unsigned int i;
  
    /* variables used for GetNetworkParams */
    FIXED_INFO *pFixedInfo;
    IP_ADDR_STRING *pIPAddr;

    /* variables used for GetAdapterInfo */
    IP_ADAPTER_INFO *pAdapterInfo;
    IP_ADAPTER_INFO *pAdapter;

    /* variables used to print DHCP time info */
    struct tm newtime;
    char buffer[32];
    errno_t error;

    /* variables used for GetInterfaceInfo */
    IP_INTERFACE_INFO *pInterfaceInfo;

    /* variables used for GetIpAddrTable */
    MIB_IPADDRTABLE *pIPAddrTable;
    DWORD dwSize;
    IN_ADDR IPAddr;
    char *strIPAddr;

    /* variables used for AddIpAddress */
    UINT iaIPAddress;
    UINT imIPMask;
    ULONG NTEContext;
    ULONG NTEInstance;

    /* variables used for GetIpStatistics */
    MIB_IPSTATS *pStats;

    /* variables used for GetTcpStatistics */
    MIB_TCPSTATS *pTCPStats;

    printf("------------------------\n");
    printf("This is GetNetworkParams\n");
    printf("------------------------\n");

    pFixedInfo = (FIXED_INFO *) MALLOC(sizeof (FIXED_INFO));
    if (pFixedInfo == NULL) {
        printf("Error allocating memory needed to call GetNetworkParams\n");
        return 1;
    }
    ulOutBufLen = sizeof (FIXED_INFO);

    if (GetNetworkParams(pFixedInfo, &ulOutBufLen) == ERROR_BUFFER_OVERFLOW) {
        FREE(pFixedInfo);
        pFixedInfo = (FIXED_INFO *) MALLOC(ulOutBufLen);
        if (pFixedInfo == NULL) {
            printf("Error allocating memory needed to call GetNetworkParams\n");
            return 1;
        }
    }

    if (dwRetVal = GetNetworkParams(pFixedInfo, &ulOutBufLen) != NO_ERROR) {
        printf("GetNetworkParams failed with error %d\n", dwRetVal);
        if (pFixedInfo)
            FREE(pFixedInfo);
        return 1;
    } else {
        printf("\tHost Name: %s\n", pFixedInfo->HostName);
        printf("\tDomain Name: %s\n", pFixedInfo->DomainName);
        printf("\tDNS Servers:\n");
        printf("\t\t%s\n", pFixedInfo->DnsServerList.IpAddress.String);

        pIPAddr = pFixedInfo->DnsServerList.Next;
        while (pIPAddr) {
            printf("\t\t%s\n", pIPAddr->IpAddress.String);
            pIPAddr = pIPAddr->Next;
        }

        printf("\tNode Type: ");
        switch (pFixedInfo->NodeType) {
        case 1:
            printf("%s\n", "Broadcast");
            break;
        case 2:
            printf("%s\n", "Peer to peer");
            break;
        case 4:
            printf("%s\n", "Mixed");
            break;
        case 8:
            printf("%s\n", "Hybrid");
            break;
        default:
            printf("\n");
        }

        printf("\tNetBIOS Scope ID: %s\n", pFixedInfo->ScopeId);

        if (pFixedInfo->EnableRouting)
            printf("\tIP Routing Enabled: Yes\n");
        else
            printf("\tIP Routing Enabled: No\n");

        if (pFixedInfo->EnableProxy)
            printf("\tWINS Proxy Enabled: Yes\n");
        else
            printf("\tWINS Proxy Enabled: No\n");

        if (pFixedInfo->EnableDns)
            printf("\tNetBIOS Resolution Uses DNS: Yes\n");
        else
            printf("\tNetBIOS Resolution Uses DNS: No\n");
    }

    /* Free allocated memory no longer needed */
    if (pFixedInfo) {
        FREE(pFixedInfo);
        pFixedInfo = NULL;
    }

    printf("------------------------\n");
    printf("This is GetAdaptersInfo\n");
    printf("------------------------\n");

    pAdapterInfo = (IP_ADAPTER_INFO *) MALLOC(sizeof (IP_ADAPTER_INFO));
    if (pAdapterInfo == NULL) {
        printf("Error allocating memory needed to call GetAdapterInfo\n");
        return 1;
    }
    ulOutBufLen = sizeof (IP_ADAPTER_INFO);

    if (GetAdaptersInfo(pAdapterInfo, &ulOutBufLen) == ERROR_BUFFER_OVERFLOW) {
        FREE(pAdapterInfo);
        pAdapterInfo = (IP_ADAPTER_INFO *) MALLOC(ulOutBufLen);
        if (pAdapterInfo == NULL) {
            printf("Error allocating memory needed to call GetAdapterInfo\n");
            return 1;
        }
    }

    if ((dwRetVal = GetAdaptersInfo(pAdapterInfo, &ulOutBufLen)) != NO_ERROR) {
        printf("GetAdaptersInfo failed with error %d\n", dwRetVal);
        if (pAdapterInfo)
            FREE(pAdapterInfo);
        return 1;
    }

    pAdapter = pAdapterInfo;
    while (pAdapter) {
        printf("\tAdapter Name: \t%s\n", pAdapter->AdapterName);
        printf("\tAdapter Desc: \t%s\n", pAdapter->Description);
        printf("\tAdapter Addr: \t");
        for (i = 0; i < (int) pAdapter->AddressLength; i++) {
            if (i == (pAdapter->AddressLength - 1))
                printf("%.2X\n", (int) pAdapter->Address[i]);
            else
                printf("%.2X-", (int) pAdapter->Address[i]);
        }
        printf("\tIP Address: \t%s\n",
               pAdapter->IpAddressList.IpAddress.String);
        printf("\tIP Mask: \t%s\n", pAdapter->IpAddressList.IpMask.String);

        printf("\tGateway: \t%s\n", pAdapter->GatewayList.IpAddress.String);
        printf("\t***\n");

        if (pAdapter->DhcpEnabled) {
            printf("\tDHCP Enabled: \tYes\n");
            printf("\tDHCP Server: \t%s\n",
                   pAdapter->DhcpServer.IpAddress.String);

            printf("\tLease Obtained: ");
            /* Display local time */
            error = _localtime32_s(&newtime, (__time32_t*) &pAdapter->LeaseObtained);
            if (error)
                printf("\tInvalid Argument to _localtime32_s\n");

            else {
                // Convert to an ASCII representation 
                error = asctime_s(buffer, 32, &newtime);
                if (error)
                    printf("Invalid Argument to asctime_s\n");
                else
                    /* asctime_s returns the string terminated by \n\0 */
                    printf("%s", buffer);
            }

            printf("\tLease Expires:  ");
            error = _localtime32_s(&newtime, (__time32_t*) &pAdapter->LeaseExpires);
            if (error)
                printf("Invalid Argument to _localtime32_s\n");
            else {
                // Convert to an ASCII representation 
                error = asctime_s(buffer, 32, &newtime);
                if (error)
                    printf("Invalid Argument to asctime_s\n");
                else
                    /* asctime_s returns the string terminated by \n\0 */
                    printf("%s", buffer);
            }
        } else
            printf("\tDHCP Enabled: \tNo\n");

        if (pAdapter->HaveWins) {
            printf("\tHave Wins: \tYes\n");
            printf("\tPrimary Wins Server: \t%s\n",
                   pAdapter->PrimaryWinsServer.IpAddress.String);
            printf("\tSecondary Wins Server: \t%s\n",
                   pAdapter->SecondaryWinsServer.IpAddress.String);
        } else
            printf("\tHave Wins: \tNo\n");

        printf("\n");
        pAdapter = pAdapter->Next;
    }

    printf("------------------------\n");
    printf("This is GetInterfaceInfo\n");
    printf("------------------------\n");

    pInterfaceInfo = (IP_INTERFACE_INFO *) MALLOC(sizeof (IP_INTERFACE_INFO));
    if (pInterfaceInfo == NULL) {
        printf("Error allocating memory needed to call GetInterfaceInfo\n");
        return 1;
    }
    ulOutBufLen = sizeof (IP_INTERFACE_INFO);
    if (GetInterfaceInfo(pInterfaceInfo, &ulOutBufLen) ==
        ERROR_INSUFFICIENT_BUFFER) {
        FREE(pInterfaceInfo);
        pInterfaceInfo = (IP_INTERFACE_INFO *) MALLOC(ulOutBufLen);
        if (pInterfaceInfo == NULL) {
            printf("Error allocating memory needed to call GetInterfaceInfo\n");
            return 1;
        }
        printf("\t The size needed for the output buffer ulLen = %ld\n",
               ulOutBufLen);
    }

    if ((dwRetVal = GetInterfaceInfo(pInterfaceInfo, &ulOutBufLen)) == NO_ERROR) {
        printf("\tNum Adapters: %ld\n\n", pInterfaceInfo->NumAdapters);
        for (i = 0; i < (unsigned int) pInterfaceInfo->NumAdapters; i++) {
            printf("\tAdapter Index[%d]: %ld\n", i,
                   pInterfaceInfo->Adapter[i].Index);
            printf("\tAdapter Name[%d]:  %ws\n\n", i,
                   pInterfaceInfo->Adapter[i].Name);
        }
        printf("GetInterfaceInfo call succeeded.\n");
    } else {
        LPVOID lpMsgBuf = NULL;

        if (FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS, NULL, dwRetVal, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),       // Default language
                          (LPTSTR) & lpMsgBuf, 0, NULL)) {
            printf("\tError: %s", lpMsgBuf);
        }
        LocalFree(lpMsgBuf);
    }

    /* If DHCP enabled, release and renew the IP address */
    /* THIS WORKS BUT IT TAKES A LONG TIME AND INTERRUPTS NET CONNECTIONS */
    if (pAdapterInfo->DhcpEnabled && pInterfaceInfo->NumAdapters) {
        printf("Calling IpReleaseAddress for Adapter[%d]\n", 0);
        if ((dwRetVal =
             IpReleaseAddress(&pInterfaceInfo->Adapter[0])) == NO_ERROR) {
            printf("Ip Release succeeded.\n");
        }
        if ((dwRetVal =
             IpRenewAddress(&pInterfaceInfo->Adapter[0])) == NO_ERROR) {
            printf("Ip Renew succeeded.\n");
        }
    }

    /* Free allocated memory no longer needed */
    if (pAdapterInfo) {
        FREE(pAdapterInfo);
        pAdapterInfo = NULL;
    }
    if (pInterfaceInfo) {
        FREE(pInterfaceInfo);
        pInterfaceInfo = NULL;
    }

    printf("----------------------\n");
    printf("This is GetIpAddrTable\n");
    printf("----------------------\n");

    pIPAddrTable = (MIB_IPADDRTABLE *) MALLOC(sizeof (MIB_IPADDRTABLE));
    if (pIPAddrTable == NULL) {
        printf("Error allocating memory needed to call GetIpAddrTable\n");
        return 1;
    }
    dwSize = 0;
    IPAddr.S_un.S_addr = ntohl(pIPAddrTable->table[1].dwAddr);
    strIPAddr = inet_ntoa(IPAddr);

    if (GetIpAddrTable(pIPAddrTable, &dwSize, 0) == ERROR_INSUFFICIENT_BUFFER) {
        FREE(pIPAddrTable);
        pIPAddrTable = (MIB_IPADDRTABLE *) MALLOC(dwSize);
        if (pIPAddrTable == NULL) {
            printf("Error allocating memory needed to call GetIpAddrTable\n");
            return 1;
        }
    }

    if ((dwRetVal = GetIpAddrTable(pIPAddrTable, &dwSize, 0)) != NO_ERROR) {
        printf("GetIpAddrTable failed with error %d\n", dwRetVal);
        if (pIPAddrTable)
            FREE(pIPAddrTable);
        return 1;
    }

    printf("\tNum Entries: %ld\n", pIPAddrTable->dwNumEntries);
    for (i = 0; i < (unsigned int) pIPAddrTable->dwNumEntries; i++) {
        printf("\n\tInterface Index[%d]:\t%ld\n", i,
               pIPAddrTable->table[i].dwIndex);
        IPAddr.S_un.S_addr = (u_long) pIPAddrTable->table[i].dwAddr;
        printf("\tIP Address[%d]:     \t%s\n", i, inet_ntoa(IPAddr));
        IPAddr.S_un.S_addr = (u_long) pIPAddrTable->table[i].dwMask;
        printf("\tSubnet Mask[%d]:    \t%s\n", i, inet_ntoa(IPAddr));
        IPAddr.S_un.S_addr = (u_long) pIPAddrTable->table[i].dwBCastAddr;
        printf("\tBroadCast[%d]:      \t%s (%ld%)\n", i, inet_ntoa(IPAddr),
               pIPAddrTable->table[i].dwBCastAddr);
        printf("\tReassembly size[%d]:\t%ld\n", i,
               pIPAddrTable->table[i].dwReasmSize);
        printf("\tAddress Index[%d]:  \t%ld\n", i,
               pIPAddrTable->table[i].dwIndex);
        printf("\tType and State[%d]:", i);
        if (pIPAddrTable->table[i].wType & MIB_IPADDR_PRIMARY)
            printf("\tPrimary IP Address");
        if (pIPAddrTable->table[i].wType & MIB_IPADDR_DYNAMIC)
            printf("\tDynamic IP Address");
        if (pIPAddrTable->table[i].wType & MIB_IPADDR_DISCONNECTED)
            printf("\tAddress is on disconnected interface");
        if (pIPAddrTable->table[i].wType & MIB_IPADDR_DELETED)
            printf("\tAddress is being deleted");
        if (pIPAddrTable->table[i].wType & MIB_IPADDR_TRANSIENT)
            printf("\tTransient address");
        printf("\n");
    }

    iaIPAddress = inet_addr("192.168.0.27");
    imIPMask = inet_addr("255.255.255.0");

    NTEContext = 0;
    NTEInstance = 0;

    if ((dwRetVal = AddIPAddress(iaIPAddress,
                                 imIPMask,
                                 pIPAddrTable->table[0].
                                 dwIndex,
                                 &NTEContext, &NTEInstance)) != NO_ERROR) {

        LPVOID lpMsgBuf;
        printf("\tError adding IP address.\n");

        if (FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS, NULL, dwRetVal, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),       // Default language
                          (LPTSTR) & lpMsgBuf, 0, NULL)) {
            printf("\tError: %s", lpMsgBuf);
        }
        LocalFree(lpMsgBuf);
    }

    if ((dwRetVal = DeleteIPAddress(NTEContext)) != NO_ERROR) {
        printf("DeleteIPAddress failed with error %d\n", dwRetVal);
    }

    /* Free allocated memory no longer needed */
    if (pIPAddrTable) {
        FREE(pIPAddrTable);
        pIPAddrTable = NULL;
    }

    printf("-------------------------\n");
    printf("This is GetIPStatistics()\n");
    printf("-------------------------\n");

    pStats = (MIB_IPSTATS *) MALLOC(sizeof (MIB_IPSTATS));
    if (pStats == NULL) {
        printf("Error allocating memory needed to call GetIpStatistics\n");
        return 1;
    }

    if ((dwRetVal = GetIpStatistics(pStats)) != NO_ERROR) {
        printf("GetIPStatistics failed with error %d\n", dwRetVal);
        if (pStats)
            FREE(pStats);
        return 1;
    }

    printf("\tNumber of IP addresses: %ld\n", pStats->dwNumAddr);
    printf("\tNumber of Interfaces: %ld\n", pStats->dwNumIf);
    printf("\tReceives: %ld\n", pStats->dwInReceives);
    printf("\tOut Requests: %ld\n", pStats->dwOutRequests);
    printf("\tRoutes: %ld\n", pStats->dwNumRoutes);
    printf("\tTimeout Time: %ld\n", pStats->dwReasmTimeout);
    printf("\tIn Delivers: %ld\n", pStats->dwInDelivers);
    printf("\tIn Discards: %ld\n", pStats->dwInDiscards);
    printf("\tTotal In: %ld\n", pStats->dwInDelivers + pStats->dwInDiscards);
    printf("\tIn Header Errors: %ld\n", pStats->dwInHdrErrors);

    /* Free allocated memory no longer needed */
    if (pStats) {
        FREE(pStats);
        pStats = NULL;
    }

    printf("-------------------------\n");
    printf("This is GetTCPStatistics()\n");
    printf("-------------------------\n");

    pTCPStats = (MIB_TCPSTATS *) MALLOC(sizeof (MIB_TCPSTATS));
    if (pTCPStats == NULL) {
        printf("Error allocating memory needed to call GetTcpStatistics\n");
        return 1;
    }

    if ((dwRetVal = GetTcpStatistics(pTCPStats)) != NO_ERROR) {
        printf("GetTcpStatistics failed with error %d\n", dwRetVal);
        if (pTCPStats)
            FREE(pTCPStats);
        return 1;
    }

    printf("\tActive Opens: %ld\n", pTCPStats->dwActiveOpens);
    printf("\tPassive Opens: %ld\n", pTCPStats->dwPassiveOpens);
    printf("\tSegments Recv: %ld\n", pTCPStats->dwInSegs);
    printf("\tSegments Xmit: %ld\n", pTCPStats->dwOutSegs);
    printf("\tTotal # Conxs: %ld\n", pTCPStats->dwNumConns);

    /* Free allocated memory no longer needed */
    if (pTCPStats) {
        FREE(pTCPStats);
        pTCPStats = NULL;
    }

    return 0;
}
```



 

 



