---
description: The CONTAINS predicate is part of the WHERE clause and supports searching for words and phrases in text columns.
ms.assetid: 53083966-54cc-4a16-a161-caa663bea7ea
title: CONTAINS Predicate
ms.topic: article
ms.date: 05/31/2018
---

# CONTAINS Predicate

The CONTAINS predicate is part of the WHERE clause and supports searching for words and phrases in text columns. The CONTAINS predicate has features for matching words, matching inflectional forms of words, searching using wildcard characters, and searching using proximity. You can also apply weights in a CONTAINS predicate to set the importance of the columns where the search term is found. The CONTAINS predicate is better suited for exact matches, in contrast to the [FREETEXT](-search-sql-freetext.md) predicate, which is better suited to finding documents containing combinations of the search words spread throughout the column. Searches are not case-sensitive.

The following is the basic syntax of the CONTAINS predicate:

```SQL
...CONTAINS(["<fulltext_column>",]'<contains_condition>'[,<LCID>])...
```

The fulltext\_column reference is optional. With it, you can limit the search to a single column or a column group against which the CONTAINS predicate is tested. When the fulltext column is specified as "ALL" or "\*", all indexed text properties are searched. Although the column is not required to be a text property, the results might be meaningless if the column is some other data type. The column name can be either a regular or delimited [identifier](-search-sql-identifiers.md), and you must separate it from the condition by a comma. If no fulltext column is specified, the System.Search.Contents column, which is the body of the document, is used.

The LCID portion of the predicate specifies the search locale. This instructs the search engine to use the appropriate word breaker and inflectional forms for the search query. To specify the locale, provide the Windows standard language code identifier (LCID). For example, 1033 is the LCID for United States-English. Place the LCID as the last item inside the parentheses of the CONTAINS clause. For important information about searching and languages, see [Using Localized Searches](-search-sql-usinglocsearches.md).

> [!NOTE]  
> The default search locale is the system default locale.

The contains\_condition portion must be enclosed in single quotation marks for single words or double quotation marks for phrases, and consists of one or more content search terms that are combined using the logical operators **AND** or **OR**. You can use the optional unary operator **NOT** after an **AND** operator to negate the logical value of a content search term.

> [!NOTE]  
> The **NOT** operator can occur only after **AND**. You cannot use the **NOT** operator if there is only one match condition, or after the **OR** operator.

You can use parentheses to group and nest content search terms. The following table describes the order of precedence for the logical operators.

| Order (precedence) | Logical operator |
|--------------------|------------------|
| First (highest)    | **NOT**          |
| Second             | **AND**          |
| Third (lowest)     | **OR**           |

Logical operators of the same type are associative, and there is no specified calculation order. For example, (A **AND** B) **AND** (C **AND** D) can be calculated (B **AND** C) **AND** (A **AND** D) with no change in the logical result.

The following table describes the types of content search terms.

<!-- markdownlint-disable MD033 -->
<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Word</td>
<td>A single word without spaces or other punctuation. Double quotation marks are not necessary.</td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS (&#39;computer&#39;)</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>Phrase</td>
<td>Multiple words or included spaces.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;&quot;computer software&quot;&#39;)

Or, to use a double quote mark:

... WHERE CONTAINS
(&#39;&quot;computer &quot;&quot;science&quot;&quot; &quot;&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>Wildcard</td>
<td>Words or phrases with the asterisk (*) added to the end. For more information, see <a href="-search-sql-wildcards.md">Using Wildcards in the CONTAINS Predicate</a>.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;&quot;compu*&quot;&#39;)

Matches &quot;computer&quot;, &quot;computers&quot;,
&quot;computation&quot;, and &quot;compulsory&quot;</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>Full-text Column</td>
<td>A property column name against which to match the remaining query.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS (System.Author,&#39;&quot;James&quot; OR &quot;Juan&quot;&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>Boolean</td>
<td>Words, phrases, and wildcard strings combined by using the Boolean operators <strong>AND</strong>, <strong>OR</strong>, or <strong>NOT</strong>. Enclose the Boolean terms in double quotation marks.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;&quot;computer monitor&quot; AND
  &quot;software program&quot; AND
  &quot;install component&quot;&#39;)

...WHERE CONTAINS
 (&#39; &quot;computer&quot; AND
  &quot;software&quot; AND
  &quot;install&quot; &#39; )

...WHERE CONTAINS
(&#39;&quot;computer software install&quot;&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>Near</td>
<td>Words, phrases, or wildcards separated by the function NEAR. For more information, see <a href="-search-sql-near.md">NEAR Term</a>.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;&quot;computer&quot; NEAR &quot;software&quot;&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>FormsOf</td>
<td>Matches a word and the inflectional versions of that word. For more information, see <a href="-search-sql-formsof.md">FORMSOF Term</a>.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;FORMSOF
 (INFLECTIONAL, &quot;happy&quot;))

Matches &quot;happy&quot;, &quot;happier&quot;,
&quot;happiest&quot;, &quot;happily&quot;, and so on.</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>IsAbout</td>
<td>Combines matching results over multiple word, phrase, or wildcard search terms. Each search term can optionally be weighted. You can optionally specify the rank calculation method, which combines the weights and how many of the items the document matches. For more information, see <a href="-search-sql-isabout.md">ISABOUT Term</a>.</td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
(&#39;ISABOUT ( &quot;computer&quot; WEIGHT (0.75) ,
    &quot;software&quot; WEIGHT (0.25) ,
    &quot;development&quot; WEIGHT (0.255)
 ) RANKMETHOD INNER PRODUCT
&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>
<!-- markdownlint-enable MD033 -->

This section includes the following topics:

- [Using Wildcards in the CONTAINS Predicate](-search-sql-wildcards.md)
- [FORMSOF Term](-search-sql-formsof.md)
- [ISABOUT Term](-search-sql-isabout.md)
- [NEAR Term](-search-sql-near.md)

## Related topics

### Reference

[WHERE Clause](-search-sql-where.md)

### Conceptual

[Full-Text Predicates](-search-sql-fulltextpredicates.md)

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
