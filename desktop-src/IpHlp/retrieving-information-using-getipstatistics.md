---
description: The GetIpStatistics function fills a pointer to an MIB\_IPSTATS structure with information about the current IP statistics associated with the system.
ms.assetid: 2b65a817-3f80-426f-ada0-bf4b34a410ed
title: Retrieving Information Using GetIpStatistics
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information Using GetIpStatistics

The [**GetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipstatistics) function fills a pointer to an [**MIB\_IPSTATS**](/windows/win32/api/ipmib/ns-ipmib-mib_ipstats_lh) structure with information about the current IP statistics associated with the system.

**To use GetIpStatistics**

1.  Declare some variables that are needed.

    Declare a **DWORD** variable `dwRetval` that will be using for error checking function calls. Declare a pointer to an [**MIB\_IPSTATS**](/windows/win32/api/ipmib/ns-ipmib-mib_ipstats_lh) variable called *pStats*, and allocate memory for the structure. Check that memory could be allocated.

    ```C++
    MIB_IPSTATS  *pStats;
    DWORD        dwRetVal = 0;

    pStats = (MIB_IPSTATS*) malloc(sizeof(MIB_IPSTATS));

    if (pStats == NULL) {
        printf("Unable to allocate memory for MIB_IPSTATS\n");
    }
    ```

    

2.  Call the [**GetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipstatistics) function with the *pStats* parameter to retrieve IP statistics for the local computer. Check for errors and return the error value in the **DWORD** variable `dwRetval`. If an error occurs, the `dwRetval` variable can be used for more extensive error checking and reporting.
    ```C++
    dwRetVal = GetIpStatistics(pStats);
    if (dwRetVal != NO_ERROR) {
        printf("GetIpStatistics call failed with %d\n", dwRetVal);
    }
    ```

    

3.  If the call to [**GetIpStatistics**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipstatistics) was successful, print out some of the data in the [**MIB\_IPSTATS**](/windows/win32/api/ipmib/ns-ipmib-mib_ipstats_lh) structure pointed to by the *pStats* parameter.
    ```C++
    printf("Number of interfaces:   %ld\n", pStats->dwNumIf);
    printf("Number of IP addresses: %ld\n", pStats->dwNumAddr);
    printf("Number of received datagrams:  %ld\n", pStats->dwInReceives);
    printf("NUmber of outgoing datagrams requested to transmit:  %ld\n", pStats->dwOutRequests);
    ```

    

4.  Free the memory allocated for the [**MIB\_IPSTATS**](/windows/win32/api/ipmib/ns-ipmib-mib_ipstats_lh) structure pointed to by the *pStats* parameter. This should be done once the application no longer needs the data returned by the *pStats* parameter.
    ```C++
    if (pStats)
        free(pStats);
    ```

    

Next Step: [Retrieving Information Using GetTcpStatistics](retrieving-information-using-gettcpstatistics.md)

Previous Step: [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md)

 

 
