---
title: The Stack Action
description: The Stack Action
ms.assetid: 14e30edb-1f1b-44e8-ba9a-1d8453d13837
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Stack Action

The stack action produces a text file that summarizes the various metrics regarding stacks. The usage for this action is:


```
-a stack [-butterfly [<min_hits>]] 
         [-export <format>]  
         [-pid <pid> ...] 
         [-tid <tid> ...]  
         [-process <process_name_regex> ...]  
         [-symbol <symbol_name_regex> ...]  
         [-event <event_name_regex> ...] 
```





| Option                                               | Description                                                                                                                                                                                           |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| butterfly \[&lt;min\_hits&gt;\] <br/>          | Display the butterfly view of stacks in this trace, including only symbols that have at least &lt;min\_hits&gt; uni-inclusive/multi-inclusive hits. The default is &lt;min\_hits&gt; = 10.<br/> |
| -range lo \[hi\] <br/>                         | Limit report to interval \[lo, hi\]. (Default: lo = 0; hi = \_I64\_MAX)<br/>                                                                                                                    |
| pid &lt;pid&gt; ... <br/>                      | Include only stacks from processes with matching process ID <br/>                                                                                                                               |
| tid &lt;tid&gt; ... <br/>                      | Include only stacks from threads with matching thread ID<br/>                                                                                                                                   |
| process &lt;process\_name\_regex&gt; ... <br/> | Include only stacks from processes with matching name <br/>                                                                                                                                     |
| symbol &lt;symbol\_name\_regex&gt; ... <br/>   | Include only stacks that contain symbols with matching name<br/>                                                                                                                                |
| event &lt;event\_name\_regex&gt; ... <br/>     | Include only stacks for events with matching name<br/>                                                                                                                                          |



 

 

 





