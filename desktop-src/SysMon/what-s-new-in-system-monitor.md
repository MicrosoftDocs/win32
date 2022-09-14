---
title: What's New in System Monitor
description: The following table identifies what is new for each release of System Monitor (SYSMON).
ms.assetid: 9cb0e0db-0933-4993-a995-74a36a24eccb
ms.topic: article
ms.date: 05/31/2018
---

# What's New in System Monitor

The following table identifies what is new for each release of System Monitor (SYSMON).



| Version     | Description of features                                                                                                                                                                                                                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version 3.7 | This version adds new graph types, the ability to select multiple counters, retrieve counter values from a point on the graph, save graphed counter values to a log file, and the option to have a line graph continuously scroll in the graph window instead of wrap-around on itself.Included in Windows Server 2008 and Windows Vista.<br/> |



 

## Version 3.7

New properties and methods that were added to [**CounterItem**](counteritem.md).

-   [**GetDataAt**](counteritem-getdataat.md)
-   [**Selected**](counteritem-selected.md)
-   [**Visible**](counteritem-visible.md)
-   Range of valid values changed for [**CounterItem.Width**](counteritem-width.md)

New properties and methods that were added to [**SystemMonitor**](systemmonitor.md).

-   [**BatchingLock**](systemmonitor-batchinglock.md)
-   [**ChartScroll**](systemmonitor-chartscroll.md)
-   [**ClearData**](systemmonitor-cleardata.md)
-   [**DataPointCount**](systemmonitor-datapointcount.md)
-   [**EnableDigitGrouping**](systemmonitor-enabledigitgrouping.md)
-   [**EnableToolTips**](systemmonitor-enabletooltips.md)
-   [**GetLogViewRange**](systemmonitor-getlogviewrange.md)
-   [**LoadSettings**](systemmonitor-loadsettings.md)
-   [**LogSourceStartTime**](systemmonitor-logsourcestarttime.md)
-   [**LogSourceStopTime**](systemmonitor-logsourcestoptime.md)
-   [**Relog**](systemmonitor-relog.md)
-   [**SaveAs**](systemmonitor-saveas.md)
-   [**ScaleToFit**](systemmonitor-scaletofit.md)
-   [**SetLogViewRange**](systemmonitor-setlogviewrange.md)
-   [**ShowTimeAxisLables**](systemmonitor-showtimeaxislabels.md)

New enumerations that were added.

-   [**SysmonDataType**](/windows/win32/api/isysmon/ne-isysmon-sysmondatatype)
-   [**SysmonFileType**](/windows/win32/api/isysmon/ne-isysmon-sysmonfiletype)
-   New display type values were added to [**DisplayTypeConstants**](/windows/win32/api/isysmon/ne-isysmon-displaytypeconstants)

 

 





