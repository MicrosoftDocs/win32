---
description: Using WMI, you can access system counter data programmatically from objects in the performance libraries.
ms.assetid: a0ed14e9-d2ec-43eb-8c8e-eac3c134ea1d
ms.tgt_platform: multiple
title: Monitoring Performance Data
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Performance Data

Using WMI, you can access system counter data programmatically from objects in the performance libraries. This is the same performance data that appears in the System Monitor in the Perfmon utility. Use the preinstalled [performance counter classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) to obtain performance data in scripts or C++ applications.

The following sections are discussed in this topic:

-   [WMI Performance Classes](#wmi-performance-classes)
-   [Performance Data Providers](#performance-data-providers)
-   [Using Formatted Performance Data Classes](#using-formatted-performance-data-classes)
-   [Using Raw Performance Data Classes](#using-raw-performance-data-classes)
-   [Related topics](#related-topics)

## WMI Performance Classes

As an example, the "NetworkInterface" object, in System Monitor, is represented in WMI by the [**Win32\_PerfRawData\_Tcpip\_NetworkInterface**](./retrieving-raw-and-formatted-performance-data.md) class for raw data and the [**Win32\_PerfFormattedData\_Tcpip\_NetworkInterface**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data) class for precalculated, or formatted data. Classes derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) must be used with a [*refresher*](gloss-r.md) object. On raw data classes, your C++ application or script must perform calculations to obtain the same output as Perfmon.exe. Formatted data classes supply precalculated data. For more information about obtaining data in C++ applications, see [Accessing Performance Data in C++](accessing-performance-data-in-c--.md). For scripting, see [Accessing Performance Data in Script](accessing-performance-data-in-script.md) and [Refreshing WMI Data in Scripts](refreshing-wmi-data-in-scripts.md).

The following VBScript code example uses [**Win32\_PerfFormattedData\_PerfProc\_Process**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data) to obtain performance data for the Idle process. The script displays the same data that appears in Perfmon for the % Processor Time counter of the Process object. The call to [**SWbemObjectEx.Refresh\_**](swbemobjectex-refresh-.md) performs the refresh operation. Be aware that the data must be refreshed, at lease once, to obtain a baseline.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" _
    & strComputer & "\root\cimv2")
set PerfProcess = objWMIService.Get(_
    "Win32_PerfFormattedData_PerfProc_Process.Name='Idle'")

While (True)
    PerfProcess.Refresh_     
    Wscript.Echo PerfProcess.PercentProcessorTime
    Wscript.Sleep 1000
Wend
```



Performance counter classes can also provide statistical data. For more information, see [Obtaining Statistical Performance Data](obtaining-statistical-performance-data.md).

## Performance Data Providers

WMI has preinstalled providers that monitor system performance on both the local system and remotely. The [WmiPerfClass](wmiperfclass-provider.md) provider creates the classes derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata). The [WmiPerfInst](wmiperfinst-provider.md) provider supplies data dynamically to both raw and formatted classes.

## Using Formatted Performance Data Classes

The following VBScript code example obtains performance data about memory, disk partitions, and server work queues. The script then determines if the values are within an acceptable range.

The script uses the following WMI provider objects and scripting objects:

-   Preinstalled WMI performance counter classes.
-   The refresher object, [**SWbemRefresher**](swbemrefresher.md).
-   Items to add to the refresher container, [**SWbemRefreshableItem**](swbemrefreshableitem.md)


```VB
Set objCimv2 = GetObject("winmgmts:root\cimv2")
Set objRefresher = CreateObject("WbemScripting.SWbemRefresher")

' Add items to the SWbemRefresher
' Without the SWbemRefreshableItem.ObjectSet call,
' the script will fail
Set objMemory = objRefresher.AddEnum _
    (objCimv2, _ 
    "Win32_PerfFormattedData_PerfOS_Memory").ObjectSet
Set objDiskQueue = objRefresher.AddEnum _
    (objCimv2, _
    "Win32_PerfFormattedData_PerfDisk_LogicalDisk").ObjectSet
Set objQueueLength = objRefresher.AddEnum _
    (objCimv2, _
    "Win32_PerfFormattedData_PerfNet_ServerWorkQueues").ObjectSet

' Initial refresh needed to get baseline values
objRefresher.Refresh
intTotalHealth = 0
' Do three refreshes to get data
For i = 1 to 3
    WScript.Echo "Refresh " & i
    For each intAvailableBytes in objMemory
        WScript.Echo "Available megabytes of memory: " _
            & intAvailableBytes.AvailableMBytes
        If intAvailableBytes.AvailableMBytes < 4 Then
            intTotalHealth = intTotalHealth + 1
        End If
    Next
    For each intDiskQueue in objDiskQueue
        WScript.Echo "Current disk queue length " & "Name: " _
            & intDiskQueue.Name & ":" _
            & intDiskQueue.CurrentDiskQueueLength
        If intDiskQueue.CurrentDiskQueueLength > 2 Then
            intTotalHealth = intTotalHealth + 1
        End If
    Next
    For each intServerQueueLength in objQueueLength
        WScript.Echo "Server work queue length: " _
            & intServerQueueLength.QueueLength
        If intServerQueueLength.QueueLength > 4 Then
            intTotalHealth = intTotalHealth + 1                       
        End If
    Wscript.Echo "  "
    Next
    If intTotalHealth > 0 Then
        Wscript.Echo "Unhealthy."
    Else
        Wscript.Echo "Healthy."
    End If
    intTotalHealth = 0
    Wscript.Sleep 5000
' Refresh data for all objects in the collection
    objRefresher.Refresh
Next
```



## Using Raw Performance Data Classes

The following VBScript code example obtains raw, current percent processor time on the local computer and converts it to a percentage. The example shows you how to obtain raw performance data from the **PercentProcessorTime** property of the [**Win32\_PerfRawData\_PerfOS\_Processor**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data) class.

To calculate the percent processor time value, you must locate the formula. Look up the value in the **CounterType** qualifier for the **PercentProcessorTime** property in the [**CounterType Qualifier**](countertype-qualifier.md) table to get the constant name. Locate the constant name in [Counter Types](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10)) to obtain the formula.


```VB
Set objService = GetObject( _
    "Winmgmts:{impersonationlevel=impersonate}!\Root\Cimv2")

For i = 1 to 8
    Set objInstance1 = objService.Get( _
        "Win32_PerfRawData_PerfOS_Processor.Name='_Total'")
    N1 = objInstance1.PercentProcessorTime
    D1 = objInstance1.TimeStamp_Sys100NS

'Sleep for two seconds = 2000 ms
    WScript.Sleep(2000)

    Set perf_instance2 = objService.Get( _
        "Win32_PerfRawData_PerfOS_Processor.Name='_Total'")
    N2 = perf_instance2.PercentProcessorTime
    D2 = perf_instance2.TimeStamp_Sys100NS
' Look up the CounterType qualifier for the PercentProcessorTime 
' and obtain the formula to calculate the meaningful data. 
' CounterType - PERF_100NSEC_TIMER_INV
' Formula - (1- ((N2 - N1) / (D2 - D1))) x 100

    PercentProcessorTime = (1 - ((N2 - N1)/(D2-D1)))*100
    WScript.Echo "% Processor Time=" , Round(PercentProcessorTime,2)
Next
```



## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 
