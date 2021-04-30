---
description: The ISABOUT term matches columns against a group of one or more search terms.
ms.assetid: e2629c4c-4b44-4427-ac1d-17f55fd969e3
title: ISABOUT Term
ms.topic: article
ms.date: 05/31/2018
---

# ISABOUT Term

**Deprecated**

This feature has been removed as of Windows 8. If you write new applications, avoid using this deprecated feature. If you modify existing applications, you are strongly encouraged to remove any dependency on this feature.

The ISABOUT term matches columns against a group of one or more search terms. It has the following syntax:


```
ISABOUT(<components>) [RANKMETHOD <method>]
```



The optional RANKMETHOD term specifies the calculation method used to rank the documents that match one or more of the components. If no RANKMETHOD is specified, the default Jaccard Coefficient ranking method is used.

The ISABOUT term can have one or more components. The columns specified in the [CONTAINS](-search-sql-contains.md) predicate are tested against each component. The document is included in the results if at least one of the components matches. Commas separate multiple components.

The component part has the following syntax:


```
<match_term> [<weight_term>]
```



You can use the optional WEIGHT term to change the relative importance of each term within the ISABOUT term. If no weight term is applied, the default 1.0 weight is implied.

The following table describes possible match term types.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
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
<td>A single word without spaces or other punctuation.</td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
 (&#39;ISABOUT (&quot;computer&quot;,&quot;software&quot;)&#39;)</code></pre></td>
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
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
 (&#39;ISABOUT (&quot;computer software&quot;,&quot;hardware&quot;)&#39;)</code></pre></td>
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
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>...WHERE CONTAINS
 (&#39;ISABOUT (&quot;compu*&quot;,&quot;soft*&quot;)&#39;)

Matches &quot;computer&quot;, &quot;computers&quot;, &quot;computation&quot;, 
and &quot;compulsory&quot;</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

## ISABOUT Column Weighting

The ISABOUT term ranks matching documents based on how closely each document matches the set of match terms in the query. You can use column weighting to place more importance on matching some match terms than others. Each match term in the ISABOUT term can have a weight value applied. The weight is applied to a single match term and is indicated by the keyword "WEIGHT". The WEIGHT term has two alternative syntaxes:


```
<match_term> WEIGHT(<weight_value>)
<match_term>:(<weight_value>)
```



The weight value must be between 0 and 1.0, with no more than three decimal places. Specifying a weight value outside this range results in an error message. The unweighted ranking value for a term is multiplied by the weight value for the term.

If no weight is specified for a match term, the default value, 1.0, is implied.

### Example

The following example applies weights to the two ISABOUT match terms, using both the long and short syntax for weight values.


```
WHERE CONTAINS( System.FileName,
      'ISABOUT("computer" WEIGHT (0.75),"software":0.25)')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FREETEXT Predicate](-search-sql-freetext.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> </dl>

 

 



