---
description: You can use the Logman tool to collect tracing information for VSS applications that use Automated System Recovery (ASR).
ms.assetid: 872609c8-a123-40a8-96ca-58f34d37f3d8
title: Using Tracing Tools with ASR Applications
ms.topic: article
ms.date: 05/31/2018
---

# Using Tracing Tools with ASR Applications

You can use the Logman tool to collect tracing information for VSS applications that use [Automated System Recovery (ASR)](using-vss-automated-system-recovery-for-disaster-recovery.md). Logman (logman.exe) is a trace controller for trace events and performance counters. It is included in Windows XP and later versions of Windows. Or, if you prefer, you can use the Tracelog tool to collect the same ASR tracing information. Tracelog is included in the Windows Driver Kit (WDK).

To use tracing tools with VSS, see [Using Tracing Tools with VSS](using-tracing-tools-with-vss.md).

## Using Logman

The following procedure describes how to use Logman with your ASR application.

**To use Logman with your ASR application**

1.  Use the following command to start tracing:

    **logman start asr -o** *x:\\***asr.etl -ets -p {6407345b-94f2-44c8-b3db-4e076be46816} 0xff 0xff**

    > [!Note]  
    > Replace "x:\\" with the path to the directory where you would like the trace log file to be stored. For best performance, the trace log file should be located on a volume that is not part of the shadow copy.

     

2.  Use the following command to stop tracing:

    **logman stop asr -ets**

The trace log file is *x:\\*asr.etl.

For more information about the Logman tool, see [Logman](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc753820(v=ws.11)).

## Using Tracelog

The following procedure describes how to use Tracelog.

**To use Tracelog**

1.  Create a text file named asr.ctl that contains only the following text:

    **6407345b-94f2-44c8-b3db-4e076be46816 asr**

2.  Use the following command to start tracing:

    **tracelog -start asr -f** *x:\\***asr.etl -guid asr.ctl -flag 0xff -level 0xff**

    > [!Note]  
    > Replace "x:\\" with the path to the directory where you would like the trace log file to be stored. For best performance, the trace log file should be located on a volume that is not part of the shadow copy.

     

3.  Use the following command to stop tracing:

    **tracelog -stop asr**

The trace log file is *x:\\*asr.etl.

For more information about the Tracelog tool, see [Tracelog](https://msdn.microsoft.com/library/ms797927.aspx).

 

 
