---
title: Diagram of Internet Connection Sharing and Internet Connection Firewall
description: The Internet Connection Sharing (ICS) API should be used for applications that run on the computer that has Internet Connection Sharing enabled. Such computers are typically performing the role of an Internet gateway for a home or small business LAN.
ms.assetid: 8a376ed0-7c00-4e7a-801a-8b439867ae28
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Diagram of Internet Connection Sharing and Internet Connection Firewall

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The [Internet Connection Sharing](internet-connection-sharing-and-internet-connection-firewall-reference.md) (ICS) API should be used for applications that run on the computer that has Internet Connection Sharing enabled. Such computers are typically performing the role of an Internet gateway for a home or small business LAN.

![ics/icf enabled computer](images/icsicf01.png)

Computers that are not serving as Internet gateways do not need to use the Internet Connection Sharing feature. In this case, only the Internet Connection Firewall functionality is required. The following diagram depicts this scenario.

![only icf enabled computer](images/icf01.png)

To configure a remote Internet Gateway Device on the local network, use [Network Address Translation Traversal](network-address-translation-traversal.md).

 

 




