---
description: The NEAR term is used to specify that two content search terms must be relatively close to one another to be recognized as matching for the CONTAINS predicate.
ms.assetid: cbc449b1-9f1d-42a2-b39e-d5cd69c052df
title: NEAR Term
ms.topic: article
ms.date: 05/31/2018
---

# NEAR Term

The NEAR term is used to specify that two content search terms must be relatively close to one another to be recognized as matching for the [CONTAINS](-search-sql-contains.md) predicate.

The syntax for the NEAR term is:


```
<content_search_term> NEAR | ~ <content_search_term>
```



The NEAR term can be represented by the keyword "NEAR" or by a tilde (~).

When the words joined by NEAR in the query are found within approximately 50 words of each other inside the column being searched, the NEAR term returns a match. The closer together the two words are, the higher the calculated rank for the NEAR term. The farther apart the two words are, the lower the rank.

> [!Note]  
> The number of words between found search terms is approximate and depends on the appearance of noise words, like "a" or "the", and how wordbreakers tokenize text. It may be less than 50.

 


The following table describes content search term types that can be used with a NEAR term in a CONTAINS predicate.



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
<td><pre><code>...WHERE CONTAINS(&#39;computer NEAR software)&#39;)</code></pre></td>
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
<td><pre><code>...WHERE CONTAINS(&#39;&quot;computer software&quot; NEAR hardware)&#39;</code></pre></td>
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
<td><pre><code>...WHERE CONTAINS(&#39;&quot;compu*&quot; NEAR &quot;soft*&quot;&#39;)</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>

> [!Note]  
> If the match words specified with the NEAR term are both found in the column being searched, but are farther apart than 50 words, the result is still returned, but has a [rank](-search-sql-understandingrelevancevalues.md) of 0.

 

### Example

The following example shows chaining of NEAR terms, using both the short and long forms of the term:


```
...WHERE CONTAINS('computer NEAR software ~ "setup application"')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Full-Text Predicates](-search-sql-fulltextpredicates.md)
</dt> <dt>

[Using Wildcards in the CONTAINS Predicate](-search-sql-wildcards.md)
</dt> </dl>

 

 



