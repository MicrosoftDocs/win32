---
title: ESE Handles
TOCTitle: ESE Handles
ms:assetid: 969ae14f-3548-431d-a19d-5df92891441d
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269349(v=EXCHG.10)
ms:contentKeyID: 32765636
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
---

# ESE Handles


_**Applies to:** Windows | Windows Server_

## ESE Handles

ESE handles are used to create sessions and access databases. They are maintained in a hierarchy, which means that the output from one level is used to access resources at the next level.

The diagram here shows the hierarchy of handles and the corresponding functions that create the handles. Also indicated along with the functions are the handles that are used in the call to create the new handle.

![ESE\_Documentation\_handles2](images/Gg269349.ESE_Documentation_handles2(EXCHG.10).gif "ESE_Documentation_handles2")

As shown in the diagram, the instance is the root handle and the level at which the database is recovered in the event of an unexpected process termination or system shutdown. The instance handle, JET\_INSTANCE, is created by [JetCreateInstance](gg269354\(v=exchg.10\).md) and [JetCreateInstance2](gg269202\(v=exchg.10\).md). The next level, the session level, is the transaction context of the database engine and the level under which all database operations are performed. The session handle, JET\_SESID, is created in the context of the instance in the call to [JetBeginSession](gg294131\(v=exchg.10\).md). The session ID is used in all subsequent calls to access tables and databases. If the instance is being used by more than one thread at a time then each thread must use its own session handle. The database handle is created using the session handle and primarily used to manage the schema of the database, but it can also be used to manage tables inside the database. Database handles can only be used in the session under which they are created. The handle to the database is created in the call to [JetCreateDatabase](gg269212\(v=exchg.10\).md) or [JetOpenDatabase](gg269299\(v=exchg.10\).md). Tables are associated with the database ID under which they are created.

The JET\_TABLEID data type contains a handle to a database cursor. It is used to scan records, search records or create update and delete records. The table handle is created in the call to [JetOpenTable](gg294118\(v=exchg.10\).md), or [JetCreateTable](gg269210\(v=exchg.10\).md). [JetOpenTempTable](gg269211\(v=exchg.10\).md), [JetOpenTempTable2](gg269302\(v=exchg.10\).md), and [JetOpenTempTable3](gg269255\(v=exchg.10\).md) also create table IDs for temporary tables, and [JetCreateTableColumnIndex](gg269343\(v=exchg.10\).md) and [JetCreateTableColumnIndex2](gg294057\(v=exchg.10\).md) return table IDs in the out structure. The columns created within the table each have a unique column identifier or COLUMN\_ID. The columns IDs are created in the calls to [JetAddColumn](gg294122\(v=exchg.10\).md), or in calls to [JetOpenTempTable](gg269211\(v=exchg.10\).md), [JetOpenTempTable2](gg269302\(v=exchg.10\).md), or [JetOpenTempTable3](gg269255\(v=exchg.10\).md) for temporary tables. Column IDs may also be retrieved for a given column by name with APIs such as [JetGetTableColumnInfo](gg294061\(v=exchg.10\).md).

