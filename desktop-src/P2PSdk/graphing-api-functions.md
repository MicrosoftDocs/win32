---
description: 'The Peer Graphing API uses the following functions:'
ms.assetid: cd05d4da-ca65-471b-bb97-82885f22e6f9
title: Graphing API Functions
ms.topic: article
ms.date: 05/31/2018
---

# Graphing API Functions

The Peer Graphing API uses the following functions:

## Initialization and Cleanup Functions



| Function                                       | Description                                                                                                        |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphShutdown**](/windows/desktop/api/P2P/nf-p2p-peergraphshutdown) | Cleans up any resources allocated by the call to [**PeerGraphStartup**](/windows/desktop/api/P2P/nf-p2p-peergraphstartup).                     |
| [**PeerGraphStartup**](/windows/desktop/api/P2P/nf-p2p-peergraphstartup)   | Indicates to the Peer Graphing Infrastructure what version of the Peer protocols the calling application requires. |



 

## Graph Creation and Access Functions



| Function                                   | Description                                                                                                                                                                                                           |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphClose**](/windows/desktop/api/P2P/nf-p2p-peergraphclose)   | Invalidates the peer graph handle returned by a call to either [**PeerGraphCreate**](/windows/desktop/api/P2P/nf-p2p-peergraphcreate) or [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen), and closes all network connections for the specified peer graph. |
| [**PeerGraphCreate**](/windows/desktop/api/P2P/nf-p2p-peergraphcreate) | Creates a new peer graph.                                                                                                                                                                                             |
| [**PeerGraphDelete**](/windows/desktop/api/P2P/nf-p2p-peergraphdelete) | Deletes the data associated with a specified peer graph.                                                                                                                                                              |
| [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten) | Indicates that a peer graph should start listening for incoming connections.                                                                                                                                          |
| [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen)     | Opens a peer graph that is created previously by either the local node or a remote node.                                                                                                                              |



 

## Graph and Node Information Functions



| Function                                                         | Description                                                                                                                                                        |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEnumNodes**](/windows/desktop/api/P2P/nf-p2p-peergraphenumnodes)                 | Creates and returns an enumeration handle used to enumerate the nodes in a peer graph.                                                                             |
| [**PeerGraphGetNodeInfo**](/windows/desktop/api/P2P/nf-p2p-peergraphgetnodeinfo)             | Retrieves information about a specific node.                                                                                                                       |
| [**PeerGraphGetProperties**](/windows/desktop/api/P2P/nf-p2p-peergraphgetproperties)         | Retrieves the current peer graph properties.                                                                                                                       |
| [**PeerGraphGetStatus**](/windows/desktop/api/P2P/nf-p2p-peergraphgetstatus)                 | Returns the current status of the peer graph.                                                                                                                      |
| [**PeerGraphSetNodeAttributes**](/windows/desktop/api/P2P/nf-p2p-peergraphsetnodeattributes) | Sets the attributes of the [**PEER\_NODE\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_node_info) structure for the local node.                                                                |
| [**PeerGraphSetPresence**](/windows/desktop/api/P2P/nf-p2p-peergraphsetpresence)             | Explicitly turns on or off the publication of presence records for a specific node. This function can override the presence settings in the peer graph properties. |
| [**PeerGraphSetProperties**](/windows/desktop/api/P2P/nf-p2p-peergraphsetproperties)         | Sets the peer graph properties.                                                                                                                                    |



 

## Record Management Functions



