---
title: Operators with Two Variants for Ordered and Non-Ordered Tables
description: Operators with Two Variants for Ordered and Non-Ordered Tables
ms.assetid: ff193501-d681-4cd7-8b63-aa602008beb5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Operators with Two Variants for Ordered and Non-Ordered Tables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators with two variants for ordered and non-ordered tables.

<dl> <dt>

<span id="DBOP_select__DBOP_order_preserving_select"></span><span id="dbop_select__dbop_order_preserving_select"></span><span id="DBOP_SELECT__DBOP_ORDER_PRESERVING_SELECT"></span>DBOP\_select, DBOP\_order\_preserving\_select
</dt> <dd>

Subset of rows based on a predicate. The required inputs are one table and one Boolean expression. If the input table is unique, so is the output table. For the "order-preserving-select" operator, if the input is an ordered table, so is the output.

</dd> <dt>

<span id="DBOP_project__DBOP_project_order_preserving"></span><span id="dbop_project__dbop_project_order_preserving"></span><span id="DBOP_PROJECT__DBOP_PROJECT_ORDER_PRESERVING"></span>DBOP\_project, DBOP\_project\_order\_preserving
</dt> <dd>

Preserve a subset of columns, possibly with some arithmetic computation within each single row. No duplicate elimination of rows is implied. The two required inputs are a table and a project\_list\_anchor input; the output is a table. For the "order-preserving-project" operator, if the input is an ordered table, so is the output. If the provider permits, some of the ordering columns may be removed by the projection operator, such that the ordering is not restorable if it were to be lost in a subsequent operation. Only unqualified names are available above a projection level; use an intervening alias node to avoid ambiguous references.

</dd> </dl>

 

 




