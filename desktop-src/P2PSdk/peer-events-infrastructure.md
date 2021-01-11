---
description: The Peer Infrastructure uses events to notify applications of changes that have occurred within a peer network, for example, a node that is added or removed from a graph.
ms.assetid: a056da1c-b8f9-4dad-8df9-df24c6b359b7
title: Peer Events Infrastructure
ms.topic: article
ms.date: 05/31/2018
---

# Peer Events Infrastructure

The Peer Infrastructure uses events to notify applications of changes that have occurred within a peer network, for example, a node that is added or removed from a graph. The Peer Graphing and Peer Grouping Infrastructures use the peer events infrastructure.

## Receiving Peer Event Notification

A peer can register to receive notification when an attribute of a graph or group changes, or a specific peer event occurs. A peer application calls the [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent) or [**PeerGroupRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupregisterevent) function, and passes an event handle to the Peer Infrastructure, which is created previously by a call to [**CreateEvent**](graphing-reference-links.md). The Peer Infrastructure uses the handle to signal an application that a peer event has occurred.

The application also passes a series of [**PEER\_GRAPH\_EVENT\_REGISTRATION**](/windows/desktop/api/P2P/ns-p2p-peer_graph_event_registration) or [**PEER\_GROUP\_EVENT\_REGISTRATION**](/windows/desktop/api/P2P/ns-p2p-peer_group_event_registration) structures that indicate to the Peer Infrastructure the specific peer events for which the application is requesting notification. The application must also specify exactly how many structures are being passed.

## Peer Graphing Events

A Peer Graphing application can register to receive notification for 9 peer graph events. Each event name is prefaced with **PEER\_GRAPH\_EVENT\_**, for example, **PEER\_GRAPH\_STATUS\_CHANGED**. Unless otherwise noted, information about a change is retrieved by using [**PeerGraphGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergraphgeteventdata).

-   **PEER\_GRAPH\_EVENT\_STATUS\_CHANGED** indicates that the status of a graph is changed, for example, a node has synchronized with a graph.
-   **PEER\_GRAPH\_EVENT\_PROPERTY\_CHANGED** indicates that a property of a graph or group is changed, for example, the friendly name of a graph has changed.
    > [!Note]  
    > The application must call [**PeerGraphGetProperties**](/windows/desktop/api/P2P/nf-p2p-peergraphgetproperties) to obtain the changed information.

     

-   **PEER\_GRAPH\_EVENT\_RECORD\_CHANGED** indicates that a record is changed, for example, a record is deleted.
-   **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** indicates that a direct connection is changed, for example, a node has connected.
-   **PEER\_GRAPH\_EVENT\_NEIGHBOR\_CONNECTION** indicates that a connection to a neighbor node is changed, for example, a node has connected.
-   **PEER\_GRAPH\_EVENT\_INCOMING\_DATA** indicates that data has been received from a direct or neighbor connection.
-   **PEER\_GRAPH\_EVENT\_CONNECTION\_REQUIRED** indicates that the Graphing Infrastructure requires a new connection.
    > [!Note]  
    > A call to [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect) connects to a new node. A call to [**PeerGraphGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergraphgeteventdata) does not return data.

     

-   **PEER\_GRAPH\_EVENT\_NODE\_CHANGED** indicates that node presence information is changed, for example, an IP address has changed.
-   **PEER\_GRAPH\_EVENT\_SYNCHRONIZED** indicates that a specific record type is synchronized.

After an application receives notification that a peer event has occurred, the application calls [**PeerGraphGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergraphgeteventdata), and passes the peer event handle returned by [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent). The Peer Infrastructure returns a pointer to a [**PEER\_GRAPH\_EVENT\_DATA**](/windows/desktop/api/P2P/ns-p2p-peer_graph_event_data) structure that contains the requested data. This function should be called until **PEER\_S\_NO\_EVENT\_DATA** is returned.

After an application does not require a peer event notification, the application calls either [**PeerGraphUnregisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphunregisterevent), and passes the peer event handle returned by [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent) when the application registered.

## Handling Graph Connection Referrals

When [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect) is called, the connecting peer is notified of success or failure through the asynchronous **PEER\_GRAPH\_EVENT\_NEIGHBOR\_CONNECTION** event. If the connection failed due to a specific networking issues (such as a misconfigured firewall), the **PEER\_GRAPH\_EVENT\_NEIGHBOR\_CONNECTION** event is raised, with the connection status set to **PEER\_CONNECTION\_FAILED**.

However, when a peer receives a referral when it attempts to connect to a busy node, the **PEER\_GRAPH\_EVENT\_NEIGHBOR\_CONNECTION** is raised on the connecting peer, with the connection status set to **PEER\_CONNECTION\_FAILED**. The connecting peer may be referred to another node which itself is busy and may send a referral, and the same event and status are raised on the connecting peer. This chain of referrals that result in **PEER\_CONNECTION\_FAILED** event statuses can continue until the maximum number of connection attempts has been exhausted. The peer does not have a mechanism to determine the difference between a full connection attempt and the connection referral.

To address this issue, developers should consider using the peer graph status change events to determine if the connection attempt suceeded. If the event is not received within a specific amount of time, the application can assume that the connecting peer is being referred and that the peer application should consider the connection attempt a failure.

## Peer Grouping Events

