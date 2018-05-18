---
title: Update Operators
description: Update Operators
ms.assetid: 'ea0dccd8-d519-4727-a922-d0bab9ffe04c'
---

# Update Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the update operators.

<dl> <dt>

<span id="DBOP_delete"></span><span id="dbop_delete"></span><span id="DBOP_DELETE"></span>DBOP\_delete
</dt> <dd>

Removes rows from a table. This operator takes two inputs ? one required and one optional The required input is a DBOP\_table\_name node describing the table being updated. The optional input is a table-valued expression representing the rows to be deleted. If the optional input is not provided, all rows of the table specified in the first required input are deleted. The requirement as to whether the input table being updated must be a base table is provider specific.

</dd> <dt>

<span id="DBOP_update"></span><span id="dbop_update"></span><span id="DBOP_UPDATE"></span>DBOP\_update
</dt> <dd>

Modifies the values of one or more columns in rows, from a table, that satisfy a condition. This operator takes two required inputs. The first is a table-valued expression describing the set of rows being updated. The second is a DBOP\_set\_list\_anchor node containing the update expressions (for example, SET A = A + 1, B = B - 5). The column names represented in the DBOP\_set\_list\_elements must be unambiguous. That is, in cases where the tuples to be updated are defined by a join expression over multiple tables, and a column being updated appears in more than one table, the reference to the updated column must be fully qualified (DBOP\_qualified\_column\_name). For example, the update statement

`UPDATE A INNER JOIN B ON A.F1=B.F1 SET A.X = 1, B.Y = 2 WHERE A.Z =10`

is represented by an update node whose first input is a subtree representing the expression

`A INNER JOIN B ON A.F1=B.F1 AND A.Z = 10`

and the second input is a DBOP\_set\_list\_anchor containing two list elements for A.X = 1, and B.Y = 2. The requirement as to whether the input table being updated must be a base table is provider specific.

</dd> <dt>

<span id="DBOP_insert"></span><span id="dbop_insert"></span><span id="DBOP_INSERT"></span>DBOP\_insert
</dt> <dd>

Adds rows to a table. This operator specifies three arguments: one required row\_constructor or table\_constructor, one required table, and one required column\_list. The number of elements of column\_list must match the number of values in the constructed row(s). Columns not listed in the column\_list must have default values or be capable of containing NULL values. Requirements as to whether table input must be a base table are provider specific.

</dd> </dl>

 

 




