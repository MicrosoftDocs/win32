---
description: The tables of the system tables group track the tables and columns of the installation database.
ms.assetid: d20be8b6-f456-4f90-aa9e-dc122c20d20c
title: System Tables Group
ms.topic: article
ms.date: 05/31/2018
---

# System Tables Group

The tables of the system tables group track the tables and columns of the installation database.

-   The [\_Tables table](-tables-table.md) tracks all the tables in the database. This includes tables that you may have created for your own custom actions. Query this table to find out if a table exists.
-   The [\_Columns table](-columns-table.md) tracks columns in the installation database. Temporary columns are currently not tracked by this table. Query this table to find out if a given column exists.
-   The [\_Streams table](-streams-table.md) lists embedded OLE data streams.
-   The [\_Storages table](-storages-table.md) lists embedded OLE data storages.
-   The [\_Validation table](-validation-table.md). The \_Validation table tracks the types and allowed ranges of every column in the database. The \_Validation table is used during the database validation process to ensure that all columns are accounted for and have the correct values. This table is not shipped with the installer database.

 

 



