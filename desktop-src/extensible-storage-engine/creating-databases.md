---
description: "Learn more about: Creating Databases"
title: Creating Databases
TOCTitle: Creating Databases
ms:assetid: d221144d-f777-4f8a-80ca-2ebdb77108dc
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294100(v=EXCHG.10)
ms:contentKeyID: 32765715
ms.date: 04/11/2016
ms.topic: article
---

# Creating Databases


_**Applies to:** Windows | Windows Server_

## Creating Databases

The ESE database comprises one or more tables that organize data by columns and rows. The ESE database is identified by name and database ID. An ESE database looks like a single file to the Microsoft Windows operating system; however, internally the database is stored as a collection of pages. These pages contain metadata that describe the data in the database, the data itself, and one or more indices that store different orders of the data. The database may contain up to 2^31 pages, or 16 Terabytes of data for a database with 8 KB pages.

The application creates an instance of the database engine, then creates a database and attaches it to the instance. Up to 6 databases can be simultaneously attached to an instance with [JetCreateDatabase](./jetcreatedatabase-function.md) or [JetAttachDatabase](./jetattachdatabase-function.md). One or more sessions should be started within the database, because all subsequent ESE operations are performed in the context of a session. A separate session should be opened for each thread using ESE.

This procedure will initialize ESE and create a database.

### To initialize ESE and create a database

1.  [JetCreateInstance](./jetcreateinstance-function.md): Creates an instance of the database engine.
    
    **Windows XP and later:** This function is available in Windows XP and later. On Windows 2000, only one instance is supported and that instance is created implicitly

2.  [JetSetSystemParameter](./jetsetsystemparameter-function.md): System parameters that the affect the physical layout such as the JET_paramLogFilePath and JET_paramSystemPath must be set before initializing the instance with [JetInit](./jetinit-function.md). The parameters set at this stage are set for all databases created in the instance. [JetSetSystemParameter](./jetsetsystemparameter-function.md) is the only function that can use the instance before it is initialized with [JetInit](./jetinit-function.md).

3.  [JetInit](./jetinit-function.md): Initializes the instance. Instance must be initialized with [JetInit](./jetinit-function.md) before it can be used with any other functions.

4.  [JetBeginSession](./jetbeginsession-function.md): Creates the session for all subsequent transactions. All database transactions take place in the context of the session ([JET_SESID](./jet-sesid.md)).

5.  [JetCreateDatabase](./jetcreatedatabase-function.md): Creates the database and returns a handle to the database ID ([JET_DBID](./jet-dbid.md)).
    
    If the database already exists, step 5 above is replaced by the following two steps:
    
    1.  [JetAttachDatabase](./jetattachdatabase-function.md): Attaches the database by name to the session
    
    2.  [JetOpenDatabase](./jetopendatabase-function.md): Returns the database ID that is used in subsequent database operations.

A database can be detached from one ESE instance using [JetDetachDatabase](./jetdetachdatabase-function.md) and later attached to another instance with [JetAttachDatabase](./jetattachdatabase-function.md). When the database is detached, it can be copied as a single file using standard Windows utilities. However, when the database is attached to an ESE instance it cannot be copied since ESE opens database files exclusively. Also, if the instance crashes then the database file cannot be copied alone because it needs the transaction log files associated with it to recover from that crash.
