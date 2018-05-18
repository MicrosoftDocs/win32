---
title: About Internet Connection Sharing and Internet Connection Firewall
description: With the Internet Connection Sharing and Internet Connection Firewall (ICS/ICF) API, you can allow applications to enable, disable, and configure these services.
ms.assetid: '8a376ed0-7c00-4e7a-801a-8b439867ae28'
keywords: ["Internet Connection Sharing ICS", "described"]
---

# About Internet Connection Sharing and Internet Connection Firewall

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

With the Internet Connection Sharing and Internet Connection Firewall (ICS/ICF) API, you can allow applications to enable, disable, and configure these services.

**Note**  All users may read the configuration settings. However, Administrator privileges are required to change ICF configuration settings.

Through the ICS/ICF API, you can allow applications to enumerate connections, enable, or disable ICS on a single connection, and configure port mappings for both ICS and ICF. ICF cannot be enabled on the network bridge connection, connections that are members of the bridge, the ICS private connection, IrDA, or a Direct Cable Connect (DCC) connection.

Altering a port-mapping through the ICS/ICF API causes a [notification](ics-icf-methods-that-provide-notifications-to-the-user-interface.md) to be displayed on the user interface of the local computer.

Beginning with Windows XP with Service Pack 2 (SP2), calling an API to open a port or enable or disable the firewall on an interface no longer requires user confirmation. No dialog box is displayed as a result of calling one of these APIs.

The ICS/ICF API makes changes only on the local computer. Applications intended to create port mappings on a remote ICS computer or Internet Gateway Device (IGD) need to use the [NAT Traversal API](network-address-translation-traversal-reference.md).

The following sections provide further detail about ICS and ICF.

-   [Getting Started Using the ICS API](getting-started-using-the-ics-and-icf-api.md)
-   [Shared Connections](shared-connections.md)
-   [Windows Firewall](about-windows-firewall.md)
-   [ICS/ICF Methods that Provide Notifications to the User Interface](ics-icf-methods-that-provide-notifications-to-the-user-interface.md)

 

 




