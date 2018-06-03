---
title: Quick Start ReadyBoot Graphs
description: Quick Start ReadyBoot Graphs
ms.assetid: 8e2009ef-b906-4c03-ad13-b8eb333ed1a9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quick Start: ReadyBoot Graphs

For information on collecting ReadyBoot trace data please see the [Quick Start: Capturing ReadyBoot Information](quick-start--capturing-readyboot-information.md) section of this document.

To view the ReadyBoot graph, open the trace as described in the previous section, [Quick Start: Opening the Trace](quick-start--opening-the-trace.md).

1.  Open the Frame List, located on the left side of the graph, by clicking the chevron.

2.  Ensure the "ReadyBoot I/O" selection is checked.

3.  Close the Frame List by clicking the chevron again.

4.  Scroll to the **ReadyBoot I/O** graph.

5.  Place the cursor on the time line.

6.  Select an approximate time interval in which the ReadyBoot events appear, in this case from about 0 to 30 seconds, by left clicking and dragging from 0 to 30 on the time line. The selection will be highlighted.

7.  Right click on on the highlighted selection to open the context menu and select **Zoom to Selection**.

The time interval selected will be applied to all of the graphs. This feature provides a consistent view of the time interval being examined across all the graphs, as in the following screen shot.

![screen shot of a readyboot i/o graph showing a readyboot events-counts histogram](images/rb-01.png)

The **ReadyBoot I/O** graph shows a histogram of ReadyBoot event counts colored by the event type for a selected time period. The dropdown legend menu in the top right corner can be used to filter displayed events by type.

 

 




