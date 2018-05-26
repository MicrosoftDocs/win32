---
title: Mixed Operators
description: Mixed Operators
ms.assetid: b47a1d61-d941-4956-8d20-f3e420cd0e8f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Mixed Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the mixed operators.

<dl> <dt>

<span id="DBOP_in"></span><span id="dbop_in"></span><span id="DBOP_IN"></span>DBOP\_in
</dt> <dd>

Membership test of a scalar or row in a table. Inputs for this operator are a row and a table; it produces a Boolean result as output.

</dd> <dt>

<span id="DBOP_exists__DBOP_unique"></span><span id="dbop_exists__dbop_unique"></span><span id="DBOP_EXISTS__DBOP_UNIQUE"></span>DBOP\_exists, DBOP\_unique
</dt> <dd>

These operators take a table T as input and produce a Boolean result as output. DBOP\_exists evaluates to TRUE if the cardinality of T is greater than zero; otherwise it evaluates to FALSE. DBOP\_unique detects duplicate rows in T. If any two rows in T are equal to one another, DBOP\_unique evaluates to FALSE; otherwise, it evaluates to TRUE.

</dd> <dt>

<span id="DBOP_subset__DBOP_proper_subset__DBOP_superset__DBOP_proper_superset__DBOP_disjoint_"></span><span id="dbop_subset__dbop_proper_subset__dbop_superset__dbop_proper_superset__dbop_disjoint_"></span><span id="DBOP_SUBSET__DBOP_PROPER_SUBSET__DBOP_SUPERSET__DBOP_PROPER_SUPERSET__DBOP_DISJOINT_"></span>DBOP\_subset, DBOP\_proper\_subset, DBOP\_superset, DBOP\_proper\_superset, DBOP\_disjoint,
</dt> <dd>

These operators take two tables T1 and T2 as input and determine whether T1 is a subset, proper\_subset, superset, proper\_superset, or disjoint set of T2. The output is Boolean.

</dd> </dl>

 

 




