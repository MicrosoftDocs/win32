---
Description: 'IP Helper can assist in the management of IP addresses associated with interfaces on the local computer. Use the functions described in the following paragraphs for IP address management.'
ms.assetid: '94da3e53-1898-4721-b5f0-0b7244574c55'
title: Managing IP Addresses
---

# Managing IP Addresses

IP Helper can assist in the management of IP addresses associated with interfaces on the local computer. Use the functions described in the following paragraphs for IP address management.

The [**GetIpAddrTable**](getipaddrtable.md) function retrieves a table that contains the mapping of IP addresses to interfaces. More than one IP address may be associated with the same interface.

Use the [**AddIPAddress**](addipaddress.md) function to add an IP address to a particular interface. To remove IP addresses that were previously added using **AddIPAddress**, use the [**DeleteIPAddress**](deleteipaddress.md) function.

The [**IpReleaseAddress**](ipreleaseaddress.md) and [**IpRenewAddress**](iprenewaddress.md) functions require the local computer to be using Dynamic Host Configuration Protocol (DHCP). The **IpReleaseAddress** function releases an IP address that was previously obtained from DHCP. The **IpRenewAddress** function renews a DHCP lease on a particular IP address. A DHCP lease allows a computer to use an IP address for a specified period of time.

-   For code samples involving [**GetIpAddrTable**](getipaddrtable.md) see [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md).

-   For code samples involving [**AddIPAddress**](addipaddress.md) and [**DeleteIPAddress**](deleteipaddress.md), see [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md).

-   For code samples involving [**IpReleaseAddress**](ipreleaseaddress.md) and [**IpRenewAddress**](iprenewaddress.md) see [Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress](managing-dhcp-leases-using-ipreleaseaddress-and-iprenewaddress.md).

 

 



