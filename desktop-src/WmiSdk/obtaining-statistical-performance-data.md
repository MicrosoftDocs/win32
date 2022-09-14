---
description: In WMI, you can define statistical performance data based on data in formatted performance classes derived from Win32\_PerfFormattedData. The available statistics are average, minimum, maximum, range, and variance, as defined in Statistical Counter Types.
ms.assetid: 5552d5fc-df8c-4353-8593-c106ee19dc84
ms.tgt_platform: multiple
title: Obtaining Statistical Performance Data
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Obtaining Statistical Performance Data

In WMI, you can define statistical performance data based on data in formatted performance classes derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata). The available statistics are average, minimum, maximum, range, and variance, as defined in [Statistical Counter Types](statistical-counter-types.md).

The following list includes the special statistical counter types:

-   [COOKER\_AVERAGE](cooker-average.md)
-   [COOKER\_MIN](cooker-min.md)
-   [COOKER\_MAX](cooker-max.md)
-   [COOKER\_RANGE](cooker-range.md)
-   [COOKER\_VARIANCE](cooker-variance.md)

The following examples show how to:

-   Create a MOF file that defines a class of calculated data.
-   Write a script that creates an instance of the class, and periodically refreshes the data in the instance with the recalculated statistical values.

## MOF File

The following MOF code example creates a new calculated data class named **Win32\_PerfFormattedData\_AvailableMBytes**. This class contains data from the **AvailableMBytes** property of the raw class [**Win32\_PerfRawData\_PerfOS\_Memory**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data). The **Win32\_PerfFormattedData\_AvailableBytes** class defines the properties **Average**, **Min**, **Max**, **Range**, and **Variance**.

The MOF file uses the [**Property Qualifiers for Formatted Performance Counter Classes**](property-qualifiers-for-performance-counter-classes.md) to define the property data source and the calculation formula.

-   The **Average** property obtains raw data from the [**Win32\_PerfRawData\_PerfOS\_Memory**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data).**AvailableMBytes** property.
-   The Counter **qualifier** for the **Average** property specifies the raw data source.
-   The **CookingType** qualifier specifies the formula [COOKER\_MIN](cooker-min.md) for calculating the data.
-   The **SampleWindow** qualifier specifies how many samples to take before performing the calculation.


```mof
// Store the new Win32_PerfFormattedData_MemoryStatistics
//     class in the Root\Cimv2 namespace
#pragma autorecover
#pragma namespace("\\\\.\\Root\\CimV2")

qualifier vendor:ToInstance;
qualifier guid:ToInstance;
qualifier displayname:ToInstance;
qualifier perfindex:ToInstance;
qualifier helpindex:ToInstance;
qualifier perfdetail:ToInstance;
qualifier countertype:ToInstance;
qualifier perfdefault:ToInstance;
qualifier defaultscale:ToInstance;

qualifier dynamic:ToInstance;
qualifier hiperf:ToInstance;
qualifier AutoCook:ToInstance;
qualifier AutoCook_RawClass:ToInstance;
qualifier CookingType:ToInstance;
qualifier Counter:ToInstance;


// Define the Win32_PerFormattedData_MemoryStatistics
//     class, derived from Win32_PerfFormattedData
[
  dynamic,
  // Name of formatted data provider: "WMIPerfInst" for Vista 
  //   and later
  provider("HiPerfCooker_v1"), 
  // Text that will identify new counter in Perfmon
  displayname("My Calculated Counter"),                            
  // A high performance class     
  Hiperf,
  // Contains calculated data 
  Cooked, 
  // Value must be 1 
  AutoCook(1), 
  // Raw performance class to get data for calculations
  AutoCook_RawClass("Win32_PerfRawData_PerfOS_Memory"),
  // Value must be 1        
  AutoCook_RawDefault(1),
  // Name of raw class property to use for timestamp in formulas 
  PerfSysTimeStamp("Timestamp_PerfTime"), 
  // Name of raw class property to use for frequency in formulas
  PerfSysTimeFreq("Frequency_PerfTime"), 
  // Name of raw class property to use for timestamp in formulas
  Perf100NSTimeStamp("Timestamp_Sys100NS"),
  // Name of raw class property to use for frequency in formulas
  Perf100NSTimeFreq("Frequency_Sys100NS"),
  // Name of raw class property to use for timestamp in formulas
  PerfObjTimeStamp("Timestamp_Object"),
  // Name of raw class property to use for frequency in formulas 
  PerfObjTimeFreq("Frequency_Object"),
  // Only one instance of class allowed in namespace
  singleton                                                   
]

class Win32_PerfFormattedData_MemoryStatistics
          : Win32_PerfFormattedData
{

// Define the properties for the class. 
// All the properties perform different
//     statistical operations on the same
//     property, AvailableMBytes, in the raw class

// Define the Average property,
//     which uses the "COOKER_AVERAGE" counter type and 
//     gets its data from the AvailableMBytes 
//     property in the raw class

    [
     CookingType("COOKER_AVERAGE"),
     Counter("AvailableMBytes"),
     SampleWindow(10)
    ]
    uint64 Average = 0;

// Define the Min property, which uses
//     the "COOKER_MIN" counter type and 
//     gets its data from the AvailableMBytes
//     property in the raw class

    [
     CookingType("COOKER_MIN"),
     Counter("AvailableMBytes"),
     SampleWindow(10)
    ]
    uint64 Min = 0;

// Define the Max property, which uses
//     the "COOKER_MAX" counter type and 
//     gets its data from the
//     AvailableMBytes property in the raw class

    [
     CookingType("COOKER_MAX"),
     Counter("AvailableMBytes"),
     SampleWindow(10)
    ]
    uint64 Max = 0;

// Define the Range property, which uses
//     the "COOKER_RANGE" counter type and 
//     gets its data from the AvailableMBytes
//     property in the raw class

    [
     CookingType("COOKER_RANGE"),
     Counter("AvailableMBytes"),
     SampleWindow(10)
    ]
    uint64 Range = 0;

// Define the Variance property, which uses
//     the "COOKER_VARIANCE" counter type and 
//     gets its data from the AvailableMBytes
//     property in the raw class

    [
     CookingType("COOKER_VARIANCE"),
     Counter("AvailableMBytes"),
     SampleWindow(10)
    ]
    uint64 Variance = 0;
};
```



