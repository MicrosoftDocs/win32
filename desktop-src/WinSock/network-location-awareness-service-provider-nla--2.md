---
description: Personal computers running Microsoft Windows often have numerous network connections, such as multiple network interface cards (NIC) connected to different networks, or a physical network connection and a dial-up connection.
ms.assetid: 73a1999d-0c19-4f9d-8e47-07f819874535
title: Network Location Awareness Service Provider (NLA)
ms.topic: article
ms.date: 05/31/2018
---

# Network Location Awareness Service Provider (NLA)

Personal computers running Microsoft Windows often have numerous network connections, such as multiple network interface cards (NIC) connected to different networks, or a physical network connection and a dial-up connection. Windows Sockets has been capable of enumerating available network interfaces for some time, but certain critical information about network connections was previously unavailable. This includes information such as the logical network to which a Windows computer is attached or whether multiple interfaces are connected to the same network.

The Network Location Awareness service provider, commonly referred to as NLA, enables Windows Sockets 2 applications to identify the logical network to which a Windows computer is attached. In addition, NLA enables Windows Sockets applications to identify to which physical network interface a given application has saved specific information. NLA is implemented as a generic Windows Sockets 2 Name Resolution service provider.

 

 



