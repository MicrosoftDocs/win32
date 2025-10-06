---
description: The Microsoft Windows Search query language supports two full-text search predicates.
ms.assetid: c753dddb-57ed-40e6-8e49-ba5b6425fdd5
title: Full-text predicates
ms.topic: reference
ms.date: 05/31/2018
---

# Full-text predicates

The Microsoft Windows Search query language supports two full-text search predicates and one semantic meaning matching predicate. 

The CONTAINS predicate performs comparisons on columns that contain text. The CONTAINS clause can perform matching on single words or phrases, based on the proximity of the search terms. In comparison, the FREETEXT predicate helps find documents containing combinations of all the search words spread throughout the content or columns specified.
 
Note that for majority of full text matching scenarios, <ins>it is highly recommended to use the newer and better tuned FREETEXT predicate</ins>. The CONTAINS predicate exists for backward compatibility, and should be used only on a need-basis for specific use cases. 
 
And finally, the CONTAINSSEMANTIC predicate is tuned to match the _meaning_ of the search phrases against text columns.
 
This section contains the following topics:
-   [CONTAINS Predicate](-search-sql-contains.md)
-   [FREETEXT Predicate](-search-sql-freetext.md)
-   [CONTAINSSEMANTIC Predicate](-search-sql-containssemantic.md)

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[FROM Clause](-search-sql-from.md)
</dt> <dt>

[SCOPE and DIRECTORY Predicates](-search-sql-folderdepth.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Non-Full-Text Predicates](-search-sql-nonfulltextpredicates.md)
</dt> </dl>

 

 



