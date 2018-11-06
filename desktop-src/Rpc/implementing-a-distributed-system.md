---
title: Implementing a Distributed System
description: One way to implement software in a distributed system is to use raw networking support.
ms.assetid: 46abbbec-caa1-4fee-a713-4a4a2b462051
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Distributed System

One way to implement software in a distributed system is to use raw networking support. This approach includes sockets, named pipes, or HTTP POSTs, GETs, and so on. All of these models force the developer to use low-level programming primitives, in one way or another, which force the developer to deal with network data representation (NDR), packaging data, managing network traffic and failure conditions, data integrity protection and encryption, and so on.

RPC offers a programming model where the developer retains granular control of the network interaction between the client and server through a rich API, while saving developers from the details and burdens that a distributed system tends to introduce.

For example, consider the burden associated with various approaches to protecting the integrity and privacy of message exchanges in a distributed system. When considering network security for packet exchanges, some protections are weaker, some stronger. There is no true network security, only various packet-based security mechanisms; security identifying the caller (which tends to be weak as well, since packet contents can often be changed in transit), security protecting the integrity of the packet without protecting its privacy (various signatures and hashes), and security protecting the privacy of the message exchange (various encryption mechanisms).

Another burden of implementing a secure distributed system is the algorithms necessary to implement security primitives such as encryption, signing, authentication, and so on. A developer can implement those algorithms, but doing so is difficult, error-prone, and even risky, since the resulting algorithms often have subtle security flaws. Alternatively, a developer can use an available security provider to implement protection for the network interactions within a distributed system.

Using RPC, both of these burdens are resolved very easily. A developer simply needs to tell RPC which security package to use, and which security protection should be applied to the message exchange (in terms of authentication, encryption, mutual authentication, caller-identity tracking, and so on). RPC takes care of all the details behind the scenes in an efficient manner, yet provides the developer with full control over precisely how the data will be protected.

 

 




