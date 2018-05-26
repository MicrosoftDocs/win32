---
Description: The Peer Graphing API uses the following functions
ms.assetid: cd05d4da-ca65-471b-bb97-82885f22e6f9
title: Graphing API Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Graphing API Functions

The Peer Graphing API uses the following functions:

## Initialization and Cleanup Functions



| Function                                       | Description                                                                                                        |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphShutdown**](/windows/win32/P2P/nf-p2p-peergraphshutdown?branch=master) | Cleans up any resources allocated by the call to [**PeerGraphStartup**](/windows/win32/P2P/nf-p2p-peergraphstartup?branch=master).                     |
| [**PeerGraphStartup**](/windows/win32/P2P/nf-p2p-peergraphstartup?branch=master)   | Indicates to the Peer Graphing Infrastructure what version of the Peer protocols the calling application requires. |



 

## Graph Creation and Access Functions



| Function                                   | Description                                                                                                                                                                                                           |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphClose**](/windows/win32/P2P/nf-p2p-peergraphclose?branch=master)   | Invalidates the peer graph handle returned by a call to either [**PeerGraphCreate**](/windows/win32/P2P/nf-p2p-peergraphcreate?branch=master) or [**PeerGraphOpen**](/windows/win32/P2P/nf-p2p-peergraphopen?branch=master), and closes all network connections for the specified peer graph. |
| [**PeerGraphCreate**](/windows/win32/P2P/nf-p2p-peergraphcreate?branch=master) | Creates a new peer graph.                                                                                                                                                                                             |
| [**PeerGraphDelete**](/windows/win32/P2P/nf-p2p-peergraphdelete?branch=master) | Deletes the data associated with a specified peer graph.                                                                                                                                                              |
| [**PeerGraphListen**](/windows/win32/P2P/nf-p2p-peergraphlisten?branch=master) | Indicates that a peer graph should start listening for incoming connections.                                                                                                                                          |
| [**PeerGraphOpen**](/windows/win32/P2P/nf-p2p-peergraphopen?branch=master)     | Opens a peer graph that is created previously by either the local node or a remote node.                                                                                                                              |



 

## Graph and Node Information Functions



| Function                                                         | Description                                                                                                                                                        |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEnumNodes**](/windows/win32/P2P/nf-p2p-peergraphenumnodes?branch=master)                 | Creates and returns an enumeration handle used to enumerate the nodes in a peer graph.                                                                             |
| [**PeerGraphGetNodeInfo**](/windows/win32/P2P/nf-p2p-peergraphgetnodeinfo?branch=master)             | Retrieves information about a specific node.                                                                                                                       |
| [**PeerGraphGetProperties**](/windows/win32/P2P/nf-p2p-peergraphgetproperties?branch=master)         | Retrieves the current peer graph properties.                                                                                                                       |
| [**PeerGraphGetStatus**](/windows/win32/P2P/nf-p2p-peergraphgetstatus?branch=master)                 | Returns the current status of the peer graph.                                                                                                                      |
| [**PeerGraphSetNodeAttributes**](/windows/win32/P2P/nf-p2p-peergraphsetnodeattributes?branch=master) | Sets the attributes of the [**PEER\_NODE\_INFO**](/windows/win32/P2P/ns-p2p-peer_node_info_tag?branch=master) structure for the local node.                                                                |
| [**PeerGraphSetPresence**](/windows/win32/P2P/nf-p2p-peergraphsetpresence?branch=master)             | Explicitly turns on or off the publication of presence records for a specific node. This function can override the presence settings in the peer graph properties. |
| [**PeerGraphSetProperties**](/windows/win32/P2P/nf-p2p-peergraphsetproperties?branch=master)         | Sets the peer graph properties.                                                                                                                                    |



 

## Record Management Functions



