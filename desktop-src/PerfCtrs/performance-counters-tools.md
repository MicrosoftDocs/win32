---
description: The following table lists the
ms.assetid: 3f47a52c-2d36-4a74-9d7f-df37645b8e72
title: Performance Counters Tools
ms.topic: article
ms.date: 08/17/2020
---

# Performance Counters Tools

## Data collection tools

The following tools are useful when consuming or manipulating Windows Performance Counter data.

|Tool|Description
|----|-----------
| [PerfMon](/windows-server/administration/windows-commands/perfmon) | GUI tool for collecting and viewing Performance Counter data. `perfmon.exe` launches MMC with the Performance Monitor snap-in, which provides access to the Performance Monitor, Data Collector Sets, and Reports tools.
| [TypePerf](/windows-server/administration/windows-commands/typeperf) |Command-line tool for collecting and printing Performance Counter data. Can be used to list available countersets, list available counters, print counter data to the console, or collect counter data to a log file (CSV, TDF, BLG).
| [Relog](/windows-server/administration/windows-commands/relog) |Command-line tool for transforming and merging log files (CSV, TDF, BLG) captured via `typeperf.exe` or via the `PDH.dll` APIs.
| [LogMan](/windows-server/administration/windows-commands/logman) |Command-line tool for controlling Data Collector Sets.

## Data provider tools

The following tools are useful when publishing Windows Performance Counter data.

|Tool|Description
|----|-----------
| [CtrPP](ctrpp.md) | Command-line build tool from the Windows SDK that validates and compiles your Performance Counters V2 provider manifest. This tool generates the `.h` headers and `.rc` resource scripts needed to build a V2 provider.
| [LodCtr](/windows-server/administration/windows-commands/lodctr) | Command-line tool used to install your provider onto a system.
| [UnlodCtr](/windows-server/administration/windows-commands/unlodctr_1) | Command-line tool used to uninstall your provider from a system.
