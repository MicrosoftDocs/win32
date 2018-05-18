---
Description: 'The DRIVER\_INFO\_8 structure contains printer driver information.'
ms.assetid: '95f62d57-300a-4179-868b-f14f29c58b4d'
title: 'DRIVER\_INFO\_8 structure'
---

# DRIVER\_INFO\_8 structure

The DRIVER\_INFO\_8 structure contains printer driver information.

## Syntax


```C++
typedef struct _DRIVER_INFO_8 {
  DWORD     cVersion;
  LPTSTR    pName;
  LPTSTR    pEnvironment;
  LPTSTR    pDriverPath;
  LPTSTR    pDataFile;
  LPTSTR    pConfigFile;
  LPTSTR    pHelpFile;
  LPTSTR    pDependentFiles;
  LPTSTR    pMonitorName;
  LPTSTR    pDefaultDataType;
  LPTSTR    pszzPreviousNames;
  FILETIME  ftDriverDate;
  DWORDLONG dwlDriverVersion;
  LPTSTR    pszMfgName;
  LPTSTR    pszOEMUrl;
  LPTSTR    pszHardwareID;
  LPTSTR    pszProvider;
  LPTSTR    pszPrintProcessor;
  LPTSTR    pszVendorSetup;
  LPTSTR    pszzColorProfiles;
  LPTSTR    pszInfPath;
  DWORD     dwPrinterDriverAttributes;
  LPTSTR    pszzCoreDriverDependencies;
  FILETIME  ftMinInboxDriverVerDate;
  DWORDLONG dwlMinInboxDriverVerVersion;
} DRIVER_INFO_8, *PDRIVER_INFO_8, *LPDRIVER_INFO_8;
```



## Members

<dl> <dt>

**cVersion**
</dt> <dd>

This member specifies the operating system version for which the driver was written. Currently it can be the following.



| Value        | Meaning                                                             |
|--------------|---------------------------------------------------------------------|
| 3<br/> | Driver for Microsoft Windows 2000, XP, or Windows Vista.<br/> |



 

</dd> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the driver (for example, QMS 810).

</dd> <dt>

**pEnvironment**
</dt> <dd>

A pointer to a null-terminated string that specifies the environment for which the driver was written (for example, Microsoft Windows NT x86, Windows NT R4000, Windows NT Alpha\_AXP, or Windows 4.0).

</dd> <dt>

**pDriverPath**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains the device driver (for example, C:\\DRIVERS\\Pscript.dll).

</dd> <dt>

**pDataFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains driver data (for example, C:\\DRIVERS\\Qms810.ppd).

</dd> <dt>

**pConfigFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's configuration dynamic-link library (for example, C:\\DRIVERS\\Pscrptui.dll).

</dd> <dt>

**pHelpFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's help file (for example, C:\\DRIVERS\\Pscrptui.hlp).

</dd> <dt>

**pDependentFiles**
</dt> <dd>

Pointer to a Multi-SZ string that contains the names of the files on which the driver depends. The file names are stored as a contiguous series of zero-terminated strings followed by an empty string. For example, Pscript.dll\\0QMS810.ppd\\0Pscriptui.dll\\0Pscriptui.hlp\\0Pstest.txt\\0\\0, where \\0 represents the terminating null character.

</dd> <dt>

**pMonitorName**
</dt> <dd>

A pointer to a null-terminated string that specifies a language monitor (for example, "PJL monitor"). This member can be **NULL** and should be specified only for printers capable of bidirectional communication.

</dd> <dt>

**pDefaultDataType**
</dt> <dd>

A pointer to a null-terminated string that specifies the default data type of the print job (for example, "EMF").

</dd> <dt>

**pszzPreviousNames**
</dt> <dd>

A pointer to a null-terminated string that specifies any previous printer driver names that are compatible with this driver (for example, OldName1\\0OldName2\\0\\0).

</dd> <dt>

**ftDriverDate**
</dt> <dd>

The date of the driver package, as coded in the driver files.

</dd> <dt>

**dwlDriverVersion**
</dt> <dd>

The version number of the driver. This comes out of the version structure of the driver.

</dd> <dt>

**pszMfgName**
</dt> <dd>

A pointer to a null-terminated string that specifies the manufacturer's name.

</dd> <dt>

**pszOEMUrl**
</dt> <dd>

A pointer to a null-terminated string that specifies the URL for the manufacturer.

</dd> <dt>

**pszHardwareID**
</dt> <dd>

A pointer to a null-terminated string that specifies the hardware ID for the printer driver.

</dd> <dt>

**pszProvider**
</dt> <dd>

A pointer to a null-terminated string that specifies the provider of the printer driver (for example, "Microsoft Windows 2000").

</dd> <dt>

**pszPrintProcessor**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print processor associated with the printer driver.

</dd> <dt>

**pszVendorSetup**
</dt> <dd>

A pointer to a null-terminated string that specifies the vendor setup DLL and entry point for vendor setup that is associated with the printer driver.

</dd> <dt>

**pszzColorProfiles**
</dt> <dd>

A pointer to a null-terminated string that specifies all color profiles that are associated with the printer driver.

