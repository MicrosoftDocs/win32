---
description: Microsoft Windows Search query language is based on Structured Query Language (SQL); however, it does not search in a relational database with user-defined tables or indexes.
ms.assetid: e81c436e-3a33-4b00-9860-9a54bc0eebbf
title: SQL Features Unavailable in Microsoft Windows Search
ms.topic: article
ms.date: 05/31/2018
---

# SQL Features Unavailable in Microsoft Windows Search

Microsoft Windows Search query language is based on Structured Query Language (SQL); however, it does not search in a relational database with user-defined tables or indexes. Because of this, many standard SQL statements and syntax features do not apply. The following is a list of the more significant SQL features that are not supported in Windows Search.


-   BATCH statements
-   COALESCE\_TABLE function
-   CONVERT function (use the CAST functions instead)
-   CREATE VIEW statement
-   Data definition language
-   DATASOURCE statement
-   Date and Time formats other than ISO date and time stamp
-   DELETE statement
-   GRANT statement
-   Information schema
-   INSERT statement
-   OLE DB data types
-   SQL-standard regular expressions (use CONTAINS or LIKE instead)
-   Parameters to SQL queries
-   Relational column comparison
-   Revision ID header
-   REVOKE statement
-   SCOPE aliases or revision numbers
-   SELECT ALL (removes duplicates automatically)
-   Stored procedures
-   Structured document expansion
-   UNION ALL
-   UNKNOWN keyword
-   UPDATE statement

Windows Search does not support Thesaurus and Noise Words.

 

 



