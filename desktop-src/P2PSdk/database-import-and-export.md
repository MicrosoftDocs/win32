---
Description: When using the Peer Graphing or the Peer Grouping Infrastructures, the information (records) that peers publish to a graph or group is stored as a database on each peer computer.
ms.assetid: 1412b2eb-c97d-4415-998c-5f21eaadcc66
title: Database Import and Export
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Database Import and Export

When using the Peer Graphing or the Peer Grouping Infrastructures, the information (records) that peers publish to a graph or group is stored as a database on each peer computer. To migrate an application from one computer to another computer, you can export a Peer Graphing or Peer Grouping database from one computer, and then import it to another.

The following list identifies important information about working with databases:

-   You can only import a database that has the same graph and peer ID.
-   You cannot call the import and export functions if [**PeerGraphListen**](/windows/win32/P2P/nf-p2p-peergraphlisten?branch=master), [**PeerGroupConnect**](/windows/win32/P2P/nf-p2p-peergroupconnect?branch=master), or [**PeerGraphConnect**](/windows/win32/P2P/nf-p2p-peergraphconnect?branch=master) have been called.

**Peer Graphing Infrastructure** uses the following calls to import and export a record database:

-   [**PeerGraphExportDatabase**](/windows/win32/P2P/nf-p2p-peergraphexportdatabase?branch=master)
-   [**PeerGraphImportDatabase**](/windows/win32/P2P/nf-p2p-peergraphimportdatabase?branch=master)

**Peer Grouping Infrastructure** uses the following calls to import and export a record database:

-   [**PeerGroupExportDatabase**](/windows/win32/P2P/nf-p2p-peergroupexportdatabase?branch=master)
-   [**PeerGroupImportDatabase**](/windows/win32/P2P/nf-p2p-peergroupimportdatabase?branch=master)

 

 



