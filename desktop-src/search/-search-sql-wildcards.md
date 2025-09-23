---
description: The CONTAINS predicate supports the use of the asterisk (\*) as a wildcard character to represent words and phrases. You can add the asterisk only at the end of the word or phrase. The presence of the asterisk enables the prefix-matching mode.
ms.assetid: 9d141c7a-a721-416e-aa61-dabdb6533462
title: Using Wildcard Characters in the CONTAINS Predicate
ms.topic: concept-article
ms.date: 02/04/2025
---

# Using Wildcard Characters in the CONTAINS Predicate

The CONTAINS predicate supports the use of the asterisk (\*) as a wildcard character to represent words and phrases. You can add the asterisk only at the end of the word or phrase. The presence of the asterisk enables the _prefix-matching_ mode. In this mode, matches are returned if the column contains the specified search word followed by zero or more other characters.

If a phrase is provided, each word contained in the phrase is considered to be a separate prefix. Therefore, a query specifying a prefix term of "local wine*" matches any rows with the text of "local winery", "locally wined and dined", and so on.

## Examples

### Word matching

This example matches documents that have any word in the FileName column beginning with "serv".

```sql
...WHERE CONTAINS(System.FileName, '"serv*"')
```

Example matching words include "server", "servers", and "service".

### Phrase matching

This example matches documents with any phrase in the FileName column that begins with "comp" and in which the next word begins with "serv".

```sql
...WHERE CONTAINS(System.FileName, '"comp serv*"')
```

Example matching phrases include "comp server", "computer servers", and "competitor's service".

### Suffix matching (not supported)

The asterisk works only for prefix-matching and can be placed only at the end of the word or phrase; it does not work for suffix-matching. The following syntax is not valid and does not match documents with any word in the FileName column ending with "serve".

```sql
-- DO NOT USE.
WHERE CONTAINS(System.FileName, '"*serve"')
```

## Related topics

**Reference**

[FREETEXT Predicate](-search-sql-freetext.md)

[WHERE Clause](-search-sql-where.md)
