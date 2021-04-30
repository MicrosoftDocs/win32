---
description: Peer-to-peer Grouping is a technology that allows a developer to create a secure peer network quickly and effectively.
ms.assetid: ee72f60b-1e5b-4b69-bda0-2ae80734c144
title: How to Work With Groups
ms.topic: article
ms.date: 05/31/2018
---

# How to Work With Groups

Peer-to-peer Grouping is a technology that allows a developer to create a secure peer network quickly and effectively. The following list identifies the major considerations in creating a peer grouping application.

-   [Obtaining a Peer Identity](#obtaining-a-peer-identity)
-   [Starting Up a Peer Group](#starting-up-the-peer-grouping-infrastructure)
-   [Registering for Grouping Events](#registering-for-peer-grouping-events)
-   [Connecting to a Group](#obtaining-a-group-handle)
-   [Creating Administrator and Member Roles](#creating-administrator-and-member-roles)
-   [Finding a Peer](#finding-a-peer)
-   [Connecting Directly to a Peer](#connecting-directly-to-a-peer)
-   [Closing and Shutting Down a Group](#closing-and-shutting-down-a-peer-group)

## Obtaining a Peer Identity

Before creating or connecting to a group, a peer must obtain a peer identity, which is a name used to uniquely identify a peer to a group. To obtain an enumerated list of all peer identities defined on the peer, call [**PeerEnumIdentities**](/windows/desktop/api/P2P/nf-p2p-peerenumidentities), which returns a handle to the enumeration. To obtain the peer identities, call [**PeerGetNextItem**](/windows/desktop/api/P2P/nf-p2p-peergetnextitem) with the enumeration handle and the number of members to retrieve. Continue calling **PeerGetNextItem** until the *pCount* parameter returns a value less than the number of peer identities requested.

If a peer identity for the peer does not exist, it can be created by calling [**PeerIdentityCreate**](/windows/desktop/api/P2P/nf-p2p-peeridentitycreate). After creating a peer identity, the peer generates an identity XML blob that contains the public key assigned to it

The peer identity information is obtained by calling [**PeerIdentityGetXML**](/windows/desktop/api/P2P/nf-p2p-peeridentitygetxml). This peer identity information is used by the group creator or an administrator to issue the credentials needed to join the group, as an invitation XML blob.

For more information on peer identities, please refer to the [Identity Manager API](identity-manager-api.md) documentation

## Starting Up the Peer Grouping Infrastructure

Before any function in the Peer Grouping API is called by an application, [**PeerGroupStartup**](/windows/desktop/api/P2P/nf-p2p-peergroupstartup) must be called. This function initializes the Peer Grouping Infrastructure for the application and sets the supported version.

## Obtaining a Group Handle

To connect to a group and begin participating, a handle to a peer group must be obtained. The following list identifies the three ways to connect to a peer group:

-   Creating a peer group by calling [**PeerGroupCreate**](/windows/desktop/api/P2P/nf-p2p-peergroupcreate), which initializes a new peer group and returns a valid handle with the peer as the owner and sole administrator.
-   Joining a peer group by calling [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin). To join a peer group, a peer must receive an invitation from a peer group administrator. To obtain an invitation, send the identity information XML blob to the administrator who creates an invitation and sends it to you by an external mechanism, such as email or FTP. The invitation and peer identity are passed to **PeerGroupJoin**, which returns a valid handle to the group.
-   Opening a peer group that a peer has joined previously by calling [**PeerGroupOpen**](/windows/desktop/api/P2P/nf-p2p-peergroupopen). In this situation, obtaining an invitation is not necessary.

After you obtain a valid peer group handle from one of the above functions, you can connect to a peer group by calling [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect) with the new handle.

> [!Note]  
> If the connection to a peer group fails, the PEER\_GROUP\_EVENT\_CONNECTION\_FAILED event occurs. The handler can attempt to reestablish the connection to the peer group.

 

## Registering for Peer Grouping Events

Before a peer participates in a peer group, the peer must register for peer group events. To register for specific peer events, call [**PeerGroupRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupregisterevent), and pass in one or more of the peer event types defined in PEER\_GROUP\_EVENT\_TYPE. You must register for each peer event that applies to your application; for example, to receive data over a direct connection, register for the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION and PEER\_GROUP\_EVENT\_INCOMING\_DATA events. Each call takes an event handle and returns an **HPEEREVENT** handle for that peer event.

Event handlers can obtain the data associated with a peer event by passing the handle to registered peer events to [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata). This peer event data is returned as a PEER\_GROUP\_EVENT\_DATA union. If the peer event queue is empty, this function returns PEER\_S\_NO\_EVENT\_DATA.

You can unregister for peer events by calling [**PeerGroupUnregisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupunregisterevent) and providing the handle for the peer event you want to unregister. After the function is called, the peer events associated with the handle are no longer registered.

## Creating Administrator and Member Roles

The peer who creates the peer group is known as the peer group creator, and has the administrator role by default. Only the peer group creator can set the group properties.

Peers invited to the peer group can be either an administrator or a member. If they are assigned an administrator role by the administrator issuing the invitation, they can invite new members to the peer group, and likewise assign the administrator role to other members.

The roles of peer group members are set in the invitations the administrator gives to a member. To add more administrators, set the value of the *pRoles* parameter of [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation) to PEER\_GROUP\_ROLE\_ADMIN when creating an invitation.

Members can participate in a peer group, but cannot invite and authorize new members, set group properties, or update or delete group records that they do not specifically create. To assign member status to a participating peer, set the value of the **pRoles** parameter of [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation) to PEER\_GROUP\_ROLE\_MEMBER when you create an invitation for that peer.

To change the role of a member, new credentials containing the new role must be issued to that member. To accomplish this, obtain the [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info) structure for this member from the PEER\_MEMBER structure returned by [**PeerGroupEnumMembers**](/windows/desktop/api/P2P/nf-p2p-peergroupenummembers). Change the **pRoles** field in **PEER\_CREDENTIAL\_INFO** to the new role, and pass the structure to [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials).

The new credentials will not go into effect for the peer until they connect to the peer group. If they are currently connected, they must close the group and reconnect to obtain the updated credentials.

## Finding a Peer

To obtain an enumerated list of all peers participating in the peer group, call [**PeerGroupEnumMembers**](/windows/desktop/api/P2P/nf-p2p-peergroupenummembers) with the group handle, which returns a handle to the enumeration. To obtain the members, call [**PeerGetNextItem**](/windows/desktop/api/P2P/nf-p2p-peergetnextitem) with the enum handle and the number of members to retrieve. Continue calling **PeerGetNextItem** until the *pCount* parameter returns a value less than the number of members requested. Note that the complete list of available members may not be returned.

Each member is represented as a [**PEER\_MEMBER**](/windows/desktop/api/P2P/ns-p2p-peer_member) structure, which contains the identity of the peer, node IDs, and IP addresses for active peers.

When finished, close the enumeration and release the associated memory by calling [**PeerEndEnumeration**](/windows/desktop/api/P2P/nf-p2p-peerendenumeration).

## Connecting Directly to a Peer

When a peer is connected to a peer group, direct one-to-one exchanges with other connected members are initiated by calling [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection) and supplying the identity of the other peer. This call is asynchronous, and returns a 64-bit connection ID. If the call is successful, you receive the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION\_EVENT peer event to indicate that the connection is successful. If the connection is successful, the connection ID is valid and can be used to send and receive data through the direct connection.

To be able to receive direct connections, the other peer must also have previously registered for the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION peer event.

To send data to a peer, call [**PeerGroupSendData**](/windows/desktop/api/P2P/nf-p2p-peergroupsenddata) with a valid connection ID. To receive data, the other peer must be registered for the PEER\_GROUP\_EVENT\_INCOMING\_DATA peer event. Likewise, if the sending peer wants to receive data in turn, it also must be registered for the PEER\_GROUP\_EVENT\_INCOMING\_DATA peer event.

To receive the total set of currently active direct connections with other peers in a group, call [**PeerGroupEnumConnections**](/windows/desktop/api/P2P/nf-p2p-peergroupenumconnections) to open the enumeration and iterate through the list of connections by using [**PeerGetNextItem**](/windows/desktop/api/P2P/nf-p2p-peergetnextitem).

To close a direct connection, call [**PeerGroupCloseDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupclosedirectconnection) and pass in the connection ID.

## Closing and Shutting Down a Peer Group

To close a connection to a peer group, call [**PeerGroupClose**](/windows/desktop/api/P2P/nf-p2p-peergroupclose), which invalidates the group handle, but does not shut down the Peer Grouping Infrastructure. Peer-to-peer group data is deleted by calling [**PeerGroupDelete**](/windows/desktop/api/P2P/nf-p2p-peergroupdelete).

When the application is finished using the Peer Grouping Infrastructure, it must call [**PeerGroupShutdown**](/windows/desktop/api/P2P/nf-p2p-peergroupshutdown).

 

 



