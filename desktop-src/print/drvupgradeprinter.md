---
Description: A printer interface DLL's DrvUpgradePrinter function is used for updating a printer's registry settings when a new version of the driver is added to a system.
ms.assetid: 5a8a764d-48bf-48f9-831a-ac22767aeca6
title: DrvUpgradePrinter function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvUpgradePrinter function

A printer interface DLL's **DrvUpgradePrinter** function is used for updating a printer's registry settings when a new version of the driver is added to a system.

## Syntax


```C++
BOOL DrvUpgradePrinter(
           DWORD  Level,
  _In_opt_ LPBYTE pDriverUpgradeInfo
);
```



## Parameters

<dl> <dt>

*Level* 
</dt> <dd>

Caller-supplied value indicating the type of structure pointed to by *pDriverUpgradeInfo*, as indicated in the following table.



| *Level* Value | Structure pointed to by *pDriverUpgradeInfo*                         |
|---------------|----------------------------------------------------------------------|
| 1<br/>  | [**DRIVER\_UPGRADE\_INFO\_1**](driver-upgrade-info-1.md)<br/> |
| 2<br/>  | [**DRIVER\_UPGRADE\_INFO\_2**](driver-upgrade-info-2.md)<br/> |



 

</dd> <dt>

*pDriverUpgradeInfo* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a structure whose type is identified by *dwLevel*.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**; otherwise, it should call SetLastError to set an error code and return **FALSE**.

## Remarks

A [printer interface DLL](https://www.bing.com/search?q=printer interface DLL) can optionally provide a **DrvUpgradePrinter** function. If it does, the spooler calls it for every printer when the printer driver is copied onto the system. This occurs when a system is upgraded from one operating system release to the next, or when an application updates a printer driver by calling the Win32 **AddPrinterDriver** function.

Often, a new driver version requires registry settings that are different from those of the old version. The **DrvUpgradePrinter** function's purpose is to update the registry so it is compatible with the driver. For more information about storing printer information in the registry, see [**DrvPrinterEvent**](drvprinterevent.md).

For Windows 2000 and later, when the spooler calls **DrvUpgradePrinter**, it supplies a DRIVER\_UPGRADE\_INFO\_2 structure pointer for *pDriverUpgradeInfo*. If the function returns **FALSE**, the spooler calls the function again, this time specifying a DRIVER\_UPGRADE\_INFO\_1 structure pointer. If this call returns **FALSE**, the spooler writes an entry in the event log.

For Windows NT 4.0 and previous, when the spooler calls **DrvUpgradePrinter**, it supplies a DRIVER\_UPGRADE\_INFO\_1 structure pointer for *pDriverUpgradeInfo*. If the function returns **FALSE**, the spooler writes an entry in the event log.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvPrinterEvent**](drvprinterevent.md)
</dt> <dt>

[**DRIVER\_UPGRADE\_INFO\_1**](driver-upgrade-info-1.md)
</dt> <dt>

[**DRIVER\_UPGRADE\_INFO\_2**](driver-upgrade-info-2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvUpgradePrinter%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





