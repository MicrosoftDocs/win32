---
Description: The DRIVER\_UPGRADE\_INFO\_2 structure is used as an input to a printer interface DLL's DrvUpgradePrinter function.
ms.assetid: 691554c5-5c99-40f0-b0d6-3556e004dd30
title: DRIVER\_UPGRADE\_INFO\_2 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DRIVER\_UPGRADE\_INFO\_2 structure

The DRIVER\_UPGRADE\_INFO\_2 structure is used as an input to a printer interface DLL's [**DrvUpgradePrinter**](drvupgradeprinter.md) function.

## Syntax


```C++
typedef struct _DRIVER_UPGRADE_INFO_2 {
  LPTSTR pPrinterName;
  LPTSTR pOldDriverDirectory;
  DWORD  cVersion;
  LPTSTR pName;
  LPTSTR pEnvironment;
  LPTSTR pDriverPath;
  LPTSTR pDataFile;
  LPTSTR pConfigFile;
  LPTSTR pHelpFile;
  LPTSTR pDependentFiles;
  LPTSTR pMonitorName;
  LPTSTR pDefaultDataType;
  LPTSTR pszzPreviousNames;
} DRIVER_UPGRADE_INFO_2, *PDRIVER_UPGRADE_INFO_2;
```



## Members

<dl> <dt>

**pPrinterName**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the name of the printer. For more information, see the Remarks section.

</dd> <dt>

**pOldDriverDirectory**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the local directory in which the old printer driver files can be found.

</dd> <dt>

**cVersion**
</dt> <dd>

Specifies the operating system version for which the driver was written.



| Value        | Operating System                                  |
|--------------|---------------------------------------------------|
| 0<br/> | Windows 95/98/Me<br/>                       |
| 1<br/> | Windows NT 3.1 through Windows NT 3.51<br/> |
| 2<br/> | Windows NT 4.0<br/>                         |
| 3<br/> | Windows 2000 and later<br/>                 |



 

</dd> <dt>

**pName**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the name of the driver (for example, "QMS 810"). For more information, see the Remarks section.

</dd> <dt>

**pEnvironment**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the environment for which the driver was written (for example, "Windows NT x86" or "Windows Itanium").

</dd> <dt>

**pDriverPath**
</dt> <dd>

Pointer to a NULL-terminated string that specifies a file name or full path and file name for the file that contains the device driver (for example, "pscript.dll").

</dd> <dt>

**pDataFile**
</dt> <dd>

Pointer to a NULL-terminated string that specifies a file name or a full path and file name for the file that contains driver data (for example, "qms810.ppd").

</dd> <dt>

**pConfigFile**
</dt> <dd>

Pointer to a NULL-terminated string that specifies a file name or a full path and file name for the device driver's configuration dynamic-link library (for example, "pscrptui.dll").

</dd> <dt>

**pHelpFile**
</dt> <dd>

Pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's help file.

</dd> <dt>

**pDependentFiles**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the files the driver depends on. Each file name in the string is also terminated with a null character (for example, "pscript.dll\\0qms810.ppd\\0pscrptui.dll\\0pscrptui.hlp\\0pstest.txt\\0\\0").

</dd> <dt>

**pMonitorName**
</dt> <dd>

Pointer to a NULL-terminated string that specifies a language monitor (for example, "PJL monitor"). This member can be **NULL** and should be specified as non-**NULL** only for printers capable of bidirectional communication.

</dd> <dt>

**pDefaultDataType**
</dt> <dd>

Pointer to a NULL-terminated string that specifies the default data type of the print job (for example, "EMF").

</dd> <dt>

**pszzPreviousNames**
</dt> <dd>

Pointer to a NULL-terminated string that specifies any previous printer driver names that are compatible with this driver (for example, "OldName1\\0OldName2\\0\\0").

</dd> </dl>

## Remarks

When DrvUpgradePrinter is called with its *pDriverUpgradeInfo* parameter pointing to a DRIVER\_UPGRADE\_INFO\_2 structure, the **pPrinterName** member points to a string containing the name of the printer to be updated. The **pName** member points to a string containing the name of the printer driver to be updated, which is not necessarily the driver for the printer whose name is pointed to by the **pPrinterName** member.

To see how this can occur, suppose that a computer is connected to two printers, one whose driver is named "Acme Plotter" and the other whose driver is named "Acme RasterMaster". Suppose also that both drivers share a common driver file, plotui.dll. When the "Acme Plotter" driver is updated by a call to the **AddPrinterDriverEx** function (described in the Microsoft Windows SDK documentation), DrvUpgradePrinter is called for both printers, because both drivers use files affected by the upgrade. In both calls, the **pName** member points to "Acme Plotter", the name of the printer driver used in the call to **AddPrinterDriverEx**. The string pointed to by the **pPrinterName** member is different in both calls to DrvUpgradePrinter, however. In each call, **pPrinterName** points to the name of the printer being updated.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvUpgradePrinter**](drvupgradeprinter.md)
</dt> <dt>

[**DRIVER\_UPGRADE\_INFO\_1**](driver-upgrade-info-1.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DRIVER_UPGRADE_INFO_2%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





