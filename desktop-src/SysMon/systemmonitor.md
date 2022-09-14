---
title: SystemMonitor object (Isysmon.h)
description: This class contains the methods and properties used to configure the System Monitor control.
ms.assetid: 5a6195ee-ed89-4f5d-85dd-88cf4a9b5155
keywords:
- SystemMonitor object SysMon
- SystemMonitor object SysMon , described
topic_type:
- apiref
api_name:
- SystemMonitor
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor object

This class contains the methods and properties used to configure the System Monitor control.

## Members

The **SystemMonitor** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **SystemMonitor** object has these events.



| Event                                                         | Description                                                                                                                 |
|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**OnCounterAdded**](systemmonitor-oncounteradded.md)        | Notifies you when a counter is added to the [**Counters**](counters.md) collection.<br/>                             |
| [**OnCounterDeleted**](-systemmonitor-oncounterdeleted.md)   | Notifies you before a counter is deleted from the [**Counters**](counters.md) collection.<br/>                       |
| [**OnCounterSelected**](-systemmonitor-oncounterselected.md) | Notifies you when a counter is selected.<br/>                                                                         |
| [**OnDblClick**](-systemmonitor-ondblclick.md)               | Notifies you when a user double-clicks the graph line, histogram bar, or report item with the left mouse button.<br/> |
| [**OnSampleCollected**](-systemmonitor-onsamplecollected.md) | Notifies you when sample values for the counters have been collected.<br/>                                            |



 

### Methods

The **SystemMonitor** object has these methods.



| Method                                                       | Description                                                                                                                                                              |
|:-------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BatchLocking**](systemmonitor-batchinglock.md)           | Locks the System Monitor to prevent it from sampling counter data from the newly added counter or log file.<br/>                                                   |
| [**BrowseCounters**](systemmonitor-browsecounters.md)       | Displays the **Add Counter** dialog box.<br/>                                                                                                                      |
| [**ClearData**](systemmonitor-cleardata.md)                 | Clears all data fields in the control.<br/>                                                                                                                        |
| [**CollectSample**](systemmonitor-collectsample.md)         | Samples a value for each counter in the **Counters** collection object.<br/>                                                                                       |
| [**Copy**](systemmonitor-copy.md)                           | Copies the control's property settings, list of counters, and counter data to the clipboard as an HTML object.<br/>                                                |
| [**DisplayProperties**](systemmonitor-displayproperties.md) | Displays the **Graph Properties** dialog box.<br/>                                                                                                                 |
| [**GetLogViewRange**](systemmonitor-getlogviewrange.md)     | Retrieves the starting date used to retrieve counter values from the log files.<br/>                                                                               |
| [**LoadSettings**](systemmonitor-loadsettings.md)           | Adds the counters in the HTML template file to the System Monitor.<br/>                                                                                            |
| [**Paste**](systemmonitor-paste.md)                         | Appends the list of counters that were copied to the clipboard to the current collection of counters. <br/>                                                        |
| [**Relog**](systemmonitor-relog.md)                         | Relogs the counter data to a new file. You can also use this method to specify a new file type and to reduce the number of samples contained in the log file.<br/> |
| [**Reset**](systemmonitor-reset.md)                         | Removes all [**CounterItem**](counteritem.md) objects from the **Counters** collection object.<br/>                                                               |
| [**SaveAs**](systemmonitor-saveas.md)                       | Saves the counter values in the graph view to a log file.<br/>                                                                                                     |
| [**ScaleToFit**](systemmonitor-scaletofit.md)               | Scale counter values to fit in the graph.<br/>                                                                                                                     |
| [**SetLogViewRange**](systemmonitor-setlogviewrange.md)     | Sets the starting date used to retrieve counter values from the log files.<br/>                                                                                    |
| [**UpdateGraph**](systemmonitor-updategraph.md)             | Refreshes the contents of the System Monitor windows.<br/>                                                                                                         |



 

### Properties

The **SystemMonitor** object has these properties.



