---
Description: 'The print spooler''s RouterAllocPrinterNotifyInfo function allocates a PRINTER\_NOTIFY\_INFO structure and an array of PRINTER\_NOTIFY\_INFO\_DATA structures.'
ms.assetid: '319bee1b-c319-4c95-8343-edb9b08e6d6c'
title: RouterAllocPrinterNotifyInfo function
---

# RouterAllocPrinterNotifyInfo function

The print spooler's `RouterAllocPrinterNotifyInfo` function allocates a PRINTER\_NOTIFY\_INFO structure and an array of PRINTER\_NOTIFY\_INFO\_DATA structures. (These structures are described in the Microsoft Windows SDK documentation.)

## Syntax


```C++
PPRINTER_NOTIFY_INFO RouterAllocPrinterNotifyInfo(
   DWORD cPrinterNotifyInfoData
);
```



## Parameters

<dl> <dt>

*cPrinterNotifyInfoData* 
</dt> <dd>

Caller-supplied number specifying size of the PRINTER\_NOTIFY\_INFO\_DATA structure array to be allocated.

</dd> </dl>

## Return value

The function returns a pointer to the allocated PRINTER\_NOTIFY\_INFO structure.

## Remarks

Print providers should call `RouterAllocPrinterNotifyInfo` to allocate the PRINTER\_NOTIFY\_INFO structure and the PRINTER\_NOTIFY\_INFO\_DATA structure array that the provider's [**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification) function must supply.

The `RouterAllocPrinterNotifyInfo` function initializes the PRINTER\_NOTIFY\_INFO structure's **Version** member to the current version of the spooler's notification implementation. It initializes the structure's **Flags** and **Count** members to zero, regardless of the number specified for *cPrinterNotifyInfoData*.

Print providers should call [**AppendPrinterNotifyInfoData**](appendprinternotifyinfodata.md) to fill in members of the PRINTER\_NOTIFY\_INFO\_DATA structure array.

If `RefreshPrinterChangeNotification` executes successfully and returns the allocated structures to the caller, you should assume that the caller will deallocate structure memory. However, if `RefreshPrinterChangeNotification` encounters an error it should call [**RouterFreePrinterNotifyInfo**](routerfreeprinternotifyinfo.md) to deallocate the memory.

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

[**AppendPrinterNotifyInfoData**](appendprinternotifyinfodata.md)
</dt> <dt>

[**RouterFreePrinterNotifyInfo**](routerfreeprinternotifyinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterAllocPrinterNotifyInfo%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





