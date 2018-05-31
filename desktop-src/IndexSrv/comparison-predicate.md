---
title: Comparison Predicate
description: Comparison Predicate
ms.assetid: 1a6f6612-dd24-4f1a-afff-ba50b152ce7b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Comparison Predicate

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A comparison predicate uses arithmetic operators to compare column data to a literal value. For a row to be selected, the predicate must evaluate to TRUE. (Indexing Service queries that use such predicates are called *relational property queries*.) This predicate is an optional part of the optional **WHERE** clause of the **SELECT** statement.

``` syntax
SELECT Select_List | *
       FROM_Clause
       [WHERE Column_Reference Arithmetic_Operator Literal
             [Boolean_Operator Column_Reference Arithmetic_Operator Literal ...]]
       [ORDER_BY_Clause]
```

### Parameters

<dl> <dt>

<span id="Select_List"></span><span id="select_list"></span><span id="SELECT_LIST"></span>*Select\_List*
</dt> <dd>

Specifies the list of column aliases (properties) making up the table (rowset) that is returned as a result of the query.

</dd> <dt>

<span id="___asterisk_"></span><span id="___ASTERISK_"></span>*\** (asterisk)
</dt> <dd>

Specifies all columns. This option is valid only when the *FROM\_Clause* parameter references a predefined view or a temporary view.

</dd> <dt>

<span id="FROM_Clause"></span><span id="from_clause"></span><span id="FROM_CLAUSE"></span>*FROM\_Clause*
</dt> <dd>

Specifies the files on which to perform the search. For details about this parameter, see [FROM Clause](from-clause.md).

</dd> <dt>

<span id="Column_Reference"></span><span id="column_reference"></span><span id="COLUMN_REFERENCE"></span>*Column\_Reference*
</dt> <dd>

Specifies the column name (alias). Its data type must be compatible with the format of the literal specified.

</dd> <dt>

<span id="Arithmetic_Operator"></span><span id="arithmetic_operator"></span><span id="ARITHMETIC_OPERATOR"></span>*Arithmetic\_Operator*
</dt> <dd>

Specifies the arithmetic operator to use to compare the column reference data to a literal value. The following table lists the operators, their symbols, and examples.



| Operator                 | Symbol         | Example                          |
|--------------------------|----------------|----------------------------------|
| Equals                   | =              | **WHERE** DocAuthor = 'John Doe' |
| Not equals               | != or &lt;&gt; | **WHERE** DocTitle != 'Finance'  |
| Less than                | &lt;           | **WHERE** WordCount &lt; 1000    |
| Greater than             | &gt;           | **WHERE** WordCount &gt; 500     |
| Less than or equal to    | &lt;=          | **WHERE** WordCount &lt;= 500    |
| Greater than or equal to | &gt;=          | **WHERE** WordCount &gt;= 500    |



 

</dd> <dt>

<span id="Literal"></span><span id="literal"></span><span id="LITERAL"></span>*Literal*
</dt> <dd>

