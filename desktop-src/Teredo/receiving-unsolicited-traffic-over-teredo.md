---
title: Receiving Unsolicited Traffic Over Teredo
description: Teredo provides global connectivity using IPv6 and NAT traversal capabilities.
ms.assetid: 0c03d1bb-15f8-4e77-9a96-e182b1d190ac
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Unsolicited Traffic Over Teredo

[Teredo](about-teredo.md) provides global connectivity using IPv6 and NAT traversal capabilities. However, many applications, including peer-to-peer, will require Teredo to receive unsolicited traffic from the Internet. An application can be programmed to receive traffic over a single IPv6 interface or all IPv6-capable interfaces. This documentation describes the requirements for applications that use the Teredo interface to receive unsolicited IPv6 traffic.

An application will receive unsolicited traffic over the Teredo interface only if the application is registered with [Windows Firewall](/previous-versions/windows/desktop/ics/windows-firewall-start-page). In order to receive unsolicited traffic the following must occur:

-   Users must be instructed to use of the Microsoft Management Console (MMC) to enable the "Edge Traversal" option for an application. This option is available under Windows Firewall Snap-In --> \<application name\> --> "Advanced" tab. The "Edge Traversal" option must be enabled individually for each application.

-   The "Edge Traversal" option is enabled by the application. It is possible for applications capable of receiving unsolicited traffic to register with Windows Firewall for "Edge Traversal" and receive unsolicited traffic over the Teredo interface. To do this an application must call the [**INetFwPolicy2**](/previous-versions/windows/desktop/api/netfw/nn-netfw-inetfwpolicy2) API with the "Edge Traversal" option set to VARIANT\_TRUE. User consent is required for this API call before an application is permitted to listen for the traffic.

-   The application sets the Winsock [IPV6\_PROTECTION\_LEVEL](/windows/desktop/WinSock/ipv6-protection-level) socket option to **PROTECTION\_LEVEL\_UNRESTRICTED** via [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt). This will allow the application to receive Edge Traversal traffic.

## Related topics

<dl> <dt>

[Receiving Solicited Traffic Over Teredo](receiving-solicited-traffic-over-teredo.md)
</dt> </dl>

 

 