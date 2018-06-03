---
title: Process Heap Actions
description: Process Heap Actions
ms.assetid: b555f1e6-14ae-4381-b3b9-1d9a1e47f4ba
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Heap Actions

Xperf actions are trace processing components that format trace files to produce text reports, csv files and xml files. Actions are designed to produce summarized reports that are specific to a set of events, in this case, heap events.

Actions are all invoked with the same command line pattern:

``` syntax
xperf -I input.etl -o output.txt -a action name [action parameters]...
```

Where &lt;action name&gt; is the name of the action. This is always preceded by the '-a' command line switch. The action name can be followed by one or more action specific parameters.

 

 




