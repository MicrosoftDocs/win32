---
Description: A port monitor UI DLLs InitializePrintMonitorUI function supplies the print spooler with addresses of DLL functions.
ms.assetid: baa80f8c-68ed-43a3-8c82-79a4388f9ab6
title: InitializePrintMonitorUI function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InitializePrintMonitorUI function

A port monitor UI DLL's **InitializePrintMonitorUI** function supplies the print spooler with addresses of DLL functions.

## Syntax


```C++
PMONITORUI WINAPI InitializePrintMonitorUI(
    void
);
```



## Parameters

<dl> <dt>

*void* 
</dt> <dd></dd> </dl>

## Return value

The function should return a pointer to an initialized [**MONITORUI**](monitorui.md) structure.

## Remarks

Port monitor UI DLLs are required to export an **InitializePrintMonitorUI** function. The function is called immediately after the DLL is loaded, and is not called again until the DLL is reloaded. Its purposes are to allow the DLL to initialize itself, and to provide the spooler with pointers to internal functions.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintMonitor**](initializeprintmonitor.md)
</dt> <dt>

[**MONITORUI**](monitorui.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20InitializePrintMonitorUI%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





