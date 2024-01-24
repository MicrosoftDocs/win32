---
description: The Peer Graphing and Peer Grouping Infrastructures allow applications to connect directly to one node (Graphing) or member (Grouping), and then exchange data directly with the node. This connection is called a direct connection.
ms.assetid: 65f3d3a5-c015-4724-b9ed-45af7fde7a45
title: Direct Connections
ms.topic: article
ms.date: 05/31/2018
---

# Direct Connections

The Peer Graphing and Peer Grouping Infrastructures allow applications to connect directly to one node (Graphing) or member (Grouping), and then exchange data directly with the node. This connection is called a **direct connection**.

## Direct Connections using the Peer Graphing Infrastructure

Before a direct connection can be established between two nodes in a graph, both nodes must be registered for the **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** event. To receive data over a direct connection, the nodes must also be registered for the **PEER\_GRAPH\_EVENT\_INCOMING\_DATA** event.

**PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** is an event that notifies an application whether or not a direct connection attempt succeeds or fails. The actual success or failure status of a call to [**PeerGraphOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergraphopendirectconnection) is returned in the [**PEER\_GRAPH\_EVENT\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_graph_event_data) structure.

To create a direct connection, an application calls [**PeerGraphOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergraphopendirectconnection), and then passes a handle to the graph, a pointer to the identity of the other node that is participating in the connection, and a pointer to an IPv6 address structure for the participating node. The node identity and IPv6 address that are specified in the call to **PeerGraphOpenDirectConnection** must be registered for the **PEER\_GRAPH\_EVENT\_INCOMING\_DATA** event, or it cannot receive data sent by a calling peer. When successful, **PeerGraphOpenDirectConnection** returns a 64-bit connection ID. However, the peer must wait for the **PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION** event before the direct connection ID can be identified as valid.

After a connection is made and a valid connection ID is confirmed, an application can call [**PeerGraphSendData**](/windows/desktop/api/P2P/nf-p2p-peergraphsenddata) to send the data across the connection specified by the valid connection ID to the participating peer—if the participating peer is registered for the **PEER\_GRAPH\_EVENT\_INCOMING\_DATA** event. The opaque data is available as a [**PEER\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_data) structure in the [**PEER\_EVENT\_INCOMING\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_event_incoming_data) returned by the **PEER\_GRAPH\_EVENT\_INCOMING\_DATA** event.

When a connection is not needed, an application calls [**PeerGraphCloseDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergraphclosedirectconnection) with the graph handle and the connection ID.

## Direct Connections using the Peer Grouping Infrastructure

Direct connections within the Peer Grouping Infrastructure are handled similar to the Peer Graphing Infrastructure.

Before a direct connection can be established between two members in a group, both members must register for the **PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION** event. If a group member wants to receive data over a direct connection, the group member must also register for the **PEER\_GROUP\_EVENT\_INCOMING\_DATA** event.

**PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION** is an event that is an event that notifies an application whether or not a direct connection attempt succeeds or fails. The actual success or failure status of a call to [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection) is returned in the [**PEER_GROUP_EVENT_DATA**](/windows/win32/api/p2p/ns-p2p-peer_group_event_data-r1) structure.

To create a direct connection, an application calls [**PeerGroupOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupopendirectconnection), and then passes a handle to the group, a pointer to the identity of the other member that will participate in this connection, and a pointer to an IPv6 address structure for the participating member. The member whose identity and IPv6 address are specified in the call to **PeerGroupOpenDirectConnection** must be registered for the **PEER\_GROUP\_EVENT\_INCOMING\_DATA** event, or the member cannot receive data sent by a calling peer. **PeerGroupOpenDirectConnection** returns a 64-bit connection ID when successful. However, a peer must wait for the **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** event to be raised before the direct connection ID can be identified as valid.

After a connection is made and a valid connection ID is confirmed, then an application can call [**PeerGroupSendData**](/windows/desktop/api/P2P/nf-p2p-peergroupsenddata) to send data across a connection specified by the valid connection ID to the participating peer—if the participating peer is registered for the **PEER\_GROUP\_EVENT\_INCOMING\_DATA** event. The opaque data is available as a [**PEER\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_data) structure in the [**PEER\_EVENT\_INCOMING\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_event_incoming_data) returned by the **PEER\_GROUP\_EVENT\_INCOMING\_DATA** event.

When the connection is not needed, the application calls [**PeerGroupCloseDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergroupclosedirectconnection) with the group handle and the connection ID.

## Example of a Direct Connection for Graphing


```C++
#include <p2p.h>

#pragma comment(lib, "p2pgraph.lib")

//-----------------------------------------------------------------------------
// Function: CreateDirectConnection
//
// Purpose:  Demonstrate how to create a direct connection.
//
// Arguments:
//           hGraph - the graph in which to create the connection
//           pwzId  - the peer identification string
//
// Returns:  ULONGLONG - the connection id or 0
//

ULONGLONG CreateDirectConnection(HGRAPH hGraph, PCWSTR pwzId)
{
    HRESULT   hr = S_OK;

    ULONGLONG ullConnection = 0; // the connection id to return

    HPEERENUM hPeerEnum = NULL;
 
    hr = PeerGraphEnumNodes(hGraph, pwzId, &hPeerEnum);

    if (SUCCEEDED(hr))
    {
        ULONG cItem = 1; // want only one matching result

        PEER_NODE_INFO ** ppNodeInfo = NULL;

        hr = PeerGraphGetNextItem(hPeerEnum, &cItem, (PVOID**) &ppNodeInfo);

        if (SUCCEEDED(hr))
        {
            if ((cItem > 0) && (NULL != ppNodeInfo))
            {
                if ((*ppNodeInfo)->cAddresses > 0)
                {
                    hr = PeerGraphOpenDirectConnection(hGraph, pwzId,
                            &(*ppNodeInfo)->pAddresses[0], &ullConnection);
                }
                PeerGraphFreeData(ppNodeInfo);
            }
        }
        PeerGraphEndEnumeration(hPeerEnum);
    }
    return ullConnection;
}

```



 

 



