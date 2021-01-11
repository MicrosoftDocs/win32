---
description: Binary data cannot be inserted into a table directly using the INSERT INTO or UPDATE SQL queries.
ms.assetid: cc055de8-eaba-48eb-a982-4d584ac7a881
title: Adding Binary Data to a Table Using SQL
ms.topic: article
ms.date: 05/31/2018
---

# Adding Binary Data to a Table Using SQL

Binary data cannot be inserted into a table directly using the INSERT INTO or UPDATE SQL queries. In order to add binary data to a table, you must first use the parameter marker (?) in the query as a placeholder for the binary value. The execution of the query should include a record that contains the binary data in one of its fields.

A marker is a parameter reference to a value supplied by a record submitted with the query. It is represented in the SQL statement by a question mark (?).

The following sample code adds binary data to a table.


```C++
#include <windows.h>
#include <Msiquery.h>
#include <tchar.h>
#pragma comment(lib, "msi.lib")


int main()  
{ 

PMSIHANDLE hDatabase = 0;
PMSIHANDLE hView = 0;
PMSIHANDLE hRec = 0;

if (ERROR_SUCCESS == MsiOpenDatabase(_T("c:\\temp\\testdb.msi"), MSIDBOPEN_TRANSACT, &hDatabase))
{
    //
    // Open view on Binary table so that we can add a new row, must use '?' to represent Binary data
    //

    if (ERROR_SUCCESS == MsiDatabaseOpenView(hDatabase, _T("INSERT INTO `Binary` (`Name`, `Data`) VALUES ('NewBlob', ?)"), &hView))
    {

        //
        // Create record with binary data in 1st field (must match up with '?' in query)
        //

        hRec = MsiCreateRecord(1);
        if (ERROR_SUCCESS == MsiRecordSetStream(hRec, 1, _T("c:\\temp\\data.bin")))
        {

            //
            // Execute view with record containing binary data value; commit database to save changes
            //

            if (ERROR_SUCCESS == MsiViewExecute(hView, hRec)
              && ERROR_SUCCESS == MsiViewClose(hView)
              && ERROR_SUCCESS == MsiDatabaseCommit(hDatabase))
            {
                //
                // New binary data successfully committed to the database
                //
            }
        }
    }
}

return 0;  
}
```



The following sample script adds binary data to a table.


```VB
Dim Installer
Dim Database
Dim View
Dim Record

Set Installer = CreateObject("WindowsInstaller.Installer")

Set Record = Installer.CreateRecord(1)
Record.SetStream 1, "c:\temp\data.bin"

Set Database = Installer.OpenDatabase("c:\temp\testdb.msi", msiOpenDatabaseModeTransact)
Set View = Database.OpenView("INSERT INTO `Binary` (`Name`, `Data`) VALUES ('NewBlob', ?)")
View.Execute Record
Database.Commit ' save changes
```



## Related topics

<dl> <dt>

[Working with Queries](working-with-queries.md)
</dt> <dt>

[SQL Syntax](sql-syntax.md)
</dt> <dt>

[Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md)
</dt> </dl>

 

 



