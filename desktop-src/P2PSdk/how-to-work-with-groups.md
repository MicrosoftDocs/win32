---
Description: 'Peer-to-peer Grouping is a technology that allows a developer to create a secure peer network quickly and effectively.'
ms.assetid: 'ee72f60b-1e5b-4b69-bda0-2ae80734c144'
title: How to Work With Groups
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

Before creating or connecting to a group, a peer must obtain a peer identity, which is a name used to uniquely identify a peer to a group. To obtain an enumerated list of all peer identities defined on the peer, call [**PeerEnumIdentities**](peerenumidentities.md), which returns a handle to the enumeration. To obtain the peer identities, call [**PeerGetNextItem**](peergetnextitem.md) with the enumeration handle and the number of members to retrieve. Continue calling **PeerGetNextItem** until the *pCount* parameter returns a value less than the number of peer identities requested.

If a peer identity for the peer does not exist, it can be created by calling [**PeerIdentityCreate**](peeridentitycreate.md). After creating a peer identity, the peer generates an identity XML blob that contains the public key assigned to it

The peer identity information is obtained by calling [**PeerIdentityGetXML**](peeridentitygetxml.md). This peer identity information is used by the group creator or an administrator to issue the credentials needed to join the group, as an invitation XML blob.

For more information on peer identities, please refer to the [Identity Manager API](identity-manager-api.md) documentation

## Starting Up the Peer Grouping Infrastructure

Before any function in the Peer Grouping API is called by an application, [**PeerGroupStartup**](peergroupstartup.md) must be called. This function initializes the Peer Grouping Infrastructure for the application and sets the supported version.

## Obtaining a Group Handle

To connect to a group and begin participating, a handle to a peer group must be obtained. The following list identifies the three ways to connect to a peer group:

-   Creating a peer group by calling [**PeerGroupCreate**](peergroupcreate.md), which initializes a new peer group and returns a valid handle with the peer as the owner and sole administrator.
-   Joining a peer group by calling [**PeerGroupJoin**](peergroupjoin.md). To join a peer group, a peer must receive an invitation from a peer group administrator. To obtain an invitation, send the identity information XML blob to the administrator who creates an invitation and sends it to you by an external mechanism, such as email or FTP. The invitation and peer identity are passed to **PeerGroupJoin**, which returns a valid handle to the group.
-   Opening a peer group that a peer has joined previously by calling [**PeerGroupOpen**](peergroupopen.md). In this situation, obtaining an invitation is not necessary.

After you obtain a valid peer group handle from one of the above functions, you can connect to a peer group by calling [**PeerGroupConnect**](peergroupconnect.md) with the new handle.

> [!Note]  
> If the connection to a peer group fails, the PEER\_GROUP\_EVENT\_CONNECTION\_FAILED event occurs. The handler can attempt to reestablish the connection to the peer group.

 

## Registering for Peer Grouping Events

Before a peer participates in a peer group, the peer must register for peer group events. To register for specific peer events, call [**PeerGroupRegisterEvent**](peergroupregisterevent.md), and pass in one or more of the peer event types defined in PEER\_GROUP\_EVENT\_TYPE. You must register for each peer event that applies to your application; for example, to receive data over a direct connection, register for the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION and PEER\_GROUP\_EVENT\_INCOMING\_DATA events. Each call takes an event handle and returns an **HPEEREVENT** handle for that peer event.

Event handlers can obtain the data associated with a peer event by passing the handle to registered peer events to [**PeerGroupGetEventData**](peergroupgeteventdata.md). This peer event data is returned as a PEER\_GROUP\_EVENT\_DATA union. If the peer event queue is empty, this function returns PEER\_S\_NO\_EVENT\_DATA.

You can unregister for peer events by calling [**PeerGroupUnregisterEvent**](peergroupunregisterevent.md) and providing the handle for the peer event you want to unregister. After the function is called, the peer events associated with the handle are no longer registered.

## Creating Administrator and Member Roles

