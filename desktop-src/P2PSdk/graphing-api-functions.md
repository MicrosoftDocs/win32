---
Description: 'The Peer Graphing API uses the following functions:'
ms.assetid: 'cd05d4da-ca65-471b-bb97-82885f22e6f9'
title: Graphing API Functions
---

# Graphing API Functions

The Peer Graphing API uses the following functions:

## Initialization and Cleanup Functions



| Function                                       | Description                                                                                                        |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphShutdown**](peergraphshutdown.md) | Cleans up any resources allocated by the call to [**PeerGraphStartup**](peergraphstartup.md).                     |
| [**PeerGraphStartup**](peergraphstartup.md)   | Indicates to the Peer Graphing Infrastructure what version of the Peer protocols the calling application requires. |



 

## Graph Creation and Access Functions



| Function                                   | Description                                                                                                                                                                                                           |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphClose**](peergraphclose.md)   | Invalidates the peer graph handle returned by a call to either [**PeerGraphCreate**](peergraphcreate.md) or [**PeerGraphOpen**](peergraphopen.md), and closes all network connections for the specified peer graph. |
| [**PeerGraphCreate**](peergraphcreate.md) | Creates a new peer graph.                                                                                                                                                                                             |
| [**PeerGraphDelete**](peergraphdelete.md) | Deletes the data associated with a specified peer graph.                                                                                                                                                              |
| [**PeerGraphListen**](peergraphlisten.md) | Indicates that a peer graph should start listening for incoming connections.                                                                                                                                          |
| [**PeerGraphOpen**](peergraphopen.md)     | Opens a peer graph that is created previously by either the local node or a remote node.                                                                                                                              |



 

## Graph and Node Information Functions



| Function                                                         | Description                                                                                                                                                        |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEnumNodes**](peergraphenumnodes.md)                 | Creates and returns an enumeration handle used to enumerate the nodes in a peer graph.                                                                             |
| [**PeerGraphGetNodeInfo**](peergraphgetnodeinfo.md)             | Retrieves information about a specific node.                                                                                                                       |
| [**PeerGraphGetProperties**](peergraphgetproperties.md)         | Retrieves the current peer graph properties.                                                                                                                       |
| [**PeerGraphGetStatus**](peergraphgetstatus.md)                 | Returns the current status of the peer graph.                                                                                                                      |
| [**PeerGraphSetNodeAttributes**](peergraphsetnodeattributes.md) | Sets the attributes of the [**PEER\_NODE\_INFO**](peer-node-info.md) structure for the local node.                                                                |
| [**PeerGraphSetPresence**](peergraphsetpresence.md)             | Explicitly turns on or off the publication of presence records for a specific node. This function can override the presence settings in the peer graph properties. |
| [**PeerGraphSetProperties**](peergraphsetproperties.md)         | Sets the peer graph properties.                                                                                                                                    |



 

## Record Management Functions



| Function                                                                     | Description                                                                                                                         |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphAddRecord**](peergraphaddrecord.md)                             | Adds a new record to a peer graph. A record added with this function is sent to each node in a peer graph.                          |
| [**PeerGraphDeleteRecord**](peergraphdeleterecord.md)                       | Marks a record as deleted within a peer graph.                                                                                      |
| [**PeerGraphEnumRecords**](peergraphenumrecords.md)                         | Creates and returns an enumeration handle used to enumerate records of a specific type of record, user, or both.                    |
| [**PeerGraphGetRecord**](peergraphgetrecord.md)                             | Retrieves a specific record based on the specified record ID.                                                                       |
| [**PeerGraphSearchRecords**](peergraphsearchrecords.md)                     | Searches the peer graph for specific records.                                                                                       |
| [**PeerGraphUpdateRecord**](peergraphupdaterecord.md)                       | Updates a record in the peer graph and then floods the record to each node in the peer graph.                                       |
| [**PeerGraphValidateDeferredRecords**](peergraphvalidatedeferredrecords.md) | Indicates to the Peer Graphing Infrastructure that it is time to resubmit any deferred records for the security module to validate. |



 

## Export and Import Functions



| Function                                                   | Description                                                                          |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**PeerGraphExportDatabase**](peergraphexportdatabase.md) | Exports a peer graph database into a file that you can move to a different computer. |
| [**PeerGraphImportDatabase**](peergraphimportdatabase.md) | Imports a file that contains the information from a peer graph database.             |



 

## Utility and Support Functions



| Function                                                                     | Description                                                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphEndEnumeration**](peergraphendenumeration.md)                   | Releases an enumeration handle, and frees the resources associated with an enumeration.                                           |
| [**PeerGraphFreeData**](peergraphfreedata.md)                               | Frees resources that several of the Peer Graphing API functions return.                                                           |
| [**PeerGraphGetItemCount**](peergraphgetitemcount.md)                       | Retrieves the number of items in an enumeration.                                                                                  |
| [**PeerGraphGetNextItem**](peergraphgetnextitem.md)                         | Obtains the next item or items in an enumeration created by a call to specific functions, which return a peer enumeration.        |
| [**PeerGraphPeerTimeToUniversalTime**](peergraphpeertimetouniversaltime.md) | Converts the peer graph-maintained reference time value to a localized time value appropriate for display on the peer's computer. |
| [**PeerGraphUniversalTimeToPeerTime**](peergraphuniversaltimetopeertime.md) | Converts a universal time value from the peer's computer to a common peer graph time value.                                       |



 

## Connection Functions



| Function                                                                 | Description                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGraphCloseDirectConnection**](peergraphclosedirectconnection.md) | Closes a specified direct connection.                                                                                                                                                                                                          |
| [**PeerGraphConnect**](peergraphconnect.md)                             | Attempts to make a connection to a specified node in a peer graph. This function starts an asynchronous operation.                                                                                                                             |
| [**PeerGraphEnumConnections**](peergraphenumconnections.md)             | Creates and returns an enumeration handle used to enumerate the connections of a local node.                                                                                                                                                   |
| [**PeerGraphOpenDirectConnection**](peergraphopendirectconnection.md)   | Allows an application to establish a direct connection with a node in a peer graph. The connection can only be made if the node to which the application is connecting has subscribed to the **PEER\_GRAPH\_EVENT\_DIRECT\_CONNECTION** event. |
| [**PeerGraphSendData**](peergraphsenddata.md)                           | Sends data to a neighbor node or a directly connected node.                                                                                                                                                                                    |



 

## Events Infrastructure Functions



| Function                                                     | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**PeerGraphGetEventData**](peergraphgeteventdata.md)       | Retrieves peer events.                                                                                       |
| [**PeerGraphRegisterEvent**](peergraphregisterevent.md)     | Registers a peer's request to be notified of changes associated with a peer graph and event type.            |
| [**PeerGraphUnregisterEvent**](peergraphunregisterevent.md) | Requests that the application no longer be notified of changes associated with a peer graph and record type. |



 

 

 



