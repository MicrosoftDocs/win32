---
description: This section describes Winsock extensions specific to Internetwork Packet Exchange/Sequenced Packet Exchange (IPX/SPX). It also describes aspects of base Winsock functions that either require special consideration or may exhibit unique behavior.
ms.assetid: 8447e063-767a-40b8-b094-724393e85be2
title: Winsock IPX/SPX Annex
ms.topic: article
ms.date: 05/31/2018
---

# Winsock IPX/SPX Annex

This section describes Winsock extensions specific to Internetwork Packet Exchange/Sequenced Packet Exchange (IPX/SPX). It also describes aspects of base Winsock functions that either require special consideration or may exhibit unique behavior.



| Element          | Description                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Protocol name(s) | IPX, SPX                                                                                                                                        |
| Description      | Provides transport services over the IPX networking layer: IPX for unreliable datagrams, SPX for reliable, connection-oriented message streams. |
| Address family   | AF\_IPX                                                                                                                                         |
| Header file      | Wsipx.h                                                                                                                                         |



 

This section discusses how to use Winsock with the IPX family of protocols, enabling traditional IPX applications to be ported to Winsock. IPX networks operate in a fundamentally different manner than IP networks, so such differences must be considered when using IPX/SPX.

 

 



