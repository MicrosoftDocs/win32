---
description: The installer supplies functions that manipulate the records in an installation database. These functions can be used in conjunction with the functions described in Working with Queries to make actual changes in a database.
ms.assetid: 5ea3fb1d-ddcb-4013-84dc-dd6f90c5751a
title: Working with Records
ms.topic: article
ms.date: 05/31/2018
---

# Working with Records

The installer supplies functions that manipulate the records in an installation database. These functions can be used in conjunction with the functions described in [Working with Queries](working-with-queries.md) to make actual changes in a database.

The following functions create or remove records:

-   To create a new record for a database, call the [**MsiCreateRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msicreaterecord) function.
-   To clear data from a record, set each field to null by calling the [**MsiRecordClearData**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordcleardata) function.

The following functions fill specified fields of records:

-   To set a record to an integer, call the [**MsiRecordSetInteger**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetinteger) function.
-   To set a record to a string, call the [**MsiRecordSetString**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstringa) function.
-   To insert an entire file into a stream field, call the [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) function.

The following functions read values from specified fields of records:

-   To read an integer value from a field, call the [**MsiRecordGetInteger**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordgetinteger) function.
-   To retrieve a string value, call the [**MsiRecordGetString**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordgetstringa) function.
-   To obtain a stream, call the [**MsiRecordReadStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordreadstream) function.
-   To determine if a particular field of a record is null, call the [**MsiRecordIsNull**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordisnull) function.

The following functions are informational record functions:

-   To get the number of fields a record contains, call the [**MsiRecordGetFieldCount**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordgetfieldcount) function.
-   To get the size of a field, call the [**MsiRecordDataSize**](/windows/desktop/api/Msiquery/nf-msiquery-msirecorddatasize) function. The return value of **MsiRecordDataSize** is sensitive to the field type.

 

 



