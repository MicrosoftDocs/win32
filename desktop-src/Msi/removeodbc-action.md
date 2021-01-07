---
description: The RemoveODBC action removes the data sources, translators, and drivers listed for removal during the installation.
ms.assetid: 548984fd-e4f7-4db8-a625-87b4a0a4bdb2
title: RemoveODBC Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveODBC Action

The RemoveODBC action removes the data sources, translators, and drivers listed for removal during the installation. This action queries the [ODBCDataSource table](odbcdatasource-table.md), [ODBCTranslator table](odbctranslator-table.md), and [ODBCDriver table](odbcdriver-table.md) for each data source, translator, or driver scheduled for removal.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages

For each driver installed.



| Field | Description of action data               |
|-------|------------------------------------------|
| \[1\] | Driver description. The ODBC driver key. |
| \[2\] | ComponentId                              |



 

For each translator installed.



| Field | Description of action data               |
|-------|------------------------------------------|
| \[1\] | Driver description. The ODBC driver key. |
| \[2\] | ComponentId                              |



 

For each data source installed.



| Field | Description of action data                              |
|-------|---------------------------------------------------------|
| \[1\] | Driver description. The ODBC driver key.                |
| \[2\] | ComponentId                                             |
| \[3\] | Registration: SQL\_REMOVE\_DSN or SQL\_REMOVE\_SYS\_DSN |



 

## Remarks

If both the ODBC usage count and the file usage count become zero, the file is removed. Registration is dependent on ODBC usage counts and file removal is based on shared DLLs key reference counts.

 

 



