---
Description: Changes made to the installation database are not written to the database until you call MsiDatabaseCommit.
ms.assetid: 65271631-457c-4d3e-9384-126d2c9d63d7
title: Committing Databases
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Committing Databases

Changes made to the installation database are not written to the database until you call [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master).

**To ensure changes made in a database are finalized**

1.  Check to see whether a table will be written when you call [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master) by calling [**MsiDatabaseIsTablePersistent**](/windows/win32/Msiquery/nf-msiquery-msidatabaseistablepersistenta?branch=master).
2.  Call the [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master) function to finalize changes to the database.

Changes made in a database are accumulated and are not reflected in the actual database until you call [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master). Temporary columns or rows are not committed to the database. When a database is closed, all changes made since the last **MsiDatabaseCommit** are automatically rolled back.

 

 



