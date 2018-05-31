---
title: Property Querying
description: Property Querying
ms.assetid: 93bbe742-7148-4f34-987d-695a7e65e888
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Querying

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

After the document properties are filtered and indexed, they are available for querying. The type of query operations that Indexing Service can perform on a specified property depends on the type of the property.

-   If the property is a text-type property, the only possible queries are content searches for the property.
-   If the property is a value-type property, queries can retrieve, relationally manipulate, and sort the property as well as perform content searches for it.

Conceptually, these capabilities exist because there are single-valued entries for the value-type properties in the "table" for the catalog, but there can be   and usually are   multi-valued entries for the text-type properties.

The following table gives several examples of query types and the types of properties that each can use.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Query Type</th>
<th>Example</th>
<th>Property Types</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Content search     (Short form)<br/>     (<strong>WHERE</strong> clause)<br/></td>
<td><pre class="syntax" data-space="preserve"><code>@Chapter &quot;Confessions&quot;
WHERE CONTAINS(Chapter,&quot;Confessions&quot;)</code></pre></td>
<td>Text and value types</td>
</tr>
<tr class="even">
<td>Retrieval     (<strong>SELECT</strong> statement)<br/></td>
<td><pre class="syntax" data-space="preserve"><code>SELECT DocTitle
  FROM SCOPE()
  WHERE CONTAINS(Chapter,&quot;Confessions&quot;)</code></pre></td>
<td>Value type</td>
</tr>
<tr class="odd">
<td>Relational     (<strong>WHERE</strong> clause)<br/></td>
<td><pre class="syntax" data-space="preserve"><code>SELECT DocTitle
  FROM SCOPE()
  WHERE Book = &#39;Stormy Night&#39;</code></pre></td>
<td>Value type</td>
</tr>
<tr class="even">
<td>Sorted     (<strong>ORDER BY</strong> clause)<br/></td>
<td><pre class="syntax" data-space="preserve"><code>SELECT DocTitle, Book
  FROM SCOPE()
  WHERE CONTAINS(Chapter,&quot;Confessions&quot;)
  ORDER BY DocTitle Book DESC</code></pre></td>
<td>Value type</td>
</tr>
</tbody>
</table>



 

 

 





