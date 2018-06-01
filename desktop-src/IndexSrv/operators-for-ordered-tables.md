---
Description: Operators for Ordered Tables
ms.assetid: 8bfd5000-40b3-43ae-a1cc-fa6b29676134
title: Operators for Ordered Tables
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Operators for Ordered Tables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for ordered tables.

<dl> <dt>

<span id="DBOP_top__DBOP_top_percent__DBOP_top_plus_ties__DBOP_top_percent_plus_ties"></span><span id="dbop_top__dbop_top_percent__dbop_top_plus_ties__dbop_top_percent_plus_ties"></span><span id="DBOP_TOP__DBOP_TOP_PERCENT__DBOP_TOP_PLUS_TIES__DBOP_TOP_PERCENT_PLUS_TIES"></span>DBOP\_top, DBOP\_top\_percent, DBOP\_top\_plus\_ties, DBOP\_top\_percent\_plus\_ties
</dt> <dd>

Take the first rows from an ordered table. These operators are different from the sampling operators because they prohibit randomness. The "top" operations require a fixed count of rows. The "top\_percent" operations require a fraction of the input rows (not an approximation). The "plus-ties" operators include all rows that are equal (with respect to the sort order of the input table) to the last one that is explicitly requested. The first required input for all operators is an ordered table. The top and top\_plus\_ties operators store the count of rows as a positive integer in the **ulValue** member of the command node. The "top\_percent\*" operators take a second required scalar\_list\_anchor input. The elements of this list contain two scalar\_constant members that represent a pair of positive integers expressing a fraction between 0 and 1. The output is an ordered table.

</dd> <dt>

<span id="DBOP_rank__DBOP_rank_ties_equally__DBOP_rank_ties_equally_and_skip"></span><span id="dbop_rank__dbop_rank_ties_equally__dbop_rank_ties_equally_and_skip"></span><span id="DBOP_RANK__DBOP_RANK_TIES_EQUALLY__DBOP_RANK_TIES_EQUALLY_AND_SKIP"></span>DBOP\_rank, DBOP\_rank\_ties\_equally, DBOP\_rank\_ties\_equally\_and\_skip
</dt> <dd>

Add a new column "rank" to the table, counting from 1 to the table's cardinality. If the column name "rank" already exists, add "rank2" ("rank3" etc.) instead. The "ties" operations assign the same rank to items that are equal (with respect to the sort order of the input table). The "and skip" variant skips an appropriate number of values in the counting sequence. An example without skipping would be 1, 2, 2, 2, 3, 4, 4, 5; an example with skipping would be 1, 2, 2, 2, 5, 6, 6, 8. The input is an ordered table. If the operator is "rank," the output is an ordered unique table; for the "ties" operators, it is an ordered table.

</dd> </dl>

 

 



