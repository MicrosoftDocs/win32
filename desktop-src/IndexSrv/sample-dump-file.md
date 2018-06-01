---
Description: Sample Dump File
ms.assetid: e3109dd3-9725-411e-94e9-c1cd9675cbc8
title: Sample Dump File
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample Dump File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When requested, the Ifilttst.exe program produces a dump containing the chunks it finds and their content. Here is an excerpt from a dump file:

``` syntax
1. Chunk ID: ........... 2
2. Chunk Break Type: ... END OF SENTENCE
3. Chunk State: ........ TEXT
4. Chunk Locale: ....... 0x411
5. Chunk Source ID: .... 2
6. Chunk Start Source .. 0x0
7. Chunk Length Source . 0x0
8. GUID ................ b725f130-47ef-101a-a5f1-02608c9eebac
9. Property ID ......... 0x13
 
10. This is a HTML filter test page
 
11. Chunk ID: ........... 3
12. Chunk Break Type: ... END OF SENTENCE
13. Chunk State: ........ TEXT
14. Chunk Locale: ....... 0x411
15. Chunk Source ID: .... 2
16. Chunk Start Source .. 0x0
17. Chunk Length Source . 0x0
18. GUID ................ f29f85e0-4ff9-1068-ab91-08002b27b3d9
19. Property ID ......... 0x2
 
20. This is a HTML filter test page
 
21. Chunk ID: ........... 4
22. Chunk Break Type: ... END OF SENTENCE
23. Chunk State: ........ VALUE
24. Chunk Locale: ....... 0x411
25. Chunk Source ID: .... 2
26. Chunk Start Source .. 0x0
27. Chunk Length Source . 0x0
28. GUID ................ f29f85e0-4ff9-1068-ab91-08002b27b3d9
29. Property ID ......... 0x2
 
30. This is a HTML filter test page
```

The first nine lines describe the current chunk structure. Note that the globally unique identifier (GUID) and the property ID correspond to PSGUID\_STORAGE / PID\_STG\_CONTENTS. This is a chunk containing plain text. The text follows the chunk structure: "This is an HTML filter test page."

The next chunk, starting at line (11), has a different GUID, corresponding to the HTML filter, and a different property ID, corresponding to an HTML HREF. This is an internal value-type property, exported by the HTML filter. The next chunk, starting at line (21), has the same GUID and property ID, but its chunk state is VALUE instead of TEXT. Note that the text in these last two chunks is the same as for the first chunk. The filter wanted three attributes (plain text, HTML HREF as text, and HTML HREF as a value) to be applied to this particular phrase, so it was emitted in three separate chunks.

 

 



