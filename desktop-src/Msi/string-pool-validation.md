---
description: The Windows Installer stores all database strings in a single shared string pool to reduce the size of the database and to improve performance.
ms.assetid: b627f3da-3545-4c1a-85b0-d8845fdac621
title: String-Pool Validation
ms.topic: article
ms.date: 05/31/2018
---

# String-Pool Validation

The Windows Installer stores all database strings in a single shared string pool to reduce the size of the database and to improve performance. The only means of validating the string pool is to use the MsiInfo tool found in the Windows Installer SDK.

String pool verification consists of two main checks:

-   [DBCS string tests](#dbcs-string-tests)
-   [Reference count verification](#reference-count-verification)

## DBCS String Tests

The DBCS string tests scan each string in the database for two criteria: For packages with a neutral code page marked, if any character is an extended character (greater than 127), the string is flagged and a message is displayed saying that the code page of the database is invalid because these characters require a specific code page to be rendered consistently on all systems.

If the database has a code page, each string is scanned for an invalid DBCS indicator. If a non-neutral string has been improperly marked, the characters will not render correctly. (This is most commonly caused by forcing the code page to a particular value using the \_ForceCodepage table with non-neutral strings already in the database.) Note that this check requires that the code page of the database be installed on the system.

If there is a code page problem, the user may fix the error by using the \_ForceCodepage table to force the code page of the database to the appropriate value. For more information, see [Code Page Handling](code-page-handling-windows-installer-.md).

## Reference Count Verification

To verify the reference counts of all strings, every table is scanned for string values, a count of each distinct string is kept, and the result is compared to the stored reference count in the database string pool.

If there is a string reference count problem, the user should immediately export each table of the database using [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta), create a new database, and import the tables into the new database using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). The new database then has the same content as the old database, but the string reference counts are correct. Adding or deleting data from a database with a corrupt string pool can increase corruption of the database and loss of data, so taking these steps quickly is important to prevent further data loss.

When rebuilding databases, remember to embed any necessary storages and streams in the new database (see [\_Streams Table](-streams-table.md) and [\_Storages Table](-storages-table.md)) and be aware of code page issues. Also remember to set each of the necessary [Summary Information Stream](summary-information-stream.md) properties.

 

 



