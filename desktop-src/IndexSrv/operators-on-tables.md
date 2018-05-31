---
title: Operators on Tables
description: Operators on Tables
ms.assetid: 595ab22b-2f4a-4873-9728-40be75f22c19
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Operators on Tables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for tables.

<dl> <dt>

<span id="DBOP_alias"></span><span id="dbop_alias"></span><span id="DBOP_ALIAS"></span>DBOP\_alias
</dt> <dd>

The alias facilities for a table. DBOP\_alias takes one mandatory input and one optional input. The first is a table-valued subtree, often a table\_name operator, representing the table being aliased. The alias name for the table is provided in the **pwszValue** member of the DBOP\_alias [**DBCOMMANDTREE**](dbcommandtree.md) structure. A second optional input is a column\_list\_anchor containing column elements representing aliases to be assigned to the columns of the input table. SQL examples: "SELECT a.\* FROM table AS a" and "SELECT x, z FROM table AS a (x, y, z)." The output table is of the same table type as the input table. The new name(s) replaces the old name(s) for the output of this operator. If the second input is provided, the size of the column\_list must be the same as the number of columns in the first input.

</dd> <dt>

<span id="DBOP_cross_join"></span><span id="dbop_cross_join"></span><span id="DBOP_CROSS_JOIN"></span>DBOP\_cross\_join
</dt> <dd>

Represents the Cartesian product of two tables; that is, ANSI-standard CROSS JOIN clause of SQL. This operator takes two tables, T1 and T2, as input and produces a table R. The columns of R are all the columns of T1 and T2. Let t1, t2, and r denote a row in T1, T2, and R, respectively. Let r\[Ti\] denote the projection of row r on the columns of Ti, i=1,2. Each row r in R is formed by taking each row t1 in T1 and concatenating it with each row t2 in T2, so that r\[T1\]=t1 and r\[T2\]=t2. The cardinality of R is the product of the cardinalities of T1 and T2. R is a unique table if both T1 and T2 are unique tables; otherwise, it is a table.

</dd> <dt>

<span id="DBOP_union_join"></span><span id="dbop_union_join"></span><span id="DBOP_UNION_JOIN"></span>DBOP\_union\_join
</dt> <dd>

Represents the UNION join of SQL. This operator takes two tables T1 and T2 as input and produces a table R. The columns of R are all the columns of T1 and T2. Let ti\_null denote a row of Ti, i=1,2, containing NULL values in every column. Each row r in R is formed by taking every row from T1 and T2 as follows: (a) r\[T1\]= t in T1 and r\[T2\] = t2\_null, or (b) r\[T1\] = t1\_null, and r\[T2\] = t in T2. The cardinality of R is the sum of the cardinalities of T1 and T2.

The output is a unique table if both inputs are unique tables; otherwise, it is a table.

</dd> <dt>

<span id="DBOP_inner_join__DBOP_left_semi_join__DBOP_right_semi_join__DBOP_left_anti_semi_join__DBOP_right_anti_semi_join__DBOP_left_outer_join__DBOP_right_outer_join__DBOP_full_outer_join"></span><span id="dbop_inner_join__dbop_left_semi_join__dbop_right_semi_join__dbop_left_anti_semi_join__dbop_right_anti_semi_join__dbop_left_outer_join__dbop_right_outer_join__dbop_full_outer_join"></span><span id="DBOP_INNER_JOIN__DBOP_LEFT_SEMI_JOIN__DBOP_RIGHT_SEMI_JOIN__DBOP_LEFT_ANTI_SEMI_JOIN__DBOP_RIGHT_ANTI_SEMI_JOIN__DBOP_LEFT_OUTER_JOIN__DBOP_RIGHT_OUTER_JOIN__DBOP_FULL_OUTER_JOIN"></span>DBOP\_inner\_join, DBOP\_left\_semi\_join, DBOP\_right\_semi\_join, DBOP\_left\_anti\_semi\_join, DBOP\_right\_anti\_semi\_join, DBOP\_left\_outer\_join, DBOP\_right\_outer\_join, DBOP\_full\_outer\_join
</dt> <dd>

