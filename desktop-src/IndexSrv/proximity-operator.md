---
title: Proximity Operator
description: Proximity Operator
ms.assetid: d9b59fbf-0549-459c-94af-7627aadcc78e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Proximity Operator

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The proximity operator is available in content queries for searching with proximity thresholds (for example, within 40 words of another term, or within the same sentence or paragraph). The proximity operator works as a weighted **AND** query, where the rank of the match increases as the terms appear "closer" together in the content stream. The proximity operator and its long form and short form are the following.



| Operator | Long form                                            | Short form | Notes                                                                 |
|----------|------------------------------------------------------|------------|-----------------------------------------------------------------------|
| **NEAR** | {**NEAR**dist = *dist\_value*, unit = *unit\_value*} | Near, ~    | Only the English spelling of the long form is available in Dialect 2. |



 

In Dialect 1, the proximity operator is localized for several non-English languages. See [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md) for complete details.

The *dist\_value* of the dist attribute specifies the threshold count of units to use between text clauses. The text clauses must appear within each other's specified counted units. If dist = 0 is specified, the text clauses must all occur within the particular unit.

The *unit\_value* of the unit attribute specifies the distance unit to use. The following table gives the valid values of the unit attribute.



| Value | Description |
|-------|-------------|
| Word  | word        |
| Sent  | sentence    |
| Par   | paragraph   |
| Chap  | chapter     |



 

If dist = 0 and unit = sent, then the text clause must appear in the same sentence. If unit = word, then dist = 0 is illegal.

> [!Note]  
> Indexing Service 3.0 only supports the **NEAR** operator with dist &lt;= 50 and unit=word. Indexing Service 3.0 does not support same sentence, same paragraph, or same chapter searching. Nor does it support any value for unit other than word.

 

The short-form version of the **NEAR** operator assumes the default value of 50 for dist and assumes that the unit is word. The following examples are equivalent in Indexing Service.

``` syntax
Dog ~ Cat
Dog near Cat
Dog {near dist = 50, unit = word} Cat 
```

 

 




