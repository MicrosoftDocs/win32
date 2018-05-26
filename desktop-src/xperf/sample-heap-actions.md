---
title: Sample Heap Actions
description: Sample Heap Actions
ms.assetid: b87f70af-2429-4601-b99f-f997af5f226a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sample Heap Actions

The action command:


```
xperf -I heapSession.etl -o output.txt -a heap  
```



Writes a text file containing the output of a sample heap action, as shown in the following screen shot.

![screen shot of a notepad window listing the output of a sample heap action](images/he-img30.png)

The action command:


```
xperf -I heapSession.etl -o frames.txt -symbols -a heap -stacks -cullLists cullfuncs.txt -top 25
```



This action may take several minutes to complete due to the heavy sorting and matching performed on large trace file. Frames listed in the cullfuncs.txt file will be deleted from the results, as shown in the following screen shot:

![screen shot of a notepad window listing a heap action limited to the top twenty-five allocations and culled for superfluous frames](images/he-img29.png)

 

 




