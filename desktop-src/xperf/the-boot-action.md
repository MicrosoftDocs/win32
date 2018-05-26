---
title: The Boot Action
description: The Boot Action
ms.assetid: 6d0cf578-a494-4ec1-bfd8-c8551c8fe0f6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Boot Action

The boot action produces an XML report that summarizes the various metrics in boot. The following command shows the usage for this action:


```
-a boot [-minCPUToShow <n>] [-maxFilesToShow <n>]  [-expectedProcessesFile <file name>]  [-minIntervalToShow <n>] 
```





| Option                            | Description                                                                                          |
|-----------------------------------|------------------------------------------------------------------------------------------------------|
| minCPUToShow <br/>          | Minimum percentage (0-100) of CPU usage to show <br/>                                          |
| maxFilesToShow <br/>        | Maximum number of files to show <br/>                                                          |
| expectedProcessesFile <br/> | Specifies a text file that contains a list of expected process names<br/>                      |
| minIntervalToShow <br/>     | Minimum interval time (in microseconds) to show; default interval time is 10 microseconds<br/> |



 

 

 





