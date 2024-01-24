---
description: The CONTAINS predicate supports the use of the asterisk (\*) as a wildcard character to represent words and phrases. You can add the asterisk only at the end of the word or phrase. The presence of the asterisk enables the prefix-matching mode.
ms.assetid: 9d141c7a-a721-416e-aa61-dabdb6533462
title: Using Wildcard Characters in the CONTAINS Predicate
ms.topic: article
ms.date: 05/31/2018
---

# Using Wildcard Characters in the CONTAINS Predicate

The CONTAINS predicate supports the use of the asterisk (\*) as a wildcard character to represent words and phrases. You can add the asterisk only at the end of the word or phrase. The presence of the asterisk enables the prefix-matching mode. In this mode, matches are returned if the column contains the specified search word followed by zero or more other characters. If a phrase is provided, matches are detected if the column contains all the specified words with zero or more other characters following the final word.

## Examples

The first example matches documents that have any word in the FileName column beginning with "serv". Example matching words include "server", "servers", and "service".


```
...WHERE CONTAINS(System.FileName, '"serv*"')
```



The second example matches documents with any phrase in the FileName column that begins with "comp" and in which the next word begins with "serv". Example matching words include "comp server", "comp servers", and "comp service".


```
...WHERE CONTAINS(System.FileName, '"comp serv*"')
```



The asterisk works only for prefix-matching and can be placed only at the end of the word or phrase; it does not work for suffix-matching. The following syntax is not valid and does not match documents with any word in the FileName column ending with "serve".


```
WHERE CONTAINS(System.FileName, '"*serve"')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FREETEXT Predicate](-search-sql-freetext.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> </dl>

 

 



