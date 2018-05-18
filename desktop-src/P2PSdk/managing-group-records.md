---
Description: 'A group record is specific data published to all active members of a peer group, for example, a chat message or an application-specific status update.'
ms.assetid: '073ee4e9-0e97-451a-a808-8265575d073c'
title: Managing Group Records
---

# Managing Group Records

A group record is specific data published to all active members of a peer group, for example, a chat message or an application-specific status update. A record is represented by the [**PEER\_RECORD**](peer-record.md) structure, and contains the following information about a peer:

-   The record ID is a value that uniquely identifies a record in the peer group.
-   A GUID that specifies the record type. Applications can support different record types. An application interprets the **data** field of a record based on the record type. Some GUIDs are reserved, and the API call returns **PEER\_E\_NOT\_AUTHORIZED** when the application attempts to use them.
-   A set of record attributes described as an XML string. The attributes are used when searching records. For more information about attributes, see [Record Attribute Schema](record-attribute-schema.md).
-   The peer time that a record is created.
-   The peer time that a record expires.
-   The peer time that a record is modified.
-   The creator of a record.
-   The member who modifies a record.
-   A [**PEER\_DATA**](peer-data.md) structure that contains the cryptographic signature for all of the fields in this [**PEER\_RECORD**](peer-record.md) structure. This field cannot be directly updated or altered by a peer.
-   A [**PEER\_DATA**](peer-data.md) structure that contains the application-specific data associated with this record as an array of bytes. The type of data present in this field is determined by application-defined record type.

## Obtaining Peer Group Records

Individual records are obtained by calling [**PeerGroupGetRecord**](peergroupgetrecord.md) with the ID of the record. When processing all records of a specific type, the enumerated set of all current peer group records is obtained by first calling [**PeerGroupEnumRecords**](peergroupenumrecords.md) to open the enumeration and then iteratively calling [**PeerGetNextItem**](peergetnextitem.md) until all records are retrieved. When finished, close the enumeration and release the memory associated with it by calling [**PeerEndEnumeration**](peerendenumeration.md).

When a record is created, deleted, or updated by a peer, the affected record is published to all members of the peer group by way of the **PEER\_GROUP\_EVENT\_RECORD\_CHANGE** event. Note that if a peer is not connected to the group, it will receive the updated record then next time it connects. It is important to register for this event with [**PeerGroupRegisterEvent**](peergroupregisterevent.md) if your application maintains or manages records in any meaningful way. Alternatively, the application can query the record database on demand using [**PeerGroupSearchRecords**](peergroupsearchrecords.md).

When the **PEER\_GROUP\_EVENT\_RECORD\_CHANGE** event is raised, the specific record ID and type as well as the type of change (add, update, delete) is received as a [**PEER\_EVENT\_RECORD\_CHANGE\_DATA**](peer-event-record-change-data.md) structure. This structure is obtained with a call to [**PeerGroupGetEventData**](peergroupgeteventdata.md). If the change is an add or an update, you should use [**PeerGroupGetRecord**](peergroupgetrecord.md) to obtain the record with the supplied ID. The local record database for the infrastructure is updated automatically.

You can also search for specific records based on specific custom attributes supplied in the **pwzAttributes** field of [**PEER\_RECORD**](peer-record.md), as well as any predefined attributes. To accomplish this, use the [**PeerGroupSearchRecords**](peergroupsearchrecords.md) function with an XML search query formatted as specified in the [Record Search Query Format](record-search-query-format.md) topic.

For more details on working with records in the Peer Infrastructure, please refer to the [Records](records.md) topic in [Using the Peer Infrastructure](using-the-peer-infrastructure.md).

## Administration of Peer Group Records

When the initial invitations are issued by the peer group's creator, it can specify that certain members serve in an administrative role (PEER\_GROUP\_ROLE\_ADMIN) whenever it issues new credentials to the user (via either [**PeerGroupCreateInvitation**](peergroupcreateinvitation.md) or [**PeerGroupIssueCredentials**](peergroupissuecredentials.md)). An administrator has the ability to directly add, delete, and update any peer group records. Conversely, a peer group member with it's role set to either **PEER\_GROUP\_ROLE\_MEMBER** or **PEER\_GROUP\_ROLE\_INVITING\_MEMBER** can only add, update, and delete its own record(s).

The creator has the administrator role by default.

To update a record, obtain the record with [**PeerGroupGetRecord**](peergroupgetrecord.md) or [**PeerGroupEnumRecords**](peergroupenumrecords.md), make the changes, and pass the updated record to [**PeerGroupUpdateRecord**](peergroupupdaterecord.md).

To delete a record, pass the record ID to delete to [**PeerGroupDeleteRecord**](peergroupdeleterecord.md).

To add a record, create a new [**PEER\_RECORD**](peer-record.md) structure and populate the following fields:

-   **dwSize**. This field contains the value of **sizeof**([**PEER\_RECORD**](peer-record.md)).
-   **ftExpiration**. This field contains the expiration date and time of this record, expressed in peer time as a **FILETIME** structure.
-   **type**. This field contains a **GUID** value that identifies the record type to the application. If this type is custom to your application infrastructure, you should also populate the **data** field.

The following fields are populated by the infrastructure, and will be ignored if set by the application:

-   **id**
-   **pwzCreatorId**
-   **pwzLastModifiedById**
-   **ftCreation**
-   **ftLastModified**
-   **securityData**

The remaining fields are optional. To add this new record to the peer group, pass it to [**PeerGroupAddRecord**](peergroupaddrecord.md).

## Importing and Exporting Records

Peer-to-peer group records are maintained locally as a database. To save a current snapshot of the peer group record database to a local file, call [**PeerGroupExportDatabase**](peergroupexportdatabase.md), and pass it the handle to the peer group. This file can then be transported to a different computer or application, which can extract and use this record database by calling [**PeerGroupImportDatabase**](peergroupimportdatabase.md).

 

 



