---
description: Describes WQL operators used in the WHERE clause or the SELECT statement.
ms.assetid: a62de66d-d5ba-49a1-8262-bfa10ac2db75
ms.tgt_platform: multiple
title: WQL Operators
ms.topic: article
ms.date: 05/31/2018
---

# WQL Operators

The Windows Management Instrumentation Query Language (WQL) supports a set of standard operators that are used in the [WHERE clause](where-clause.md) of a SELECT statement, as follows.



| Operator       | Description              |
|----------------|--------------------------|
| =              | Equal to                 |
| <           | Less than                |
| >           | Greater than             |
| <=          | Less than or equal to    |
| >=          | Greater than or equal to |
| != or <> | Not equal to             |



 

There are a few additional WQL-specific operators: IS, IS NOT, ISA, and LIKE. The IS and IS NOT operators are valid in the WHERE clause only if the constant is **NULL**. For example, the following queries are valid:


```sql
SELECT * FROM Win32_LogicalDisk WHERE FileSystem IS NULL
SELECT * FROM Win32_LogicalDisk WHERE FileSystem IS NOT NULL
```



The following queries show invalid uses of IS and IS NOT:


```sql
SELECT * FROM Win32_LogicalDisk WHERE DriveType IS 5
SELECT * FROM Win32_LogicalDisk WHERE FileSystem IS NOT "NTFS"
```



The ISA operator is used in the WHERE clause of data and event queries to test embedded objects for a class hierarchy. The ISA operator eliminates the need for keeping track of newly derived classes when requesting a hierarchy of classes. When you use ISA, newly created and existing subclasses of the requested class are automatically included in the result set.

For more information about the syntax and use of this operator, see the following topics:

-   [ISA Operator for Data Queries](isa-operator-for-data-queries.md)
-   [ISA Operator for Event Queries](isa-operator-for-event-queries.md)
-   [ISA Operator for Schema Queries](isa-operator-for-schema-queries.md)

The LIKE operator is valid in the WHERE clause and is used to determine whether a given character string matches a specified pattern. For example, the following query returns all instances of Win32\_ classes.


```sql
SELECT * FROM Meta_Class WHERE __Class LIKE "%Win32%"
```



For more information about the syntax and use of this operator, see [LIKE Operator](like-operator.md).

 

 



