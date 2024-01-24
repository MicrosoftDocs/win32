---
description: This topic discusses how an application connects to a peer group using the Peer Grouping APIs.
ms.assetid: 56fa28d8-3b3a-4cd5-8448-c8c4ce8d0b2c
title: How to Connect to a Peer Group
ms.topic: article
ms.date: 05/31/2018
---

# How to Connect to a Peer Group

This topic discusses how an application connects to a peer group using the Peer Grouping APIs.

## Joining a Peer Group

To join a peer group, call [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin), passing in the identity name of the peer and the invitation (and an optional PNRP cloud name, if the cloud name in the invitation is ambiguous).

If successful, [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin) returns a handle to the peer group.

If the peer has previously joined the peer group and then closed the handle, the peer group should be reopened by calling [**PeerGroupOpen**](/windows/desktop/api/P2P/nf-p2p-peergroupopen) and passing in the name of the peer group. This call returns a new peer group handle.

Once the peer group is successfully joined, the peer may connect directly to the peer group and begin interacting by calling [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect). After connecting, the peer is considered to be "online".

If an application will not interact with the group at the time, it can remain "offline". If it chooses to participate directly in the peer group at a later instance, a subsequent call to [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect) will bring it online. After a peer has joined the peer group, it must connect at least once before it will be able to publish records to the peer group.

## Opening a Peer Group Without Connecting (Offline)

Often, you may wish to have an application connect to a peer group but not directly participate it, receiving and publishing record updates but not sending or receiving data messages. An application is in this "offline" state immediately after [**PeerGroupCreate**](/windows/desktop/api/P2P/nf-p2p-peergroupcreate), [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin), or [**PeerGroupOpen**](/windows/desktop/api/P2P/nf-p2p-peergroupopen) have been called.

An offline application can go online at any time by calling [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect). Once connected, a peer group cannot go offline until all other applications associated with this identity and sharing this group have closed connections to it as well.

A peer group is a shared resource, with the same peer group available to multiple applications. If more than one application for the same identity and Windows user is using the same peer group, they also share the same underlying database and connections (neighbor and direct). If any one of these applications calls [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect), all of the other applications for this identity/user participating in the group also connect to the group. If a record is added by one application while the group is offline, other applications are also be able to see it. As a result, an application must be ready to go online at any time.

## Connecting to a Peer Group (Online)

To begin participating in a group, call [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect) after creating, joining, or opening the group. In this state, direct connections can be opened with other peers participating in the same group by calling [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection).

To detect if a connection attempt has failed, register for the PEER\_GROUP\_EVENT\_CONNECTION\_FAILED event. This event is raised if the grouping infrastructure cannot find another member to connect to, or if the connection fails before the group database is synchronized and another connection cannot be established.

Although multiple applications executing on the peer and participating in the same group with the same peer identity may be offline, a call to [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect) by any one of the applications results in all of the applications becoming online.

Also, if one application on the peer has connected to the group, any other applications that call [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin) or [**PeerGroupOpen**](/windows/desktop/api/P2P/nf-p2p-peergroupopen) are immediately connected as well. If an application calls [**PeerGroupClose**](/windows/desktop/api/P2P/nf-p2p-peergroupclose), the handle is closed for only that application. Thus, a subsequent call to **PeerGroupOpen** by the application returns a new group handle, and the application is brought online immediately if any other applications participating in the same group are still connected.

## Sending and Receiving Data

To send and receive data between specific member nodes in the group, direct connections must be established with those members you intend to interact with. Establishing a direct connection is an asynchronous call to [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection), passing in the handle for a connected group as well as the identity of the peer within the group you wish to connect to. This method will return a connection ID. If the call is successful, a PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION event is raised on the peer, validating the connection ID.

To receive direct connections from other online peers, register for the PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION event with a call to [**PeerGroupRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupregisterevent).

Once a direct connection has been successfully established, the application can begin sending data with calls to [**PeerGroupSendData**](/windows/desktop/api/P2P/nf-p2p-peergroupsenddata), passing the valid connection ID. The ordering of multipart data transmissions is handled by **PeerGroupSendData**. However, applications should implement a proper protocol stack for handling the opaque data returned by this API call.

To receive data over a direct connection, the application must register for the PEER\_GROUP\_EVENT\_INCOMING\_DATA event with [**PeerGroupRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupregisterevent). The event handler is responsible for obtaining and ordering the opaque data, and passing it to the application. This data is obtained within the event handler by calling [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata) with the handle to the registered events.

A direct connection is closed by calling [**PeerGroupCloseDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupclosedirectconnection) and passing in the connection ID obtained by a previous call to [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection) or received in the event data for PEER\_EVENT\_GROUP\_DIRECT\_CONNECTION.

 

 



