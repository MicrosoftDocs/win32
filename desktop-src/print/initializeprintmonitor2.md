---
Description: A print monitor's InitializePrintMonitor2 function initializes a print monitor for use with clustered print servers.
ms.assetid: 73348405-0cc1-412a-b9b1-cfcc300190d7
title: InitializePrintMonitor2 function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InitializePrintMonitor2 function

A print monitor's **InitializePrintMonitor2** function initializes a print monitor for use with clustered print servers.

## Syntax


```C++
LPMONITOR2 InitializePrintMonitor2(
  _In_  PMONITORINIT pMonitorInit,
  _Out_ PHANDLE      phMonitor
);
```



## Parameters

<dl> <dt>

*pMonitorInit* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**MONITORINIT**](monitorinit.md) structure.

</dd> <dt>

*phMonitor* \[out\]
</dt> <dd>

Caller-supplied location in which the function returns a monitor handle.

</dd> </dl>

## Return value

If the operation succeeds, the function should return a pointer to a [**MONITOR2**](monitor2.md) structure. Otherwise the function should call SetLastError (described in the Microsoft Windows SDK documentation) to set an error code, and return **NULL**.

## Remarks

The **InitializePrintMonitor2** function must be exported by [language monitors](https://www.bing.com/search?q=language+monitors) and by port monitor server DLLs. The function is called immediately after the monitor DLL is loaded, and is not called again until the DLL is reloaded. Its purposes are to allow the monitor to initialize itself, and to provide the spooler with pointers to internal monitor functions. Function pointers are contained in a [**MONITOR2**](monitor2.md) structure.

The [**MONITOR2**](monitor2.md) structure is larger in Windows XP than it was in Windows 2000. In order to ensure that a monitor developed with the Windows XP Driver Development Kit (DDK) will install on Windows XP and Windows 2000, the monitor must do the following:

-   Perform a run-time check to determine which operating system version the monitor is running on.

-   If the monitor is running on Windows 2000, it must set the **cbSize** member of the MONITOR2 structure to MONITOR2\_SIZE\_WIN2K (defined in Winsplp.h), the size appropriate for Windows 2000 version of this structure.

The following function determines whether the current operating system version is Windows 2000.


```
BOOL  Is_Win2000()
{
  OSVERSIONINFOEX osvi;
  DWORDLONG dwlConditionMask = 0;

  // Initialize the OSVERSIONINFOEX structure.

  ZeroMemory(&amp;osvi, sizeof(OSVERSIONINFOEX));
  osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);
  osvi.dwMajorVersion = 5;
  osvi.dwMinorVersion = 0;

  // Initialize the condition mask.
  VER_SET_CONDITION( dwlConditionMask, VER_MAJORVERSION, VER_EQUAL );
  VER_SET_CONDITION( dwlConditionMask, VER_MINORVERSION, VER_EQUAL );

  // Perform the test.
  return VerifyVersionInfo(
      &amp;osvi,
      VER_MAJORVERSION | VER_MINORVERSION,
      dwlConditionMask);
}
```



For a monitor that is loading on Windows 2000, the following code sets the MONITOR2 structure's **cbSize** member appropriately.


```
if ( Is_Win2000( ) )
    Monitor2.cbSize = MONITOR2_SIZE_WIN2K;
```



## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**MONITORINIT**](monitorinit.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20InitializePrintMonitor2%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





