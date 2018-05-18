---
Description: 'The IpReleaseAddress and IpRenewAddress functions are used to release and renew the current Dynamic Host Configuration Protocol (DHCP) lease.'
ms.assetid: '0ed699dd-0bfb-4581-900d-7f5bc1e8acff'
title: Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress
---

# Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress

The [**IpReleaseAddress**](ipreleaseaddress.md) and [**IpRenewAddress**](iprenewaddress.md) functions are used to release and renew the current Dynamic Host Configuration Protocol (DHCP) lease. The **IpReleaseAddress** function releases an IPv4 address previously obtained through DHCP. The **IpRenewAddress** function renews a lease on an IPv4 address previously obtained through DHCP. It is common to use these two functions together, first releasing the lease with a call to **IpReleaseAddress**, and then renewing the lease with a call to the **IpRenewAddress** function.

When a DHCP client has previously obtained a DHCP lease and [**IpReleaseAddress**](ipreleaseaddress.md) is not called before the [**IpRenewAddress**](iprenewaddress.md) function, the DHCP client request is sent to the DHCP server that issued the initial DHCP lease. This DHCP server may not available or the DHCP request may fail. When a host has previously obtained a DHCP lease and **IpReleaseAddress** is called before the **IpRenewAddress** function, the DHCP client first releases the IP address obtained and sends a DHCP client request for a response from any available DHCP server.

> [!Note]  
> The [**IpReleaseAddress**](ipreleaseaddress.md) and [**IpRenewAddress**](iprenewaddress.md) functions require that DHCP be enabled to perform correctly.

 

The [**IpReleaseAddress**](ipreleaseaddress.md) function takes a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](ip-adapter-index-map.md) structure as its only parameter. To obtain this parameter, first call [**GetInterfaceInfo**](getinterfaceinfo.md). For help with the **GetInterfaceInfo** function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md).

**To use IpReleaseAddress**

1.  Obtain a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](ip-adapter-index-map.md) structure using the [**GetInterfaceInfo**](getinterfaceinfo.md) function. (For help with the GetInterfaceInfo function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)). Create a **DWORD** object `dwRetVal` (used for error checking). It is assumed that the variable returned by **GetInterfaceInfo** is called `pInfo`.
    ```C++
    DWORD dwRetVal;
    
    ```

    

2.  If DHCP is enabled, call the [**IpReleaseAddress**](ipreleaseaddress.md) function, passing the [**IP\_ADAPTER\_INDEX\_MAP**](ip-adapter-index-map.md) variable `Adapter` as its parameter. Check for general errors and return its value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    > [!Note]  
    > The [**GetAdaptersInfo**](getadaptersinfo.md) function returns a parameter that can be used to check whether DHCP is enabled before calling these functions. For help with **GetAdaptersInfo**, see [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md).

     

    ```C++
    if ((dwRetVal = IpReleaseAddress(&amp;pInfo->Adapter[0])) == NO_ERROR) {
        printf("Ip Release succeeded.\n");
    }
    
    ```

    

> [!Note]  
> It is common to use these two functions together, calling the [**IpReleaseAddress**](ipreleaseaddress.md) function and then calling the [**IpRenewAddress**](iprenewaddress.md) function, passing the same structure as the parameter to both functions. The following procedure assumes that the functions are not used together; however, if the functions are used together, skip step 1.

 

**To use IpRenewAddress**

1.  Obtain a pointer to an [**IP\_ADAPTER\_INDEX\_MAP**](ip-adapter-index-map.md) structure using the [**GetInterfaceInfo**](getinterfaceinfo.md) function. (For help with the **GetInterfaceInfo** function, see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)). Declare a **DWORD** object `dwRetVal` (used for error checking) if this variable has not been declared. It is assumed that the variable returned by **GetInterfaceInfo** is called `pInfo`.
    ```C++
    DWORD dwRetVal;
    
    ```

    

2.  Call the [**IpRenewAddress**](iprenewaddress.md) function, passing the [**IP\_ADAPTER\_INDEX\_MAP**](ip-adapter-index-map.md) variable `Adapter` as its parameter. Check for general errors and return its value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    ```C++
    if ((dwRetVal = IpRenewAddress(&amp;pInfo->Adapter[0])) == NO_ERROR) {
        printf("Ip Renew succeeded.\n");
    }
    ```

    

Next Step: [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md)

Previous Step: [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md)

 

 



