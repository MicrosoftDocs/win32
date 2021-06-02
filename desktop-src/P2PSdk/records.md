---
description: Records are a way to communicate between nodes in a graph or members in a group.
ms.assetid: 'f4c0869f-f147-4c2b-9418-3b407e22cb16'
title: Records
ms.topic: article
ms.date: 05/31/2018
---

# Records

Records are a way to communicate between nodes in a graph or members in a group. A record consists of the following two parts:

-   Record header
-   Specific opaque data content

The header contains information about the record, including the version, creator, and type of data being published. The header also contains an XML attributes field that allows applications to add name-value attributes that describe the data, and to efficiently search the record database for specific records that have previously been published. The content is the application-defined data, and is opaque to the Peer Infrastructure.

When a record is published, it (both header and data) is flooded throughout the graph or group. Synchronized peers receive this data and store it in a local database. Unsynchronized and offline peers receive the data the next time they connect and synchronize with the peer graph or group.

For information about working with records, see the following topics:

-   [Record Dependencies](record-dependencies.md)
-   [Record Management](record-management.md)
-   [Record Attribute Schema](record-attribute-schema.md)
-   [Record Search Query Format](record-search-query-format.md)

 

 



