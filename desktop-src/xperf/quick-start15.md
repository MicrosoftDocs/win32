---
title: Quick Start
description: Quick Start
ms.assetid: '017a1659-ceeb-40b0-8b52-6de037ae7787'
keywords: ["Event Tracing for Windows", "kernel flags", "kernel groups", "NT Kernel Logger", "provider", ".etl files", "Xperfview.exe", "Xperf.exe"]
---

# Quick Start

### Introduction

The following is a brief example of using Windows Performance Analyzer (WPA) to identify factors that can influence CPU processor power usage. This example is not a complete review of WPA function or CPU power management. It is meant to give the first time user of WPA a high level overview of the product and some of the product function provided. For a complete review of WPA, see the MSDN article located at [Windows Performance Analyzer (WPA)](http://go.microsoft.com/fwlink/p/?linkid=141497). For more information on how to use CPU processor power function, see the[How To Use CPU Processor Power Management.](http://go.microsoft.com/fwlink/p/?linkid=144216)

### Terms

The following table defines WPA terms that we use in this example.



| WPA Term                                   | Usage                                                                                                                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event Tracing for Windows - ETW<br/> | A Windows infrastructure that makes kernel and application events or state changes available for collection and analysis. For more information on ETW, see [Windows Events](http://go.microsoft.com/fwlink/p/?linkid=144218).<br/> |
| Kernel Flags<br/>                    | Options enumerated when invoking Xperf.exe. These options specify what kernel events are included in the trace.<br/>                                                                                                               |
| Kernel Groups<br/>                   | Sets of options that have been logically grouped to simplify passing of kernel options to Xperf.exe.<br/>                                                                                                                          |
| NT Kernel Logger<br/>                | The NT Kernel Logger trace session generates a trace of Windows kernel events. For more information on NT Kernel Logger, see [NT Kernel Logger Trace Session](http://go.microsoft.com/fwlink/p/?linkid=144219).<br/>               |
| Provider<br/>                        | A kernel or application component that makes events available for capture.<br/>                                                                                                                                                    |
| Trace files or etl files<br/>        | Contain data produced by WPA. Individual trace files may be merged with other trace files to include events gathered in other sessions.<br/>                                                                                       |
| Xerfview.exe <br/>                   | Presents trace content in the form of interactive graphs and summary tables.<br/>                                                                                                                                                  |
| Xperf.exe <br/>                      | Captures and processes traces and supports trace analysis.<br/>                                                                                                                                                                    |



 

 

 





