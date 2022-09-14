---
description: The FORMSOF term performs matches using other linguistic forms of the word.
ms.assetid: b705b8bc-dc2c-4cee-8306-f494b0f96cbf
title: FORMSOF Term
ms.topic: article
ms.date: 05/31/2018
---

# FORMSOF Term

The FORMSOF term performs matches using other linguistic forms of the word. The following is the FORMSOF term syntax:


```
FORMSOF (<generation_type>,<match_words>)
```



The generation type specifies how Microsoft Windows Search chooses the alternative word forms. The **INFLECTIONAL** value chooses alternative inflection forms for the match words. If the word is a verb, alternative tenses are used. If the word is a noun, the singular, plural, and possessive forms are used to detect matches.

The match\_words value is one or more words, separated by commas.

## Examples

The following example searches for inflectional matches for the word "run". This example matches documents containing "run", "running", or "ran".


```
...CONTAINS('FORMSOF(INFLECTIONAL,"run")')
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FREETEXT Predicate](-search-sql-freetext.md)
</dt> <dt>

[WHERE Clause](-search-sql-where.md)
</dt> </dl>

 

 



