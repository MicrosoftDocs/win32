---
title: The Boot Prefetch Action
description: The Boot Prefetch Action
ms.assetid: '29d15d03-d901-4104-b3f1-c2b621f4a17d'
---

# The Boot Prefetch Action

The Boot Prefetch action collates and summarizes events relevant to boot when using On/Off Trace Capture Tool.


```
 xperf -i <trace file> ... [-o <output>] -a bootprefetch ...
```





| Option               | Description                                                      |
|----------------------|------------------------------------------------------------------|
| -summary<br/>  | Show the summary of boot prefetching<br/>                  |
| -events<br/>   | Dump ReadyBoot events with earliness information<br/>      |
| -disktime<br/> | Show the disk time breakdown during boot prefetching.<br/> |



 

If the -events option is used the -pattern option may be used



| Option               | Description                                                 |
|----------------------|-------------------------------------------------------------|
| -pattern <br/> | Dump also overlapping events when dumping events<br/> |



 

If the -pattern option is used, -type name may be used.



| Option                | Description                                                                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -type name<br/> | Dump only specific type of events when dumping events in pattern view<br/> name is one of the five types: hit, prefetch, miss, pend, and write<br/> |



 

If the -events option is used the -range option may be used.



| Option                  | Description                                                            |
|-------------------------|------------------------------------------------------------------------|
| -range t1 t2<br/> | Process ReadyBoot events completed between times T1 and T2.<br/> |



 

If no report type is selected, default is to show the summary.

 

 





