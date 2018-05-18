---
Description: 'When using the Peer Graphing or the Peer Grouping Infrastructures, the information (records) that peers publish to a graph or group is stored as a database on each peer computer.'
ms.assetid: '1412b2eb-c97d-4415-998c-5f21eaadcc66'
title: Database Import and Export
---

# Database Import and Export

When using the Peer Graphing or the Peer Grouping Infrastructures, the information (records) that peers publish to a graph or group is stored as a database on each peer computer. To migrate an application from one computer to another computer, you can export a Peer Graphing or Peer Grouping database from one computer, and then import it to another.

The following list identifies important information about working with databases:

-   You can only import a database that has the same graph and peer ID.
-   You cannot call the import and export functions if [**PeerGraphListen**](peergraphlisten.md), [**PeerGroupConnect**](peergroupconnect.md), or [**PeerGraphConnect**](peergraphconnect.md) have been called.

**Peer Graphing Infrastructure** uses the following calls to import and export a record database:

-   [**PeerGraphExportDatabase**](peergraphexportdatabase.md)
-   [**PeerGraphImportDatabase**](peergraphimportdatabase.md)

**Peer Grouping Infrastructure** uses the following calls to import and export a record database:

-   [**PeerGroupExportDatabase**](peergroupexportdatabase.md)
-   [**PeerGroupImportDatabase**](peergroupimportdatabase.md)

 

 



