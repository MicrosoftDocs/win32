---
Description: 'The print spooler''s PartialReplyPrinterChangeNotification function allows a print provider to update the spooler''s database of printer changes associated with a notification handle.'
ms.assetid: 'a884920c-1824-418f-90c8-0edf1381678b'
title: PartialReplyPrinterChangeNotification function
---

# PartialReplyPrinterChangeNotification function

The print spooler's `PartialReplyPrinterChangeNotification` function allows a print provider to update the spooler's database of printer changes associated with a notification handle.

## Syntax


```C++
BOOL PartialReplyPrinterChangeNotification(
  _In_     HANDLE                    hNotify,
  _In_opt_ PPRINTER_NOTIFY_INFO_DATA pInfoDataSrc
);
```



## Parameters

<dl> <dt>

*hNotify* \[in\]
</dt> <dd>

Caller-supplied handle. This handle must have been previously received as the *hNotify* input to the print provider's [**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification) function.

</dd> <dt>

*pInfoDataSrc* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a PRINTER\_NOTIFY\_INFO\_DATA structure (described in the Microsoft Windows SDK documentation). Can be **NULL**. For more information, see the following Remarks section.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**. The caller can obtain an error code by calling **GetLastError**.

## Remarks

For the specified notification handle, the spooler's `PartialReplyPrinterChangeNotification` function adds the contents of the specified PRINTER\_NOTIFY\_INFO\_DATA structure to the array within the spooler's stored PRINTER\_NOTIFY\_INFO structure. (These structures are described in the Windows SDK documentation.)

Calling `PartialReplyPrinterChangeNotification` does not cause the spooler to notify the application that changes have occurred. If the print provider's [**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification) function did not set the PRINTER\_NOTIFY\_STATUS\_POLL flag, the provider must call [**ReplyPrinterChangeNotification**](replyprinterchangenotification.md) to cause the application to be notified.

If *pInfoDataSrc* is **NULL**, all stored information associated with the specified handle is deleted from the spooler. The function accomplishes this deletion by freeing all buffers associated with *pBuf* members of PRINTER\_NOTIFY\_INFO\_DATA structures belonging to the specified handle. The function then sets the PRINTER\_NOTIFY\_INFO\_DISCARDED flag in the stored PRINTER\_NOTIFY\_INFO structure.

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

[**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification)
</dt> <dt>

[**ReplyPrinterChangeNotification**](replyprinterchangenotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PartialReplyPrinterChangeNotification%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





