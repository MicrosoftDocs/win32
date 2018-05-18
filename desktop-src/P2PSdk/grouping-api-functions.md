---
Description: 'The Grouping API uses the following functions:'
ms.assetid: '56ea2880-b468-4816-b6c9-5780c807b3f1'
title: Grouping API Functions
---

# Grouping API Functions

The Grouping API uses the following functions:

## Group Initialization and Cleanup Functions



| Function                                       | Description                                                                                                            |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupShutdown**](peergroupshutdown.md) | Closes a peer group created with [**PeerGroupStartup**](peergroupstartup.md) and disposes of any allocated resources. |
| [**PeerGroupStartup**](peergroupstartup.md)   | Initiates a peer group by using a requested version of the Peer infrastructure.                                        |



 

## Group Creation and Access Functions



| Function                                                                       | Description                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupClose**](peergroupclose.md)                                       | Invalidates the peer group handle obtained by a previous call to the [**PeerGroupCreate**](peergroupcreate.md), [**PeerGroupJoin**](peergroupjoin.md), or [**PeerGroupOpen**](peergroupopen.md) function. |
| [**PeerGroupConnect**](peergroupconnect.md)                                   | Initiates a PNRP search for a peer group and attempts to connect to it. After this function is called successfully, a peer can communicate with other members of the peer group.                             |
| [**PeerGroupConnectByAddress**](peergroupconnectbyaddress.md)                 | Attempts to connect to the peer group that other peers with known IPv6 addresses are participating in.                                                                                                       |
| [**PeerGroupCreate**](peergroupcreate.md)                                     | Creates a new peer group.                                                                                                                                                                                    |
| [**PeerGroupCreateInvitation**](peergroupcreateinvitation.md)                 | Returns an XML string that can be used by the specified peer to join a group.                                                                                                                                |
| [**PeerGroupCreatePasswordInvitation**](peergroupcreatepasswordinvitation.md) | Returns an XML string that can be used by the specified peer to join a group with a matching password.                                                                                                       |
| [**PeerGroupDelete**](peergroupdelete.md)                                     | Deletes the local data and certificate associated with a peer group.                                                                                                                                         |
| [**PeerGroupGetStatus**](peergroupgetstatus.md)                               | Retrieves the current status of a group.                                                                                                                                                                     |
| [**PeerGroupIssueCredentials**](peergroupissuecredentials.md)                 | Issues credentials, including a GMC, to a specific identity, and optionally returns an invitation XML string the invited peer can use to join a peer group.                                                  |
| [**PeerGroupJoin**](peergroupjoin.md)                                         | Allows a peer with an invitation to join an existing peer group.                                                                                                                                             |
| [**PeerGroupOpen**](peergroupopen.md)                                         | Opens a peer group that a peer has created or joined.                                                                                                                                                        |
| [**PeerGroupParseInvitation**](peergroupparseinvitation.md)                   | Returns a [**PEER\_INVITATION\_INFO**](peer-invitation-info.md) structure with the details of a specific invitation.                                                                                        |
| [**PeerGroupPasswordJoin**](peergrouppasswordjoin.md)                         | Allows a peer with an invitation and the correct password to join a password-protected peer group.                                                                                                           |



 

## Group and Member Information Functions



| Function                                                 | Description                                                                                                                        |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupEnumMembers**](peergroupenummembers.md)     | Creates an enumeration of available peer group members and the associated membership information.                                  |
| [**PeerGroupGetProperties**](peergroupgetproperties.md) | Retrieves information on the properties of a specified group.                                                                      |
| [**PeerGroupSetProperties**](peergroupsetproperties.md) | Sets the current peer group properties. In version 1.0 of this API, only the creator of the peer group can perform this operation. |



 

## Records and Record Management Functions



| Function                                                 | Description                                                                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**PeerGroupAddRecord**](peergroupaddrecord.md)         | Adds a new record to the peer group, which is propagated to all participating peers. |
| [**PeerGroupDeleteRecord**](peergroupdeleterecord.md)   | Deletes a record from a peer group. Only the creator of a record can delete it.      |
| [**PeerGroupEnumRecords**](peergroupenumrecords.md)     | Creates an enumeration of peer group records.                                        |
| [**PeerGroupGetRecord**](peergroupgetrecord.md)         | Retrieves a specific group record.                                                   |
| [**PeerGroupSearchRecords**](peergroupsearchrecords.md) | Searches the local peer group database for records that match the supplied criteria. |
| [**PeerGroupUpdateRecord**](peergroupupdaterecord.md)   | Updates a record within a specific peer group.                                       |



 

## Group Database Import/Export Functions



| Function                                                   | Description                                                                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupExportDatabase**](peergroupexportdatabase.md) | Exports a peer group database to a specific file, which can be transported to another computer and imported with the [**PeerGroupImportDatabase**](peergroupimportdatabase.md) function. |
| [**PeerGroupImportDatabase**](peergroupimportdatabase.md) | Imports a peer group database from a local file.                                                                                                                                          |



 

## Direct Connection Functions



| Function                                                                 | Description                                                         |
|--------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**PeerGroupCloseDirectConnection**](peergroupclosedirectconnection.md) | Closes a specific direct connection between two peers.              |
| [**PeerGroupEnumConnections**](peergroupenumconnections.md)             | Creates an enumeration of connections currently active on the peer. |
| [**PeerGroupOpenDirectConnection**](peergroupopendirectconnection.md)   | Establishes a direct connection with another peer in a peer group.  |
| [**PeerGroupSendData**](peergroupsenddata.md)                           | Sends data to a member over a neighbor or direct connection.        |



 

## Group Events Infrastructure



| Function                                                     | Description                                                                                    |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**PeerGroupGetEventData**](peergroupgeteventdata.md)       | Allows an application to retrieve the data returned by a grouping event.                       |
| [**PeerGroupRegisterEvent**](peergroupregisterevent.md)     | Registers a peer for specific peer group events.                                               |
| [**PeerGroupUnregisterEvent**](peergroupunregisterevent.md) | Unregisters a peer from notification of peer events associated with the supplied event handle. |



 

## Group Time Conversion Functions



| Function                                                                     | Description                                                                                                                   |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupPeerTimeToUniversalTime**](peergrouppeertimetouniversaltime.md) | Converts the peer group-maintained reference time value to a localized time value appropriate for display on a peer computer. |
| [**PeerGroupUniversalTimeToPeerTime**](peergroupuniversaltimetopeertime.md) | Converts a local time value from a peer's computer to a common peer group time value.                                         |



 

## Group Configuration Functions



| Function                                               | Description                                                                                                                       |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**PeerGroupExportConfig**](peergroupexportconfig.md) | Exports the group configuration for a peer as an XML string that contains the identity, group name, and the GMC for the identity. |
| [**PeerGroupImportConfig**](peergroupimportconfig.md) | Imports a peer group configuration for an identity based on the specific settings in a supplied XML configuration string.         |



 

 

 