All join operators take two required table inputs, T1 and T2, and produce a table R as output. A third required input is a Boolean-valued expression specifying the join condition (that is, the ON or WHERE clause of SQL). The columns of R are specified as follows:

-   For inner\_join and all outer\_joins, the columns of R are all the columns of T1 and T2, in that order;
-   For left\_semi\_join and left\_anti\_semi\_join, the columns of R are the columns of T1; and
-   For right\_semi\_join and right\_anti\_semi\_join, the columns of R are the columns of T2.

The rows in R are specified as follows:

-   For inner\_join, R contains the subset of rows from the Cartesian product of T1 and T2. The subset satisfies the join condition. If the join condition is the predicate TRUE or a tautology (for example, 5 = 5), then R is exactly the Cartesian product of T1 and T2.
-   For left\_semi\_join, R contains all rows of T1 that have a matching row in T2 satisfying the join condition. If the join condition is always TRUE, then R contains the same rows as T1. If the join condition is always FALSE, then R is empty.
-   For left\_anti\_semi\_join, R contains all rows of T1 that do not have a matching row in T2 satisfying the join condition. If the join condition is always TRUE, then R is empty. If the join condition is always FALSE, then R contains the same rows as T1.
-   For right\_semi\_join, R contains all rows in T2 that have a matching row in T1 satisfying the join condition. If the join condition is always TRUE, then R contains the same rows as T2. If the join condition is always FALSE, then R is empty.
-   For right\_anti\_semi\_join, R contains all rows in T2 that do not have a matching row in T1 satisfying the join condition. If the join condition is always TRUE, then R is empty. If the join condition is always FALSE, then R contains the same rows as T2.
-   For left\_outer\_join, R contains all tuple data objects in the inner\_join of T1 and T2, and all tuples in the left\_anti\_semi\_join of T1 and T2 concatenated with t2\_null;
-   For right\_outer\_join, R contains all tuples in the inner\_join of T1 and T2, and all tuples in the right\_anti\_semi\_join of T1 and T2 concatenated with t1\_null.
-   For full\_outer\_join, R contains all tuples in the inner\_join of T1 and T2, all tuples in the left\_anti\_semi\_join of T1 and T2 concatenated with t2\_null, and all tuples in the right\_anti\_semi\_join of T1 and T2 concatenated with t1\_null.

In general, the output R is a table; it is a unique table in the three following cases:

-   For inner\_join and all outer joins, if both inputs are unique tables.
-   For left\_semi\_join and left\_anti\_semi\_join, if the left input is a unique table.
-   For right\_semi\_join and right\_anti\_semi\_join, if the right input is a unique table.

</dd> <dt>

<span id="DBOP_natural_join__DBOP_natural_left_outer_join__DBOP_natural_right_outer_join__DBOP_natural_full_outer_join"></span><span id="dbop_natural_join__dbop_natural_left_outer_join__dbop_natural_right_outer_join__dbop_natural_full_outer_join"></span><span id="DBOP_NATURAL_JOIN__DBOP_NATURAL_LEFT_OUTER_JOIN__DBOP_NATURAL_RIGHT_OUTER_JOIN__DBOP_NATURAL_FULL_OUTER_JOIN"></span>DBOP\_natural\_join, DBOP\_natural\_left\_outer\_join, DBOP\_natural\_right\_outer\_join, DBOP\_natural\_full\_outer\_join
</dt> <dd>

All natural join operators take two required table inputs, T1 and T2, and produce a table R as output. A third optional input is a column\_list node type that specifies the columns on which to test the join predicate (such as the USING clause of SQL). Natural joins are different from the join operations described above in that they have an implicit projection and an implicit join condition. Let CC represent the columns that are common to both T1 and T2, T1C represent the columns of T1 not in CC, and T2C represent the columns of T2 not in CC. The columns of R are T1C, CC, and T2C. Producing the set of columns CC only once in R represents the implied projection. The implied join condition is the conjunction of terms T1.Ci = T2.Ci, for every Ci in CC. If the column\_list input of these operators is included, then the join condition is restricted to the terms involving only the columns in the column list, which can only reference columns in CC. Other than the implied projection and join condition, the semantics of the natural join operators are exactly the same as their non-natural counterparts. That is, the cardinality of R is the cardinality of the non-natural join operators. If CC is the empty set, then the implied join predicate is TRUE and R contains the cross join of T1 and T2.

