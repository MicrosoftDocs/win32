---
title: The PreFetch Action
description: The PreFetch Action
ms.assetid: '098b9b6e-8953-459e-9381-3e681bfb93f0'
---

# The PreFetch Action

The PreFetch action produces a text file that summarizes the various metrics regarding context switches. The usage for this action is:


```
-a prefetch [-summary] 
            [-timeunit <unit> [<precision>]]
            [-min <duration>] 
```





| Option                                                  | Description                                                                                                                                  |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| summary <br/>                                     | Display the prefetch scenarios in this trace <br/>                                                                                     |
| timeunit &lt;unit&gt; \[&lt;precision&gt;\] <br/> | Configure time presentation to use time unit &lt;unit&gt; and time precision &lt;precision&gt;. The units can be ns, us, ms, or s<br/> |
| min &lt;duration&gt; <br/>                        | Only show individual timings longer or equal to &lt;duration&gt; <br/>                                                                 |



 

If no activity is selected, summary is selected by default.

 

 





