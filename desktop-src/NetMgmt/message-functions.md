---
title: Message Functions (Network Management)
description: The network management message functions send messages and maintain message aliases. The message functions are listed following.
ms.assetid: 9face737-3472-4a53-97b6-e861a60ee96a
ms.topic: article
ms.date: 05/31/2018
---

# Message Functions (Network Management)

\[The message functions are not supported as of Windows Vista because the alerter and messenger services are not supported.\]

The network management message functions send messages and maintain message aliases. The message functions are listed following.

**Windows Server 2003:** The alerter and messenger services are disabled by default. You must re-enable the services before calling the network management [Alert functions](alert-functions.md) or the network management Message functions.



| Function                                               | Description                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------|
| [**NetMessageBufferSend**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagebuffersend)   | Sends a message to a registered message alias.                                  |
| [**NetMessageNameAdd**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenameadd)         | Registers a message alias in the message name table.                            |
| [**NetMessageNameDel**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenamedel)         | Deletes a message alias from the message name table.                            |
| [**NetMessageNameEnum**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenameenum)       | Lists all the message aliases stored in the message name table.                 |
| [**NetMessageNameGetInfo**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenamegetinfo) | Returns information about a particular message alias in the message name table. |



 

A *message* is a buffer of text data sent to a user or application on the network. To receive a message, a user or application must register a message alias in a computer's table of message names. The following aliases are registered by default: "user", "machine", "domain", or "\*" (the current domain of the computer). The "domain" alias specifies the set of computers that have the same domain name defined as their domain or as their workgroup and listen to broadcasts on the same subnet. For NetBIOS over TCP/IP, specifying the "domain" alias can also succeed across subnets if the domain name is resolved by a name server, or if NetBIOS datagram broadcasts are forwarded across routers. Therefore, messages sent to a domain do not have guaranteed delivery to all members of the domain. It is also possible for some domain members to receive the message multiple times if they have multiple transports installed that support NetBIOS.

You can also register a message alias by calling the [**NetMessageNameAdd**](/windows/desktop/api/Lmmsg/nf-lmmsg-netmessagenameadd) function. A *message name table* contains a list of registered message aliases (users and applications) permitted to receive messages. The aliases registered in the message name table are case insensitive.

The messenger service must be running on the receiving computer to display a pop-up message when the message is received. In addition, the Workstation service must be running on the local computer. NetBIOS is the transport mechanism used between the sender and receiver.

Message functions are available at two information levels:

-   [**MSG\_INFO\_0**](/windows/desktop/api/Lmmsg/ns-lmmsg-msg_info_0)
-   [**MSG\_INFO\_1**](/windows/desktop/api/Lmmsg/ns-lmmsg-msg_info_1)

The **MSG\_INFO\_1** information level exists only for compatibility. The messenger service does not forward names or allow names to be forwarded to it.

 

 




