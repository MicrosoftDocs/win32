---
title: WPA Heap Glossary
description: WPA Heap Glossary
ms.assetid: '41525136-b170-4ade-a6db-63a9fc821285'
---

# WPA Heap Glossary



| WPA Term                               | Usage                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AI, AO<br/>                      | Identifies allocations done inside and outside a time based analysis selection.<br/> AI refers to allocations that are made within the selection. <br/> AO refers to allocations that are made before the selection but were outstanding for some portion of the selection.<br/>          |
| FI, FO<br/>                      | Identifies allocations that have been freed within the time based selection.<br/> FI refers to allocations that are released within the selection. <br/> FO refers to allocations that are released outside of the selection but were outstanding for some portion of the selection.<br/> |
| AIFI<br/>                        | Allocations that were made and released within the time based selection.<br/>                                                                                                                                                                                                                         |
| AIFO<br/>                        | Allocations that were made within the selection and remain outstanding at the end of the time based selection.<br/>                                                                                                                                                                                   |
| AOFI<br/>                        | Allocations that were made before the selection but released before the end of the time based selection.<br/>                                                                                                                                                                                         |
| AOFO<br/>                        | Allocations that were made before the selection and remain outstanding at the end of the time based selection.<br/>                                                                                                                                                                                   |
| Heap Allocation Count<br/>       | The sum of the outstanding allocations per heap.<br/>                                                                                                                                                                                                                                                 |
| Heap Allocation Size<br/>        | The sum of the outstanding sizes of all of the allocations per heap and total across all heaps. The sizes or sums do not include the 8 bytes of heap overhead per allocation or the rounding of the allocation to the size of the LFH bucket or 8 byte boundary.<br/>                                 |
| Heap Total Allocation Count<br/> | This is the sum of all allocations by count per heap and the total across all heaps.<br/>                                                                                                                                                                                                             |
| Heap Total Allocation Size<br/>  | This is the sum of the sizes of all of the allocations per heap and total across all heaps. The sizes or sums do not include the 8 bytes of heap overhead per allocation or the rounding of the allocation to the size of the LFH bucket or 8 byte boundary.<br/>                                     |
| Kernel Flags (options)<br/>      | Specify what kernel events are to be included in the trace.<br/>                                                                                                                                                                                                                                      |
| Kernel Groups<br/>               | Sets of options that have been logically grouped in order to simplify passing of kernel options to *Xperf.exe* .<br/>                                                                                                                                                                                 |
| Logger Session<br/>              | The data collection facility that captures events and stores those events for analysis.<br/>                                                                                                                                                                                                          |
| NT Kernel Logger<br/>            | The default data collection logger for WPA that captures a trace of Windows kernel events. For more information on NT Kernel Logger please see [Loggers](loggers.md).<br/>                                                                                                                           |
| Outstanding<br/>                 | Refers to those allocations that have not been released at that point in the trace. <br/>                                                                                                                                                                                                             |
| Provider<br/>                    | A kernel or application component that makes events available for capture.<br/>                                                                                                                                                                                                                       |
| Trace files or "etl" files<br/>  | Files containing data produced by WPA. Individual trace files may be merged in order to include events gathered in other sessions.<br/>                                                                                                                                                               |
| *Xperf.exe* <br/>                | WPA component which captures and processes traces and supports trace analysis. *Xperf.exe* can be used in place of *Xperfview.exe*.<br/>                                                                                                                                                              |
| *Xperfview.exe*<br/>             | WPA component which presents trace content in the form of interactive graphs and summary tables.<br/>                                                                                                                                                                                                 |



 

 

 