</dd> <dt>

<span id="DBOP_set_intersection__DBOP_set_union__DBOP_set_left_difference__DBOP_set_right_difference__DBOP_set_anti_difference"></span><span id="dbop_set_intersection__dbop_set_union__dbop_set_left_difference__dbop_set_right_difference__dbop_set_anti_difference"></span><span id="DBOP_SET_INTERSECTION__DBOP_SET_UNION__DBOP_SET_LEFT_DIFFERENCE__DBOP_SET_RIGHT_DIFFERENCE__DBOP_SET_ANTI_DIFFERENCE"></span>DBOP\_set\_intersection, DBOP\_set\_union, DBOP\_set\_left\_difference, DBOP\_set\_right\_difference, DBOP\_set\_anti\_difference
</dt> <dd>

Set operations, requiring "union compatible" input tables. These operators take two required inputs, T1 and T2, and produce a result table R. Let A1, A2,..., An denote the columns of T1, and B1, B2,..., Bm denote the columns of T2. T1 and T2 are union compatible if: n = m, and the types of Ai and Bi, I = 1,..,n, are compatible. The rules determining when the types of two columns are compatible and what the type of the resulting columns will be are provider-specific. If Ai, Bi, have the same name, that name is propagated to the output; otherwise, the resulting name is provider-specific. Left-difference is the usual difference operator; right-difference is the opposite (T1 right-difference T2 == T2 left-difference T1). The anti-difference is the union of the left- and right-differences. For SQL's "union corresponding," the tree node requires a third optional input, which must be a non-empty column\_list\_anchor. If the third input is present, the input tables are projected on the columns named in that list before the set operation proceeds. If the third input is not included and the Boolean **fValue** member [**DBCOMMANDTREE**](dbcommandtree.md) node is set to TRUE, then the command processor decides the maximal set of columns from the two inputs that are union-compatible (and should therefore be preserved). The output is a unique table.

</dd> <dt>

<span id="DBOP_bag_intersection__DBOP_bag_union__DBOP_bag_left_difference__DBOP_bag_right_difference__DBOP_bag_anti_difference"></span><span id="dbop_bag_intersection__dbop_bag_union__dbop_bag_left_difference__dbop_bag_right_difference__dbop_bag_anti_difference"></span><span id="DBOP_BAG_INTERSECTION__DBOP_BAG_UNION__DBOP_BAG_LEFT_DIFFERENCE__DBOP_BAG_RIGHT_DIFFERENCE__DBOP_BAG_ANTI_DIFFERENCE"></span>DBOP\_bag\_intersection, DBOP\_bag\_union, DBOP\_bag\_left\_difference, DBOP\_bag\_right\_difference, DBOP\_bag\_anti\_difference
</dt> <dd>

Multi-set (bag) operations, requiring "union-compatible" input tables. The number of occurrences of a row in the output table is the minimum (intersection), sum (union), or difference, respectively, of the number of occurrences of that row in the two input tables. Variants are the same as those for set operations. DBOP\_bag\_union represents SQL's UNION ALL operator. These operations require two or more table inputs; the output is a table.

Given table A with two occurrences of row X and table B with one occurrence of row X, then:

-   (A bag\_intersection B) will contain one (min(2,1)) occurrence of row X;
-   (A bag\_union B) will contain three (2+1) occurrences of row X;
-   (A bag\_left\_difference B) will contain one (2-1) occurrence of row X;
-   (A bag\_right\_difference B) will contain zero occurrences of row X, since 1-2 is a negative number.
-   (A bag\_anti\_difference B) will contain one (1+0) occurrence of row X corresponding to the bag\_union of the bag\_left\_difference and bag\_right\_difference.

</dd> <dt>

<span id="DBOP_division"></span><span id="dbop_division"></span><span id="DBOP_DIVISION"></span>DBOP\_division
</dt> <dd>

