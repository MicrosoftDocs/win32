---
description: The Netsh commands for IPv6 provide a command-line tool that you can use to query and configure IPv6 interfaces, address, caches, and routes. The Netsh interface IPv6 commands are supported on Windows XP with Service Pack 1 (SP1) and later.
ms.assetid: 68e17a55-4dd5-40cd-8996-25fa278ddd19
title: Netsh.exe
ms.topic: article
ms.date: 05/31/2018
---

# Netsh.exe

The Netsh commands for IPv6 provide a command-line tool that you can use to query and configure IPv6 interfaces, address, caches, and routes. The Netsh interface IPv6 commands are supported on Windows XP with Service Pack 1 (SP1) and later.

Netsh.exe has many subcommands for IPv6. A complete list of options for Netsh Interface IPv6 is available from the command prompt on Windows XP with SP1 and later by typing the following:

**netsh interface ipv6 /?**

Documentation on all of the **netsh** commands for IPv6 is also available online on Technet. For more information on **netsh** on Windows Server 2008, please see [Netsh commands for Interface (IPv4 and IPv6)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770948(v=ws.10)). For more information on **netsh** on Windows Server 2003, please see [Netsh commands for Interface IPv6](/previous-versions/windows/it-pro/windows-server-2003/cc740203(v=ws.10)).

The following are a few commonly used commands for IPv6, although many other commands are supported:

<dl> <dt>

<span id="netsh_interface_ipv6_add_address"></span><span id="NETSH_INTERFACE_IPV6_ADD_ADDRESS"></span>**netsh interface ipv6 add address**
</dt> <dd>

Adds an IPv6 address to a specific interface on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_add_dns"></span><span id="NETSH_INTERFACE_IPV6_ADD_DNS"></span>**netsh interface ipv6 add dns**
</dt> <dd>

Adds a DNS server IPv6 address to the statically-configured list of DNS servers for the specified interface on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_add_route"></span><span id="NETSH_INTERFACE_IPV6_ADD_ROUTE"></span>**netsh interface ipv6 add route**
</dt> <dd>

Adds a route for a specified IPv6 prefix address on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_delete_address"></span><span id="NETSH_INTERFACE_IPV6_DELETE_ADDRESS"></span>**netsh interface ipv6 delete address**
</dt> <dd>

Deletes the specified IPv6 address from a specific interface on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_delete_dns"></span><span id="NETSH_INTERFACE_IPV6_DELETE_DNS"></span>**netsh interface ipv6 delete dns**
</dt> <dd>

Deletes a DNS server address from the statically-configured list of DNS servers for the specified interface on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_delete_interface"></span><span id="NETSH_INTERFACE_IPV6_DELETE_INTERFACE"></span>**netsh interface ipv6 delete interface**
</dt> <dd>

Deletes a specified interface from the IPv6 stack on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_delete_route"></span><span id="NETSH_INTERFACE_IPV6_DELETE_ROUTE"></span>**netsh interface ipv6 delete route**
</dt> <dd>

Deletes a route for a specified IPv6 prefix address on the local computer. This command has suboption parameters that must to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_dump"></span><span id="NETSH_INTERFACE_IPV6_DUMP"></span>**netsh interface ipv6 dump**
</dt> <dd>

Creates a script that contains the commands to create the current configuration. If saved to a file, this script can be used to restore altered configuration settings.

</dd> <dt>

<span id="netsh_interface_ipv6_install"></span><span id="NETSH_INTERFACE_IPV6_INSTALL"></span>**netsh interface ipv6 install**
</dt> <dd>

Installs the IPv6 protocol on the local computer.

</dd> <dt>

<span id="netsh_interface_ipv6_renew"></span><span id="NETSH_INTERFACE_IPV6_RENEW"></span>**netsh interface ipv6 renew**
</dt> <dd>

Restarts the IPv6 interfaces on the local computer.

</dd> <dt>

<span id="netsh_interface_ipv6_reset"></span><span id="NETSH_INTERFACE_IPV6_RESET"></span>**netsh interface ipv6 reset**
</dt> <dd>

Resets the IPv6 configuration state on the local computer.

</dd> <dt>

<span id="netsh_interface_ipv6_show_global"></span><span id="NETSH_INTERFACE_IPV6_SHOW_GLOBAL"></span>**netsh interface ipv6 show global**
</dt> <dd>

Displays the global configuration parameters for IPv6 on the local computer.

</dd> <dt>

<span id="netsh_interface_ipv6_show_address"></span><span id="NETSH_INTERFACE_IPV6_SHOW_ADDRESS"></span>**netsh interface ipv6 show address**
</dt> <dd>

Displays all IPv6 addresses or all IPv6 addresses on a specific interface on the local computer. This command has suboption parameters that may need to be specified.

</dd> <dt>

<span id="netsh_interface_ipv6_uninstall"></span><span id="NETSH_INTERFACE_IPV6_UNINSTALL"></span>**netsh interface ipv6 uninstall**
</dt> <dd>

Uninstalls the IPv6 protocol on the local computer.

</dd> </dl>

## Netsh commands for IPv4

Similar Netsh commands are available for IPv4. A complete list of options for Netsh commands for use with IPv4 is available from the command prompt on Windows XP with SP1 and later by typing the following:

**netsh interface ip /?**

Documentation on all of the Netsh commands for IPv4 is also available online on Technet. For more information, please see [Netsh commands for Interface IP](/previous-versions/windows/it-pro/windows-server-2003/cc738592(v=ws.10))

 

 
