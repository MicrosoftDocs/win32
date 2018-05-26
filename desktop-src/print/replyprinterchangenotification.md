---
Description: The print spoolers ReplyPrinterChangeNotification function allows a print provider to update the spoolers database of print queue events associated with a notification handle, and to notify the client that print queue events have occurred.
ms.assetid: a884920c-1824-418f-90c8-0edf1381678b
title: ReplyPrinterChangeNotification function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ReplyPrinterChangeNotification function

The print spooler's `ReplyPrinterChangeNotification` function allows a print provider to update the spooler's database of print queue events associated with a notification handle, and to notify the client that print queue events have occurred.

## Syntax


```C++
BOOL ReplyPrinterChangeNotification(
  _In_      HANDLE hNotify,
            DWORD  fdwFlags,
  _Out_opt_ PDWORD pdwResult,
  _In_opt_  PVOID  pPrinterNotifyInfo
);
```



## Parameters

<dl> <dt>

*hNotify* \[in\]
</dt> <dd>

Caller-supplied handle. This handle must have been previously received as the *hNotify* input to the print provider's [**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification) function.

</dd> <dt>

*fdwFlags* 
</dt> <dd>

One or more caller-supplied PRINTER\_CHANGE\_-prefixed flags, listed in the Microsoft Windows SDK documentation's description of **FindNextPrinterChangeNotification**.

</dd> <dt>

*pdwResult* \[out, optional\]
</dt> <dd>

Optional. If not **NULL**, it receives spooler-supplied PRINTER\_NOTIFY\_INFO-prefixed flags indicating results of updating the supplied information.

</dd> <dt>

*pPrinterNotifyInfo* \[in, optional\]
</dt> <dd>

Optional. Caller-supplieid address of a PRINTER\_NOTIFY\_INFO structure (described in the Windows SDK documentation). Can be **NULL** if no new notification information is being added.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**. The caller can obtain an error code by calling **GetLastError**.

## Remarks

Print providers that do not support polling (see [**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification)) must notify the spooler of the occurrence of any events represented by the PRINTER\_CHANGE\_-prefixed flags received by the provider's **FindFirstPrinterChangeNotification** function. When an event occurs, the print provider can call `ReplyPrinterChangeNotification` to inform the spooler of the event and to supply information associated with the event. The spooler keeps track of this event information, for each notification handle, and delivers the information to an application when the application calls **FindNextPrinterChangeNotification** (described in the Windows SDK documentation).

When a print provider calls `ReplyPrinterChangeNotification`, it must identify the event that has occurred by setting a PRINTER\_CHANGE\_-prefixed flag in *fwdFlags* or by using *pPrinterNotifyInfo* to return a PRINTER\_NOTIFY\_INFO structure. (Use the flags listed in the Windows SDK documentation's description of **FindNextPrinterChangeNotification**--not the flags listed in the Windows SDK documentation's description of **FindFirstPrinterChangeNotification**.)

Calling `ReplyPrinterChangeNotification` causes the spooler to signal the client application that a print queue event has occurred. This happens even if the provider supplies **NULL** for *pPrinterNotifyInfo*. To update the spooler's record of print queue changes without causing the client to be notified, use [**PartialReplyPrinterChangeNotification**](partialreplyprinterchangenotification.md). It is common to call **PartialReplyPrinterChangeNotification** several times to update the spooler's database, then to call `ReplyPrinterChangeNotification` to notify the client that changes have occurred.

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

[**PartialReplyPrinterChangeNotification**](partialreplyprinterchangenotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ReplyPrinterChangeNotification%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