The peer who creates the peer group is known as the peer group creator, and has the administrator role by default. Only the peer group creator can set the group properties.

Peers invited to the peer group can be either an administrator or a member. If they are assigned an administrator role by the administrator issuing the invitation, they can invite new members to the peer group, and likewise assign the administrator role to other members.

The roles of peer group members are set in the invitations the administrator gives to a member. To add more administrators, set the value of the *pRoles* parameter of [**PeerGroupCreateInvitation**](peergroupcreateinvitation.md) to PEER\_GROUP\_ROLE\_ADMIN when creating an invitation.

Members can participate in a peer group, but cannot invite and authorize new members, set group properties, or update or delete group records that they do not specifically create. To assign member status to a participating peer, set the value of the **pRoles** parameter of [**PeerGroupCreateInvitation**](peergroupcreateinvitation.md) to PEER\_GROUP\_ROLE\_MEMBER when you create an invitation for that peer.

To change the role of a member, new credentials containing the new role must be issued to that member. To accomplish this, obtain the [**PEER\_CREDENTIAL\_INFO**](peer-credential-info.md) structure for this member from the PEER\_MEMBER structure returned by [**PeerGroupEnumMembers**](peergroupenummembers.md). Change the **pRoles** field in **PEER\_CREDENTIAL\_INFO** to the new role, and pass the structure to [**PeerGroupIssueCredentials**](peergroupissuecredentials.md).

The new credentials will not go into effect for the peer until they connect to the peer group. If they are currently connected, they must close the group and reconnect to obtain the updated credentials.

## Finding a Peer

To obtain an enumerated list of all peers participating in the peer group, call [**PeerGroupEnumMembers**](peergroupenummembers.md) with the group handle, which returns a handle to the enumeration. To obtain the members, call [**PeerGetNextItem**](peergetnextitem.md) with the enum handle and the number of members to retrieve. Continue calling **PeerGetNextItem** until the *pCount* parameter returns a value less than the number of members requested. Note that the complete list of available members may not be returned.

Each member is represented as a [**PEER\_MEMBER**](peer-member.md) structure, which contains the identity of the peer, node IDs, and IP addresses for active peers.

When finished, close the enumeration and release the associated memory by calling [**PeerEndEnumeration**](peerendenumeration.md).

## Connecting Directly to a Peer

When a peer is connected to a peer group, direct one-to-one exchanges with other connected members are initiated by calling [**PeerGroupOpenDirectConnection**](peergroupopendirectconnection.md) and supplying the identity of the other peer. This call is asynchronous, and returns a 64-bit connection ID. If the call is successful, you receive the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION\_EVENT peer event to indicate that the connection is successful. If the connection is successful, the connection ID is valid and can be used to send and receive data through the direct connection.

To be able to receive direct connections, the other peer must also have previously registered for the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION peer event.

To send data to a peer, call [**PeerGroupSendData**](peergroupsenddata.md) with a valid connection ID. To receive data, the other peer must be registered for the PEER\_GROUP\_EVENT\_INCOMING\_DATA peer event. Likewise, if the sending peer wants to receive data in turn, it also must be registered for the PEER\_GROUP\_EVENT\_INCOMING\_DATA peer event.

To receive the total set of currently active direct connections with other peers in a group, call [**PeerGroupEnumConnections**](peergroupenumconnections.md) to open the enumeration and iterate through the list of connections by using [**PeerGetNextItem**](peergetnextitem.md).

To close a direct connection, call [**PeerGroupCloseDirectConnection**](peergroupclosedirectconnection.md) and pass in the connection ID.

## Closing and Shutting Down a Peer Group

To close a connection to a peer group, call [**PeerGroupClose**](peergroupclose.md), which invalidates the group handle, but does not shut down the Peer Grouping Infrastructure. Peer-to-peer group data is deleted by calling [**PeerGroupDelete**](peergroupdelete.md).

When the application is finished using the Peer Grouping Infrastructure, it must call [**PeerGroupShutdown**](peergroupshutdown.md).

 

 



