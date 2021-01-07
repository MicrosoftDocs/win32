---
description: On Windows XP a later, a new command-line tool is provided for configuring and managing IPv4. This tool uses the &\#0034;netsh interface ip&\#0034; command for configuring and managing IPv4.
ms.assetid: d27eb0c2-4ae0-42d1-b92e-055a1c232e1c
title: Using IPv6
ms.topic: article
ms.date: 05/31/2018
---

# Using IPv6

On Windows XP a later, a new command-line tool is provided for configuring and managing IPv4. This tool uses the "netsh interface ip" command for configuring and managing IPv4.

On Windows XP with Service Pack 1 (SP1) and later, this new command-line tool was enhanced to support the configuration and management of IPv6. This enhanced tool is the "netsh interface ipv6" command. Configuration changes made using the Netsh.exe commands are permanent and are not lost when the computer or the IPv6 protocol is restarted.

The following command is available on Windows XP with SP1 and later to query and configure IPv6 on a local computer:

-   [Netsh.exe](netsh-exe.md)

Prior to Windows XP with Service Pack 1 (SP1), IPv6 configuration and management used several older command-line tools to configure and manage IPv6. Using these older tools, the IPv6 changes are not permanent and are lost when the computer or the IPv6 protocol was restarted.

The following older commands are available on Windows XP

-   [Net.exe](net-exe-2.md)
-   [Ipv6.exe](ipv6-exe-2.md)
-   [Ipsec6.exe](ipsec6-exe-2.md)

These older tools were also provided in the IPv6 Technology Preview for Windows 2000

Configuration changes using these older tools could be maintained by placing them as command lines in a command script file (.cmd) that is run after restarting the computer or the IPv6 protocol. To reinstate configuration changes automatically after restarting, is was possible to use the Windows Scheduled Tasks to run the .cmd file when the computer starts.

These older tools are not provided on Windows Server 2003 and later. The "netsh interface ipv6" tool is provided for configuring and managing IPv6 from the command-line on Windows Server 2003 and later.

## Related topics

<dl> <dt>

[Internet Protocol Version 6 (IPv6)](internet-protocol-version-6-ipv6-2.md)
</dt> <dt>

[IPv6 Guide for Windows Sockets Applications](ipv6-guide-for-windows-sockets-applications-2.md)
</dt> <dt>

[IPv6 Technology Preview for Windows 2000](https://www.microsoft.com/downloads/details.aspx?FamilyID=27b1e6a6-bbdd-43c9-af57-dae19795a088)
</dt> </dl>

 

 