Specifies a constant data value that complies with the constraints of its data type. The following table lists the literal types that are supported.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Literal Type</th>
<th>Description and Examples</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Basic String</td>
<td>The basic string literal can be an ANSI string constant or a Unicode string constant. Since strings are surrounded by single quotes, to specify a quote character as part of the string, use two single quotes. An empty string is denoted by two single quotes in succession ('). Examples:
<pre class="syntax" data-space="preserve"><code>&#39;Once upon a time&#39;
&#39;John&#39;&#39;s children&#39;</code></pre></td>
</tr>
<tr class="even">
<td>Exact Numeric</td>
<td>An exact numeric literal can be an integer or a number with a decimal point. When an exact numeric literal is an integer, it can be one, two, four, or eight bytes in size. Examples:
<pre class="syntax" data-space="preserve"><code>-300           (2 byte integer)
67000          (4 byte integer)
5000000000     (8 byte integer)
.55
-366.12</code></pre></td>
</tr>
<tr class="odd">
<td>Approximate Numeric</td>
<td>An approximate numeric literal is composed of a mantissa and a signed or unsigned exponent. Examples:
<pre class="syntax" data-space="preserve"><code>2.5E-5
-.5E20</code></pre></td>
</tr>
<tr class="even">
<td>Hexadecimal</td>
<td>A hexadecimal literal is an integer expressed in hexadecimal notation. The hexadecimal expression has to be prefixed with &quot;0x&quot;. Example:
<pre class="syntax" data-space="preserve"><code>0x2F456 </code></pre></td>
</tr>
<tr class="odd">
<td>Boolean</td>
<td>A Boolean literal can only have the values TRUE or FALSE.</td>
</tr>
<tr class="even">
<td>Absolute Date/Time</td>
<td>The absolute date/time literal can be expressed as a date string or as a timestamp string. Note that the &quot;/&quot; (slash) and the &quot;-&quot; (dash) are interchangeable. Examples:
<pre class="syntax" data-space="preserve"><code>&#39;1996/01/25&#39;
&#39;1996/01/25 02:05:00&#39;
&#39;1996-02-28 10:59:03&#39;</code></pre>
<blockquote>
[!Note]<br />
The Indexing Service engine requires dates to be in terms of file times based on Greenwich Mean Time (GMT).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Relative Date/Time</td>
<td>The relative date/time literal expresses a date relative to the current date. The syntax for the DATEADD() function is:
<pre class="syntax" data-space="preserve"><code>DATEADD( Time, Relative_Interval,
{ Relative_Date/Time | GETGMTDATE()) }</code></pre>
<em>Time</em> has the following values: <br/>
<ul>
<li><em>year</em> or <em>yy</em></li>
<li><em>quarter</em> or <em>qq</em></li>
<li><em>month</em> or <em>mm</em></li>
<li><em>day</em> or <em>dd</em></li>
<li><em>week</em> or <em>wk</em></li>
<li><em>hour</em> or <em>hh</em></li>
<li><em>minute</em> or <em>mi</em></li>
<li><em>second</em> or <em>ss</em></li>
</ul>
The <strong>GETGMTDATE()</strong> function is modeled after the <strong>GETDATE()</strong> function in Microsoft SQL Server , but <strong>GETGMTDATE()</strong> indicates the current GMT rather than the current time on the local computer. <br/> Use the following format to specify the relative date/time: <br/> For example, to express an Indexing Service relative time value of -2 years, enter:<br/>
<pre class="syntax" data-space="preserve"><code>DATEADD(year, -2, GETGMTDATE())</code></pre>
To express a relative time value of - 3 years, 24 days, and 5 hours, enter: <br/>
<pre class="syntax" data-space="preserve"><code>DATEADD(hh, -5, DATEADD(dd, -24, DATEADD(yy, -3, GETGMTDATE())))</code></pre>
<blockquote>
[!Note]<br />
Positive (future) dates are not supported. The Indexing Service engine requires dates to be in terms of file times based on GMT.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>NULL</td>
<td>A <strong>NULL</strong> literal is an undefined literal.
<blockquote>
[!Note]<br />
When determining whether a literal is defined, use <strong>IS</strong> and <strong>IS NOT</strong> instead of the equals operator ( <strong>=</strong> ).
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="Boolean_Operator"></span><span id="boolean_operator"></span><span id="BOOLEAN_OPERATOR"></span>*Boolean\_Operator*
</dt> <dd>

Specifies the Boolean operator to use to combine the comparison predicates. For details about the Boolean operators and precedence rules, see the Remarks section of [WHERE Clause](where-clause.md).

</dd> <dt>

<span id="ORDER_BY_Clause"></span><span id="order_by_clause"></span><span id="ORDER_BY_CLAUSE"></span>*ORDER\_BY\_Clause*
</dt> <dd>

Specifies the ordering of the resulting rowset. This clause is optional. For details about this parameter, see [ORDER BY Clause](order-by-clause.md).

</dd> </dl>

### Examples

The following example returns all the files that have the phrase Financial Data as the title of their document.


```
... WHERE DocTitle = 'Financial Data'
```



The following example returns all the files that have the phrase Financial Data as the title of their document or that have John James as the author.


```
... WHERE DocTitle = 'Financial Data'      OR DocAuthor = 'John James'
```



The following example returns all the files that have a size less than 10,0000 or a word count less than or equal to 800.


```
... WHERE size < 10000
      OR DocWordCount <= 800
```



## Related topics

<dl> <dt>

[ARRAY Predicate](array-predicate.md)
</dt> <dt>

[CONTAINS Predicate](contains-predicate.md)
</dt> <dt>

[FREETEXT Predicate](freetext-predicate.md)
</dt> <dt>

[LIKE Predicate](like-predicate.md)
</dt> <dt>

[MATCHES Predicate](matches-predicate.md)
</dt> <dt>

[NULL Predicate](null-predicate.md)
</dt> <dt>

[WHERE Clause](where-clause.md)
</dt> </dl>

 

 





