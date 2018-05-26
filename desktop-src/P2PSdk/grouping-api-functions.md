---
Description: The Grouping API uses the following functions
ms.assetid: 56ea2880-b468-4816-b6c9-5780c807b3f1
title: Grouping API Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Grouping API Functions

The Grouping API uses the following functions:

## Group Initialization and Cleanup Functions



| Function                                       | Description                                                                                                            |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupShutdown**](/windows/win32/P2P/nf-p2p-peergroupshutdown?branch=master) | Closes a peer group created with [**PeerGroupStartup**](/windows/win32/P2P/nf-p2p-peergroupstartup?branch=master) and disposes of any allocated resources. |
| [**PeerGroupStartup**](/windows/win32/P2P/nf-p2p-peergroupstartup?branch=master)   | Initiates a peer group by using a requested version of the Peer infrastructure.                                        |



 

## Group Creation and Access Functions



| Function                                                                       | Description                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupClose**](/windows/win32/P2P/nf-p2p-peergroupclose?branch=master)                                       | Invalidates the peer group handle obtained by a previous call to the [**PeerGroupCreate**](/windows/win32/P2P/nf-p2p-peergroupcreate?branch=master), [**PeerGroupJoin**](/windows/win32/P2P/nf-p2p-peergroupjoin?branch=master), or [**PeerGroupOpen**](/windows/win32/P2P/nf-p2p-peergroupopen?branch=master) function. |
| [**PeerGroupConnect**](/windows/win32/P2P/nf-p2p-peergroupconnect?branch=master)                                   | Initiates a PNRP search for a peer group and attempts to connect to it. After this function is called successfully, a peer can communicate with other members of the peer group.                             |
| [**PeerGroupConnectByAddress**](/windows/win32/P2P/nf-p2p-peergroupconnectbyaddress?branch=master)                 | Attempts to connect to the peer group that other peers with known IPv6 addresses are participating in.                                                                                                       |
| [**PeerGroupCreate**](/windows/win32/P2P/nf-p2p-peergroupcreate?branch=master)                                     | Creates a new peer group.                                                                                                                                                                                    |
| [**PeerGroupCreateInvitation**](/windows/win32/P2P/nf-p2p-peergroupcreateinvitation?branch=master)                 | Returns an XML string that can be used by the specified peer to join a group.                                                                                                                                |
| [**PeerGroupCreatePasswordInvitation**](/windows/win32/P2P/nf-p2p-peergroupcreatepasswordinvitation?branch=master) | Returns an XML string that can be used by the specified peer to join a group with a matching password.                                                                                                       |
| [**PeerGroupDelete**](/windows/win32/P2P/nf-p2p-peergroupdelete?branch=master)                                     | Deletes the local data and certificate associated with a peer group.                                                                                                                                         |
| [**PeerGroupGetStatus**](/windows/win32/P2P/nf-p2p-peergroupgetstatus?branch=master)                               | Retrieves the current status of a group.                                                                                                                                                                     |
| [**PeerGroupIssueCredentials**](/windows/win32/P2P/nf-p2p-peergroupissuecredentials?branch=master)                 | Issues credentials, including a GMC, to a specific identity, and optionally returns an invitation XML string the invited peer can use to join a peer group.                                                  |
| [**PeerGroupJoin**](/windows/win32/P2P/nf-p2p-peergroupjoin?branch=master)                                         | Allows a peer with an invitation to join an existing peer group.                                                                                                                                             |
| [**PeerGroupOpen**](/windows/win32/P2P/nf-p2p-peergroupopen?branch=master)                                         | Opens a peer group that a peer has created or joined.                                                                                                                                                        |
| [**PeerGroupParseInvitation**](/windows/win32/P2P/nf-p2p-peergroupparseinvitation?branch=master)                   | Returns a [**PEER\_INVITATION\_INFO**](/windows/win32/P2P/ns-p2p-peer_invitation_info_tag?branch=master) structure with the details of a specific invitation.                                                                                        |
| [**PeerGroupPasswordJoin**](/windows/win32/P2P/nf-p2p-peergrouppasswordjoin?branch=master)                         | Allows a peer with an invitation and the correct password to join a password-protected peer group.                                                                                                           |



 

## Group and Member Information Functions



| Function                                                 | Description                                                                                                                        |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupEnumMembers**](/windows/win32/P2P/nf-p2p-peergroupenummembers?branch=master)     | Creates an enumeration of available peer group members and the associated membership information.                                  |
| [**PeerGroupGetProperties**](/windows/win32/P2P/nf-p2p-peergroupgetproperties?branch=master) | Retrieves information on the properties of a specified group.                                                                      |
| [**PeerGroupSetProperties**](/windows/win32/P2P/nf-p2p-peergroupsetproperties?branch=master) | Sets the current peer group properties. In version 1.0 of this API, only the creator of the peer group can perform this operation. |



 

