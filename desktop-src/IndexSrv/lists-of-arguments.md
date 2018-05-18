---
title: Lists of Arguments
description: Lists of Arguments
ms.assetid: '24c8cb0a-3a69-4d05-b571-fd77b688acb8'
---

# Lists of Arguments

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes operators with lists of arguments. An empty list is denoted by the corresponding anchor node with no element nodes.

<dl> <dt>

<span id="DBOP_column_list_anchor__DBOP_column_list_element"></span><span id="dbop_column_list_anchor__dbop_column_list_element"></span><span id="DBOP_COLUMN_LIST_ANCHOR__DBOP_COLUMN_LIST_ELEMENT"></span>DBOP\_column\_list\_anchor, DBOP\_column\_list\_element
</dt> <dd>

These operators are used to define a list of column aliases (see DBOP\_alias). Each element represents the name alias as a string value in the **pwszValue** field of the command node. Elements take no inputs.

</dd> <dt>

<span id="DBOP_command_list_anchor__DBOP_command_list_element"></span><span id="dbop_command_list_anchor__dbop_command_list_element"></span><span id="DBOP_COMMAND_LIST_ANCHOR__DBOP_COMMAND_LIST_ELEMENT"></span>DBOP\_command\_list\_anchor, DBOP\_command\_list\_element
</dt> <dd>

These operators are used to define a sequence of OLE DB commands. Each element takes one command tree input representing either a data manipulation language (DML) or data definition language (DDL) command.

</dd> <dt>

<span id="DBOP_from_list_anchor__DBOP_from_list_element"></span><span id="dbop_from_list_anchor__dbop_from_list_element"></span><span id="DBOP_FROM_LIST_ANCHOR__DBOP_FROM_LIST_ELEMENT"></span>DBOP\_from\_list\_anchor, DBOP\_from\_list\_element
</dt> <dd>

The list of tables in a SQL FROM clause. Each element requires a table-valued expression as input, which can be represented by a table\_name or alias to serve as a SQL "correlation name."

</dd> <dt>

<span id="DBOP_project_list_anchor__DBOP_project_list_element"></span><span id="dbop_project_list_anchor__dbop_project_list_element"></span><span id="DBOP_PROJECT_LIST_ANCHOR__DBOP_PROJECT_LIST_ELEMENT"></span>DBOP\_project\_list\_anchor, DBOP\_project\_list\_element
</dt> <dd>

The anchor and an element in a list of columns for a projection. The anchor has an element as its first child, but no other information. Each element assigns a column name, which is stored in the string portion of the tree node, to a scalar expression, which is given as the element node's input tree. In addition, outall\_name and qualifier\_name must be in the project\_list of a project node (as opposed to a project\_list of an aggregate node). If a project list includes the member outall\_name and a column\_name that is a member of the columns implied by outall\_name, then that column will appear twice in the result.

</dd> <dt>

<span id="DBOP_row_list_anchor__DBOP_row_list_element"></span><span id="dbop_row_list_anchor__dbop_row_list_element"></span><span id="DBOP_ROW_LIST_ANCHOR__DBOP_ROW_LIST_ELEMENT"></span>DBOP\_row\_list\_anchor, DBOP\_row\_list\_element
</dt> <dd>

The anchor and element in a list of rows for constructing a table. Each element has one DBOP\_row input. At least one row\_list\_element must be in each list.

</dd> <dt>

<span id="DBOP_scalar_list_anchor__DBOP_scalar_list_element"></span><span id="dbop_scalar_list_anchor__dbop_scalar_list_element"></span><span id="DBOP_SCALAR_LIST_ANCHOR__DBOP_SCALAR_LIST_ELEMENT"></span>DBOP\_scalar\_list\_anchor, DBOP\_scalar\_list\_element
</dt> <dd>

The anchor and element in a list of scalar constants for constructing a row. Each element takes one DBOP\_scalar\_constant as input. At least one scalar list element must be in each list.

</dd> <dt>

<span id="DBOP_set_list_anchor__DBOP_set_list_element"></span><span id="dbop_set_list_anchor__dbop_set_list_element"></span><span id="DBOP_SET_LIST_ANCHOR__DBOP_SET_LIST_ELEMENT"></span>DBOP\_set\_list\_anchor, DBOP\_set\_list\_element
</dt> <dd>

The anchor and element in a list of columns for updating. Each element has two inputs, one a column name and one an expression of the same type as the column. At least one set\_list\_element must be in each list.

</dd> <dt>

<span id="DBOP_sort_list_anchor__DBOP_sort_list_element"></span><span id="dbop_sort_list_anchor__dbop_sort_list_element"></span><span id="DBOP_SORT_LIST_ANCHOR__DBOP_SORT_LIST_ELEMENT"></span>DBOP\_sort\_list\_anchor, DBOP\_sort\_list\_element
</dt> <dd>

The anchor and an element in a list of columns for sorting. This list is different from a projection list in that no new column name is assigned but an ascending or descending flag and an optional locale ID are indicated. Each element includes a scalar input expression.

</dd> </dl>

 

 




