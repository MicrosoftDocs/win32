---
title: Constructors and Coercion Operators
description: Constructors and Coercion Operators
ms.assetid: 5637a576-fe51-4ca8-9132-a788f2300dd9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constructors and Coercion Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for constructors and coercion.

<dl> <dt>

<span id="DBOP_row"></span><span id="dbop_row"></span><span id="DBOP_ROW"></span>DBOP\_row
</dt> <dd>

Constructs a row from a list of scalar values. Similar to SQL-92's row-value constructor from column values or literals, as in "(t.a, t.b, t.c) &lt; VALUES (2, 3, 5)." It takes a scalar\_list\_anchor as input and produces a single row.

</dd> <dt>

<span id="DBOP_table"></span><span id="dbop_table"></span><span id="DBOP_TABLE"></span>DBOP\_table
</dt> <dd>

Constructs a table from a list of union-compatible row constructors. It takes a row\_list\_anchor as input and produces a table.

</dd> <dt>

<span id="DBOP_sort"></span><span id="dbop_sort"></span><span id="DBOP_SORT"></span>DBOP\_sort
</dt> <dd>

Sorts a table in increasing or decreasing order according to a list of columns or expressions over its columns. A DBOP\_sort has two required child nodes. The first child represents the input table to be sorted. The second child is a DBOP\_sort\_list\_anchor node representing the list of sort keys. Each element of the sort\_list, specified by a sort\_list\_element, contains the order of sort in the [**DBSORTINFO**](dbsortinfo.md) member, and points to the column name or expression on which to sort. This operator produces an ordered table. If the input to sort is a unique table, it produces an ordered-unique table. If the input to sort is a hierarchical table, the sort operator applies only to the root rowset in that table. That is, the list of columns on which to sort should reference only non-chaptered columns of the root rowset; otherwise, the sort specification is invalid. The output of sort in this case is a hierarchical table with the rows in the root rowset ordered. For example: Let T1-&gt;T2-&gt;T3 be a hierarchical rowset, where the columns of each rowset are T1(A,B,C,X), T2(D,E,F,Y), and T3(G,H), assume X, and Y represent the chaptered columns of T1 and T2, respectively. Assume DBOP\_sort specifies a list W of columns on which to sort. W must reference only subsets of {A,B,C}.

</dd> <dt>

<span id="DBOP_distinct__DBOP_distinct_order_preserving"></span><span id="dbop_distinct__dbop_distinct_order_preserving"></span><span id="DBOP_DISTINCT__DBOP_DISTINCT_ORDER_PRESERVING"></span>DBOP\_distinct, DBOP\_distinct\_order\_preserving
</dt> <dd>

These operators remove duplicate rows from a table. The DBOP\_distinct operator takes a table as input and produces a unique table. The DBOP\_distinct\_order\_preserving operator takes an ordered or unordered table as input and produces a unique table maintaining the row order of the input table. If the input table is ordered, then the output is an ordered unique table.

</dd> </dl>

 

 




