---
description: The GetTcpStatistics function fills a pointer to an MIB\_TCPSTATS structure with information on the TCP protocol statistics for the local computer.
ms.assetid: cb405d46-cf3e-4f3c-870a-935a0cc8118f
title: Retrieving Information Using GetTcpStatistics
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information Using GetTcpStatistics

The [**GetTcpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatistics) function fills a pointer to an [**MIB\_TCPSTATS**](/windows/win32/api/tcpmib/ns-tcpmib-mib_tcpstats_lh) structure with information on the TCP protocol statistics for the local computer.

**To use GetTcpStatistics**

1.  Declare some variables that are needed.

    Declare a **DWORD** variable `dwRetVal` that will be using for error checking function calls. Declare a pointer to an [**MIB\_TCPSTATS**](/windows/win32/api/tcpmib/ns-tcpmib-mib_tcpstats_lh) variable called *pTCPStats*, and allocate memory for the structure. Check that memory could be allocated.

    ```C++
    DWORD dwRetVal = 0;
    PMIB_TCPSTATS pTCPStats;

    pTCPStats = (MIB_TCPSTATS *) malloc(sizeof (MIB_TCPSTATS));
    if (pTCPStats == NULL) {
        printf("Error allocating memory\n");
    }
    ```

    

2.  Call the [**GetTcpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-gettcpstatistics) function with the *pTCPStats* parameter to retrieve TCP statistics for IPv4 on the local computer. Check for errors and return the error value in the **DWORD** variable `dwRetVal`. If an error occurs, the `dwRetVal` variable can be used for more extensive error checking and reporting.
    ```C++
        if ((dwRetVal = GetTcpStatistics(pTCPStats)) != NO_ERROR) {
            printf("GetTcpStatistics failed with error: %ld\n", dwRetVal);
        } 
    ```

    

3.  If the call was successful, access the data returned in the [**MIB\_TCPSTATS**](/windows/win32/api/tcpmib/ns-tcpmib-mib_tcpstats_lh) pointed to by the *pTCPStats* parameter.
    ```C++
    printf("\tNumber of active opens:  %u\n", pTCPStats->dwActiveOpens);
    printf("\tNumber of passive opens: %u\n", pTCPStats->dwPassiveOpens);
    printf("\tNumber of segments received: %u\n", pTCPStats->dwInSegs);
    printf("\tNumber of segments transmitted: %u\n", pTCPStats->dwOutSegs);
    printf("\tNumber of total connections: %u\n", pTCPStats->dwNumConns);
    ```

    

4.  Free the memory allocated for the [**MIB\_TCPSTATS**](/windows/win32/api/tcpmib/ns-tcpmib-mib_tcpstats_lh) structure pointed to by the *pTCPStats* parameter. This should be done once the application no longer needs the data returned by the *pTCPStats* parameter.
    ```C++
    if (pTCPStats)
        free(pTCPStats);
    ```

    

Next Step: [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md)

Previous Step: [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md)

## Complete Source Code

-   [Complete IP Helper Application Source Code](complete-ip-helper-application-source-code.md)

 

 
