---
Description: The print spoolers AppendPrinterNotifyInfoData function adds the contents of a specified PRINTER\_NOTIFY\_INFO\_DATA structure to a specified PRINTER\_NOTIFY\_INFO structure.
ms.assetid: 558b81c5-5f6b-41a5-8d89-6ee39b9c1cd1
title: AppendPrinterNotifyInfoData function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AppendPrinterNotifyInfoData function

The print spooler's **AppendPrinterNotifyInfoData** function adds the contents of a specified PRINTER\_NOTIFY\_INFO\_DATA structure to a specified PRINTER\_NOTIFY\_INFO structure.

## Syntax


```C++
BOOL AppendPrinterNotifyInfoData(
  _In_     PPRINTER_NOTIFY_INFO      pInfoDest,
  _In_opt_ PPRINTER_NOTIFY_INFO_DATA pInfoDataSrc,
           DWORD                     fdwFlags
);
```



## Parameters

<dl> <dt>

*pInfoDest* \[in\]
</dt> <dd>

Caller-supplied pointer to a PRINTER\_NOTIFY\_INFO structure (defined in the Microsoft Windows SDK documentation).

</dd> <dt>

*pInfoDataSrc* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a PRINTER\_NOTIFY\_INFO\_DATA structure (defined in the Windows SDK documentation).

</dd> <dt>

*fdwFlags* 
</dt> <dd>

Caller-supplied flags. The following flag is defined.

<dl> <dt>

<span id="PRINTER_NOTIFY_INFO_DATA_COMPACT"></span><span id="printer_notify_info_data_compact"></span>PRINTER\_NOTIFY\_INFO\_DATA\_COMPACT
</dt> <dd>

If set, the function examines the **Type**, **Field**, and **Id** members of the supplied PRINTER\_NOTIFY\_INFO\_DATA structure. If they all match an existing element of the PRINTER\_NOTIFY\_INFO\_DATA structure array, the existing element is overwritten with the supplied element. If a match is not found, the function adds the specified structure to the end of the array.

</dd> </dl> </dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise, the function returns **FALSE**. The caller can obtain an error code by calling GetLastError (described in the Windows SDK documentation).

## Remarks

A print provider's [**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification) function should call **AppendPrinterNotifyInfoData** as often as necessary to populate a PRINTER\_NOTIFY\_INFO\_DATA structure array, after first calling [**RouterAllocPrinterNotifyInfo**](routerallocprinternotifyinfo.md) to allocate storage for the array and its associated PRINTER\_NOTIFY\_INFO structure.

Based on whether the PRINTER\_NOTIFY\_INFO\_DATA\_COMPACT flag is set, the function either appends the specified PRINTER\_NOTIFY\_INFO\_DATA structure to the end of the structure array or overwrites an existing array element. If the structure is appended, the function increments the PRINTER\_NOTIFY\_INFO structure's **Count** member.

If **AppendPrinterNotifyInfoData** detects that the PRINTER\_NOTIFY\_INFO\_DISCARDED flag is set in the specified PRINTER\_NOTIFY\_INFO structure, the function clears all PRINTER\_NOTIFY\_INFO\_DATA structures and sets the error code to ERROR\_OUT\_OF\_STRUCTURES.

If **NULL** is specified for *pInfoDataSrc*, **AppendPrinterNotifyInfoData** sets the PRINTER\_NOTIFY\_INFO\_DISCARDED flag in the specified PRINTER\_NOTIFY\_INFO structure, clears all PRINTER\_NOTIFY\_INFO\_DATA structures, and sets the error code to ERROR\_OUT\_OF\_STRUCTURES.

(For more information about the PRINTER\_NOTIFY\_INFO\_DISCARDED flag, see the description of FindNextPrinterChangeNotification in the Windows SDK documentation.)

For additional information, see [Supporting Printer Change Notifications](print.supporting_printer_change_notifications).

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification)
</dt> <dt>

[**RouterAllocPrinterNotifyInfo**](routerallocprinternotifyinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20AppendPrinterNotifyInfoData%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





