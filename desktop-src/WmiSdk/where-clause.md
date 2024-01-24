---
description: Use the WHERE clause to narrow the scope of a data, event, or schema query.
ms.assetid: b275f8e0-773d-422c-be21-b427e7a1fb6b
ms.tgt_platform: multiple
title: WHERE Clause (WMI)
ms.topic: article
ms.date: 05/31/2018
---

# WHERE Clause (WMI)

Use the WHERE clause to narrow the scope of a data, event, or schema query. For more information, see [Querying with WQL](querying-with-wql.md). The WHERE clause is made up of a property or keyword, an operator, and a constant. All WHERE clauses must specify one of the predefined operators that are included in the Windows Management Instrumentation (WMI) Query Language (WQL). You can append the WHERE clause to the SELECT statement using one of the following forms:


```sql
SELECT * FROM class WHERE property operator constant
SELECT * FROM class WHERE constant operator property
```



where \* is the item queried about, class is the class in which to query, and constant, operator, and property are the constant, operator, and property or keyword to use. For more information about the SELECT statement, see [SELECT Statement for Data Queries](select-statement-for-data-queries.md), [SELECT Statement for Event Queries](select-statement-for-event-queries.md), or [SELECT Statement for Schema Queries](select-statement-for-schema-queries.md).

The value of the constant must be of the correct type for the property. Moreover, the operator must be among the list of valid [WQL operators](wql-operators.md). Either a property name or a constant must appear on either side of the operator in the WHERE clause.

You may use string literals, such as "NTFS", in a WHERE clause. If you wish to include the following special characters in your string, you must first escape the character by prefixing the character with a backslash (\\):

-   backslash (\\\\)
-   double quotes (\\")
-   single quotes (\\')

Arbitrary arithmetic expressions cannot be used. For example, the following query returns only the instances of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class that represent NTFS drives:


```sql
SELECT * FROM Win32_LogicalDisk WHERE FileSystem = "NTFS"
```



Property names cannot appear on both sides of the operator. The following query is an example of an invalid query:


```sql
SELECT * FROM PhysicalDisk WHERE Partitions < (4 + 7 - 2) 
    OR   (Partitions = SectorsPerTrack / 7)
```



For most uses of class descriptors in a WHERE clause, WMI flags the query as invalid and returns an error. However, use the dot (.) operator for properties of type **object** in WMI. For example, the following query is valid if Prop is a valid property of MyClass and is type **object**:

``` syntax
SELECT * FROM MyClass WHERE Prop.embedprop = 5
```

Comparison tests are always case-insensitive. That is, the following three statements all evaluate to **TRUE**:


```sql
SELECT * FROM MyClass WHERE Prop1 = "cat"
SELECT * FROM MyClass WHERE Prop1 = "CAT"
SELECT * FROM MyClass WHERE Prop1 = "cAt"
```



You can construct a query that includes Boolean data types, but the only valid Boolean operand types are the =, != and <> types. The value **TRUE** is equivalent to the number 1, and the value **FALSE** is equivalent to the number 0. The following examples are of queries that compare a Boolean value against the values **TRUE** or **FALSE**.


```sql
SELECT * FROM MyClass WHERE BoolProp = 1
SELECT * FROM MyClass WHERE BoolProp = TRUE
SELECT * FROM MyClass WHERE BoolProp <> FALSE
SELECT * FROM MyClass WHERE BoolProp = 0
SELECT * FROM MyClass WHERE BoolProp = FALSE
SELECT * FROM MyClass WHERE BoolProp != 1
SELECT * FROM MyClass WHERE BoolProp != FALSE
SELECT * FROM MyClass WHERE BoolProp <> FALSE
```



The following examples are of invalid queries that attempt to use invalid operands.


```sql
SELECT * FROM MyClass WHERE BoolProp <= TRUE
SELECT * FROM MyClass WHERE BoolProp >= 0
SELECT * FROM MyClass WHERE BoolProp > FALSE
SELECT * FROM win32_computersystem WHERE infraredsupported >= null
```



Multiple groups of properties, operators, and constants can be combined in a WHERE clause using logical operators and parenthetical subexpressions. Each group must be joined with the AND, OR, or NOT [operators](wql-operators.md) as is shown in the following queries. The first query retrieves all instances of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class with the **Name** property set to either C or D:


```sql
SELECT * FROM Win32_LogicalDisk WHERE Name = "C:" OR Name = "D:"
```



The second query retrieves disks named "C:" or "D:" only if they have a certain amount of free space remaining and have NTFS file systems:


```sql
SELECT * FROM Win32_LogicalDisk WHERE (Name = "C:" OR Name = "D:") 
    AND  FreeSpace > 2000000  AND   FileSystem = "NTFS"
```



This example shows a schema query using the WHERE clause.


```sql
SELECT * FROM meta_class WHERE __this ISA "myClassName"
```



The class meta\_class identifies this as a schema query, the property called \_\_this identifies the target class of the query and the [ISA operator](isa-operator-for-schema-queries.md) requests definitions for the subclasses of the target class. Therefore, the preceding query returns the definition for the myClassName class and definitions for all of its subclasses.

The following example is a data query using the [ASSOCIATORS OF statement](associators-of-statement.md) with WHERE:


```sql
ASSOCIATORS OF {myClass.keyVal="Value1"} WHERE ClassDefsOnly
```



The next example shows a schema query using ASSOCIATORS OF and WHERE:


```sql
ASSOCIATORS OF {myClass} WHERE SchemaOnly
```



The following example is a data query using the [REFERENCES OF statement](references-of-statement.md) and WHERE:


```sql
REFERENCES OF {myClass.keyVal="Value1"} 
    WHERE RequiredQualifier = myQual
```



This last example is a schema query using REFERENCES OF and WHERE:


```sql
REFERENCES OF {myClass} WHERE SchemaOnly
```



In addition to the WMI [DATETIME](date-and-time-format.md) format, the WQL WHERE clause supports several other date and time formats:

-   [WQL-Supported Date Formats](wql-supported-date-formats.md)
-   [WQL-Supported Time Formats](wql-supported-time-formats.md)

 

 
