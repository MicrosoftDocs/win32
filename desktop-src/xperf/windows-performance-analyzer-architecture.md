---
title: Windows Performance Analyzer Architecture
description: Windows Performance Analyzer Architecture
ms.assetid: e7cc2fbb-3e06-468a-8479-e5b65abf3a5e
keywords:
- Windows Performance Analyzer, architecture
- Windows Performance Analyzer, kernel trace control
- Windows Performance Analyzer, trace profiles
- Windows Performance Analyzer, xperf.exe
- Windows Performance Analyzer, xperfview.exe
- Windows Performance Analyzer, xbootmgr.exe
- kernel trace control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Performance Analyzer Architecture

Windows Performance Analyzer is composed of three executable programs (.exe). These programs are typically called from the command line or from a script. This table lists the programs that comprise Windows Performance Analyzer.



| Program Name                              | Function                                                                                                                                                                                            |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Xperf.exe*<br/>                    | Captures traces, processes and formats those traces. Traces can be exported to any machine that supports WPA for processing and analysis.<br/>                                                |
| *Xperf.exe* or *Xperfview.exe*<br/> | Presents trace content in the form of interactive graphs and summary tables. Note that *Xperf.exe* and *Xperfview.exe* can be used interchangeably to present graphs and summary tables.<br/> |
| *Xbootmgr.exe*<br/>                 | Automates on/off state transitions and captures traces during these transitions.<br/>                                                                                                         |



 

Additionally, certain kernel call stack data can be captured programmatically and analyzed using WPA. For more information on programmatically capturing kernel stack trace information, please see the [Kernel Trace Control](programmatically-controlling-kernel-traces.md)section of this document.

Flags, options and parameters allow customization of the output. Many of the flags and parameters have been aggregated into groups in order that the syntax does not become burdensome. A complete description of defined groups of flags, options and parameters provided with WPA is listed in feature specific areas of this document.

 

 





