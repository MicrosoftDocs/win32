---
title: Relational Operators
description: Relational Operators
ms.assetid: 'a147340d-bc96-419f-b3c7-8dd01411fb1b'
---

# Relational Operators

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Relational operators provide a means of selecting documents with values of a value-type property restricted to a specified interval. The following table lists the standard relational operators.



| Operator | Description              |
|----------|--------------------------|
| &lt;     | less than                |
| &lt;=    | less than or equal to    |
| =        | equal to                 |
| &gt;=    | greater than or equal to |
| &gt;     | greater than             |
| !=       | not equal to             |



 

The following table gives some simple relational queries.



| Long Form                                   | Short Form           |
|---------------------------------------------|----------------------|
| {prop name = shoesize} &gt;= 6 {/prop}      | @shoesize &gt;= 6    |
| {prop name = createdate} &gt;= -1d6 {/prop} | @CreateDate &gt; -1d |
| {prop name = DocAuthor} = "David"           | @DocAuthor = "David" |



 

 

 




