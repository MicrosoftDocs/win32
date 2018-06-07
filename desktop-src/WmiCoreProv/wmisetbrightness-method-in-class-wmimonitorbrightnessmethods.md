---
Description: Sets the display brightness of a computer monitor.
ms.assetid: 900cf5fd-6888-4f0b-8e0b-01eeaaeeeb8f
title: WmiSetBrightness method of the WmiMonitorBrightnessMethods class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WmiSetBrightness method of the WmiMonitorBrightnessMethods class

The **WmiSetBrightness** method sets the display brightness of a computer monitor.

## Syntax


```mof
uint32 WmiSetBrightness(
   uint32 Timeout,
   uint8  Brightness
);
```



## Parameters

<dl> <dt>

*Timeout* 
</dt> <dd>

Timeout, in seconds.

</dd> <dt>

*Brightness* 
</dt> <dd>

Brightness, in percent.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For more information about error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Examples

For an extended discussion of retrieving and setting monitor brightness, see the Scripting Guy's [Use PowerShell to Report and Set Monitor Brightness](http://blogs.technet.com/b/heyscriptingguy/archive/2013/07/25/use-powershell-to-report-and-set-monitor-brightness.aspx) blog topic.

The following PowerShell sample sets the brightness of the monitor to 50%.


```PowerShell
$brightness = 50
$delay = 5
$myMonitor = Get-WmiObject -Namespace root\wmi -Class WmiMonitorBrightnessMethods
$myMonitor.wmisetbrightness($delay, $brightness)
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**WmiMonitorBrightnessMethods**](wmimonitorbrightnessmethods.md)
</dt> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




