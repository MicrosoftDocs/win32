---
description: The GetIpAddrTable function fills a pointer to an MIB\_IPADDRTABLE structure with information about the current IP addresses associated with the system.
ms.assetid: f041cb37-926d-4eeb-835c-f8b9d5ee4d2e
title: Managing IP Addresses Using GetIpAddrTable
ms.topic: article
ms.date: 05/31/2018
---

# Managing IP Addresses Using GetIpAddrTable

The [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) function fills a pointer to an [**MIB\_IPADDRTABLE**](/windows/win32/api/ipmib/ns-ipmib-mib_ipaddrtable) structure with information about the current IP addresses associated with the system.

**To use GetIpAddrTable**

1.  Declare a pointer to an [**MIB\_IPADDRTABLE**](/windows/win32/api/ipmib/ns-ipmib-mib_ipaddrtable) object called *pIPAddrTable*, and a **DWORD** object called *dwSize*. These variables are passed as parameters to the [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) function. Also create a **DWORD** variable called *dwRetVal* (used for error checking).
    ```C++
    MIB_IPADDRTABLE  *pIPAddrTable;
    DWORD            dwSize = 0;
    DWORD            dwRetVal;
    
    ```

    

2.  Allocate memory for the structure.
    > [!Note]  
    > The size of *dwSize* is not sufficient to hold the information. See the next step.

     

    ```C++
    pIPAddrTable = (MIB_IPADDRTABLE*) malloc( sizeof(MIB_IPADDRTABLE) );
    
    ```

    

3.  Make an initial call to [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) to get the size needed into the *dwSize* variable.
    > [!Note]  
    > This call to the function is meant to fail, and is used to ensure that the *dwSize* variable specifies a size sufficient for holding all the information returned to *pIPAddrTable*. This is a common programming model for data structures and functions of this type.

     

    ```C++
    if (GetIpAddrTable(pIPAddrTable, &dwSize, 0) == ERROR_INSUFFICIENT_BUFFER) {
        free( pIPAddrTable );
        pIPAddrTable = (MIB_IPADDRTABLE *) malloc ( dwSize );
    }
    
    ```

    

4.  Make a second call to [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) with general error checking and return its value to the **DWORD** variable *dwRetVal* (for more advanced error checking).
    ```C++
    if ( (dwRetVal = GetIpAddrTable( pIPAddrTable, &dwSize, 0 )) != NO_ERROR ) { 
        printf("GetIpAddrTable call failed with %d\n", dwRetVal);
    }
    
    ```

    

5.  If the call was successful, access the data from the *pIPAddrTable* data structure.
    ```C++
    printf("IP Address:         %ld\n", pIPAddrTable->table[0].dwAddr);
    printf("IP Mask:            %ld\n", pIPAddrTable->table[0].dwMask);
    printf("IF Index:           %ld\n", pIPAddrTable->table[0].dwIndex);
    printf("Broadcast Addr:     %ld\n", pIPAddrTable->table[0].dwBCastAddr);
    printf("Re-assembly size:   %ld\n", pIPAddrTable->table[0].dwReasmSize);
    
    ```

    

6.  Free any memory allocated for the *pIPAddrTable* structure.
    ```C++
    if (pIPAddrTable)
            free(pIPAddrTable);
    
    ```

    

> [!Note]  
> The **DWORD** objects *dwAddr* and *dwMask* are returned as numerical values in host byte order, not network byte order. These values are not dotted IP addresses.

 

Next Step: [Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress](managing-dhcp-leases-using-ipreleaseaddress-and-iprenewaddress.md)

Previous Step: [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)

 

 
