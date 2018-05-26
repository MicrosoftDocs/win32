---
title: Indexing Text-Type and Value-Type Properties
description: Indexing Text-Type and Value-Type Properties
ms.assetid: 187e0142-8508-4779-96af-e8c60a8a0b8d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Indexing Text-Type and Value-Type Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service indexes all text-type properties using their associated, unformatted text. The unformatted text undergoes word breaking and noise-word removal before eventually being merged into the master index of the catalog. Text-type properties are entered as words in the index along with their name, so that queries for text selected by property name are possible.

Indexing Service indexes value-type properties according to their data type identifiers.

-   Properties with a textual data type are indexed identically to text-type properties. Textual data type identifiers are: VT\_LPSTR, VT\_LPWSTR, VT\_BSTR, and combinations of these made by a logical OR operation with VT\_VECTOR.
-   Properties with a non-textual data type are indexed similarly to text-type properties using the appropriate data type and the data value of the property. Non-textual data type identifiers include: VT\_I4, VT\_I8, VT\_R8, VT\_DATE, and others.

 

 




