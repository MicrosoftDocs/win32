---
description: 'The following shows the basic syntax of the SELECT statement for a local query:'
ms.assetid: 334aa2b9-0ef2-4a4b-9352-de5ded95afa6
title: SELECT Statement
ms.topic: article
ms.date: 05/31/2018
---

# SELECT Statement

The following shows the basic syntax of the SELECT statement for a local query:


```
SELECT [TOP <positive integer>] <columns>
FROM [machinename.]SystemIndex
[WHERE <conditions>]
[ORDER BY <column>] 
            
```



The following shows the column portion of the SELECT statement syntax:


```
SELECT [TOP <positive integer>] <column> [ {, <column>} ...]
```



The column specifier(s) must be valid property name columns, separated by commas. Valid column names are registered property descriptions or are defined by the Shell's Property System Schema. You can select only those columns that are marked as retrievable in the Property System Schema. If you use mixed case to identify properties that are not system-defined properties, you must enclose the column specifier in double quotation marks. System-defined property names include all properties beginning with "System" (for example, System.Contact.FirstName) and do not require quotation marks.

> [!Note]  
> You can also enclose system-defined property names in double quotation marks for readability. This does not affect compatibility.

 

When the query returns a document that does not have the requested column, the value of that column for the document is **NULL**.

You must provide at least one column name in a SELECT statement. In the Structured Query Language (SQL) query, you are allowed to use the asterisk (\*) to specify that all columns in a table are to be returned. However, no defined and fixed set of properties applies to all documents. For this reason, the SQL asterisk is not permitted in the <columns> specifier of the SELECT statement.

## Getting the Top n Results

You can specify a maximum number of results to return by using the TOP syntax:


```
SELECT TOP <positive integer> <column> [ {, <column>} ...]
```



## Casting Column Data Types

At times, you might need to cast string data extracted from documents as another data type so that an appropriate comparison can be made. For more information, refer to [Casting the Data Type of a Column](-search-sql-castingdatacolumntype.md).

## Examples

The following examples return the name and URL of matching documents.


```
SELECT System.ItemName, System.ItemUrl FROM SystemIndex WHERE CONTAINS('Microsoft')

SELECT TOP 10 System.ItemName, System.ItemUrl FROM SystemIndex WHERE CONTAINS('Microsoft') 
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Casting the Data Type of a Column](-search-sql-castingdatacolumntype.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[System Properties](https://msdn.microsoft.com/library/bb763010(VS.85).aspx)
</dt> </dl>

 

 



