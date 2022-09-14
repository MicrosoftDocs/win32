---
description: This topic discusses specific security considerations when using the Peer Infrastructure.
ms.assetid: 088a2111-f4ee-4bec-98a9-ac138950958b
title: Security Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations

This topic discusses specific security considerations when using the Peer Infrastructure.

When you develop a peer application using the Peer Infrastructure, for security reasons you must consider directory permissions, guest access to peer networking services, information disclosure, and Security Service Provider Implementation.

## Directory Permissions

Peer-to-peer networking services store data in the user profile directory tree of a user. A user must have write permissions in the **application data** subtree of the profile. By default, this access control list (ACL) is set correctly, but a user can change it manually.

## Guest Access to Peer Networking Services

A Guest account and members of the **Guests** Windows Security Group do not have access to most peer services. Applications should have local user access or higher.

## Information Disclosure

Information disclosure involves address, database, and identity and group credentials. The following sections identify and define the information disclosure.

**Address Disclosure** Peer Name Resolution Protocol (PNRP) is an identifier resolution service that allows a peer name identifier to be resolved into an IP address. Similar to DNS, PNRP publishes an IP address so that users who know the corresponding identifier can resolve it to that address.

-   Publishing an identifier in PNRP means any user can resolve the identifier to the published IP address, and determine the IP address of the PNRP service that published the identity.
-   The Peer Grouping Infrastructure automatically publishes the peer group name of the local group instance in PNRP. While connected to a peer group, anyone who knows the peer name for the group can resolve the addresses of active members, and knows the current address of each user.

The ability of a user to connect to other peer group members or peer graph nodes while logged on is a primary feature of peer networking. While connected to a peer group or graph, the current IP address of a user can be published in a presence record within the peer group or graph. By default, anyone participating in that peer group or graph can enumerate members of the group or graph, and determine the current addresses of the members. This ability is a configurable Peer Grouping and Peer Graphing property.

**Database Disclosure**The Peer Grouping and Graphing Infrastructures record databases are stored on the local file system. Any Windows user with administrative access to the local file system (such as a local administrator) can theoretically access the data in the local peer graph or group database. This is consistent with the ability of local administrators to access any data on the local computer.

**Identity and Group Credentials Disclosure**Peer-to-peer grouping requires that members establish connections with each other to authenticate using modified X.509 certificate chains. As part of authentication, each member's corresponding identity and Group Membership Certificate (GMC) chains are exchanged.

While connected to a peer group, the Peer Grouping Infrastructure publishes the group peer name with PNRP. As part of the normal PNRP operation, the GMC chain for that group can be provided to other PNRP instances to prove authorization to publish the group peer name.

## Security Service Provider Implementation

The Peer Graphing Infrastructure is as secure as the Security Service Provider (SSP) that the application developer implements. The stronger the SSP, the stronger the security of the Peer Graphing application.

 

 