| Function                                                                     | Description                                                                                                                         |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphAddRecord**](/windows/desktop/api/P2P/nf-p2p-peergraphaddrecord)                             | Adds a new record to a peer graph. A record added with this function is sent to each node in a peer graph.                          |
| [**PeerGraphDeleteRecord**](/windows/desktop/api/P2P/nf-p2p-peergraphdeleterecord)                       | Marks a record as deleted within a peer graph.                                                                                      |
| [**PeerGraphEnumRecords**](/windows/desktop/api/P2P/nf-p2p-peergraphenumrecords)                         | Creates and returns an enumeration handle used to enumerate records of a specific type of record, user, or both.                    |
| [**PeerGraphGetRecord**](/windows/desktop/api/P2P/nf-p2p-peergraphgetrecord)                             | Retrieves a specific record based on the specified record ID.                                                                       |
| [**PeerGraphSearchRecords**](/windows/desktop/api/P2P/nf-p2p-peergraphsearchrecords)                     | Searches the peer graph for specific records.                                                                                       |
| [**PeerGraphUpdateRecord**](/windows/desktop/api/P2P/nf-p2p-peergraphupdaterecord)                       | Updates a record in the peer graph and then floods the record to each node in the peer graph.                                       |
| [**PeerGraphValidateDeferredRecords**](/windows/desktop/api/P2P/nf-p2p-peergraphvalidatedeferredrecords) | Indicates to the Peer Graphing Infrastructure that it is time to resubmit any deferred records for the security module to validate. |



 

## Export and Import Functions



| Function                                                   | Description                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**PeerGraphExportDatabase**](/windows/desktop/api/P2P/nf-p2p-peergraphexportdatabase) | Exports a peer graph database into a file that you can move to a different computer. |
| [**PeerGraphImportDatabase**](/windows/desktop/api/P2P/nf-p2p-peergraphimportdatabase) | Imports a file that contains the information from a peer graph database.             |



 

## Utility and Support Functions



| Function                                                                     | Description                                                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEndEnumeration**](/windows/desktop/api/P2P/nf-p2p-peergraphendenumeration)                   | Releases an enumeration handle, and frees the resources associated with an enumeration.                                           |
| [**PeerGraphFreeData**](/windows/desktop/api/P2P/nf-p2p-peergraphfreedata)                               | Frees resources that several of the Peer Graphing API functions return.                                                           |
| [**PeerGraphGetItemCount**](/windows/desktop/api/P2P/nf-p2p-peergraphgetitemcount)                       | Retrieves the number of items in an enumeration.                                                                                  |
| [**PeerGraphGetNextItem**](/windows/desktop/api/P2P/nf-p2p-peergraphgetnextitem)                         | Obtains the next item or items in an enumeration created by a call to specific functions, which return a peer enumeration.        |
| [**PeerGraphPeerTimeToUniversalTime**](/windows/desktop/api/P2P/nf-p2p-peergraphpeertimetouniversaltime) | Converts the peer graph-maintained reference time value to a localized time value appropriate for display on the peer's computer. |
| [**PeerGraphUniversalTimeToPeerTime**](/windows/desktop/api/P2P/nf-p2p-peergraphuniversaltimetopeertime) | Converts a universal time value from the peer's computer to a common peer graph time value.                                       |



 

## Connection Functions



| Function                                                                 | Description                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphCloseDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergraphclosedirectconnection) | Closes a specified direct connection.                                                                                                                                                                                                          |
| [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect)                             | Attempts to make a connection to a specified node in a peer graph. This function starts an asynchronous operation.                                                                                                                             |
| [**PeerGraphEnumConnections**](/windows/desktop/api/P2P/nf-p2p-peergraphenumconnections)             | Creates and returns an enumeration handle used to enumerate the connections of a local node.                                                                                                                                                   |
| [**PeerGraphOpenDirectConnection**](/windows/desktop/api/P2P/nf-p2p-peergraphopendirectconnection)   | Allows an application to establish a direct connection with a node in a peer graph. The connection can only be made if the node to which the application is connecting has subscribed to the **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** event. |
| [**PeerGraphSendData**](/windows/desktop/api/P2P/nf-p2p-peergraphsenddata)                           | Sends data to a neighbor node or a directly connected node.                                                                                                                                                                                    |



 

## Events Infrastructure Functions



| Function                                                     | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**PeerGraphGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergraphgeteventdata)       | Retrieves peer events.                                                                                       |
| [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent)     | Registers a peer's request to be notified of changes associated with a peer graph and event type.            |
| [**PeerGraphUnregisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphunregisterevent) | Requests that the application no longer be notified of changes associated with a peer graph and record type. |



 

 

 



