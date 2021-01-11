---
title: Manage DHCP leases with IpReleaseAddress, IpRenewAddress
description: The IpReleaseAddress and IpRenewAddress functions are used to release and renew the current Dynamic Host Configuration Protocol (DHCP) lease.
ms.assetid: 0ed699dd-0bfb-4581-900d-7f5bc1e8acff
ms.topic: article
ms.date: 05/31/2018
---

# Manage DHCP leases with IpReleaseAddress, IpRenewAddress

The [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) and [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) functions are used to release and renew the current Dynamic Host Configuration Protocol (DHCP) lease. The **IpReleaseAddress** function releases an IPv4 address previously obtained through DHCP. The **IpRenewAddress** function renews a lease on an IPv4 address previously obtained through DHCP. It is common to use these two functions together, first releasing the lease with a call to **IpReleaseAddress**, and then renewing the lease with a call to the **IpRenewAddress** function.

When a DHCP client has previously obtained a DHCP lease and [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) is not called before the [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) function, the DHCP client request is sent to the DHCP server that issued the initial DHCP lease. This DHCP server may not available or the DHCP request may fail. When a host has previously obtained a DHCP lease and **IpReleaseAddress** is called before the **IpRenewAddress** function, the DHCP client first releases the IP address obtained and sends a DHCP client request for a response from any available DHCP server.

> [!Note]  
> The [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) and [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) functions require that DHCP be enabled to perform correctly.

 

The [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) function takes a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) structure as its only parameter. To obtain this parameter, first call [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo). For help with the **GetInterfaceInfo** function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md).

**To use IpReleaseAddress**

1.  Obtain a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) structure using the [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo) function. (For help with the GetInterfaceInfo function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)). Create a **DWORD** object `dwRetVal` (used for error checking). It is assumed that the variable returned by **GetInterfaceInfo** is called `pInfo`.
    ```C++
    DWORD dwRetVal;
    
    ```

    

2.  If DHCP is enabled, call the [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) function, passing the [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) variable `Adapter` as its parameter. Check for general errors and return its value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    > [!Note]  
    > The [**GetAdaptersInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getadaptersinfo) function returns a parameter that can be used to check whether DHCP is enabled before calling these functions. For help with **GetAdaptersInfo**, see [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md).

     

    ```C++
    if ((dwRetVal = IpReleaseAddress(&pInfo->Adapter[0])) == NO_ERROR) {
        printf("Ip Release succeeded.\n");
    }
    
    ```

    

> [!Note]  
> It is common to use these two functions together, calling the [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) function and then calling the [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) function, passing the same structure as the parameter to both functions. The following procedure assumes that the functions are not used together; however, if the functions are used together, skip step 1.

 

**To use IpRenewAddress**

1.  Obtain a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) structure using the [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo) function. (For help with the **GetInterfaceInfo** function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)). Declare a **DWORD** object `dwRetVal` (used for error checking) if this variable has not been declared. It is assumed that the variable returned by **GetInterfaceInfo** is called `pInfo`.
    ```C++
    DWORD dwRetVal;
    
    ```

    

2.  Call the [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) function, passing the [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) variable `Adapter` as its parameter. Check for general errors and return its value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    ```C++
    if ((dwRetVal = IpRenewAddress(&pInfo->Adapter[0])) == NO_ERROR) {
        printf("Ip Renew succeeded.\n");
    }
    ```

    

Next Step: [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md)

Previous Step: [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md)

 

 



