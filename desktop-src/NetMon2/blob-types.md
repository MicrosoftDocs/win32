---
description: Network Monitor uses three types of binary large objects (BLOBs) to select and connect network interface cards (NICs), capture data, and manipulate NPP data.
ms.assetid: f7cbceb1-1a85-4a05-8420-90b32c9c9b61
title: BLOB Types
ms.topic: article
ms.date: 05/31/2018
---

# BLOB Types

Network Monitor uses three types of binary large objects (BLOBs) to select and connect network interface cards (NICs), capture data, and manipulate NPP data.

## NPP BLOB

Applications use NPP BLOBs to connect to a specific NIC through an NPP. (The application makes the connection with a call to **CreateNPPInterface** and location data in the NPP BLOB.) An application can also store its configuration data in the NPP BLOB to configure the NPP. Also, an application that saves its NPP BLOB is not required to go through the Finder to reuse that BLOB.

## Filter BLOB

A filter BLOB contains application-defined criteria that you can use to select an NPP and a NIC. For example, an application can request a specific NIC, only Ethernet cards, or cards that support a specific frame capture rate.

## Special BLOB

When an NPP requires additional data before it can return an NPP BLOB to an application, the NPP uses a special BLOB. Most often, the application will not need or use special BLOBs so they are not returned to an application unless a specific flag is set in one function call. For example, a remote NPP uses a special BLOB because a path name is required to make a connection. An application that receives a remote NPP special BLOB could add the string and call back into the Finder to get an NPP BLOB table. For more information, see [Special BLOB Entries](special-blob-entries.md).

 

 



