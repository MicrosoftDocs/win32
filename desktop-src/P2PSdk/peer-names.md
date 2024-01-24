---
description: Peer names are used by Peer Name Resolution Protocol (PNRP), the Peer Identity Manager, and the Peer Grouping Infrastructure.
ms.assetid: b0d78b17-6f48-4294-b8a2-8fcc1a7f8ef1
title: Peer Names
ms.topic: article
ms.date: 05/31/2018
---

# Peer Names

Peer names are used by Peer Name Resolution Protocol (PNRP), the Peer Identity Manager, and the Peer Grouping Infrastructure. Peer names are stable names for resources such as computers, users, groups, or services. PNRP uses peer names to identify nodes in a peer network.

> [!Note]  
> An endpoint that the Peer Infrastructure uses is actually a tuple that consists of an IPv4 or IPv6 address, port, and protocol (either TCP or UDP). One peer name can have more than one tuple.

 

A peer name is a text string that has the following format:

-   "Authority.Classifier"

The value of an Authority depends on whether the name is secure or unsecured. The Classifier of a peer name is a string. A Classifier can be any name that contains 150 or less UNICODE characters. Peer names are case-sensitive and can be registered as secured or unsecured. The following list identifies some examples of peer names:

-   "0.MyUnsecuredPeerName"
-   "0.JohnDoe.Games"
-   "6520c005f63fc1864b7d8f3cabebd4916ae7f33d.JohnDoe"

## Secure Peer Names

For a secure name, the Authority is the Secure Hash Algorithm (SHA) hash of the public key of the peer name, and results in a 40 character hexadecimal string. A secure peer name can only be registered with PNRP by the owner or delegate of the peer name owner. A secured peer name must be created by calling [**PeerCreatePeerName**](/windows/desktop/api/P2P/nf-p2p-peercreatepeername).

## Unsecured Peer Names

For an unsecured name, the Authority is zero (0), and the Classifier is the only significant part of the peer name, which creates an unsecured peer name without an associated [identity](identity-manager-api.md). Unsecured peer names are used in PNRP name registration and resolution. Unsecured peer names provide a useful way to register and resolve resources that do not require secure name resolution. However, any node can publish any unsecured name. Applications concerned with security must ensure that they are robust and secure in their consumption of unsecured peer names.

> [!Note]  
> Anyone can register an unsecured peer name with PNRP.

 

## PNRP and the Nearest Peer Name Instance

There can be more than one instance of a peer name. When using [PNRP](pnrp-namespace-provider-api.md) to resolve a peer name, there is a concept of a **nearest** peer name instance, which means that the name has a service location closest to the **saHint** member specified in [**PNRPINFO\_V1**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1) or [**PNRPINFO\_V2**](/previous-versions/windows/desktop/legacy/aa371671(v=vs.85)). If no hint is supplied, closest to one of the local IP addresses.

 

 
