---
Description: Operators for Hierarchical Tables
ms.assetid: 15da90d7-8f9f-4a89-b385-9c91b72d9ac3
title: Operators for Hierarchical Tables
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Operators for Hierarchical Tables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for hierarchical tables.

<dl> <dt>

<span id="DBOP_navigate"></span><span id="dbop_navigate"></span><span id="DBOP_NAVIGATE"></span>DBOP\_navigate
</dt> <dd>

Given two tables, one or both of which may be hierarchical tables, this operator computes their join. However, instead of creating large rows with columns from both join inputs, it attaches to each row of the first table all matching rows from the second table, thus creating a hierarchy of rowsets. It also adds expression-valued columns to both the new parent rowset and the new child rowset.

This operator has six inputs:

-   Two table-valued subtrees representing the input to the operator.
-   A join predicate to make the connection.
-   A list element with a name for the new column representing the nested column. The alias name for child levels is mandatory and must be unique across the hierarchy.
-   A list specifying expression-valued columns to be added to the parent level (such as sub-totals).
-   A list adding expression-valued columns to the child level (such as running sums).

</dd> </dl>

 

 



