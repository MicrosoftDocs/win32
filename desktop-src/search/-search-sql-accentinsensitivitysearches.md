---
description: By default, the Windows Search engine and catalog are insensitive to diacritics, which are accent marks added to letters to alter a word's meaning or pronunciation.
ms.assetid: 71007bd4-5232-469c-982b-ff0d24bd0c1f
title: Diacritic Sensitivity in Searches
ms.topic: article
ms.date: 05/31/2018
---

# Diacritic Sensitivity in Searches

By default, the Windows Search engine and catalog are insensitive to diacritics, which are accent marks added to letters to alter a word's meaning or pronunciation. However, Windows Search enables you to change this for your catalog using the [Catalog Manager](-search-3x-wds-mngidx-catalog-manager.md) to set diacritic sensitivity. For example, with diacritic sensitivity set to **FALSE**, the catalog would treat "resume" and "resumé" as if they were the same word.

At the query layer, query terms with diacritics in FREETEXT and CONTAINS clauses are passed through to the engine and are then normalized (as they would be at index time) for matching. Matching against the catalog is always diacritic sensitive.

> [!Note]  
> This is not the case for the character ranges 0x2e81-f8ff and 0x1100-0x11ff.

 

 

 



