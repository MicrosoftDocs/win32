---
description: The WMI Query Language (WQL) is a subset of the American National Standards Institute Structured Query Language (ANSI SQL)&\#8212;with minor semantic changes. The following table lists the WQL keywords.
ms.assetid: 72a7ec04-9af3-41ae-9189-6e1d46803fa9
ms.tgt_platform: multiple
title: WQL (SQL for WMI)
ms.topic: concept-article
ms.date: 05/31/2018
---

# WQL (SQL for WMI)

The WMI Query Language (WQL) is a subset of the American National Standards Institute Structured Query Language (ANSI SQL) with minor semantic changes. The following table lists the WQL keywords.

| WQL keyword | Meaning |
| --- | --- |
| :::no-loc text="AND"::: | Combines two Boolean expressions, and returns **TRUE** when both expressions are **TRUE**. |
| [:::no-loc text="ASSOCIATORS OF":::](associators-of-statement.md) | Retrieves all instances that are associated with a source instance.<br>Use this statement with schema queries and data queries. |
| [:::no-loc text="\_\_CLASS":::](--class-identifier.md) | References the class of the object in a query. |
| :::no-loc text="FROM"::: | Specifies the class that contains the properties listed in a SELECT statement. Windows Management Instrumentation (WMI) supports data queries from only one class at a time. |
| [:::no-loc text="GROUP Clause":::](group-clause.md) | Causes WMI to generate one notification to represent a group of events.<br>Use this clause with event queries. |
| [:::no-loc text="HAVING":::](having-clause.md) | Filters the events that are received during the grouping interval that is specified in the [WITHIN clause](within-clause.md). |
| [:::no-loc text="IS":::](wql-operators.md) | Comparison operator used with NOT and **NULL**. The syntax for this statement is the following:<br>IS \[NOT\] **NULL**<br>(where NOT is optional) |
| [:::no-loc text="ISA":::](wql-operators.md) | Operator that applies a query to the subclasses of a specified class. For more information, see [ISA Operator for Event Queries](isa-operator-for-event-queries.md), [ISA Operator for Data Queries](isa-operator-for-data-queries.md), and [ISA Operator for Schema Queries](isa-operator-for-schema-queries.md). |
| :::no-loc text="KEYSONLY"::: | Used in [REFERENCES OF](references-of-statement.md) and [ASSOCIATORS OF](associators-of-statement.md) queries to ensure that the resulting instances are only populated with the keys of the instances, which reduces the overhead of the call. |
| [:::no-loc text="LIKE":::](wql-operators.md) | Operator that determines whether or not a given character string matches a specified pattern. |
| :::no-loc text="NOT"::: | Comparison operator that use in a WQL SELECT query, for example:<br>`SELECT * FROM meta_class WHERE NOT __class < "Win32" AND NOT __this ISA "Win32_Account"` |
| :::no-loc text="NULL"::: | Indicates an object does not have an explicitly assigned value. **NULL** is not equivalent to zero (0) or blank. |
| :::no-loc text="OR"::: | Combines two conditions.<br>When more than one logical operator is used in a statement, the OR operators are evaluated after the AND operators. |
| [:::no-loc text="REFERENCES OF":::](references-of-statement.md) | Retrieves all association instances that refer to a specific source instance. Use this statement with schema and data queries. The [REFERENCES OF](references-of-statement.md) statement is similar to the [ASSOCIATORS OF](associators-of-statement.md) statement. However, it does not retrieve endpoint instances; it retrieves the association instances. |
| :::no-loc text="SELECT"::: | Specifies the properties that are used in a query.<br>For more information, see [SELECT Statement for Data Queries](select-statement-for-data-queries.md), [SELECT Statement for Event Queries](select-statement-for-event-queries.md), or [SELECT Statement for Schema Queries](select-statement-for-schema-queries.md). |
| :::no-loc text="TRUE"::: | Boolean operator that evaluates to -1 (minus one). |
| [:::no-loc text="WHERE":::](where-clause.md) | Narrows the scope of a data, event, or schema query. |
| [:::no-loc text="WITHIN":::](within-clause.md) | Specifies a polling or grouping interval.<br>Use this clause with event queries. |
| :::no-loc text="FALSE"::: | Boolean operator that evaluates to 0 (zero). |

> [!Note]  
> Using a WQL key word as an object name can result in a query that cannot be parsed even when the query compiles without error.

 

## Related topics

<dl> <dt>

[WQL Operators](wql-operators.md)
</dt> <dt>

[WQL-Supported Date Formats](wql-supported-date-formats.md)
</dt> <dt>

[WQL-Supported Time Formats](wql-supported-time-formats.md)
</dt> </dl>

 

 




