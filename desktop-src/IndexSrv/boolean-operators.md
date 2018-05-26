---
title: Boolean Operators
description: Boolean Operators
ms.assetid: 6b2ea051-b349-454b-8771-096e0be0686b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Boolean Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The standard Boolean operators, **AND**, **OR**, and **NOT**, can be used in both content and property-value queries. The **NOT** operator is supported in an **AND NOT** operation as the full form of the **NOT** operator. Unary **NOT** is supported as an operator for value-type property queries (for example, ! @size &gt; 100). In addition, the Boolean operators can be replaced by symbols. The Boolean operators and their associated full forms and symbols are the following.



| Operator                               | Full form              | Symbol        | Notes                                                                                                                          |
|----------------------------------------|------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| **AND**<br/>                     | **AND**<br/>     | &<br/>  | Only the English spelling of the long form is available in Dialect 2.<br/>                                               |
| **OR**<br/>                      | **OR**<br/>      | \|<br/> | Only the English spelling of the long form is available in Dialect 2.<br/>                                               |
| **NOT**<br/> (binary)<br/> | **AND NOT**<br/> | &!<br/> | Only the English spelling of the long form is available in Dialect 2.<br/>                                               |
| **NOT**<br/> (unary)<br/>  | **NOT**<br/>     | !<br/>  | Unary **NOT**for value-type property queries. Only the English spelling of the long form is available in Dialect 2.<br/> |



 

In Dialect 1, the Boolean operators are localized for several non-English languages. See [Incompatibilities of Dialect 2 with Dialect 1](incompatibilities-of-dialect-2-with-dialect-1.md) for complete details.

 

 





