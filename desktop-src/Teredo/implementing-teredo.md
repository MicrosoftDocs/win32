---
title: Implementing Teredo
ms.assetid: f32e908e-a96d-48a2-8b79-e2e53c64cb68
description: "Learn more about: Implementing Teredo"
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Teredo

While it is not required to make programming changes for [Teredo](about-teredo.md), it is recommended that developers make minor changes that result in the most efficient use of the Teredo interface:

-   It is possible for applications that are only capable of IPv6 traffic to utilize Teredo. However, the processing of both IPv4 and IPv6 traffic should be taken into consideration while developing the application protocol. The application will need to bind to AF\_INET6 or AF\_UNSPEC in socket options.
-   Applications that are capable of listening for unsolicited traffic from the Internet are required to enable the Network Address Translation (NAT) Traversal option inside Windows Firewall. This is accomplished by calling the [**INetFwPolicy2**](/previous-versions/windows/desktop/api/netfw/nn-netfw-inetfwpolicy2) API with the "Edge Traversal" option set to VARIANT\_TRUE. Windows Vista ensures that the Teredo address is available for use when an application requires it. As a result, the Teredo address automatically stabilizes when the Teredo interface is used. If an application wants to ensure that the Teredo address is stable, calling the [**NotifyStableUnicastIpAddressTable**](/windows/desktop/api/netioapi/nf-netioapi-notifystableunicastipaddresstable) API triggers Teredo to transition into a stable state.
-   Applications can also use the [IPV6\_PROTECTION\_LEVEL](/windows/desktop/WinSock/ipv6-protection-level) Winsock socket option to set the protection level, which allows unsolicited inbound traffic to pass through the firewall. See [Receiving Unsolicited Traffic Over Teredo](receiving-unsolicited-traffic-over-teredo.md) for more information.

The Internet Protocol Helper (IP Helper) implementation of specific Teredo functions serves as an example of how the Teredo address can be verified and made available to an application. For more information see, [Using Teredo With IP Helper](using-teredo-with-ip-helper.md).

 

 
