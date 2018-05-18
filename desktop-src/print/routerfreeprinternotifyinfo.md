---
Description: 'The print spooler''s RouterFreePrinterNotifyInfo function deallocates a specified PRINTER\_NOTIFY\_INFO structure and its associated PRINTER\_NOTIFY\_INFO\_DATA structure array.'
ms.assetid: '11beef0b-061a-4d73-b723-d0214f479503'
title: RouterFreePrinterNotifyInfo function
---

# RouterFreePrinterNotifyInfo function

The print spooler's `RouterFreePrinterNotifyInfo` function deallocates a specified PRINTER\_NOTIFY\_INFO structure and its associated PRINTER\_NOTIFY\_INFO\_DATA structure array. (These structures are described in the Microsoft Windows SDK documentation.)

## Syntax


```C++
BOOL RouterFreePrinterNotifyInfo(
  _In_opt_ PPRINTER_NOTIFY_INFO pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a PRINTER\_NOTIFY\_INFO structure (described in the Windows SDK documentation).

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**.

## Remarks

A print provider's [**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification) function should call `RouterFreePrinterNotifyInfo` to deallocate structures previously allocated by [**RouterAllocPrinterNotifyInfo**](routerallocprinternotifyinfo.md), but only if **RefreshPrinterChangeNotification** encounters a error. If **RefreshPrinterChangeNotification** succeeds, you should assume that the client application will deallocate the structures.

Besides deallocating the specified PRINTER\_NOTIFY\_INFO structure and its associated PRINTER\_NOTIFY\_INFO\_DATA structure array, the function also deallocates buffer space pointed to by *pBuf* in any element of the PRINTER\_NOTIFY\_INFO\_DATA structure array.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterFreePrinterNotifyInfo%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





