---
title: Quick Start Example
description: Quick Start Example
ms.assetid: 'cc183f1c-3ba7-4630-85ea-72d86353cc06'
---

# Quick Start Example

This example creates a directory for symbols and the xperf SymCache, sets the symbol path to use a local cache and the Microsoft public symbol server, traces heap allocations for notepad.exe, creates 2 summary reports, and launches the xperf viewer.


```
if not exist c:\TestSymbols md c:\TestSymbols
if not exist c:\TestSymCache md c:\TestSymCache
if not exist TestCullFuncs.txt echo. >TestCullFuncs.txt

set _NT_SYMBOL_PATH=srv*c:\TestSymbols*http://msdl.microsoft.com/download/symbols;
set _NT_SYMCACHE_PATH=c:\TestSymCache

xperf -on base -buffersize 64 -minbuffers 1024 -maxbuffers 1024
xperf -start HeapSession -heap -PidNewProcess "notepad.exe" -stackwalk HeapCreate+HeapAlloc+HeapRealloc -BufferSize 64 -MinBuffers 2048 -MaxBuffers 2048
pause
xperf -stop "NT Kernel Logger" -stop HeapSession -d HeapTrace.etl

xperf -i HeapTrace.etl -o HeapTrace_Frames_tot.txt -symbols verbose dbghelplog -a heap -frames st -cullLists TestCullFuncs.txt -top 20
xperf -i HeapTrace.etl -o HeapTrace_Frames_out.txt -symbols verbose dbghelplog -a heap -frames so -cullLists TestCullFuncs.txt -top 20
xperf -i HeapTrace.etl -o HeapTrace_Stacks_tot.txt -symbols verbose dbghelplog -a heap -stacks st -cullLists TestCullFuncs.txt -top 20
xperf -i HeapTrace.etl -o HeapTrace_Stacks_out.txt -symbols verbose dbghelplog -a heap -stacks so -cullLists TestCullFuncs.txt -top 20

xperfview HeapTrace.etl
```



 

 




