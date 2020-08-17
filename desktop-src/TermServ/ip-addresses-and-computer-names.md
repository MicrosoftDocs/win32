---
title: IP addresses and computer names
description: It is not safe to assume that the computer name or the IP address assigned to the computer are associated with a single user because multiple users can be logged on simultaneously to a Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 17cfd14e-1fff-4154-89a6-8dbbf19a6cae
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# IP addresses and computer names

Multiple users can be logged on simultaneously to a Remote Desktop Session Host (RD Session Host) server. Consequently, it is not safe to assume that the computer name or the IP address assigned to the computer are associated with a single user. This differs from a single-user Windows environment, in which only one user is logged on at a time.

Applications that use the computer name or IP address for licensing or as a means of identifying an iteration of the application on the network will not work properly in a Remote Desktop Services environment, because the server's computer name or IP address can be associated with many users.

In a Remote Desktop Services environment, each client terminal or terminal emulator has a separate IP address and computer name. To retrieve the IP address and computer name of a client, call the [**WTSQuerySessionInformation**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsquerysessioninformationa) function. Other functions that retrieve these network addresses and computer names retrieve the name and address of the RD Session Host server. For example, the [**GetComputerNameEx**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getcomputernameexa) function returns the computer name of the server.

 

 