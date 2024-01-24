---
description: A handoff set specifies the protocols that follow a protocol. The parser uses a handoff set only when the parser can identify the next protocol from the data in a protocol instance.
ms.assetid: d1f44646-98ee-4e3a-a81a-83d6c87c23f4
title: Specifying a Handoff Set
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Handoff Set

A handoff set specifies the protocols that follow a protocol. The parser uses a handoff set only when the parser can identify the next protocol from the data in a protocol instance.

For example, the TCP protocol has a port property that identifies the protocol that follows the TCP protocol. A property value of 20 indicates that the next protocol is FTP. A property value of 53 indicates that the next protocol is DNS. Because the port property identifies the protocol that follows, the TCP parser can use the following handoff set to get a handle for the protocol that the port property specifies.

``` syntax
[TCP_HandoffSet]
  20    = FTP
  21    = FTP
  23    = TELNET
  25    = SMTP
  53    = DNS
  79    = FINGER
  80    = HTTP
  102   = ISO
  111   = RPC
  119   = NNTP
  137   = NBT, 1000
  138   = NBT, 1002
  139   = NBT, 1001
  389   = LDAP
  445   = NBT, 1001
  515   = LPR
  612   = HMMP
  613   = HMMP
  1024  = NBT, 1001
  1047  = NBT, 1001
  1362  = TDS
  1433  = TDS
  1723  = PPTP
  3020  = NBT, 1001
  3268  = LDAP
  5678  = PPTP
```

Handoff sets are stored in the parser INI file. For example, the preceding TCP handoff set is located in tcpip.ini file. Note that if a parser DLL supports multiple protocols, each parser that uses a handoff set has its own location in the INI file.

Handoff set information is specified during the implementation of the [**ParserAutoInstallInfo**](parserautoinstallinfo.md) function. The parser can specify the protocols that precede the parser protocol, and the protocols that follow the parser protocol. Network Monitor takes all the protocols that precede, and adds the parser protocol to the follow set sections of the parser INI file — for each preceding protocol. Network Monitor stores the list of protocols that follow in the handoff set section of the parser INI file.

Network Monitor stores the handoff set information in the parser INI file, but the parser does not access the INI files directly. To use the information in the handoff set, the parser calls the [**CreateHandoffTable**](createhandofftable.md) function to create a handoff table. Typically, the handoff table is created when the parser registers the protocol. After the protocol is registered, Network Monitor creates a handoff set table that the parser can use.

The parser uses its handoff set when recognizing data. First the parser reads the value of the property that identifies the next protocol. Then the parser calls the [**GetProtocolFromTable**](getprotocolfromtable.md) to get a handle to the next protocol. Last, the parser returns a pointer to the handle in the *phNextProtocol* parameter of [**RecognizeFrame**](recognizeframe.md).

 

 