A Peer Grouping application can register to receive notification for 8 peer events. Each event name is prefaced with **PEER\_GROUP\_EVENT\_**; for example, **PEER\_GROUP\_EVENT\_STATUS\_CHANGED**. Unless otherwise noted, information about a change is retrieved by using [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata).

-   **PEER\_GROUP\_EVENT\_STATUS\_CHANGED** indicates that the group status has changed. There are two status values possible: **PEER\_GROUP\_STATUS\_LISTENING**, which indicates that the group has no connections and is waiting for new members; and **PEER\_GROUP\_STATUS\_HAS CONNECTIONS**, which indicates that the group has at least one connection. This status value can be obtained by calling [**PeerGroupGetStatus**](/windows/desktop/api/P2P/nf-p2p-peergroupgetstatus) after this event is raised.
-   **PEER\_GROUP\_EVENT\_PROPERTY\_CHANGED** indicates that the group properties have been changed or updated by the group creator.
-   **PEER\_GROUP\_EVENT\_RECORD\_CHANGED** indicates that a record operation has been performed. This event is raised when a peer participating in the group publishes, updates, or deletes a record. For example, this event is raised when a chat application sends a chat message.
-   **PEER\_GROUP\_EVENT\_MEMBER\_CHANGED** indicates that a member's status within the group has changed. Status changes include:
    -   **PEER\_MEMBER\_CONNECTED**. A peer has connected to the group.
    -   **PEER\_MEMBER\_DISCONNECTED**. A peer has disconnected from the group.
    -   **PEER\_MEMBER\_JOINED**. New membership information has been published for a peer.
    -   **PEER\_MEMBER\_UPDATED**. A peer has updated with new information, such as a new IP address.
-   **PEER\_GROUP\_EVENT\_NEIGHBOR\_CONNECTION**. Peers who will participate in neighbor connections within the group must register for this event. Note that registering for this event does not enable the peer to receive data; registration for this event only ensures notification when a request for a neighbor connection is received.
-   **PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION**. Peers who will participate in direct connections within the group must register for this event. Note that registering for this event does not enable the peer to receive data; registration for this event only ensures notification when a request for a direct connection is received.
-   **PEER\_GROUP\_EVENT\_INCOMING\_DATA**. Peers who will receive data over a neighbor or direct connection must register for this event. When this event is raised, the opaque data transmitted by the other participating peer can be obtained by calling [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata). Note that to receive this event, the peer must have previously registered for **PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION** or **PEER\_GROUP\_EVENT\_NEIGHBOR\_CONNECTION**.
-   **PEER\_GROUP\_EVENT\_CONNECTION\_FAILED**. A connection failed for some reason. No data is provided when this event is raised, and [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata) should not be called.

After an application receives notification that a peer event has occurred (excluding **PEER\_GROUP\_EVENT\_CONNECTION\_FAILED**), the application calls [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata), and passes the peer event handle returned by [**PeerGroupRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupregisterevent). The Peer Infrastructure returns a pointer to a [**PEER\_GROUP\_EVENT\_DATA**](/windows/win32/api/p2p/ns-p2p-peer_group_event_data-r1) structure that contains the requested data. This function must be called until **PEER\_S\_NO\_EVENT\_DATA** is returned. When an application no longer requires notification for a peer event, a call must be made to [**PeerGroupUnregisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergroupunregisterevent), passing the peer event handle returned by **PeerGroupRegisterEvent** when the application registered for the particular event.

## Example of Registering for Peer Graphing Events

The following code sample shows you how to register with the Peer Graphing events.


```C++
//-----------------------------------------------------------------------------
// Function: RegisterForEvents
//
// Purpose:  Registers the EventCallback function so it can be called for only
//           the events that are specified.
//
// Returns:  HRESULT
//
HRESULT RegisterForEvents()
{
    HPEEREVENT  g_hPeerEvent = NULL;        // The one PeerEvent handle
    HANDLE      g_hEvent = NULL;            // Handle signaled by Graphing when we have an event
    HRESULT hr = S_OK;
    PEER_GRAPH_EVENT_REGISTRATION regs[] = {
        { PEER_GRAPH_EVENT_RECORD_CHANGED, 0 },
        { PEER_GRAPH_EVENT_NODE_CHANGED,   0 },
        { PEER_GRAPH_EVENT_STATUS_CHANGED, 0 },
        { PEER_GRAPH_EVENT_DIRECT_CONNECTION, 0 },
        { PEER_GRAPH_EVENT_INCOMING_DATA, 0 },
    };

    g_hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
    if (g_hEvent == NULL)
    {
        wprintf(L"CreateEvent call failed.\n");
        hr = E_OUTOFMEMORY;
    }
    else
    {
        hr = PeerGraphRegisterEvent(g_hGraph, g_hEvent, celems(regs), regs,  &g_hPeerEvent);
        if (FAILED(hr))
        {
           wprintf(L"PeerGraphRegisterEvent call failed.\n");
            CloseHandle(g_hEvent);
            g_hEvent = NULL;
        }
    }

    if (SUCCEEDED(hr))
    {
        if (!RegisterWaitForSingleObject(&g_hWait, g_hEvent, EventCallback, NULL, INFINITE, WT_EXECUTEDEFAULT))
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
            wprintf(L"Could not set up event callback.\n");
            CloseHandle(g_hEvent);
            g_hEvent = NULL;
        }
    }

    return hr;
}
```



 

 