| Function                                                                     | Description                                                                                                                         |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphAddRecord**](/windows/win32/P2P/nf-p2p-peergraphaddrecord?branch=master)                             | Adds a new record to a peer graph. A record added with this function is sent to each node in a peer graph.                          |
| [**PeerGraphDeleteRecord**](/windows/win32/P2P/nf-p2p-peergraphdeleterecord?branch=master)                       | Marks a record as deleted within a peer graph.                                                                                      |
| [**PeerGraphEnumRecords**](/windows/win32/P2P/nf-p2p-peergraphenumrecords?branch=master)                         | Creates and returns an enumeration handle used to enumerate records of a specific type of record, user, or both.                    |
| [**PeerGraphGetRecord**](/windows/win32/P2P/nf-p2p-peergraphgetrecord?branch=master)                             | Retrieves a specific record based on the specified record ID.                                                                       |
| [**PeerGraphSearchRecords**](/windows/win32/P2P/nf-p2p-peergraphsearchrecords?branch=master)                     | Searches the peer graph for specific records.                                                                                       |
| [**PeerGraphUpdateRecord**](/windows/win32/P2P/nf-p2p-peergraphupdaterecord?branch=master)                       | Updates a record in the peer graph and then floods the record to each node in the peer graph.                                       |
| [**PeerGraphValidateDeferredRecords**](/windows/win32/P2P/nf-p2p-peergraphvalidatedeferredrecords?branch=master) | Indicates to the Peer Graphing Infrastructure that it is time to resubmit any deferred records for the security module to validate. |



 

## Export and Import Functions



| Function                                                   | Description                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**PeerGraphExportDatabase**](/windows/win32/P2P/nf-p2p-peergraphexportdatabase?branch=master) | Exports a peer graph database into a file that you can move to a different computer. |
| [**PeerGraphImportDatabase**](/windows/win32/P2P/nf-p2p-peergraphimportdatabase?branch=master) | Imports a file that contains the information from a peer graph database.             |



 

## Utility and Support Functions



| Function                                                                     | Description                                                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEndEnumeration**](/windows/win32/P2P/nf-p2p-peergraphendenumeration?branch=master)                   | Releases an enumeration handle, and frees the resources associated with an enumeration.                                           |
| [**PeerGraphFreeData**](/windows/win32/P2P/nf-p2p-peergraphfreedata?branch=master)                               | Frees resources that several of the Peer Graphing API functions return.                                                           |
| [**PeerGraphGetItemCount**](/windows/win32/P2P/nf-p2p-peergraphgetitemcount?branch=master)                       | Retrieves the number of items in an enumeration.                                                                                  |
| [**PeerGraphGetNextItem**](/windows/win32/P2P/nf-p2p-peergraphgetnextitem?branch=master)                         | Obtains the next item or items in an enumeration created by a call to specific functions, which return a peer enumeration.        |
| [**PeerGraphPeerTimeToUniversalTime**](/windows/win32/P2P/nf-p2p-peergraphpeertimetouniversaltime?branch=master) | Converts the peer graph-maintained reference time value to a localized time value appropriate for display on the peer's computer. |
| [**PeerGraphUniversalTimeToPeerTime**](/windows/win32/P2P/nf-p2p-peergraphuniversaltimetopeertime?branch=master) | Converts a universal time value from the peer's computer to a common peer graph time value.                                       |



 

## Connection Functions



| Function                                                                 | Description                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphCloseDirectConnection**](/windows/win32/P2P/nf-p2p-peergraphclosedirectconnection?branch=master) | Closes a specified direct connection.                                                                                                                                                                                                          |
| [**PeerGraphConnect**](/windows/win32/P2P/nf-p2p-peergraphconnect?branch=master)                             | Attempts to make a connection to a specified node in a peer graph. This function starts an asynchronous operation.                                                                                                                             |
| [**PeerGraphEnumConnections**](/windows/win32/P2P/nf-p2p-peergraphenumconnections?branch=master)             | Creates and returns an enumeration handle used to enumerate the connections of a local node.                                                                                                                                                   |
| [**PeerGraphOpenDirectConnection**](/windows/win32/P2P/nf-p2p-peergraphopendirectconnection?branch=master)   | Allows an application to establish a direct connection with a node in a peer graph. The connection can only be made if the node to which the application is connecting has subscribed to the **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** event. |
| [**PeerGraphSendData**](/windows/win32/P2P/nf-p2p-peergraphsenddata?branch=master)                           | Sends data to a neighbor node or a directly connected node.                                                                                                                                                                                    |



 

## Events Infrastructure Functions



| Function                                                     | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**PeerGraphGetEventData**](/windows/win32/P2P/nf-p2p-peergraphgeteventdata?branch=master)       | Retrieves peer events.                                                                                       |
| [**PeerGraphRegisterEvent**](/windows/win32/P2P/nf-p2p-peergraphregisterevent?branch=master)     | Registers a peer's request to be notified of changes associated with a peer graph and event type.            |
| [**PeerGraphUnregisterEvent**](/windows/win32/P2P/nf-p2p-peergraphunregisterevent?branch=master) | Requests that the application no longer be notified of changes associated with a peer graph and record type. |



 

 

 



