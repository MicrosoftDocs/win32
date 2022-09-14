---
description: Uniscribe provides APIs to support typography and to support the display and editing of international text, including the complex rules of Middle Eastern and Asian scripts.
ms.assetid: d27e82df-ee97-4f55-bfab-0d1e10eaa1b7
title: Using Uniscribe
ms.topic: article
ms.date: 05/31/2018
---

# Using Uniscribe

Uniscribe provides APIs to support typography and to support the display and editing of international text, including the complex rules of Middle Eastern and Asian scripts. Uniscribe provides low-level routines for handling fully formatted text, and a simple ScriptString API set for unformatted text.

Using Uniscribe, applications only have to manage a backing store of Unicode character codes. Text layout applications do not have to maintain any other buffer or mapping table to track character order. Each application only has to store and manage the order in which the characters are entered by the user, which is the same logical order as defined by Unicode. The backing store never changes as a result of layout operations. Uniscribe maintains an index from the reordered clusters to the original character boundaries passed by the application.

The following topics are covered in this section.

**Shaping**

-   [Determining If a Script Requires Glyph Shaping](determining-if-a-script-requires-glyph-shaping.md)
-   [Using Shaping Engines](using-shaping-engines.md)

**Other Processing**

-   [Caching](caching.md)
-   [Displaying Text with Uniscribe](displaying-text-with-uniscribe.md)
-   [Processing Complex Scripts](processing-complex-scripts.md)
-   [Using Font Fallback](using-font-fallback.md)
-   [Using the ScriptString Functions](using-the-scriptstring-functions.md)

**Caret**

-   [Displaying the Caret in Bidirectional Strings](displaying-the-caret-in-bidirectional-strings.md)
-   [Managing Caret Placement and Hit Testing](managing-caret-placement-and-hit-testing.md)
-   [Translating Mouse Hit X Offset to Caret Position](translating-mouse-hit-x-offset-to-caret-position.md)

**Words and Character Clusters**

-   [Using Character Clusters](using-character-clusters.md)
-   [Using Word Break Points](using-word-break-points.md)
-   [Working with Relationships Among Caret Positions, Justification Points, and Clusters](working-with-relationships-among-caret-positions--justification-points--and-clusters.md)

 

 



