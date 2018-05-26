---
title: The Difference Between KLinks and ALinks
description: Keyword links (KLinks) and Associative links (ALinks) are similar in the way that they are created and used, except for one important difference the user never sees an ALink name.
ms.assetid: E2DDF4A9-F8FF-4b61-9C21-92FEC7C08022
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Difference Between KLinks and ALinks

Keyword links (KLinks) and Associative links (ALinks) are similar in the way that they are created and used, except for one important difference: the user never sees an ALink name. Instead, in cases where more than one file contains the same ALink name, a user sees a list of topics they can choose from. Keywords, on the other hand, are always visible on the **Index** tab.

ALinks are especially useful in situations where you are merging a collection of help files. ALink names can be shared by the authors of each .chm file in the collection so that all topics with the same ALink name can be linked to. Topics with this ALink name added to the collection at a later date will also be found by the original ALinks.

ALinks and KLinks look for exact matches. A KLink will look for the exact entry you made in the index or in any KLink keywords you added to HTML files. An ALink will look for the exact entry you made when you added an ALink name to an HTML file. For example, if you add the keyword "procedure" in a KLink, but you specified "procedures" as the keyword, the topic will not be found.

## What do you want to do?

-   [Learn about working with KLinks](working-with-klinks.md)
-   [Learn about working with ALinks](working-with-alinks.md)

## Related topics

<dl> <dt>

[Working with Links](work-with-links.md)
</dt> </dl>

 

 




