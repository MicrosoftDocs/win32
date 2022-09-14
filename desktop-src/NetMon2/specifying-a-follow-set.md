---
description: A follow set specifies the protocols that follow a protocol. Network Monitor uses a follow set when the parser cannot identify the next protocol from the data in a protocol instance.
ms.assetid: 9e73c724-a540-42f8-b273-4f02c39d81c4
title: Specifying a Follow Set
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Follow Set

A follow set specifies the protocols that follow a protocol. Network Monitor uses a follow set when the parser cannot identify the next protocol from the data in a protocol instance.

For example, the NetBIOS parser specifies a follow set because the data in the NetBIOS protocol does not identify which protocol is next. As a result the NetBIOS parser must create a follow set of all the protocols that may follow.

The following code example identifies the NetBIOS follow set in the [*Parser.ini*](p.md) file. The follow set contains server message block (SMB), and Microsoft remote procedure call (MSRPC) protocols. These are the only protocols that can follow an instance of the NetBIOS protocol.

``` syntax
[NETBIOS]
   Comment    = "Network Basic Input/Output System protocol"
   FollowSet  = SMB, MSRPC
   HelpFile   =
```

A parser specifies a follow set during the implementation of the [**ParserAutoInstallInfo**](parserautoinstallinfo.md) function. A parser can specify which protocols precede, and which protocols follow. When a parser specifies the protocols that precede, Network Monitor adds the parser protocol to the follow sets of the specified protocols. When a parser specifies the protocols that follow, Network Monitor creates a new section in the Parser.ini file that includes the follow set of the parser.

 

 