</dd> <dt>

**pszInfPath**
</dt> <dd>

A pointer to a null-terminated string that specifies the path of the INF file inside the driver store from which the printer driver was installed. Must be **NULL** if using the [AddPrinterDriver](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183346.aspx) or [AddPrinterDriverEx](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183347.aspx) functions with DRIVER\_INFO\_8.

</dd> <dt>

**dwPrinterDriverAttributes**
</dt> <dd>

This member specifies printer driver related properties. Must be zero if using the [AddPrinterDriver](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183346.aspx) or [AddPrinterDriverEx](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183347.aspx) functions with DRIVER\_INFO\_8. The following table shows the flags that have been defined for the *dwPrinterDriverAttributes* parameter.



| Flag name/value                                                         | Meaning                                                                                                                                                                                                                                                                                                                                             | Minimum OS                                             |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| PRINTER\_DRIVER\_PACKAGE\_AWARE<br/> 0x00000001<br/>        | The printer driver is part of a driver package.                                                                                                                                                                                                                                                                                                     | Windows Vista                                          |
| PRINTER\_DRIVER\_XPS<br/> 0x00000002<br/>                   | The printer driver supports the Microsoft XPS format described in the [XML Paper Specification: Overview](http://msdn.microsoft.com/en-us/windows/hardware/gg463373.aspx), and also in [Product Behavior, section &lt;27&gt;](http://msdn.microsoft.com/en-us/library/e81cbc09-ab05-4a32-ae4a-8ec57b436c43#id27).                        | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_SANDBOX\_ENABLED<br/> 0x00000004<br/>      | The printer driver is compatible with [printer driver isolation](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#printer-driver-isolation). For more information, see [Product Behavior, section &lt;28&gt;](http://msdn.microsoft.com/en-us/library/e81cbc09-ab05-4a32-ae4a-8ec57b436c43#id28). | Windows 7<br/> Windows Server 2008 R2<br/> |
| PRINTER\_DRIVER\_CLASS<br/> 0x00000008<br/>                 | The printer driver is a [class printer driver](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#class-printer-driver).                                                                                                                                                                                       | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_DERIVED<br/> 0x00000010<br/>               | The printer driver is a [derived printer driver](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#derived-printer-driver).                                                                                                                                                                                   | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_NOT\_SHAREABLE<br/> 0x00000020<br/>        | Printers using this printer driver cannot be shared.                                                                                                                                                                                                                                                                                                | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_FAX<br/> 0x00000040<br/>         | The printer driver is intended for use with [fax printers](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#fax-printer).                                                                                                                                                                                    | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_FILE<br/> 0x00000080<br/>        | The printer driver is intended for use with [file printers](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#file-printer).                                                                                                                                                                                  | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_VIRTUAL<br/> 0x00000100<br/>     | The printer driver is intended for use with [virtual printers](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#virtual-printer).                                                                                                                                                                            | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_SERVICE<br/> 0x00000200<br/>     | The printer driver is intended for use with [service printers](http://msdn.microsoft.com/en-us/library/831cd729-be7c-451e-b729-bd8d84ce4d24#service-printer).                                                                                                                                                                            | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_SOFT\_RESET\_REQUIRED<br/> 0x00000400<br/> | Printers that use this printer driver should follow the guidelines outlined in [USB Device Class Definition](http://go.microsoft.com/fwlink/p/?linkid=517016). For more information, see [Product Behavior, section &lt;36&gt;](http://msdn.microsoft.com/en-us/library/e81cbc09-ab05-4a32-ae4a-8ec57b436c43#id36)                       | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_3D<br/> 0x00001000<br/>          | The printer driver is intended for use with 3D printers.<br/>                                                                                                                                                                                                                                                                                 | Windows 8<br/> Windows Server 2012<br/>    |



 

</dd> <dt>

**pszzCoreDriverDependencies**
</dt> <dd>

A pointer to a null-terminated string that contains all the core printer driver dependencies for the driver package that are defined by *pszInfPath*. Must be **NULL** if using the [AddPrinterDriver](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183346.aspx) or [AddPrinterDriverEx](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183347.aspx) functions with DRIVER\_INFO\_8.

</dd> <dt>

**ftMinInboxDriverVerDate**
</dt> <dd>

The earliest allowed date of any drivers that shipped with Windows and on which this driver depends.

</dd> <dt>

**dwlMinInboxDriverVerVersion**
</dt> <dd>

The earliest allowed version of any drivers that shipped with Windows and on which this driver depends.

</dd> </dl>

## Remarks

The strings for these members are contained in the INF file that is used to add the driver.

If you call **AddPrinterDriver** or **AddPrinterDriverEx** with Level not equal to 6 or 8, and then you call **GetPrinterDriver** or **EnumPrinterDrivers** with Level equal to 6 or 8, the **DRIVER\_INFO\_8** structure is returned with pszMfgName, pszOEMUrl, pszHardwareID, and pszProvider set to **NULL**, dwlDriverVersion set to zero, and ftDriverDate set to (0,0).

This structure is available in Windows Vista.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DRIVER_INFO_8%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




