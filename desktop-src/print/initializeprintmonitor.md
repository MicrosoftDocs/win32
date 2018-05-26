---
Description: The InitializePrintMonitor function is obsolete and is supported only for compatibility purposes.
ms.assetid: 825ae98b-74d7-4e41-944b-0dc77cc0cc51
title: InitializePrintMonitor function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InitializePrintMonitor function

The **InitializePrintMonitor** function is obsolete and is supported only for compatibility purposes. New print monitors should implement [**InitializePrintMonitor2**](initializeprintmonitor2.md) so that they can be used with print server clusters.

A print monitor's **InitializePrintMonitor** function initializes a print monitor.

## Syntax


```C++
LPMONITOREX InitializePrintMonitor(
  _In_ LPWSTR pRegistryRoot
);
```



## Parameters

<dl> <dt>

*pRegistryRoot* \[in\]
</dt> <dd>

Caller-supplied pointer to a string identifying a registry path that the print monitor can use to store monitor-specific values.

</dd> </dl>

## Return value

If the operation succeeds, the function should return a pointer to a [**MONITOREX**](monitorex.md) structure. Otherwise the function should call SetLastError (described in the Microsoft Windows SDK documentation) to set an error code, and return **NULL**.

## Remarks

The **InitializePrintMonitor** function must be exported by [language monitors](print.language_monitors) and by port monitor server DLLs. The function is called immediately after the monitor DLL is loaded, and is not called again until the DLL is reloaded. Its purposes are to allow the monitor to initialize itself, and to provide the spooler with pointers to internal monitor functions. Function pointers are contained in a [**MONITOR**](monitor.md) structure, which is referenced through the [**MONITOREX**](monitorex.md) function.

The *pRegistryRoot* parameter supplies a pointer a string representing the path to a *MonitorName* registry key, where *MonitorName* is the monitor name that was specified when the spooler's **AddMonitor** function was called to add the monitor. The monitor can use this key to store monitor-specific value names and values. When the spooler's **DeleteMonitor** function is called, the spooler deletes the *MonitorName* key and all values stored underneath it. (The **AddMonitor** and **DeleteMonitor** functions are described in the Windows SDK documentation.)

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintMonitorUI**](initializeprintmonitorui.md)
</dt> <dt>

[**MONITOREX**](monitorex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20InitializePrintMonitor%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