Represents the relational division operator. This operator takes two required table inputs, T1 and T2, and produces a unique table R as result. The first input, T1, is the dividend table; the second input, T2, is the divisor table. The set of columns of T2 must be a subset of the columns of T1. Let CC be the columns that are common to T1 and T2, and T1C be the columns in T1 not in T2. Table R has all the columns in T1C. Let t1 denote a row in T1 and t2 a row in T2. The result R contains the set of rows r such that for every row t1 in T1, there is a row t2 in T2 with r = t1\[T1C\] and t1\[T2\] = t2.

</dd> <dt>

<span id="DBOP_relative_sampling"></span><span id="dbop_relative_sampling"></span><span id="DBOP_RELATIVE_SAMPLING"></span>DBOP\_relative\_sampling
</dt> <dd>

A random sampling of rows from a table based on a reduction factor (given as a percentage, which must be an integer between 0 and 100). Randomness is guaranteed only to the ability of the provider to generate random numbers. The only required input is a table. The percentage between 0 and 100 is represented as an integer in the **ulValue** member of the [**DBCOMMANDTREE**](dbcommandtree.md) node. If the input table is unique, so is the output table; otherwise, the output is a table.

</dd> <dt>

<span id="DBOP_absolute_sampling"></span><span id="dbop_absolute_sampling"></span><span id="DBOP_ABSOLUTE_SAMPLING"></span>DBOP\_absolute\_sampling
</dt> <dd>

A random sampling of rows from a table with a known, fixed output cardinality. The output cardinality is given as a positive integer stored in the **ulValue** member of the [**DBCOMMANDTREE**](dbcommandtree.md) node (values larger than the input cardinality raise an error). Randomness is guaranteed only to the ability of the provider to generate random numbers. The only required input is a table. If the input table is unique, so is the output table; otherwise, the output is a table.

</dd> <dt>

<span id="DBOP_transitive_closure"></span><span id="dbop_transitive_closure"></span><span id="DBOP_TRANSITIVE_CLOSURE"></span>DBOP\_transitive\_closure
</dt> <dd>

This operator performs recursive computations that involve traversal of all paths in a directed graph, starting from a set of initial nodes as defined by Agrawal \[Institute of Electrical and Electronics Engineers (IEEE) Transactions on Software Engineering, Volume 14, Number 7, 1988\]. Suppose the input table T is of the form T(K1, K2, P1, P2, ..., Pm), where K1 and K2 are columns belonging to the same domain. K1 and K2 can consist of more than one, but an equal number of, columns. T can be represented as a directed graph in which each row t in T is represented as a link (arc) from node t\[K1\] to node t\[K2\]. The values t\[Pi\], i = 1,..., m, represent link properties. Semantically, the transitive\_closure operator computes a table representing all paths in that graph as the following iterative program.


```
let R = T;
do
  let R = select * from T
          union
          select R.K1, T.K2 from R inner join T on R.K2 = T.K1;
while "R changes";
```



The operator takes four mandatory inputs. The first is a table T representing directed links in a graph. The second is a join predicate to determine when a link and a path can be concatenated (for example, R.K2 = T.K1). The third is a project\_list input representing the columns to be preserved after such a concatenation; each column may be the result of a scalar computation (including aggregate functions). In the preceding sample code, it is represented by R.K1, T.K2, but it may also include Pi columns from R and T. The fourth input is a predicate to select result tuples based on their derivation history (see the following table). A fifth optional input represents a selection condition on the initial table. The derivation path that led to the existence of a row in the transitive\_closure of T is captured in an additional chaptered column called Delta that gets implicitly attached to each result row. Thus, the operator's output is a hierarchical table R, having the same columns as T, plus the chaptered column.

</dd> <dt>

<span id="DBOP_recursive_union"></span><span id="dbop_recursive_union"></span><span id="DBOP_RECURSIVE_UNION"></span>DBOP\_recursive\_union
</dt> <dd>

As required by SQL-3 (but not SQL-92), the recursive union starts with an input table and adds to that table (in the result, not in the stored database) rows that can be computed by a predicate from rows already in the table. When viewed as a computation on graphs, this operation starts with a set of nodes and adds nodes that may be reached by one or more steps in the graph. The starting points are specified in the input table, and the steps are specified by the predicate. Alternatively, the starting table's rows can represent a set of arcs in a graph, and the predicate can express how links connect and can be combined into new links (paths).

</dd> </dl>

 

 