## Records and Record Management Functions



| Function                                                 | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**PeerGroupAddRecord**](/windows/win32/P2P/nf-p2p-peergroupaddrecord?branch=master)         | Adds a new record to the peer group, which is propagated to all participating peers. |
| [**PeerGroupDeleteRecord**](/windows/win32/P2P/nf-p2p-peergroupdeleterecord?branch=master)   | Deletes a record from a peer group. Only the creator of a record can delete it.      |
| [**PeerGroupEnumRecords**](/windows/win32/P2P/nf-p2p-peergroupenumrecords?branch=master)     | Creates an enumeration of peer group records.                                        |
| [**PeerGroupGetRecord**](/windows/win32/P2P/nf-p2p-peergroupgetrecord?branch=master)         | Retrieves a specific group record.                                                   |
| [**PeerGroupSearchRecords**](/windows/win32/P2P/nf-p2p-peergroupsearchrecords?branch=master) | Searches the local peer group database for records that match the supplied criteria. |
| [**PeerGroupUpdateRecord**](/windows/win32/P2P/nf-p2p-peergroupupdaterecord?branch=master)   | Updates a record within a specific peer group.                                       |



 

## Group Database Import/Export Functions



| Function                                                   | Description                                                                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupExportDatabase**](/windows/win32/P2P/nf-p2p-peergroupexportdatabase?branch=master) | Exports a peer group database to a specific file, which can be transported to another computer and imported with the [**PeerGroupImportDatabase**](/windows/win32/P2P/nf-p2p-peergroupimportdatabase?branch=master) function. |
| [**PeerGroupImportDatabase**](/windows/win32/P2P/nf-p2p-peergroupimportdatabase?branch=master) | Imports a peer group database from a local file.                                                                                                                                          |



 

## Direct Connection Functions



| Function                                                                 | Description                                                         |
|--------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**PeerGroupCloseDirectConnection**](/windows/win32/P2P/nf-p2p-peergroupclosedirectconnection?branch=master) | Closes a specific direct connection between two peers.              |
| [**PeerGroupEnumConnections**](/windows/win32/P2P/nf-p2p-peergroupenumconnections?branch=master)             | Creates an enumeration of connections currently active on the peer. |
| [**PeerGroupOpenDirectConnection**](/windows/win32/P2P/nf-p2p-peergroupopendirectconnection?branch=master)   | Establishes a direct connection with another peer in a peer group.  |
| [**PeerGroupSendData**](/windows/win32/P2P/nf-p2p-peergroupsenddata?branch=master)                           | Sends data to a member over a neighbor or direct connection.        |



 

## Group Events Infrastructure



| Function                                                     | Description                                                                                    |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**PeerGroupGetEventData**](/windows/win32/P2P/nf-p2p-peergroupgeteventdata?branch=master)       | Allows an application to retrieve the data returned by a grouping event.                       |
| [**PeerGroupRegisterEvent**](/windows/win32/P2P/nf-p2p-peergroupregisterevent?branch=master)     | Registers a peer for specific peer group events.                                               |
| [**PeerGroupUnregisterEvent**](/windows/win32/P2P/nf-p2p-peergroupunregisterevent?branch=master) | Unregisters a peer from notification of peer events associated with the supplied event handle. |



 

## Group Time Conversion Functions



| Function                                                                     | Description                                                                                                                   |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupPeerTimeToUniversalTime**](/windows/win32/P2P/nf-p2p-peergrouppeertimetouniversaltime?branch=master) | Converts the peer group-maintained reference time value to a localized time value appropriate for display on a peer computer. |
| [**PeerGroupUniversalTimeToPeerTime**](/windows/win32/P2P/nf-p2p-peergroupuniversaltimetopeertime?branch=master) | Converts a local time value from a peer's computer to a common peer group time value.                                         |



 

## Group Configuration Functions



| Function                                               | Description                                                                                                                       |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupExportConfig**](/windows/win32/P2P/nf-p2p-peergroupexportconfig?branch=master) | Exports the group configuration for a peer as an XML string that contains the identity, group name, and the GMC for the identity. |
| [**PeerGroupImportConfig**](/windows/win32/P2P/nf-p2p-peergroupimportconfig?branch=master) | Imports a peer group configuration for an identity based on the specific settings in a supplied XML configuration string.         |



 

 

 



