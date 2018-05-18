---
title: Access Control
description: These APIs are subject to the following access controls.
ms.assetid: 'edc9085c-8c5c-4e50-9236-c4554dfa4548'
---

# Access Control

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

These APIs are subject to the following access controls.

-   A caller must have administrative or system credentials to call a routine that modifies state. Furthermore, the group policy settings on the machine must allow for firewall configuration.
-   All callers can call routines that do not modify state.

The following methods modify state:

-   [**INetFwV6Mgr::put\_LogfilePath**](inetfwv6mgr-logfilepath.md)
-   [**INetFwV6Mgr::put\_LogfileMaximumSize**](inetfwv6mgr-logfilemaximumsize.md)
-   [**INetFwV6Mgr::put\_LogDroppedPackets**](inetfwv6mgr-logdroppedpackets.md)
-   [**INetFwV6Mgr::put\_LogConnections**](inetfwv6mgr-logconnections.md)
-   [**INetFwV6Connection::EnableFirewall**](inetfwv6connection-enablefirewall.md)
-   [**INetFwV6Connection::DisableFirewall**](inetfwv6connection-disablefirewall.md)
-   [**INetFwV6Connection::OpenPort**](inetfwv6connection-openport.md)
-   [**INetFwV6Connection::ClosePort**](inetfwv6connection-closeport.md)

 

 