| Property                                                                                | Description                                                                                                                                                                                                                             |
|:----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Appearance**](systemmonitor-appearance.md)<br/>                               | Retrieves or sets the appearance of the control to include or omit three-dimensional display effects.<br/>                                                                                                                        |
| [**BackColor**](systemmonitor-backcolor.md)<br/>                                 | Retrieves or sets the background color of the graph and report views.<br/>                                                                                                                                                        |
| [**BackColorCtl**](systemmonitor-backcolorctl.md)<br/>                           | Retrieves or sets the background color of the control.<br/>                                                                                                                                                                       |
| [**BorderStyle**](systemmonitor-borderstyle.md)<br/>                             | Retrieves or sets the border style of the control.<br/>                                                                                                                                                                           |
| [**ChartScroll**](systemmonitor-chartscroll.md)<br/>                             | Retrieves or sets a value that determines if the line graph scrolls in the view.<br/>                                                                                                                                             |
| [**Counters**](systemmonitor-counters.md)<br/>                                   | Retrieves the collection of [**CounterItem**](counteritem.md) objects.<br/>                                                                                                                                                      |
| [**DataPointCount**](systemmonitor-datapointcount.md)<br/>                       | Retrieves or sets the number of data points displayed in a line graph.<br/>                                                                                                                                                       |
| [**DataSourceType**](systemmonitor-datasourcetype.md)<br/>                       | Retrieves or sets the source of the performance counter data.<br/>                                                                                                                                                                |
| [**DisplayType**](systemmonitor-displaytype.md)<br/>                             | Retrieves or sets the type of graph used to graph the performance counter data.<br/>                                                                                                                                              |
| [**EnableDigitGrouping**](systemmonitor-enabledigitgrouping.md)<br/>             | Retrieves or sets a value that determines if SYSMON uses digit grouping when displaying numeric values.<br/>                                                                                                                      |
| [**EnableToolTips**](systemmonitor-enabletooltips.md)<br/>                       | Retrieves or sets a value that determines if a tool tip is shown when the mouse hovers over a counter in one of the graph views.<br/>                                                                                             |
| [**Font**](systemmonitor-font.md)<br/>                                           | Retrieves or sets the font used in the control.<br/>                                                                                                                                                                              |
| [**ForeColor**](systemmonitor-forecolor.md)<br/>                                 | Retrieves or sets the color of the text that appears in the control.<br/>                                                                                                                                                         |
| [**GraphTitle**](systemmonitor-graphtitle.md)<br/>                               | Retrieves or sets the title of the graph.<br/>                                                                                                                                                                                    |
| [**GridColor**](systemmonitor-gridcolor.md)<br/>                                 | Retrieves or sets the color of the grid lines used in the graph.<br/>                                                                                                                                                             |
| [**Highlight**](systemmonitor-highlight.md)<br/>                                 | Retrieves or sets a value indicating whether the values of the selected counters are highlighted in the graph.<br/>                                                                                                               |
| [**LogFileName**](systemmonitor-logfilename.md)<br/>                             | Obsolete. Retrieves or sets the name of a log file to use as the source of counter values displayed in the System Monitor.<br/>                                                                                                   |
| [**LogFiles**](systemmonitor-logfilename.md)<br/>                                | Collection of one or more log files to use as the source of counter values displayed in the System Monitor.<br/>                                                                                                                  |
| [**LogSourceStartTime**](systemmonitor-logsourcestarttime.md)<br/>               | Retrieves the time stamp of the earliest counter value from a counter in your counter collection that was logged in the log files.<br/>                                                                                           |
| [**LogSourceStopTime**](systemmonitor-logsourcestoptime.md)<br/>                 | Retrieves the time stamp of the latest counter value from a counter in your counter collection that was logged in the log files.<br/>                                                                                             |
| [**LogViewStart**](systemmonitor-logviewstart.md)<br/>                           | Retrieves or sets the starting date used to retrieve counter values from the log files.<br/>                                                                                                                                      |
| [**LogViewStop**](systemmonitor-logviewstop.md)<br/>                             | Retrieves or sets the ending date used to retrieve counter values from the log files.<br/>                                                                                                                                        |
| [**ManualUpdate**](systemmonitor-manualupdate.md)<br/>                           | Retrieves or sets a value indicating whether the contents of the System Monitor will be updated manually, or automatically at specified intervals.<br/>                                                                           |
| [**MaximumScale**](systemmonitor-maximumscale.md)<br/>                           | Retrieves or sets the maximum value of the vertical (Y) axis of the graph.<br/>                                                                                                                                                   |
| [**MinimumScale**](systemmonitor-minimumscale.md)<br/>                           | Retrieves or sets the minimum value of the vertical (Y) axis of the graph.<br/>                                                                                                                                                   |
| [**MonitorDuplicateInstances**](systemmonitor-monitorduplicateinstances.md)<br/> | Retrieves or sets a value that determines whether multiple instances of a counter can be monitored.<br/>                                                                                                                          |
| [**ReadOnly**](systemmonitor-readonly.md)<br/>                                   | Retrieves or sets a value that determines whether a user can modify the property values of the control.<br/>                                                                                                                      |
| [**ReportValueType**](systemmonitor-reportvaluetype.md)<br/>                     | Retrieves or sets a value that determines if the Histogram and Report views graph the last value sampled during the sampling interval or a calculated value from the sampling, such as the average or minimum counter value.<br/> |
| [**ShowHorizontalGrid**](systemmonitor-showhorizontalgrid.md)<br/>               | Retrieves or sets a value that determines whether horizontal grid lines are displayed in the graph.<br/>                                                                                                                          |
| [**ShowLegend**](systemmonitor-showlegend.md)<br/>                               | Retrieves or sets a value that determines whether the legend is displayed.<br/>                                                                                                                                                   |
| [**ShowScaleLabels**](systemmonitor-showscalelabels.md)<br/>                     | Retrieves or sets a value that determines whether the scale labels are displayed on the vertical axis of the graph.<br/>                                                                                                          |
| [**ShowTimeAxisLabels**](systemmonitor-showtimeaxislabels.md)<br/>               | Retrieves or sets a value that determines if the horizontal (X) axis of the graph view contains labels.<br/>                                                                                                                      |
| [**ShowToolbar**](systemmonitor-showtoolbar.md)<br/>                             | Retrieves or sets a value that determines whether the toolbar is displayed on the control.<br/>                                                                                                                                   |
| [**ShowValueBar**](systemmonitor-showvaluebar.md)<br/>                           | Retrieves or sets a value that determines whether the value bar (the set of statistical values below the graph) is displayed on the control.<br/>                                                                                 |
| [**ShowVerticalGrid**](systemmonitor-showverticalgrid.md)<br/>                   | Retrieves or sets a value that determines whether vertical grid lines are displayed in the graph.<br/>                                                                                                                            |
| [**SqlDsnName**](systemmonitor-sqldsnname.md)<br/>                               | Retrieves or sets the ODBC data source name.<br/>                                                                                                                                                                                 |
| [**SqlLogSetName**](systemmonitor-sqllogsetname.md)<br/>                         | Retrieves or sets the friendly name of the log set.<br/>                                                                                                                                                                          |
| [**TimeBarColor**](systemmonitor-timebarcolor.md)<br/>                           | Retrieves or sets the color of the time bar (the vertical bar that moves across the graph window to indicate the passage of each sampling interval in the line graph view).<br/>                                                  |
| [**UpdateInterval**](systemmonitor-updateinterval.md)<br/>                       | Retrieves or sets the length of time that SYSMON waits before the next time it updates the graph or report.<br/>                                                                                                                  |
| [**YAxisLabel**](systemmonitor-yaxislabel.md)<br/>                               | Retrieves or sets the label of the vertical (Y) axis of the graph.<br/>                                                                                                                                                           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Isysmon.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





