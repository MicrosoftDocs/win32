---
title: Implementing the Teredo Security Model
description: The Teredo security model is based on the Windows Filtering Platform (WFP) technology built into Windows Vista. As a result, it is recommended that third-party firewalls use WFP to enforce the Teredo security model.
ms.assetid: ee81e5f1-e3e0-440e-a53f-2accced476bc
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Teredo Security Model

The Teredo security model is based on the [Windows Filtering Platform](/windows/desktop/FWP/windows-filtering-platform-start-page) (WFP) technology built into Windows Vista. As a result, it is recommended that third-party firewalls use WFP to enforce the [Teredo](about-teredo.md) security model.

The general implementation of the [Teredo Security Model](the-teredo-security-model.md) requires the following:

-   An IPv6-capable host firewall must be registered with the Windows Security app on the machine. In the absence of a host-based firewall, or the Windows Security app itself, the Teredo interface will not be available for use. This is the only requirement to receive solicited traffic from the Internet over the Teredo interface.
-   Any application that receives unsolicited traffic from the Internet over the Teredo interface must register with an IPv6-capable firewall, like [Windows Firewall](/previous-versions/windows/desktop/ics/windows-firewall-start-page), before receiving the unsolicited traffic.

A Teredo address will become dormant if traffic has not been sent or received over the Teredo interface for one hour and if applications that meet the required security criteria for unsolicited traffic are not running or do not have listening sockets open.

After the reboot of a machine, or if the Teredo address loses its qualifications, Windows Vista will automatically qualify the address and makes it available for use as soon as an application binds to IPv6-capable sockets. It is important to note that the Windows Firewall "Edge Traversal" option set by an application to allow unsolicited traffic via Teredo is persistent across reboots.

## Firewall Requirements for Teredo

Firewall vendors can easily incorporate Teredo support in their products and protect their users by using the capabilities of the Windows Filtering Platform. This can be accomplished by registering the IPv6-capable firewall with the Windows Security app, adding appropriate rules into the WFP Teredo sublayer, and using built-in APIs in Windows to enumerate applications that might listen to unsolicited traffic over Teredo. In situations where an application does not need to listen to solicited traffic over Teredo, firewalls do not require additional rules added to the WFP. However an IPv6 capable firewall registration with the Windows Security app is still a requirement to make the Teredo address to available for use.

In order to support this scenario, the firewall must be IPv6-capable and registered with the Windows Security app. Additionally, the firewall must not change the running or startup state of the Windows Security app service (wscsvc), as Teredo is dependent on the state information provided through the WSC APIs.

The API utilized to register a firewall with the Windows Security app can be obtained by contacting Microsoft at wscisv@microsoft.com. A Non-Disclosure Agreement (NDA) is required for the disclosure of this API due to security concerns.

The following documentation details the filters and exceptions utilized to ensure optimal compatibility with Teredo:

-   [Implementing Firewall Filters for Teredo](implementing-firewall-filters-for-teredo.md)
-   [Required Firewall Exceptions for Teredo](required-firewall-exceptions-for-teredo.md)
-   [Required Windows Filtering Platform Exceptions for Teredo](required-windows-filtering-platform-exceptions-for-teredo.md)

## Firewall Requirements for Other IPv6 Transition Technologies

In order to support other IPv6 transition technologies (such as 6to4 and ISATAP), the host firewall product must be capable of processing IPv6 traffic. The IP Protocol 41 indicates when an IPv6 header follows an IPv4 header. When a host firewall encounters protocol 41, it must recognize that the packet is an IPv6-encapsulated packet and as a result must process the packet appropriately and make the accept/deny decisions based on the IPv6 rules in its policy.
