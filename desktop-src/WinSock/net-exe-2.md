---
description: Net.exe can be used to stop and start the IPv6 protocol.
ms.assetid: faa555d9-eb20-4b7a-94eb-b67a48ee630e
title: Net.exe
ms.topic: article
ms.date: 05/31/2018
---

# Net.exe

Net.exe can be used to stop and start the IPv6 protocol. Restarting IPv6 reinitializes the protocol as if the computer were restarting, which may change interface numbers. Net.exe has many subcommands. The following commands are relevant to IPv6:

<dl> <dt>

<span id="net_stop_tcpip6"></span><span id="NET_STOP_TCPIP6"></span>**net stop tcpip6**
</dt> <dd>

Stops the IPv6 protocol and unloads it from memory. This command fails if any IPv6 sockets are open.

</dd> <dt>

<span id="net_start_tcpip6"></span><span id="NET_START_TCPIP6"></span>**net start tcpip6**
</dt> <dd>

Starts the IPv6 protocol if it was stopped. If a new Tcpip6.sys driver file is present in the %systemroot%\\System32\\Drivers directory, that driver file is loaded.

</dd> </dl>

 

 



