---
description: The WMI Query Language (WQL) is a subset of the American National Standards Institute Structured Query Language (ANSI SQL)&\#8212;with minor semantic changes. The following table lists the WQL keywords.
ms.assetid: 72a7ec04-9af3-41ae-9189-6e1d46803fa9
ms.tgt_platform: multiple
title: WQL (SQL for WMI)
ms.topic: article
ms.date: 05/31/2018
---

# WQL (SQL for WMI)

The WMI Query Language (WQL) is a subset of the American National Standards Institute Structured Query Language (ANSI SQL) with minor semantic changes. The following table lists the WQL keywords.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>WQL keyword</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AND<br/></td>
<td>Combines two Boolean expressions, and returns <strong>TRUE</strong> when both expressions are <strong>TRUE</strong>.<br/></td>
</tr>
<tr class="even">
<td><a href="associators-of-statement.md">ASSOCIATORS OF</a></td>
<td>Retrieves all instances that are associated with a source instance.<br/> Use this statement with schema queries and data queries.<br/></td>
</tr>
<tr class="odd">
<td><a href="--class-identifier.md">__CLASS</a></td>
<td>References the class of the object in a query.<br/></td>
</tr>
<tr class="even">
<td>FROM<br/></td>
<td>Specifies the class that contains the properties listed in a SELECT statement. Windows Management Instrumentation (WMI) supports data queries from only one class at a time.<br/></td>
</tr>
<tr class="odd">
<td><a href="group-clause.md">GROUP Clause</a></td>
<td>Causes WMI to generate one notification to represent a group of events.<br/> Use this clause with event queries.<br/></td>
</tr>
<tr class="even">
<td><a href="having-clause.md">HAVING</a></td>
<td>Filters the events that are received during the grouping interval that is specified in the <a href="within-clause.md">WITHIN clause</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="wql-operators.md">IS</a></td>
<td>Comparison operator used with NOT and <strong>NULL</strong>. The syntax for this statement is the following:<br/> IS [NOT] <strong>NULL</strong><br/> (where NOT is optional)<br/></td>
</tr>
<tr class="even">
<td><a href="wql-operators.md">ISA</a></td>
<td>Operator that applies a query to the subclasses of a specified class. For more information, see <a href="isa-operator-for-event-queries.md">ISA Operator for Event Queries</a>, <a href="isa-operator-for-data-queries.md">ISA Operator for Data Queries</a>, and <a href="isa-operator-for-schema-queries.md">ISA Operator for Schema Queries</a>.<br/></td>
</tr>
<tr class="odd">
<td>KEYSONLY<br/></td>
<td>Used in <a href="references-of-statement.md">REFERENCES OF</a> and <a href="associators-of-statement.md">ASSOCIATORS OF</a> queries to ensure that the resulting instances are only populated with the keys of the instances, which reduces the overhead of the call.<br/></td>
</tr>
<tr class="even">
<td><a href="wql-operators.md">LIKE</a></td>
<td>Operator that determines whether or not a given character string matches a specified pattern.<br/></td>
</tr>
<tr class="odd">
<td>NOT<br/></td>
<td>Comparison operator that use in a WQL SELECT query, for example:<br/>
<pre data-space="preserve"><code>SELECT * FROM meta_class WHERE NOT __class < &quot;Win32&quot; AND NOT __this ISA &quot;Win32_Account&quot;</code></pre></td>
</tr>
<tr class="even">
<td><strong>NULL</strong></td>
<td>Indicates an object does not have an explicitly assigned value. <strong>NULL</strong> is not equivalent to zero (0) or blank.<br/></td>
</tr>
<tr class="odd">
<td>OR<br/></td>
<td>Combines two conditions.<br/> When more than one logical operator is used in a statement, the OR operators are evaluated after the AND operators.<br/></td>
</tr>
<tr class="even">
<td><a href="references-of-statement.md">REFERENCES OF</a></td>
<td>Retrieves all association instances that refer to a specific source instance. Use this statement with schema and data queries. The <a href="references-of-statement.md">REFERENCES OF</a> statement is similar to the <a href="associators-of-statement.md">ASSOCIATORS OF</a> statement. However, it does not retrieve endpoint instances; it retrieves the association instances.<br/></td>
</tr>
<tr class="odd">
<td>SELECT<br/></td>
<td>Specifies the properties that are used in a query.<br/> For more information, see <a href="select-statement-for-data-queries.md">SELECT Statement for Data Queries</a>, <a href="select-statement-for-event-queries.md">SELECT Statement for Event Queries</a>, or <a href="select-statement-for-schema-queries.md">SELECT Statement for Schema Queries</a>.<br/></td>
</tr>
<tr class="even">
<td><strong>TRUE</strong></td>
<td>Boolean operator that evaluates to -1 (minus one).<br/></td>
</tr>
<tr class="odd">
<td><a href="where-clause.md">WHERE</a></td>
<td>Narrows the scope of a data, event, or schema query.<br/></td>
</tr>
<tr class="even">
<td><a href="within-clause.md">WITHIN</a></td>
<td>Specifies a polling or grouping interval.<br/> Use this clause with event queries.<br/></td>
</tr>
<tr class="odd">
<td>FALSE<br/></td>
<td>Boolean operator that evaluates to 0 (zero).</td>
</tr>
</tbody>
</table>



 

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

 

 




