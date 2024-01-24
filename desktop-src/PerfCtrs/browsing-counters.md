---
description: To display a dialog box that lists the performance objects and counters defined on the computer, call the PdhBrowseCounters function.
ms.assetid: f2fac1d3-f643-43c9-a445-112015baecdd
title: Browsing Counters
ms.topic: article
ms.date: 05/31/2018
---

# Browsing Counters

To display a dialog box that lists the performance objects and counters defined on the computer, call the [**PdhBrowseCounters**](/windows/desktop/api/Pdh/nf-pdh-pdhbrowsecountersa) function. The dialog box lets the user browse and select performance counters. You use the [**PDH\_BROWSE\_DLG\_CONFIG**](/windows/win32/api/pdh/ns-pdh-pdh_browse_dlg_config_a) structure to specify the configuration of the dialog box. For example, you can configure the dialog to return one selection or multiple selections.

On input, the **szReturnPathBuffer** member contains the default performance object and counter that is selected in the dialog box. On output, the buffer contains the performance object and counter that the user selected. You can also use the **pCallBack** member to specify a callback function to process the counter names returned by the dialog box.

Note that this dialog box can return PDH\_DIALOG\_CANCELLED if **bSingleCounterPerDialog** is **FALSE** and the user clicks the Close button, so your error handling would have to account for this.

For an example that uses the [**PdhBrowseCounters**](/windows/desktop/api/Pdh/nf-pdh-pdhbrowsecountersa) function, see [Browsing Performance Counters](browsing-performance-counters.md).

To retrieve a list of performance objects on the computer, you can also call the [**PdhEnumObjects**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectsa) function. To retrieve a list of counters and instances for a performance object, call the [**PdhEnumObjectItems**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectitemsa) function. You can also use these functions to identify the performance objects and counters contained in a log file. Repeated calls to **PdhEnumObjectItems** will return the same list of counters and instances until you call **PdhEnumObjects** to refresh the list of performance objects first. For an example that enumerates objects and counters, see [Enumerating Process Objects](enumerating-process-objects.md).

## Selecting the data source

You can use [**PdhSelectDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhselectdatasourcea) in conjunction with [**PdhBrowseCounters**](/windows/desktop/api/Pdh/nf-pdh-pdhbrowsecountersa) to prompt the user to select whether the data source is in real-time or from a log file, and, if it is a log file, its name. If you do not want the data source dialog to be displayed, you can call **PdhSelectDataSource** to display only the file browser catalog. To do this, specify PDH\_FLAGS\_FILE\_BROWSER\_ONLY as the second parameter of the call to **PdhSelectDataSource**.

 

 



