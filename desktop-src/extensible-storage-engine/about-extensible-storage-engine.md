---
description: "Learn more about: About Extensible Storage Engine"
title: About Extensible Storage Engine
TOCTitle: About Extensible Storage Engine
ms:assetid: 06d1526e-169d-4677-b409-2ed415287de6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269181(v=EXCHG.10)
ms:contentKeyID: 32765484
ms.date: 07/10/2026
ms.topic: concept-article
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

## Security considerations

Applications that use ESENT are responsible for securing the directories and files used by the database engine, including database files (.edb), transaction logs, checkpoint files, and backup copies.

ESENT stores data in locations specified by the application and does not enforce application-specific access controls on those files. To protect sensitive information, applications should:

- Store database and log files in directories with appropriate filesystem permissions.
- Restrict access to only the accounts and services that require access to the data.
- Consider operating system features such as volume encryption or file encryption where appropriate.
- Ensure that backup copies of database and log files receive the same level of protection as the live database.
- Avoid storing database files in locations that are writable or accessible by untrusted users.

Failure to adequately protect database and log files may allow an attacker with filesystem access to read, modify, replace, copy, or delete application data. An attacker with write access to the database or log files can trigger attacker-supplied code execution in processes that later consume the database or logs.

