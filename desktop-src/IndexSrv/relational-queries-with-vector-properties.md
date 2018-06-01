---
Description: Relational Queries with Vector Properties
ms.assetid: 1f64bff7-bbfb-4856-a5aa-9cc00cf255b2
title: Relational Queries with Vector Properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Relational Queries with Vector Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A vector property has more than one element, each with a value. When used with vector properties, the relational operators are applied to corresponding vector elements in turn, left to right. A complete test passes if all the individual element tests pass.

Consider the two vector properties, A and B, with the following elements: A (a1; a2; a3) and B (b1; b2; b3). With these elements, A &gt; B if, and only if, a1 &gt; b1 **AND** a2 &gt; b2 **AND** a3 &gt; b3.

If one vector has more elements than the other, the test is only applied against the matching elements and the extra elements are ignored.

A series of relational comparisons connected by other operators apply to the most recently specified property. The following two queries are equivalent.

``` syntax
@shoesize > 6 AND < 10
@shoesize > 6 AND @shoesize < 10
```

To perform a relational query with the long-form property tag, a {/prop} can be (optionally) used to complete the clause and to improve readability. The following query is a valid property restriction.

``` syntax
{prop name = shoesize} > 6 & < 10{/prop}
```

The {/prop} construct is used to separate property clauses but it can usually be omitted, because a new property specification (either long or short) implies closure of the previous clause. It is also assumed that there is a "super" closure at the end of the query expression to close all property tags.

 

 



