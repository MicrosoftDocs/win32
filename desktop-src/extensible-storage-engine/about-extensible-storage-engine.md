---
description: "Learn about the Extensible Storage Engine (ESE) database features, and how to secure ESENT database, transaction log, and backup files on Windows."
title: Extensible Storage Engine (ESE)
TOCTitle: About Extensible Storage Engine
ms:assetid: 06d1526e-169d-4677-b409-2ed415287de6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269181(v=EXCHG.10)
ms:contentKeyID: 32765484
ms.date: 08/13/2026
ms.topic: concept-article
---

# About Extensible Storage Engine

_**Applies to:** Exchange Server 2013 | Windows | Windows Server_

The Extensible Storage Engine (ESE) is a database engine that stores information in a logical sequence. You can retrieve information either sequentially or by accessing defined indices. ESE implements updates to the database within a transaction to ensure secure operations. ESE provides simultaneous access to multiple databases, including transaction-log file databases that you can use for system recovery. ESE is scalable to large or small applications. The following features are available with the ESE application programming interface (API):

- Backup and restore: An application can make consistent copies of the data state while it's on-line and modifying data state.

- Cursor navigation: The application can navigate with the cursor to access data either sequentially or by using indices.

- Database: A collection of tables that you back up and restore as a single unit.

- Logging and crash recovery: The ESE API ensures application-defined data consistency even during a system crash.

- Tables: The fundamental structure of the ESE database that stores data.

- Transaction: The ESE database engine provides Atomic Consistent Isolated Durable (ACID) transactions that allow applications to retrieve data only from reliable data states, and maintains data consistency during an unexpected process termination or system shutdown.

- Scalable: The application can create databases as large as 100 GB or as small as 1 MB.

## Security considerations for ESENT database and log files

ESENT is the Windows implementation of the Extensible Storage Engine (ESE). Applications that use ESENT are responsible for securing the directories and files that the database engine uses, including database files (.edb), transaction logs, checkpoint files, and backup copies.

ESENT stores data in locations that the application specifies, and doesn't enforce application-specific access controls on those files. To protect sensitive information, applications should:

- Store database and log files in directories with appropriate filesystem permissions.
- Restrict access to only the accounts and services that require access to the data.
- Consider operating system features such as volume encryption or file encryption where appropriate.
- Ensure that backup copies of database and log files receive the same level of protection as the live database.
- Avoid storing database files in locations that are writable or accessible by untrusted users.

Failure to adequately protect database and log files might allow an attacker with filesystem access to read, modify, replace, copy, or delete application data. An attacker with write access to the database or log files can trigger attacker-supplied code execution in processes that later consume the database or logs.

