---
title: Win32\_ReliabilityStabilityMetrics class
description: The Win32\_ReliabilityStabilityMetrics WMI class contains metrics related to system reliability. .
ms.assetid: 3422ab03-1c6c-4712-b6c1-e6aebe2b2fb9
keywords:
- Win32_ReliabilityStabilityMetrics class
- Win32_ReliabilityStabilityMetrics class, described
topic_type:
- apiref
api_name:
- Win32_ReliabilityStabilityMetrics
- Win32_ReliabilityStabilityMetrics.EndMeasurementDate
- Win32_ReliabilityStabilityMetrics.RelID
- Win32_ReliabilityStabilityMetrics.StartMeasurementDate
- Win32_ReliabilityStabilityMetrics.SystemStabilityIndex
- Win32_ReliabilityStabilityMetrics.TimeGenerated
api_location:
- RacWmiProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ReliabilityStabilityMetrics class

The **Win32\_ReliabilityStabilityMetrics** [WMI class](https://msdn.microsoft.com/library/aa393244) contains metrics related to system reliability. .

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("ReliabilityMetricsProvider"), Dynamic]
class Win32_ReliabilityStabilityMetrics : Win32_Reliability
{
  datetime EndMeasurementDate;
  string   RelID;
  datetime StartMeasurementDate;
  real64   SystemStabilityIndex;
  datetime TimeGenerated;
};
```

## Members

The **Win32\_ReliabilityStabilityMetrics** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ReliabilityStabilityMetrics** class has these methods.



| Method                                                                     | Description                                                                                       |
|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**GetRecordCount**](win32-reliabilitystabilitymetrics-getrecordcount.md) | Retrieves the number of instances in the **Win32\_ReliabilityStabilityMetrics** class.<br/> |



 

### Properties

The **Win32\_ReliabilityStabilityMetrics** class has these properties.

<dl> <dt>

EndMeasurementDate
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the most recent UTC time at which reliability metric data was collected.

</dd> <dt>

RelID
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a **GUID** that is used to correlate reliability metrics on this computer. The **GUID** will be reset if an error prevents reliability metrics from being calculated.

</dd> <dt>

StartMeasurementDate
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the UTC time at which reliability metric data collection began.

</dd> <dt>

SystemStabilityIndex
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the system stability index value. The stability index ranges from 1 (the least stable) to 10 (the most stable). You can use the index to help evaluate the reliability of a computer.

</dd> <dt>

TimeGenerated
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Specifies the UTC time at which the system stability index value was calculated. This value is used to uniquely identify an instance of this class.

</dd> </dl>

## Remarks

The **Win32\_ReliabilityStabilityMetrics** class is derived from **Win32\_Reliability**. To access information from this WMI class, the group policy Configure Reliability WMI Providers must be enabled. On Windows client systems, the policy is enabled by default. On Windows Server systems, the policy is disabled by default. Disabling the policy will clear existing data within one hour. The **Win32\_ReliabilityStabilityMetrics** class is not available on Itanium-based versions of the Windows operating system, or the Server Core installation option of Windows Server operating systems.

## Examples

The following Windows PowerShell example displays the most recent stability index from the local computer.


```PowerShell
get-wmiobject Win32_ReliabilityStabilityMetrics -computername 127.0.0.1 -property "SystemStabilityIndex" | 
  select-object -first 1 SystemStabilityIndex | format-table *
```



The following Windows PowerShell example displays the most recent stability indices from multiple computers.


```PowerShell
@("127.0.0.1", "localhost") |
  foreach-object -process {
    get-wmiobject Win32_ReliabilityStabilityMetrics -computername $_ -property @("__SERVER", "SystemStabilityIndex") | 
    select-object -first 1 __SERVER,SystemStabilityIndex |
    format-table *
  }
```



The following Windows PowerShell example displays a vertically oriented graph of the stability index for the local computer.


```PowerShell
get-wmiobject Win32_ReliabilityStabilityMetrics -property @("SystemStabilityIndex","EndMeasurementDate") | 
  foreach-object -process 
 {
    $t = ""; 
    for ($i = 0; $i -le $_.SystemStabilityIndex * 5; $i++) { $t = $t + "=" }; 
    $_.EndMeasurementDate + " " + $t 
  }
```



## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>RacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ReliabilityRecords**](win32-reliabilityrecords.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[**Win32\_NTLogEvent**](https://msdn.microsoft.com/library/aa394226)
</dt> </dl>

 

 





