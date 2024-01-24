---
description: "Learn more about: About Extensible Storage Engine"
title: About Extensible Storage Engine
TOCTitle: About Extensible Storage Engine
ms:assetid: 06d1526e-169d-4677-b409-2ed415287de6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269181(v=EXCHG.10)
ms:contentKeyID: 32765484
ms.date: 04/11/2016
ms.topic: article
---

# About Extensible Storage Engine


_**Applies to:** Exchange Server 2013 | Windows | Windows Server_

## About Extensible Storage Engine

The extensible storage engine (ESE) is a database engine that stores information in a logical sequence. Information can be retrieved either sequentially or by accessing defined indices. Updates to the database are implemented with a transaction in order to ensure secure operations. ESE enables simultaneous access to multiple databases, including transaction-log file databases that can be used for system recovery. ESE is scalable to large or small applications. The following features are available with the ESE application programming interface (API):

  - Backup and restore: An application can make consistent copies of the data state while it is on-line and actively modifying data state.

  - Cursor Navigation: The application can navigate with the cursor to access data either sequentially or by using indices.

  - Database: A collection of tables that are backed up and restored as a single unit.

  - Logging and crash recovery: The ESE API ensures that application-defined data consistency is honored even in the event of a system crash.

  - Tables: The fundamental structure of the ESE database that is used to store data.

  - Transaction: The ESE database engine provides Atomic Consistent Isolated Durable (ACID) transactions that allow applications to retrieve data only from reliable data states and maintains data consistency in the event of an unexpected process termination or system shutdown.

  - Scalable: The application can create databases as large as 100 GB or as small as 1MB.

