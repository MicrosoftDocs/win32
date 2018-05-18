---
title: About the Stream Buffer Engine
description: About the Stream Buffer Engine
ms.assetid: '138e36f4-fb0f-4b02-ae1b-f003a6ada7e5'
---

# About the Stream Buffer Engine

This topic applies to Windows XP Service Pack 1 or later.

The Stream Buffer Engine uses two or more independent filter graphs. One filter graph, called the *sink* graph, captures data from a live source. The other graphs, called *source* graphs, render the data. Using several filter graphs is more flexible and scalable than using a single graph for both capture and rendering. The sink graph stores the data in a temporary buffer or in permanent files, while the source graphs read the data from those files. Several source graphs can read data from the same sink source.

A source graph can:

-   Seek forward or backward within the stored content.
-   Pause playback, without interrupting the data coming from the capture graph.
-   Play faster or slower than normal.
-   Play in reverse.

Tasks such as scheduling a viewing session or a recording session are left to the client application.

 

 




