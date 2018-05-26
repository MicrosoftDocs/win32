---
Description: Before working with a database you must first obtain a handle to it.
ms.assetid: 53cf73bc-4d52-471c-8384-46d106a36e38
title: Obtaining a Database Handle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining a Database Handle

Before working with a database you must first obtain a handle to it.

**To access information about an installer database**

1.  Obtain a handle to the database in one of two ways:
    -   If an installation is in progress, get a handle to the active database by calling the [**MsiGetActiveDatabase**](/windows/win32/Msiquery/nf-msiquery-msigetactivedatabase?branch=master) function.
    -   If an installation is not in progress, open any specified database by calling the [**MsiOpenDatabase**](/windows/win32/Msiquery/nf-msiquery-msiopendatabasea?branch=master) function.
2.  After the database has been opened, you can call functions to obtain information about the database or to manipulate the database.
    -   Create a **View** object and specify a SQL query of the open database by calling the [**MsiDatabaseOpenView**](/windows/win32/Msiquery/nf-msiquery-msidatabaseopenviewa?branch=master) function.
    -   Obtain a record that contains all primary keys of a specified table in the open database by calling the [**MsiDatabaseGetPrimaryKeys**](/windows/win32/Msiquery/nf-msiquery-msidatabasegetprimarykeysa?branch=master) function.
    -   Check the current state of an open database by calling the [**MsiGetDatabaseState**](/windows/win32/Msiquery/nf-msiquery-msigetdatabasestate?branch=master) function. With the **MsiGetDatabaseState** function, you can determine the read/write status for a database or if the handle is valid.

 

 



