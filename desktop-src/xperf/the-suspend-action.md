---
title: The Suspend Action
description: The Suspend Action
ms.assetid: '5f23842b-5870-4a58-8872-cc3c03e03800'
---

# The Suspend Action

The suspend action produces an XML file that summarizes the various metrics regarding the suspend sequence. The usage for this action is:


```
-a suspend [-summary] [-timeunit <unit> [<precision>]]  [-min <duration>]
```





| Option                                                  | Description                                                                                                                                              |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| summary <br/>                                     | Display the suspend transitions in this trace <br/>                                                                                                |
| timeunit &lt;unit&gt; \[&lt;precision&gt;\] <br/> | Configure time presentation to use time unit &lt;unit&gt; and time precision &lt;precision&gt;. The units for time include ns, us, ms, and s <br/> |
| min &lt;duration&gt; <br/>                        | Only show individual timings longer or equal to &lt;duration&gt;<br/>                                                                              |



 

If no activity is selected, summary is selected by default.

 

 





