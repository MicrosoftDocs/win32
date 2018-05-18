---
title: profile
description: Displays the profile options.
ms.assetid: 'f45cad0b-2479-472b-a513-6ecf06b605bb'
keywords: ["profile Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- profile
api_type:
- NA
---

# profile

Displays the profile options.

``` syntax
Action invocation:
xperf -i <trace file> ... [-o <output>] -a profile

Action help:
profile [-util [n]] [-detail] [-range T1 [T2]]
```

## Parameters

<dl> <dt>

<span id="-util__n__"></span><span id="-UTIL__N__"></span>-util \[n\] 
</dt> <dd>

Show CPU utilization for n second intervals, the default is one second.

</dd> <dt>

<span id="-detail_______"></span><span id="-DETAIL_______"></span>-detail 
</dt> <dd>

Show CPU samples bucketed by process and module if symbol decoding is not enabled and by process and function name if symbol decoding is enabled.

</dd> <dt>

<span id="-range_T1__T2__"></span><span id="-range_t1__t2__"></span><span id="-RANGE_T1__T2__"></span>-range T1 \[T2\] 
</dt> <dd>

Show data between times T1 and T2, both in us. If T2 is not present, the end of the trace is used instead.

</dd> <dt>

<span id="-freq_________"></span><span id="-FREQ_________"></span>-freq 
</dt> <dd>

Show constant sampling frequency zones in the trace.

</dd> </dl>

### Comments

If no report type is selected, the default is to show CPU utilization report.

Use the command **xperf-help symbols** for help on how to enable symbol decoding.

 

 




