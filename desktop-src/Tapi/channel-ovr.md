---
description: Each line has one or more channels. The service providers normally handle how channels are exposed as addresses to an application, and the end user or server does not require specific knowledge of channels.
ms.assetid: 8c7d38e0-1863-461f-9225-7a0b419532a3
title: Channel (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Channel (Telephony API)

Each line has one or more channels. The service providers normally handle how channels are exposed as addresses to an application, and the end user or server does not require specific knowledge of channels.

Channels are identical and therefore interchangeable. In POTS (Plain Old Telephone Service), exactly one channel exists on a line, and the channel is used exclusively for voice. With ISDN, at least three (and as many as 30 or more) channels can exist on a line simultaneously.

Each channel can have its own address, which means a line could have as many addresses as it has channels. The precise relationship between channels and addresses exposed to an application is dependent on a service provider's implementation.

Some service providers support the assignment of more than one address to a single channel. On POTS lines, multiple addresses are made possible by various systems, such as direct inward dialing (DID) or distinctive ringing, which are extra-fee services that the telephone company provides.

Many large corporations use DID for incoming calls. Before a call is connected, its destination extension number is signaled to the PBX, which causes the extension to ring instead of the operator's phone. An example of distinctive ringing in a private home would be if the parents used one address, the children another, and a fax machine a third. Because only one line connects the house to the telephone network, all phones ring when a call appears, but the ring pattern is different depending on the number that the calling party dialed. With distinctive ringing, the people know who the incoming call is for, and the fax machine answers its calls by recognizing its own ringing style.

In ISDN, the various B channels might not have separate addresses. Because these B channels might be on the same address, it is the service provider (and not the application or a person who has dialed the number) that assigns calls to these channels.

 

 



