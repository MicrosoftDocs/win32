---
Description: 'The AddIPAddress function adds the specified IPv4 address to the specified adapter.'
ms.assetid: '71cf6b4d-192c-4b2a-b534-be0b3da552f9'
title: Managing IP Addresses Using AddIPAddress and DeleteIPAddress
---

# Managing IP Addresses Using AddIPAddress and DeleteIPAddress

The [**AddIPAddress**](addipaddress.md) function adds the specified IPv4 address to the specified adapter. The [**DeleteIPAddress**](deleteipaddress.md) function deletes the specified IPv4 address from the specified adapter. These functions can be used to add and delete IPv4 addresses to a network adapter.

An IPv4 address added by the [**AddIPAddress**](addipaddress.md) function is not persistent. The IPv4 address exists only as long as the adapter object exists. Restarting the computer destroys the IPv4 address, as does manually resetting the network interface card (NIC).

After [**AddIPAddress**](addipaddress.md) has been called successfully, DHCP will be disabled for the IP address that was added. Therefore, functions such as [**IpReleaseAddress**](ipreleaseaddress.md), which require DHCP to be enabled, will not be functional on the added IP address. The [**DeleteIPAddress**](deleteipaddress.md) function can be used to delete the added IPv4 address.

> [!Note]  
> Group policies, enterprise policies, and other restrictions on the network may prevent these functions from completing successfully. Ensure that the application has the necessary network permissions before attempting to use these functions.

 

**To use AddIPAddress**

1.  Declare **ULONG** variables named `NTEContext` and `NTEInstance`, both initialized to zero.
    > [!Note]  
    > The `NTEContext` variable is the only parameter to the [**DeleteIPAddress**](deleteipaddress.md) function; to delete the IP address that is added, `NTEContext` must be stored and unchanged.

     

    ```C++
        ULONG NTEContext = 0;
        ULONG NTEInstance = 0;
    
    ```

    

    > [!Note]  

     

2.  Declare variables for the IPAddr and IPMask structures named `iaIPAddress` and `iaIPMask`, respectively. These values are simply unsigned integers. Initialize the `iaIPAddress` and `iaIPMask` variables using the [**inet\_addr**](winsock.inet_addr_2) function.
    ```C++
    UINT iaIPAddress;
    UINT iaIPMask;

    iaIPAddress = inet_addr("192.168.0.5");
    iaIPMask    = inet_addr("255.255.255.0");
    ```

    

3.  Call the [**AddIPAddress**](addipaddress.md) function to add the IPv4 address. Check for errors and return the error value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    ```C++
    dwRetVal = AddIPAddress(iaIPAddress, iaIPMask, pIPAddrTable->table[0].dwIndex, 
                                 &amp;NTEContext, &amp;NTEInstance);
    if (dwRetVal != NO_ERROR) {
        printf("AddIPAddress call failed with %d\n", dwRetVal);
    }
    ```

    

    > [!Note]  
    > The third parameter is the adapter index, which can be obtained by calling the [**GetIpAddrTable**](getipaddrtable.md) function. It is assumed that the variable returned by this function is named `pIPAddrTable`. For help with the **GetIpAddrTable** function, see [Managing IP Address Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md).

     

**To use DeleteIpAddress**

-   Call the [**DeleteIPAddress**](deleteipaddress.md) function, passing the `NTEContext` variable as its parameter. Check for errors and return the error value to the **DWORD** variable `dwRetVal` (for more extensive error checking).
    ```C++
    dwRetVal = DeleteIPAddress(NTEContext);
    if (dwRetVal != NO_ERROR) {
            printf("\tDeleteIPAddress failed with error: %d\n", dwRetVal);
    } 
    ```

    

> [!Note]  
> To use [**DeleteIPAddress**](deleteipaddress.md), [**AddIPAddress**](addipaddress.md) must first be called to get the handle `NTEContext`. The previous procedure assumes that **AddIPAddress** has already been called somewhere in the code, and `NTEContext` has been saved and remains uncorrupted.

 

Next Step: [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md)

Previous Step: [Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress](managing-dhcp-leases-using-ipreleaseaddress-and-iprenewaddress.md)

 

 



