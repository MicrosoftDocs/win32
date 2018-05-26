---
title: Aggregate Functions
description: Aggregate Functions
ms.assetid: faec3725-4cc2-4a0c-98a3-68b2774ad99b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Aggregate Functions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following list describes the operators for aggregate functions.

<dl> <dt>

<span id="DBOP_min__DBOP_max__DBOP_count__DBOP_sum__DBOP_avg__DBOP_any_sample__DBOP_stddev__DBOP_stddev_pop__DBOP_var__DBOP_var_pop__DBOP_first__DBOP_last"></span><span id="dbop_min__dbop_max__dbop_count__dbop_sum__dbop_avg__dbop_any_sample__dbop_stddev__dbop_stddev_pop__dbop_var__dbop_var_pop__dbop_first__dbop_last"></span><span id="DBOP_MIN__DBOP_MAX__DBOP_COUNT__DBOP_SUM__DBOP_AVG__DBOP_ANY_SAMPLE__DBOP_STDDEV__DBOP_STDDEV_POP__DBOP_VAR__DBOP_VAR_POP__DBOP_FIRST__DBOP_LAST"></span>DBOP\_min, DBOP\_max, DBOP\_count, DBOP\_sum, DBOP\_avg, DBOP\_any\_sample, DBOP\_stddev, DBOP\_stddev\_pop, DBOP\_var, DBOP\_var\_pop, DBOP\_first, DBOP\_last
</dt> <dd>

These are aggregate functions, to be used in the aggregation operation, including standard deviation and variance for samples (using division by "N - 1") and complete populations (division by "N"). All operators (except \_count) take one mandatory input representing a column\_name on which the function is computed. A count node with no inputs indicates SQL's COUNT(\*). The DISTINCT and ALL SQL set quantifiers; for example, SELECT SUM (DISTINCT X) FROM T, SELECT SUM (ALL X) FROM T) are indicated by setting the appropriate bits of the **dwSetQuantifier** member of the [**DBSETFUNC**](dbsetfunc.md) structure using the [aggregate function constants](aggregate-function-constants.md). The node produces a scalar output.

</dd> </dl>

 

 




