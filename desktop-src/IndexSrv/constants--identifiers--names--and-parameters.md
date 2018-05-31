---
title: Constants, Identifiers, Names, and Parameters
description: Constants, Identifiers, Names, and Parameters
ms.assetid: 2fe47b7d-92ef-49d8-87d7-5e43beb8365f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants, Identifiers, Names, and Parameters

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Note that names in the name operators that contain special characters do not need to be quoted (unlike names in SQL statements). If a name in an operator is quoted, these quotes are part of the name.

The following list describes the operators for constants, identifiers, names, and parameters.

<dl> <dt>

<span id="DBOP_scalar_constant_"></span><span id="dbop_scalar_constant_"></span><span id="DBOP_SCALAR_CONSTANT_"></span>DBOP\_scalar\_constant 
</dt> <dd>

Represents a scalar constant whose value can use any element of the value union of the [**DBCOMMANDTREE**](dbcommandtree.md) structure. A scalar value can be of any OLE DB type. This node has no inputs. The result type is the type of the scalar value represented by the node.

</dd> <dt>

<span id="DBOP_DEFAULT__DBOP_NULL"></span><span id="dbop_default__dbop_null"></span>DBOP\_DEFAULT, DBOP\_NULL
</dt> <dd>

SQL's "DEFAULT" and "NULL" value indicators. There are no inputs. The result type can be any type of scalar.

</dd> <dt>

<span id="DBOP_bookmark_name"></span><span id="dbop_bookmark_name"></span><span id="DBOP_BOOKMARK_NAME"></span>DBOP\_bookmark\_name
</dt> <dd>

Represents the bookmark column of a table (for example, SELECT T.\*, T.bookmark FROM T). It takes one optional input, a DBOP\_table\_name, to which the bookmark belongs. A string representing the name of the column can optionally be assigned in the **pwszValue** member of [**DBCOMMANDTREE**](dbcommandtree.md).

</dd> <dt>

<span id="DBOP_catalog_name__DBOP_column_name"></span><span id="dbop_catalog_name__dbop_column_name"></span><span id="DBOP_CATALOG_NAME__DBOP_COLUMN_NAME"></span>DBOP\_catalog\_name, DBOP\_column\_name
</dt> <dd>

Represent the name of a catalog and column, respectively. These nodes have no inputs. A name may be specified by a **pwszValue** member that is not a null pointer, by a [**DBID**](dbid.md) structure, or by a moniker in the node's value field. For column names, the column may be denoted as an unsigned integer value (for example, SELECT A, B FROM T ORDER BY 2).

</dd> <dt>

<span id="DBOP_schema_name"></span><span id="dbop_schema_name"></span><span id="DBOP_SCHEMA_NAME"></span>DBOP\_schema\_name
</dt> <dd>

Represents the name of a schema. A name may be specified by a **pwszValue** member that is not a null pointer, by a [**DBID**](dbid.md) structure, or by a moniker in the node's value field. A schema name node has an optional input DBOP\_catalog\_name node.

</dd> <dt>

<span id="DBOP_outall_name"></span><span id="dbop_outall_name"></span><span id="DBOP_OUTALL_NAME"></span>DBOP\_outall\_name
</dt> <dd>

Specifies that all input columns (for example, SQL's "SELECT \*") must be output. This node has no inputs contains contains no other [**DBCOMMANDTREE**](dbcommandtree.md) value. DBOP\_outall\_name is used as an input to the DBOP\_project\_list\_element node, but not to the set\_list\_element, sort\_list\_element, column\_list\_element or from\_list\_element nodes.

</dd> <dt>

<span id="DBOP_qualifier_name"></span><span id="dbop_qualifier_name"></span><span id="DBOP_QUALIFIER_NAME"></span>DBOP\_qualifier\_name
</dt> <dd>

Specifies all columns in a table (for example, SQL's "table.\*"). This node has no inputs. The table name is represented by a **pwszValue** member that is not a null pointer. DBOP\_qualifier\_name is used as an input to the DBOP\_project\_list\_element node, but not to the set\_list\_element, sort\_list\_element, column\_list\_element or from\_list\_element nodes.

</dd> <dt>

<span id="DBOP_qualified_column_name"></span><span id="dbop_qualified_column_name"></span><span id="DBOP_QUALIFIED_COLUMN_NAME"></span>DBOP\_qualified\_column\_name
</dt> <dd>

Represents a column name. It takes two inputs: a DBOP\_table\_name, and a DBOP\_column\_name, in that order. It contains no other [**DBCOMMANDTREE**](dbcommandtree.md) value.

</dd> <dt>

<span id="DBOP_table_name"></span><span id="dbop_table_name"></span><span id="DBOP_TABLE_NAME"></span>DBOP\_table\_name
</dt> <dd>

Represents a table name, possibly in another catalog or schema. A table name may be specified by a **pwszValue** member that is not a null pointer, by a [**DBID**](dbid.md) structure, or by a moniker in the value field of the node. This node takes an optional input: DBOP\_schema\_name.

</dd> <dt>

<span id="DBOP_nested_table_name"></span><span id="dbop_nested_table_name"></span><span id="DBOP_NESTED_TABLE_NAME"></span>DBOP\_nested\_table name
</dt> <dd>

Represents a nested table name. A nested table is a table containing at least one chaptered column. The component of the nested name is stored as a **pwszValue** member that is not a null pointer, by a [**DBID**](dbid.md) structure, or by a moniker in the value field of the node. This node takes a DBOP\_nested\_table\_name or a DBOP\_table\_name input. For example, the nested table "Customers.Orders" with chapter "Detail" is represented as follows:


```
        DBOP_nested_table_name (pwsz = "Detail")
            |
    DBOP_nested_table_name (pwsz = "Orders" )
        |
DBOP_table_name (pwsz = "Customers")
```



</dd> <dt>

<span id="DBOP_nested_column_name"></span><span id="dbop_nested_column_name"></span><span id="DBOP_NESTED_COLUMN_NAME"></span>DBOP\_nested\_column\_name
</dt> <dd>

Specifies a column in a nested table. This node takes one DBOP\_nested\_table\_name and a DBOP\_column\_name as inputs, in that order.

</dd> </dl>

 

 




