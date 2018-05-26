---
Description: The WcsSetUsePerUserProfiles function allows the user to specify whether or not to use a per-user profile association list for the specified device.
ms.assetid: e14f944f-67fe-4eb8-85b2-9ba262e2e549
title: WcsSetUsePerUserProfiles function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WcsSetUsePerUserProfiles function

The `WcsSetUsePerUserProfiles` function allows the user to specify whether or not to use a per-user profile association list for the specified device.

## Syntax


```C++
BOOL WcsSetUsePerUserProfiles(
  _In_ LPCWSTR pDeviceName,
  _In_ DWORD   dwDeviceClass,
  _In_ BOOL    usePerUserProfiles
);
```



## Parameters

<dl> <dt>

*pDeviceName* \[in\]
</dt> <dd>

A pointer to a string that contains the friendly name of the device.

</dd> <dt>

*dwDeviceClass* \[in\]
</dt> <dd>

A flag value that specifies the class of the device. This parameter must take one of the following values:

<dl> <dt>

<span id="CLASS_MONITOR"></span><span id="class_monitor"></span>CLASS\_MONITOR
</dt> <dd>

Specifies a display device.

</dd> <dt>

<span id="CLASS_PRINTER"></span><span id="class_printer"></span>CLASS\_PRINTER
</dt> <dd>

Specifies a printer.

</dd> <dt>

<span id="CLASS_SCANNER"></span><span id="class_scanner"></span>CLASS\_SCANNER
</dt> <dd>

Specifies an image capture device.

</dd> </dl> </dd> <dt>

*usePerUserProfiles* \[in\]
</dt> <dd>

A Boolean value that is **TRUE** if the user wants to use a per-user profile association list for the specified device; otherwise **FALSE**.

</dd> </dl>

## 

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

This function will fail if the device pointed to by *pDeviceName* is not of the class specified by *dwDeviceClass*.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**WcsGetUsePerUserProfiles**](wcsgetuseperuserprofiles.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsSetUsePerUserProfiles%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





