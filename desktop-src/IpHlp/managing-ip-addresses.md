---
description: IP Helper can assist in the management of IP addresses associated with interfaces on the local computer. Use the functions described in the following paragraphs for IP address management.
ms.assetid: 94da3e53-1898-4721-b5f0-0b7244574c55
title: Managing IP Addresses
ms.topic: article
ms.date: 05/31/2018
---

# Managing IP Addresses

IP Helper can assist in the management of IP addresses associated with interfaces on the local computer. Use the functions described in the following paragraphs for IP address management.

The [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) function retrieves a table that contains the mapping of IP addresses to interfaces. More than one IP address may be associated with the same interface.

Use the [**AddIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-addipaddress) function to add an IP address to a particular interface. To remove IP addresses that were previously added using **AddIPAddress**, use the [**DeleteIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipaddress) function.

The [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) and [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) functions require the local computer to be using Dynamic Host Configuration Protocol (DHCP). The **IpReleaseAddress** function releases an IP address that was previously obtained from DHCP. The **IpRenewAddress** function renews a DHCP lease on a particular IP address. A DHCP lease allows a computer to use an IP address for a specified period of time.

-   For code samples involving [**GetIpAddrTable**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getipaddrtable) see [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md).

-   For code samples involving [**AddIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-addipaddress) and [**DeleteIPAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-deleteipaddress), see [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md).

-   For code samples involving [**IpReleaseAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-ipreleaseaddress) and [**IpRenewAddress**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-iprenewaddress) see [Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress](managing-dhcp-leases-using-ipreleaseaddress-and-iprenewaddress.md).

 

 



