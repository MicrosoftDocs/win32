---
title: The RPC Name Service Database
description: A name service is a service that maps names to objects, and usually maintains the (name, object) pairs in a database.
ms.assetid: 9ced2307-cf30-45d5-bcd2-c1e4aae8c63b
keywords:
- Remote Procedure Call RPC , described, name service database
ms.topic: article
ms.date: 05/31/2018
---

# The RPC Name Service Database

A name service is a service that maps names to objects, and usually maintains the (name, object) pairs in a database. Generally, the name is a logical name that is easy for users to remember and use. For example, a name service would allow a user to use the logical name "laserprinter." The name service maps this name to the network-specific name used by the print server.

To use a simplified explanation, the RPC name service maps a name to a binding handle and maintains the (name, binding handle) mappings in the RPC name service database. The RPC name service allows client applications to use a logical name instead of a specific protocol sequence and network address. The use of the logical name makes it easier for network administrators to install and configure your distributed application.

An RPC name service database entry has one of the following attributes: **server**, **group**, or **profile**. In the Microsoft implementation, entries can have only one attribute, so these entries are also known as server entries, group entries, and profile entries.

The server entry consists of interface UUIDs, object UUIDs (needed when the server implements multiple-entry points), network address, protocol sequence, and any endpoint information associated with well-known endpoints. When a dynamic endpoint is used, the endpoint information is kept in the endpoint-map database rather than the name service database, and the endpoint is resolved like any other dynamic endpoint. Server entries are managed by functions that start with the prefix "RpcNsBinding".

The group entry can contain server entries or other group entries. Group entries are managed by functions that start with the prefix "RpcNsGroup".

The profile entry can contain profile, group, or server entries. Profile entries are managed by the functions that start with the prefix "RpcNsProfile".

This section presents an overview of the name service database in the following topics:

-   [Name Service Application Guidelines](name-service-application-guidelines.md)
-   [An Overview of the Name Service Entry](an-overview-of-the-name-service-entry.md)
-   [Criteria for Name Service Entries](criteria-for-name-service-entries.md)
-   [Name Service Entry Cleanup](name-service-entry-cleanup.md)
-   [What Happens During a Query](what-happens-during-a-query.md)
-   [Using Microsoft Locator](using-microsoft-locator.md)
-   [Using the Cell Directory Service (CDS)](using-the-cell-directory-service-cds-.md)
-   [Name Syntax](name-syntax.md)

 

 