## Script

The following script code example obtains statistics about available memory, in megabytes, using the MOF created previously. The script uses the [**SWbemRefresher**](swbemrefresher.md) scripting object to create a refresher that contains one instance of the statistics class that the MOF file creates, which is **Win32\_PerfFormattedData\_MemoryStatistics**. For more information about using scripts, see [Refreshing WMI Data in Scripts](refreshing-wmi-data-in-scripts.md). If working in C++, see [Accessing Performance Data in C++](accessing-performance-data-in-c--.md).

> [!Note]  
> [**SWbemRefreshableItem.Object**](swbemrefreshableitem-object.md) must be called after obtaining the item from the call to [**SWbemRefresher.Add**](swbemrefresher-add.md) or the script will fail. [**SWbemRefresher.Refresh**](swbemrefresher-refresh.md) must be called before entering the loop to obtain baseline values, or the statistical properties is zero (0) on the first pass.

 


```VB
' Connect to the Root\Cimv2 namespace
strComputer = "."
Set objService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" _
    & strComputer & "\root\cimv2")

' Create a refresher
Set Refresher = CreateObject("WbemScripting.SWbemRefresher")
If Err <> 0 Then
WScript.Echo Err
WScript.Quit
End If

' Add the single instance of the statistics
'    class to the refresher
Set obMemoryStatistics = Refresher.Add(objService, _
    "Win32_PerfFormattedData_MemoryStatistics=@").Object

' Refresh once to obtain base values for cooking calculations
Refresher.Refresh

Const REFRESH_INTERVAL = 10

' Refresh every REFRESH_INTERVAL seconds 
For I=1 to 3
  WScript.Sleep REFRESH_INTERVAL * 1000
  Refresher.Refresh

  WScript.Echo "System memory statistics" _
      & "(Available Megabytes) " _
      & "for the past 100 seconds - pass " & i 
  WScript.Echo "Average = " _
     & obMemoryStatistics.Average & VBNewLine & "Max = " _
     & obMemoryStatistics.Max & VBNewLine & "Min = " _
     & obMemoryStatistics.Min & VBNewLine & "Range = " _ 
     & obMemoryStatistics.Range & VBNewLine & "Variance = " _
     & obMemoryStatistics.Variance 
Next
```



## Running the Script

The following procedure describes how to run the example.

**To run the example script**

1.  Copy both the MOF code and script to files on your computer.
2.  Give the MOF file a .mof extension and the script file a .vbs description.
3.  On the command line, change to the directory where the files are stored, and run [**Mofcomp**](mofcomp.md) on the MOF file. For example, if you name the file *CalculatedData.mof*, then the command is **Mofcomp** *CalculatedData.mof*
4.  Run the script.

## Related topics

<dl> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](accessing-wmi-preinstalled-performance-classes.md)
</dt> <dt>

[**Property Qualifiers for Formatted Performance Counter Classes**](property-qualifiers-for-performance-counter-classes.md)
</dt> <dt>

[Statistical Counter Types](statistical-counter-types.md)
</dt> </dl>

 

 
