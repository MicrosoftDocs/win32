---
Description: 'Changes made to the installation database are not written to the database until you call MsiDatabaseCommit.'
ms.assetid: '65271631-457c-4d3e-9384-126d2c9d63d7'
title: Committing Databases
---

# Committing Databases

Changes made to the installation database are not written to the database until you call [**MsiDatabaseCommit**](msidatabasecommit.md).

**To ensure changes made in a database are finalized**

1.  Check to see whether a table will be written when you call [**MsiDatabaseCommit**](msidatabasecommit.md) by calling [**MsiDatabaseIsTablePersistent**](msidatabaseistablepersistent.md).
2.  Call the [**MsiDatabaseCommit**](msidatabasecommit.md) function to finalize changes to the database.

Changes made in a database are accumulated and are not reflected in the actual database until you call [**MsiDatabaseCommit**](msidatabasecommit.md). Temporary columns or rows are not committed to the database. When a database is closed, all changes made since the last **MsiDatabaseCommit** are automatically rolled back.

 

 



