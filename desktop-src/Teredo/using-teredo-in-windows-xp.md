---
title: Using Teredo in Windows XP
ms.assetid: 21590e3b-03de-48a4-b142-5d1934dacc38
description: "Learn more about: Using Teredo in Windows XP"
ms.topic: article
ms.date: 05/31/2018
---

# Using Teredo in Windows XP

To use the Teredo client or host-specific relay on computers running Windows XP with Service Pack 1 (SP1) with the Advanced Networking Pack, Windows XP with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1), or Windows Server 2003 with Service Pack 2 (SP2), an application developer must do the following:

-   Ensure that the application is compatible with IPv6 by using new Windows Sockets 2 programming elements (functions and structures) that support both IPv4 and IPv6. For more information, see the [IPv6 Guide for Windows Sockets Applications](../winsock/ipv6-guide-for-windows-sockets-applications-2.md).
-   Enable the use of Teredo in your application by setting the IPV6\_PROTECTION\_LEVEL Windows Sockets socket option to the PROTECTION\_LEVEL\_UNRESTRICTED level. For more information, see [Using IPV6\_PROTECTION\_LEVEL](/previous-versions/aa916826(v=msdn.10)). You can also set this option through the [System.Net.Sockets](/dotnet/api/system.net.sockets?view=netcore-3.1) .NET Framework class.
-   Create an exception for the Windows Firewall to allow unsolicited incoming Teredo traffic. Use the [Windows Firewall](/previous-versions/windows/desktop/ics/windows-firewall-start-page) APIs to create a port exception for the UDP port assigned for Teredo traffic. For more information and examples detailing required security and traffic considerations for Teredo, see [Using Teredo](using-teredo.md).

To ensure that Teredo is available for use when the application runs, application developers should do the following during the application's installation process:

-   Install IPv6 with the **netsh interface ipv6 install** command. Windows Firewall protects the user's computer from unsolicited incoming IPv6 traffic in the same way as IPv4 traffic.
-   Enable Teredo with the **netsh interface ipv6 set teredo client** command.

Optionally, you can test whether IPv6 is installed each time your application runs and install IPv6 and enable Teredo as needed. You should also inform the user that IPv6 is being installed and that Teredo is being enabled.

 

 
